# START TIME: 4:13
import sys, os

def test_valid(d):
    try:
        int(d['FILE_SIZE'])
    except ValueError as e:
        print("FILE_SIZE is not int")
        return False

    date = d['LAST_MODIFIED_DATE'].split('-')
    try:
        if len(date) != 3 or len(date[0]) != 4 or int(date[1]) > 12 or int(date[2]) > 31:
            print('LAST_MODIFIED_DATE is not valid')
            return False
    except:
        print('LAST_MODIFIED_DATE is not valid')
        return False
    return True


def main():
    print(sys.argv)

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file-name>")
        return

    file_name = sys.argv[1]
    if not os.path.exists(file_name):
        print(f"Path does not exist: {file_name}")
        return
    if not os.path.isfile(file_name):
        print(f"Path is not file: {file_name}")
        return
    
    f_sizes = {}
    oldest_date = ''
    duplicates = []
    parsed_f = []
    top_3_f = {}

    for line in open(file_name):
        fields = line.split('|')
        if len(fields) != 4:
            continue
        d = {
            'FILE_NAME': fields[0].strip(),
            'FILE_SIZE': fields[1].strip(),
            'FILE_TYPE': fields[2].strip(),
            'LAST_MODIFIED_DATE': fields[3].strip(),
        }
        print(d)
        
        if not test_valid(d):
            continue

        f_sizes[d['FILE_TYPE']] += d['FILE_SIZE']

        files_like = list(filter(lambda x: x['FILE_TYPE'] == d['FILE_TYPE'] and x['FILE_SIZE'] == d['FILE_SIZE'], parsed_f))
        if len(files_like) > 0:
            duplicates += [(d['FILE_NAME'],f['FILE_NAME']) for f in files_like]

        parsed_f.append(d)
    

    print("Duplicates:", duplicates)
    parsed_f.sort(key=lambda x: x['LAST_MODIFIED_DATE'])
    print("Oldest:", parsed_f[0])

    
    print(":)")

main()
