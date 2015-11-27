'''
DocStrings
Python有一个很奇妙的特性，称为 文档字符串 ，它通常被简称为 docstrings 。DocStrings是一个
重要的工具，由于它帮助你的程序文档更加简单易懂，你应该尽量使用它。你甚至可以在程序
运行的时候，从函数恢复文档字符串！
'''
'''
文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。
'''
def printMax(x, y):
	'''Prints the m axim um of two num bers.
	The two values m ust be integers.'''
	x = int(x) # convert to integers, if possible
	y = int(y)
	if x > y:
		print(x, 'is m axim um ')
	else:
		print(y, 'is m axim um ')


printMax(3, 5)
print(printMax.__doc__)

print(dir())