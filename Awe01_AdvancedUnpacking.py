'''
先进的拆包

Feature 1: Advanced unpacking
'''
# You can already do this:
a,b = range(2)
print(a,b)

# Now you can do this:
a,b,*rest = range(10)

print(a)
print(b)
print(rest)
'''
0
1
[2, 3, 4, 5, 6, 7, 8, 9]
'''



# *rest can go anywhere:
a,*rest,b = range(10)

print(a)
print(b)
print(rest)
'''
0
9
[1, 2, 3, 4, 5, 6, 7, 8]
'''



*rest,b = range(10)

print(b)
print(rest)
'''
9
[0, 1, 2, 3, 4, 5, 6, 7, 8]
'''



# Get the first and last lines of a file
with open("test.txt") as f:
    first,*_,last = f.readlines()
print(first)
print(last)


# Refactor your functions 重构函数
def f(a,b,*args):
    pass

def f(*args):
    a,b,*args = args
    pass