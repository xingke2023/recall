就是看到的代码
覆盖的意义点有哪些
没有覆盖的有哪些

myopenai
返回一个函数赋值给一个变量，那么就可以用这个变量调用他的返回的函数的参数

可以引入文件，就是文件里所有的
可以引入包，也就是文件夹，也就是执行__init__.py
可以引入文件里的某个东西
引入了一个文件，就是一个域
这个文件有好几个类，有全局变量
比如说是一个类，那么就是有直接的类变量，像一个对象的操作
对象就是有自己的操作数据和方法
类如果不对象化，那么就是有自己的类变量，和方法，一样直接使用
几种方式，可以调用类比如new对象，可以调用变量
可以是from  import * 可以直接使用一个类，或者是包.类的用法
也可以是__init__.py import进来的文件里的类
类的对象化无非就是执行了初始化有了数据，他的方法一直都存在，但是类不能调用对象的方法

两个文件的交互，也就是import的东西如何使用
全局的函数
全局的class
全局的变量
可以在引入的包里，new一个对象


函数，或者方法，作为一个独立的块单位，
也就是首先是函数是如何组织的，然后函数内部是做什么
里面的东西，每一条语句都是，清晰明确的东西，以下是一些清晰的东西，其他可以列为未覆盖的函数里面的操作
一个是需要什么样的参数
其实里面可以有任何全局的东西，比如requests.post()，比如
messages = []
    messages.append({"role":"system","content":"我希望你充当文案专员、文本润色员、拼写纠正员和改进员"})
这些语句肯定是做一些事情，比如requests.post()完成了一个操作
messages.append是数组结构自身增加了数据
另外一些是调用了函数然后return了数据，赋值给了一个变量
response2 = openai.chat.completions.create()
为什么会有多重的openai.chat.completions.create()




