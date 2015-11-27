#!/usr/bin/python
# Filename: using_file.py

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''
# 模式可以为读模式（'r'）、写模式（'w'）或追加模式（'a'）。
# 写
f = open('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

# 读
f = open('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print(line,end='')
    # 对end赋值：print(something, something,.., end='')，使end值为空，这个换行就消除了。
f.close() # close the file