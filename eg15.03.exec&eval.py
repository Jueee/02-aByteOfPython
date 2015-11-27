# exec语句用来执行储存在字符串或文件中的Python语句。
# 例如，我们可以在运行时生成一个包含Python代码的字符串，然后使用exec语句执行这些语句。
exec("print('hello')")


# eval语句用来计算存储在字符串中的有效Python表达式。
print(eval('2*3*5**2'))

print(pow(2,10))