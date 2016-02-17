'''
关键词只有参数
Feature 2: Keyword only arguments
'''
import shutil

def f(a,b,*args,option=True):
    pass

'''
def sum(a,b,biteme=False):
    if biteme:
        shutil.rmtree('/')
    else:
        return a+b

print(sum(1,2))
'''




def maxall(iterable,key=None):
    key = key or (lambda x: x)
    m = max(iterable, key=key)
    return [i for i in iterable if key(i) == key(m)]

print(maxall(['a','ab','bc','abc','bac'], len))



