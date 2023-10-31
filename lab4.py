import copy

class Stack:
    def __init__(self):
        self.l = []

    def pop(self):
        if len(self.l) > 0:
            return self.l.pop(len(self.l) - 1)
        
    def peek(self):
        if len(self.l) > 0:
            return self.l[len(self.l) - 1]
        
    def push(self, val):
        self.l.append(val)

def test_Stack():
    a = Stack()
    a.push(12)
    a.push(3)
    assert a.pop() == 3
    assert a.peek() == 12
    assert a.peek() == 12
    assert a.pop() == 12
    assert a.pop() is None
    assert a.peek() is None


class Queue:
    def __init__(self):
        self.l = []

    def pop(self):
        if len(self.l) > 0:
            return self.l.pop(0)
        
    def peek(self):
        if len(self.l) > 0:
            return self.l[0]
        
    def push(self, val):
        self.l.append(val)
   
def test_Queue():
    a = Queue()
    a.push(12)
    a.push(3)
    assert a.pop() == 12
    assert a.peek() == 3
    assert a.peek() == 3
    assert a.pop() == 3
    assert a.pop() is None
    assert a.peek() is None


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.mat = [[0 for j in range(m)] for i in range(n)]

    def __iter__(self):
        return iter(list(sum(iter(self.mat), start=[])))

    def __str__(self):
        s = ""
        for i in self.mat:
            s += str(i) + '\n'
        return s

    def get(self, i, j):
        if (0 <= i < self.n and 0 <= j < self.m):
            return self.mat[i][j]
        else:
            raise IndexError
        
    def set(self, i, j, val):
        if (0 <= i < self.n and 0 <= j < self.m):
            self.mat[i][j] = val
        else:
            raise IndexError

    def transpose(self):
        new = [[self.mat[i][j] for i in range(self.n)] for j in range(self.m)]

        self.mat = new

        t = self.n
        self.n = self.m
        self.m = t

    def map_iter(self, f):
        return map(f, [self.mat[i][j] for i in range(self.n) for j in range(self.m)])
    
    def map(self, f):
        self.mat = [[f(self.mat[i][j]) for j in range(self.m)] for i in range(self.n)]

    def mul(self, other_mat):
        if self.m != other_mat.n:
            raise Exception
        
        result = Matrix(self.n, other_mat.m)

        for i in range(result.n):
            for j in range(result.m):
                # print(list(zip(self.mat[i], [k[j] for k in other_mat.mat])))
                result.set(i, j, sum(map(lambda x: x[0]*x[1], zip(self.mat[i], [k[j] for k in other_mat.mat]))))
        # print()
        print("Multiplied:\n",self,"*\n",other_mat,"=\n",result, sep='')
        return result 

def test_Matrix():
    a = Matrix(3,3)
    for i in range(3):
        for j in range(3):
            a.set(i,j, i*3+j)
    print(a)
    assert a.get(0,0) == 0
    assert a.get(1,2) == 5
    assert a.get(2,2) == 8
    try:
        a.get(4,5)
    except IndexError:
        pass

    c = copy.deepcopy(a)
    c.transpose()
    print("transposed:")
    print(c)

    f = lambda x: x*2
    print("transposed * 2:")
    print("map_iter:",list(c.map_iter(f)),sep='\n')
    print("map builtin :",list(map(f,c)),sep='\n')
    c.map(f)
    print("map member f:",c,sep='\n')


    # print("Multiplying:\n",a,"*\n",c,"=\n",a.mul(c), sep='')
    a.mul(c)

    a = Matrix(1,2)
    a.set(0,0,1)
    a.set(0,1,2)
    c = copy.deepcopy(a)
    c.transpose()
    c.mul(a)


test_Stack()
test_Queue()
test_Matrix()