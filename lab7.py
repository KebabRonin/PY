import sys, os

def read_files_with_extension(path, extension):
    found = False
    if not extension.startswith('.'):
        extension = '.' + extension
    try:
        if not os.path.exists(path):
            raise Exception(f"Path does not exist: {path}")
        if not os.path.isdir(path):
            raise Exception(f"Path is not directory: {path}")
        for file in os.listdir(path):
            p = os.path.join(path,file)
            if os.path.isfile(p) and os.path.splitext(p)[1] == extension:
                found = True
                print()
                print("".center(80,'='))
                print(str(p).center(80,'='))
                print("".center(80,'='))
                try:
                    with open(p, "rt", encoding="UTF-8") as f:
                        for line in f:
                            print(line)
                except PermissionError as e:
                    print(e)
        if found == False:
            raise Exception(f"No files with extension '{extension}' were found in {path}")
    except FileNotFoundError as e:
        raise Exception(f"Directory does not exist: {path}") from e


def rename_files_sequential(path):
    try:
        if not os.path.exists(path):
            raise Exception(f"Path does not exist: {path}")
        if not os.path.isdir(path):
            raise Exception(f"Path is not directory: {path}")
        index = 1
        for file in os.listdir(path):
            p = os.path.join(path,file)
            if os.path.isfile(p):
                try:
                    os.rename(p, os.path.join(path, f"{index}{file}"))
                    index += 1
                except:
                    print("File could not be renamed:", p)
    except FileNotFoundError as e:
        raise Exception(f"Directory does not exist: {path}") from e


def sum_sizes(path):
    s = 0
    try:
        if not os.path.exists(path):
            raise Exception(f"Path does not exist: {path}")
        if not os.path.isdir(path):
            raise Exception(f"Path is not directory: {path}")
        for file in os.listdir(path):
            p = os.path.join(path,file)
            if os.path.isfile(p):
                try:
                    s += os.path.getsize(p)
                except:
                    print("File could not be renamed:", p)
            elif os.path.isdir(p):
                s += sum_sizes(p)
    except FileNotFoundError as e:
        raise Exception(f"Directory does not exist: {path}") from e
    finally:
        return s
        

def count_files_with_extension(path):
    exts = {}
    try:
        if not os.path.exists(path):
            raise Exception(f"Path does not exist: {path}")
        if not os.path.isdir(path):
            raise Exception(f"Path is not directory: {path}")
        if len(os.listdir(path)) == 0:
            raise Exception(f"Empty directory: {path}")
        for file in os.listdir(path):
            p = os.path.join(path,file)
            if os.path.isfile(p):
                ext = os.path.splitext(p)[1]
                exts[ext] = exts[ext] + 1 if ext in exts else 1
    except FileNotFoundError as e:
        raise Exception(f"Directory does not exist: {path}") from e
    print(exts)


try:
    if len(sys.argv) < 2:
        raise Exception(f"Usage:{sys.argv[0]} ex[1-4] <arguments>")

    match sys.argv[1]:
        case "ex1":
            if len(sys.argv) < 4:
                raise Exception(f"Usage:{sys.argv[0]} ex1 <path> <extension>")
            read_files_with_extension(sys.argv[2], sys.argv[3])
        case "ex2":
            if len(sys.argv) < 3:
                raise Exception(f"Usage:{sys.argv[0]} ex2 <path>")
            rename_files_sequential(sys.argv[2])
        case "ex3":
            if len(sys.argv) < 3:
                raise Exception(f"Usage:{sys.argv[0]} ex3 <path>")
            print(sum_sizes(sys.argv[2]), "bytes")
        case "ex4":
            if len(sys.argv) < 3:
                raise Exception(f"Usage:{sys.argv[0]} ex4 <path>")
            count_files_with_extension(sys.argv[2])
        case _:
            raise Exception(f"Usage:{sys.argv[0]} ex[1-4] <arguments>")
except Exception as e:
    print(e)
