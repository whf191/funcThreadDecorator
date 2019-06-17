# funcThreadDecorator
函数线程装饰器，让你的函数以线程的方式运行

# 说明
funcThreadDecoratorNotResult: 函数线程装饰器没有返回值

funcThreadDecoratorResult: 函数线程装饰器有返回值

#使用例子

@funcThreadDecoratorResult
def test1(b, c, d, a=100):
    print(b)
    print(c)
    print(d)
    print(a)
    print("test is ok ")
    return 1
