"""
This module implements a binary diff utility, based on Myers' Difference Algorithm.

The diff file is binary. The format for each change is:
<op(+/-)><byte offset><length>[data for insert]
"""
import sys, os


def create(latest: str, *targets: str):
	print("create", latest, targets)


def update(target: str, diff_file: str):
	print("update", target, diff_file)


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