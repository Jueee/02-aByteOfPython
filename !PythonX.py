# Unpacking 取值
s = ('simon','shi',66,'weiyq10580@hundsun.com')

f1,f2,f3,f4 = s
print(f1,f2,f3,f4)

# Swap Values 交换元素
a = 3
b = 5
print(a,b)
a,b = b,a
print(a,b)

# Don’t Underestimate 一次性赋值
a,b,c = (1,2,3)
print(a,b,c)

# Concatenating Strings 字符串数组拼接
fruits = ['cherry','coconut','blueberry','kiwi']

s = fruits[0]
for i in fruits[1:]:
    s += ', ' + i
print(s)

print(', '.join(fruits))


# Looping over a collection 循环集合
colors = ['red', 'green', 'blue', 'yellow']
# bad
for i in range(len(colors)):
    print(colors[i])
# idiomatic
for color in colors:
    print(color)

# Looping backwards 倒序输出集合
for color in reversed(colors):
    print(color)
for color in colors[::-1]:
    print(color)

# Looping with indices 带序号输出集合
colors = ['red', 'green', 'blue', 'yellow']
# bad
for i in range(len(colors)):
    print(i,'-->',colors[i])
# idiomatic
for i,color in enumerate(colors):
    print(i,'-->',color)

# Looping over a dictionary 循环输出字典
codes = {'Xian': '29', 'Beijing':'10', 'Shanghai':'21'}
# bad
for k in codes:
    print(k,'-->',codes[k])
# recommended
for k,v in codes.items():
    print(k,'-->',v)


# ‘defaultdict’ 按类别归类
names = ['james', 'peter', 'simon', 'jack', 'john', 'lawrence']
# expected result
{8: ['lawrence'], 4: ['jack', 'john'], 5: ['james', 'peter', 'simon']}
# old way
groups = {}
for name in names:
    key = len(name)
    if key not in groups:
        groups[key] = []
    groups[key].append(name)
print(groups)
# use ‘setdefault’ with default value prepared
groups = {}
for name in names:
    groups.setdefault(len(name),[]).append(name)
print(groups)
# use ‘defaultdict’
from collections import defaultdict
groups = defaultdict(list)
for name in names:
    groups[len(name)].append(name)
print(groups)


# Comprehensions
# 判断是否为偶数
def isOdd(integer):
    #assert isinstance(integer, int)
    return integer % 2 == 1
# bad
A,odd_or_even = [1,1,2,3,5,8,13,21],[]
for number in A:
    odd_or_even.append(isOdd(number))
print(odd_or_even)
# expected result
[True, True, False, True, True, False, True, True]

# idiomatic way
print([isOdd(a) for a in A])    # [True, True, False, True, True, False, True, True]
print([a for a in A if a%2!=0]) # [1, 1, 3, 5, 13, 21]

# list
print([a**2 for a in A])            # [1, 1, 4, 9, 25, 64, 169, 441]
# set
print({a**2 for a in A})            # {64, 1, 4, 9, 169, 25, 441}
# dict
print({a:a%3 for a in A if a%3})    # {8: 2, 1: 1, 2: 2, 5: 2, 13: 1}




ages = [42, 21, 18, 33, 19]
# old way
are_all_adult = True
for age in ages:
    if age < 18:
        are_all_adult = False
        break
if are_all_adult:
    print('All are adults!')

ages = [42, 21, 18, 33, 19]
# idiomatic way
for age in ages:
    if age < 18:
        break
else: # go through without break
    print('All are adults!')

# old way
f = open('text.txt')
try:
    data = f.read()
finally:
    f.close()

# idiomatic way
with open('text.txt') as f:
    data = f.read()


# Looping with two collections 循环两个集合
colors = ['red', 'blue', 'green', 'yellow']
fruits = ['cherry', 'blueberry', 'kiwi']
# old way
min_len = min(len(colors),len(fruits))
for i in range(min_len):
    print('[old]',fruits[i],'-->',colors[i])
# idiomatic way
for fruit,color in zip(fruits,colors):
    print('[idiomatic]',fruit,'-->',color)

# Building Dictionaries 创建字典 
fruits = ['cherry', 'blueberry', 'kiwi', 'mango']
colors = ['red', 'blue', 'green', 'yellow']
# old way
pairs = {}
for fruit,color in zip(fruits,colors):
    pairs[fruit] = color
print(pairs)

pairs2 = dict(zip(fruits,colors))
print(pairs2)


# groupby
from itertools import groupby
names = ['james', 'peter', 'simon', 'jack', 'john', 'lawrence']
print({k:list(v) for k,v in groupby(names,len)})    # {8: ['lawrence'], 4: ['jack', 'john'], 5: ['james', 'peter', 'simon']}





