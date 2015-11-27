#!/usr/bin/python
# Filename: objvar.py
'''
事实上，它们只是与类和对象的名称空间 绑定 的普通变量，即这些名称只在这些类与对象的前提下有效。
有两种类型的 域 ——类的变量和对象的变量，它们根据是类还是对象 拥有 这个变量而区分。
类的变量 由一个类的所有对象（实例）共享使用。
只有一个类变量的拷贝，所以当某个对象对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。
对象的变量 由类的每个对象/实例拥有。
因此每个对象有自己对这个域的一份拷贝，即它们不是共享的，在同一个类的不同实例中，虽然对象的变量有相同的名称，但是是互不相关的。
通过一个例子会使这个易于理解。
'''
'''
这里，population属于Person类，因此是一个类的变量。name变量属于对象（它使用self赋值）因此是对象的变量。
观察可以发现__init__方法用一个名字来初始化Person实例。
在这个方法中，我们让population增加1，这是因为我们增加了一个人。
同样可以发现，self.name的值根据每个对象指定，这表明了它作为对象的变量的本质。
记住，你只能使用self变量来参考同一个对象的变量和方法。这被称为 属性参考 。
在这个程序中，我们还看到docstring对于类和方法同样有用。
我们可以在运行时使用Person.__doc__和Person.sayHi.__doc__来分别访问类与方法的文档字符串。

就如同__init__方法一样，还有一个特殊的方法__del__，它在对象消逝的时候被调用。
对象消逝即对象不再被使用，它所占用的内存将返回给系统作它用。

在这个方法里面，我们只是简单地把Person.population减1。
当对象不再被使用时，__del__方法运行，但是很难保证这个方法究竟在 什么时候 运行。
如果你想要指明它的运行，你就得使用del语句，就如同我们在以前的例子中使用的那样。
'''
class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print('(Initializing %s)' % self.name)

        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    def __del__(self):
        '''I am dying.'''
        print('%s says bye.' % self.name)

        Person.population -= 1

        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left.' % Person.population)

    def sayHi(self):
        '''Greeting by the person.

        Really, that's all it does.'''
        print('Hi, my name is %s.' % self.name)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person.population)

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

Jue = Person('Jue')
Jue.sayHi()
Jue.howMany()

swaroop.sayHi()
swaroop.howMany()