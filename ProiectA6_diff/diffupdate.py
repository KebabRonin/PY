"""
This module implements a binary diff utility, based on Myers' Difference Algorithm.

The diff file is binary. The format for each change is:
<op(+/-)><byte offset><length>[data for insert]
"""
import sys, os


def create(latest: str, *targets: str):
	print("create", latest, targets)


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