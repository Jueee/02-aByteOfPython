'''
在Python的类中有很多方法的名字有特殊的重要意义。
现在我们将学习__init__方法的意义。

__init__方法在类的一个对象被建立时，马上运行。
这个方法可以用来对你的对象做一些你希望的 初始化 。
注意，这个名称的开始和结尾都是双下划线。
'''

#!/usr/bin/python
# Filename: class_init.py
class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print ('Hello, my name is', self.name)

p = Person('Swaroop')
p.sayHi()