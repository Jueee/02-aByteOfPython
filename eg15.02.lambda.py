# lambda语句被用来创建新的函数对象，并且在运行时返回它们。


# 本质上，lambda需要一个参数，后面仅跟单个表达式作为函数体，而表达式的值被这个新建的函数返回。
# 注意，即便是print语句也不能用在lambda形式中，只能使用表达式。

def make_repeater(n):
	return lambda s:s*n

twice = make_repeater(4)

print(twice('word'))
print(twice('5'))