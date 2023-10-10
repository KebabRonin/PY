def ex1():
    numbers = map(int, input("Space separated numbers to gcd: ").split())

    gcd = None

    for nr in numbers:
        if gcd is None:
            gcd = nr
        else:
            while gcd != nr:
                if gcd > nr:
                    gcd -= nr
                else:
                    nr -= gcd

    return gcd


def ex2(text):
    text = str(text).lower()
    count = 0

    for letter in text:
        if letter in "aeiou":
            count += 1

    return count


def ex3(text1, text2):
    return str(text1).count(str(text2))


def ex4(text):
    text = str(text)
    snaked = ""

    for letter in text:
        if letter.isupper():
            if snaked == "":
                snaked += letter.lower()
            else:
                snaked += "_" + letter.lower()
        else:
            snaked += letter

    return snaked


def ex5alt(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            print("Matrix is not square")
            return

    dirs = [(0,1), (-1,0), (0,-1), (1,0)]
    i = 0; j = 0; current_dir = 0; consec_failures = 0

    while consec_failures < 4:
        print(matrix[i][j], end='')
        matrix[i][j] = None
        
        while not (0 <= i + dirs[current_dir][0] < len(matrix) and \
                   0 <= j + dirs[current_dir][1] < len(matrix[0]) and \
                    matrix[i + dirs[current_dir][0]][j + dirs[current_dir][1]] is not None):
            current_dir = (current_dir + 1) % 4
            consec_failures += 1
            if consec_failures >= 4:
                break
        else:
            i += dirs[current_dir][0]
            j += dirs[current_dir][1]
            consec_failures = 0

    print("")


def ex5(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            print("ERR: Matrix is not square")
            return

    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    i = 0; j = 0; current_dir = 0
    min_row = min_col = 0; max_row = max_col = n - 1

    while min_row <= max_row and min_col <= max_row:
        
        print(matrix[i][j], end='')

        if not ((min_row <= i + dirs[current_dir][0] <= max_row) and \
            (min_col <= j + dirs[current_dir][1] <= max_col)):
            match current_dir:
                case 1:
                    max_col -= 1
                case 2:
                    max_row -= 1
                case 3:
                    min_col += 1
                case 0:
                    min_row += 1
            current_dir = (current_dir + 1) % 4        

        i += dirs[current_dir][0]
        j += dirs[current_dir][1]
        
    print("")


def ex6(nr):
    cnr = nr
    pal = 0

    while cnr:
        pal = pal * 10 + cnr % 10
        cnr = cnr // 10

    return pal == nr 
    

def ex7(text):
    numflag = False
    number = None

    for letter in text:
        if letter.isnumeric():
            if not numflag:
                number = int(letter)
                numflag = True
            else:
                number = number * 10 + int(letter)
        else:
            if numflag:
                break

    return number
        

def ex8(nr):
    bits = 0
    while nr:
        bits += nr % 2
        nr = nr // 2
    
    return bits


def ex9(text):
    text = text.lower()
    letters = {}

    maxl = None

    for letter in text:

        if not letter.isalpha():
            continue

        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

        if maxl is None or letters[maxl] < letters[letter]:
            maxl = letter

    return (maxl, letters[maxl])


def ex10(text):
    return len(text.split())



print("ex1:  ", ex1(), sep = '')                         # gcd from list; asks for input
print("ex2:  ", ex2("Ana are mere"), sep = '')           # vowel count
print("ex3:  ", ex3("Ana are mere", "re"), sep = '')     # substring count
print("ex4:  ", ex4("UpperCamelCase"), sep = '')         # UpperCamelCase to snake_case
print("ex5:  ", end = '')                                # matrix spiral; ex5 prints the result itself
ex5([
        ['f','i','r','s'],
        ['n','_','l','t'],
        ['o','b','a','_'],
        ['h','t','y','p'],
    ])        
print("ex6:  ", ex6(12), sep = '')                       # is palindrome?
print("ex7:  ", ex7("aiuf__di D12D-dk 91"), sep = '')    # extract first number
print("ex8:  ", ex8(24), sep = '')                       # count '1' bits
print("ex9:  ", ex9("Ana are merer"), sep = '')          # most frequent letter
print("ex10: ", ex10("a b c de f"), sep = '')            # count words