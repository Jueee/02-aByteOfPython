self

类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，但是在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本身，按照惯例它的名称是self。

虽然你可以给这个参数任何名称，但是 强烈建议 你使用self这个名称——其他名称都是不赞成你使用的。使用一个标准的名称有很多优点——你的程序读者可以迅速识别它，如果使用self的话，还有些IDE（集成开发环境）也可以帮助你。

给C++/Java/C#程序员的注释
Python中的self等价于C++中的self指针和Java、C#中的this参考。
你一定很奇怪Python如何给self赋值以及为何你不需要给它赋值。举一个例子会使此变得清晰。假如你有一个类称为MyClass和这个类的一个实例MyObject。当你调用这个对象的方法MyObject.method(arg1, arg2)的时候，这会由Python自动转为MyClass.method(MyObject, arg1, arg2)——这就是self的原理了。

这也意味着如果你有一个不需要参数的方法，你还是得给这个方法定义一个self参数。