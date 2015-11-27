a = 'a';
print(a)

b = "b"
print(b)
'''
使用三引号
利用三引号，你可以指示一个多行的字符串。你可以在三引号中自由的使用单引号和双引号。
'''
c = '''asd
asds
asda
asdasd
a'''
print(c)
#在一个字符串中，行末的单独一个反斜杠表示字符串在下一行继续，而不是开始一个新的行。
d = "asdqwe吴千语\
asd\
asd\
asd"
print(d)

e = r"asd"
print(e)
#字面意义级连字符串
#如果你把两个字符串按字面意义相邻放着，他们会被Python自动级连。
f = "aedafa" "asd"
f = "asasdd" "qwqeqe"
print(f)