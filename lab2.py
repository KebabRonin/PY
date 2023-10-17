def ex1(n):
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    fibo = [1, 1]

    for i in range(2, n):
        fibo.append(fibo[i - 2] + fibo[i - 1])

    return fibo


def ex2(input_list):
    primes_list = [x for x in input_list if x == 2 or 
                   (x > 1 and x % 2 != 0 and len([div for div in range(3, x//2 + 1, 2) if x % div == 0]) == 0)]

    # primes_list = []

    # for x in input_list:
    #     if x < 2:
    #         continue
    #     if x == 2:
    #         primes_list.append(2)
    #         continue
    #     if x % 2 == 0:
    #         continue
    #     for y in range(3, x//2 + 1, 2):
    #         if x % y == 0:
    #             continue
        
    #     primes_list.append(x)

    return primes_list


def ex3(a, b):
    intersection = [val for val in a if val in b]
    a_dif_b = [val for val in a if val not in intersection]
    b_dif_a = [val for val in b if val not in intersection]
    union = a + b_dif_a

    return (intersection, union, a_dif_b, b_dif_a)


def ex4(notes, steps, start):
    index = start
    song = [notes[index]]

    for step in steps:
        index = (index + step) % len(notes)
        song.append(notes[index])
    
    return song


def ex5(matrix):
    lins = len(matrix)
    cols = len(matrix[0])

    for i in range(0,lins):
        for j in range(0,cols):
            if i > j:
                matrix[i][j] = 0

    return matrix


def ex6(lolists, x):
    dict = {}

    for list in lolists:
        for y in list:
            if y in dict:
                dict[y] += 1
            else:
                dict[y] = 1

    result = [key for key, count in dict.items() if count == x]

    return result


def ex7(input_list):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    pals = list(filter(is_palindrome, input_list))

    count = len(pals)
    max_pal = max(pals)

    return (count, max_pal)


def ex8(input_list, x = 1, flag = True):
    response = []
    for string in input_list:
        word_response = list(filter(lambda letter: (ord(letter) % x == 0) == flag, string))
        response.append(word_response)

    return response


def ex9(matrix):
    lins = len(matrix)
    cols = len(matrix[0])
    list = []

    for col_id in range(0, cols):
        max_height = 0
        for lin_id in range(0, lins):
            if matrix[lin_id][col_id] <= max_height:
                list.append((lin_id, col_id))
            else:
                max_height = matrix[lin_id][col_id]

    return list


def ex10(*input_lists):
    response = []
    depth = max([len(x) for x in input_lists])

    for i in input_lists:
        i.extend([None for _ in range(0, (depth - len(i)))])

    return [tuple(list[i] for list in input_lists) for i in range(0, depth)]


def ex11(tuples):
    return sorted(tuples, key = lambda x: ord(x[1][2]))


def ex12(words):
    rhymes = []
    for word in words:
        if word[-2:] not in rhymes:
            rhymes.append(word[-2:])
    
    grouped = list(map(lambda rhyme: [x for x in words if x[-2:] == rhyme],rhymes))
    return grouped


print("ex1:  ", ex1(10))
print("ex2:  ", ex2([1,3,20,5,11,4, 2]))
print("ex3:  ", ex3([1,2,4,3], [3,5,4,6]))
print("ex4:  ", ex4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
print("ex5:  ", ex5([[1,2,3], [4,5,6],[7,8,9]]))
print("ex6:  ", ex6([[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]], 2))
print("ex7:  ", ex7([1, 3, 11, 231, 1221, 121]))
print("ex8:  ", ex8(["test", "hello", "lab002"], flag = False, x = 2))
print("ex9:  ", ex9([
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]]
 ))
print("ex10: ", ex10([1,2,3], [5,6], ["a", "b", "c"]))
print("ex11: ", ex11([('abc', 'bcd'), ('abc', 'zza')]))
print("ex12: ", ex12(['ana', 'banana', 'carte', 'arme', 'parte']))