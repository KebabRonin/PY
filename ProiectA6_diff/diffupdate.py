"""
This module implements a binary diff utility, based on Myers' Difference Algorithm.

The diff file is binary. The format for each change is:
<op(+/-)><byte offset><length>[data for insert]
"""
import sys, os
from math import ceil


def find_middle_snake(old_sequence: bytes, N: int, new_sequence: bytes, M: int) -> tuple[int]:
	"""A variant of the 'find middle snake' function that uses O(min(len(a), len(b)))
	memory instead of O(len(a) + len(b)) memory. It searches from both ends of the sequence at the same time.

	Args:
		old_sequence (bytes): the sequence to be edited
		N (int): length of `old_sequence`
		new_sequence (bytes): the target sequence
		M (int): length of `new_sequence`

	Returns:
		tuple[int]: Number of edits to get from `old_sequence` to `new_sequence`, start index in `old_sequence`, start index in `new_sequence`, end index in `old_sequence`, end index in `new_sequence`
	"""
	MAX = N + M
	Delta = N - M

	V_SIZE=2*min(M,N) + 2
	# The array that holds the 'best possible x values' in search from top left to bottom right.
	Vf = [None] * V_SIZE
	# The array that holds the 'best possible x values' in search from bottom right to top left.
	Vb = [None] * V_SIZE
	# The initial point at (0, -1)
	Vf[1] = 0
	# The initial point at (N, M+1)
	Vb[1] = 0
	# Iterate to ceil((max edit length)/2) because we're searching in both directions.
	for D in range(0, ceil(MAX/2) + 1):
		# Forward Pass
		# max for boundry checking
		for k in range(-(D - 2*max(0, D-M)),( D - 2*max(0, D-N)) + 1, 2):
			if k == -D or k != D and Vf[(k - 1) % V_SIZE] < Vf[(k + 1) % V_SIZE]:
				# Did not increase x, take the better x value from the k line above
				x = Vf[(k + 1) % V_SIZE]
			else:
				# Increase x by building on the best path from the k line above
				x = Vf[(k - 1) % V_SIZE] + 1

			y = x - k
			# Remember the initial point before the snake
			x_i = x
			y_i = y
			# While the sequences match, keep moving through the graph with no cost
			while x < N and y < M and old_sequence[x] == new_sequence[y]:
				x = x + 1
				y = y + 1
			# New best x value
			Vf[k % V_SIZE] = x
			# Only check for connections from the forward search when N - M is odd and when there is a k line coming from the other direction.
			inverse_k = (-(k - Delta))
			if (Delta % 2 == 1) and inverse_k >= -(D -1) and inverse_k <= (D -1):
				if Vf[k % V_SIZE] + Vb[inverse_k % V_SIZE] >= N:
					return 2 * D -1, x_i, y_i, x, y

		# Backward Pass
		for k in range(-(D - 2*max(0, D-M)), (D - 2*max(0, D-N)) + 1, 2):
			if k == -D or k != D and Vb[(k - 1) % V_SIZE] < Vb[(k + 1) % V_SIZE]:
				x = Vb[(k + 1) % V_SIZE]
			else:
				x = Vb[(k - 1) % V_SIZE] + 1
			y = x - k
			x_i = x
			y_i = y
			while x < N and y < M and old_sequence[N - x - 1] == new_sequence[M - y - 1]:
				x = x + 1
				y = y + 1
			Vb[k % V_SIZE] = x
			inverse_k = (-(k - Delta))
			if (Delta % 2 == 0) and inverse_k >= -D and inverse_k <= D:
				if Vb[k % V_SIZE] + Vf[inverse_k % V_SIZE] >= N:
					return 2 * D, N - x, M - y, N - x_i, M - y_i


def shortest_edit_script(old_sequence : bytes, new_sequence: bytes, current_x: int =0, current_y: int =0) -> list[dict]:
	"""This function is a concrete implementation of the algorithm for finding the shortest edit script that was'left as an exercise' on page 12 of 'An O(ND) Difference Algorithm and Its Variations' by EUGENE W. MYERS.

	Args:
		old_sequence (bytes): the sequence to be edited
		new_sequence (bytes): the target sequence
		current_x (int, optional): The start index of `old_sequence` in the global sequence (for recursion). Defaults to 0.
		current_y (int, optional): The start index of `new_sequence` in the global sequence (for recursion). Defaults to 0.

	Returns:
		list[dict]: A list of objects that describe the edits necessary to get from `old_sequence` to `new_sequence`.

	The returned objects have the following structure:
	* `operation` - 'delete' or 'insert'
	* `position_old` - the index in `old_sequence` the operation should take place at
	* `position_new` - the index in `new_sequence` of the byte to be inserted
	"""
	N = len(old_sequence)
	M = len(new_sequence)
	rtn = []
	if N > 0 and M > 0:
		D, x, y, u, v = find_middle_snake(old_sequence, N, new_sequence, M) # find match
		# If the graph represented by the current sequences can be further subdivided.
		if D > 1 or (x != u and y != v):
			# Collect delete/inserts before the snake
			rtn += shortest_edit_script(old_sequence[0:x], new_sequence[0:y], current_x, current_y)
			# Collect delete/inserts after the snake
			rtn += shortest_edit_script(old_sequence[u:N], new_sequence[v:M], current_x + u, current_y + v)
		elif M > N:
			# M is longer than N, and there is a maximum of one edit to transform old_sequence into new_sequence
			# The first N elements of both sequences in this case will represent the snake, and the last element will represent a single insertion.
			rtn += shortest_edit_script(old_sequence[N:N], new_sequence[N:M], current_x + N, current_y + N)
		elif M < N:
			# N is longer or equal to M, and there is a maximum of one edit to transform old_sequence into new_sequence
			# The first M elements of both sequences in this case will represent the snake, and the last element will represent a single deletion.
			# If M == N, then this reduces to a snake which does not contain any edits.
			rtn += shortest_edit_script(old_sequence[M:N], new_sequence[M:M], current_x + M, current_y + M)
	elif N > 0:
		# This area of the graph consist of only horizontal edges that represent deletions.
		for i in range(0, N):
			rtn.append({"operation": "delete", "position_old": current_x + i})
	else:
		# This area of the graph consist of only vertical edges that represent insertions.
		for i in range(0, M):
			rtn.append({"operation": "insert", "position_old": current_x, "position_new": current_y + i})
	return rtn


def normalize_diff(changes: list[dict]) -> list[dict]:
	"""Used to compress changes produced by `shortest_edit_script()`.

	Args:
		changes (list[dict]): list of atomic changes(len=1), as generated by the output of `shortest_edit_script()`

	Returns:
		list[dict]: The compressed changes, in a format simmilar to `shortest_edit_script()`

	The returned objects have the following structure:
	* `operation` - 'delete' or 'insert'
	* `position_old` - the start index in `old_sequence` the operation should take place at
	* `position_new` - the start index in `new_sequence` of the byte to be inserted
	* `len` - the length of bytes to be deleted/inserted

	"""
	# Process operations separately
	deletes = list(filter(lambda x: x['operation'] == 'delete', changes))
	inserts = list(filter(lambda x: x['operation'] == 'insert', changes))

	# DELETE Operations
	current_index = -10
	compact_deletes = []
	for d in deletes:
		if d['position_old'] == current_index + 1:
			# Merge operations
			compact_deletes[-1]['len'] += 1
		else:
			compact_deletes.append(d)
			compact_deletes[-1]['len'] = 1
		current_index = d['position_old']

	# INSERT Operations
	current_index, ci_old = -10, -10
	compact_inserts = []
	for d in inserts:
		if d['position_old'] == ci_old and d['position_new'] == current_index + 1:
			# Merge operations
			compact_inserts[-1]['len'] += 1
		else:
			compact_inserts.append(d)
			compact_inserts[-1]['len'] = 1
		ci_old = d['position_old']
		current_index = d['position_new']

	# Interleave operations to get final diff, delete operations take precedence over insert operations
	rez = []
	while len(compact_inserts) > 0 and len(compact_deletes) > 0:
		if compact_deletes[0]['position_old'] <= compact_inserts[0]['position_old']:
			rez.append(compact_deletes.pop(0))
		else:
			rez.append(compact_inserts.pop(0))
	while len(compact_inserts) > 0:
		rez.append(compact_inserts.pop(0))
	while len(compact_deletes) > 0:
		rez.append(compact_deletes.pop(0))

	return rez


def create(latest: str, *targets: str) -> int:
	"""Creates .diff files that bring each `target` to the file specified by `latest`

	Args:
		latest (str): the name/path of the latest file
		*targets (str): the names/paths of the files to be updated

	Returns:
		int: 0 for success, -1 for errors
	"""
	try:
		with open(latest, "rb") as new:
			for target in targets:
				new.seek(0)
				try:
					with open(target, "rb") as old:
						old_data = old.read()
						new_data = new.read()
						changes = shortest_edit_script(old_data, new_data)
						changes = normalize_diff(changes)

						with open(os.path.basename(target).split('.')[0] + ".diff", "wb") as f:
							for c in changes:
								header = [0 if c['operation'] == 'delete' else 1]
								header += list(c['position_old'].to_bytes(4))
								header += list(c['len'].to_bytes(4))
								f.write(bytes(header))
								if c['operation'] == 'insert':
									# write the raw bytes to be inserted
									f.write(bytes(new_data[c['position_new']:(c['position_new']+c['len'])]))

							print(f"{target}: Diff file saved as '{f.name}'")
				except Exception as e:
					print(f"{target}: Error: {e}")
					continue
	except Exception as e:
		print(f"{latest}: Error: {e}")
		return -1


def update(target: str, diff_file: str) -> int:
	"""Creates an updated file (.latest) by applying the changes in `diff_file` to the `target` file.

	Args:
		target (str): the name/path of the file to be updated
		diff_file (str): the name/path of the diff file to be applied

	Returns:
		int: 0 for success, -1 for errors

	"""
	try:
		with open(target, "rb") as old:
			try:
				with open(diff_file, "rb") as diff:
					try:
						with open(os.path.basename(target).split('.')[0] + ".latest", "wb") as new:
							while True:
								header = diff.read(9)

								if len(header) < 9:
									# reached EOF
									if len(header) > 0:
										# and have incomplete header
										print("Fatal error: incomplete header")
										return -1
									break

								offset = int.from_bytes(header[1:5])
								length = int.from_bytes(header[5:9])

								# write what hasn't changed as is
								if offset - old.tell() > 0:
									new.write(old.read(offset - old.tell()))

								if header[0] == 0: # delete (-)
									old.seek(length, 1) # skip from current position
								elif header[0] == 1: # add (+)
									new.write(diff.read(length))
								else:
									print("Fatal error: Invalid operation:", header[0])
									return -1

							# finish writing the rest of the file
							new.write(old.read())

							print("Updated file at", new.name)
					except Exception as e:
						print(f"Error creating .latest file: {e}")
						return -1
			except Exception as e:
				print(f"{diff_file}: Error: {e}")
				return -1
	except Exception as e:
		print(f"{target}: Error: {e}")
		return -1


def diffupdate():
	"""Runs the diffupdate program according to sys.argv
	"""
	if len(sys.argv) > 1:
		match sys.argv[1]:
			case 'create':
				if len(sys.argv) < 4:
					print("Usage:	{} create <latest_file> <target> [targets]".format(sys.argv[0]))
				else:
					create(sys.argv[2], *sys.argv[3:])
			case 'update':
				if len(sys.argv) < 4:
					print("Usage:	{} update <latest_file> <diff_file>".format(sys.argv[0]))
				else:
					update(sys.argv[2], sys.argv[3])
			case _:
				print("Unrecognized command:", sys.argv[1])
	else:
		print("Usage:	{} <create|update> <latest_file> <args>".format(sys.argv[0]))



if __name__ == '__main__':
	diffupdate()