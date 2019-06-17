#!/usr/bin/python
# coding=utf-8
from __future__ import print_function
import sys, threading
import functools

"""
funcThreadDecoratorNotResult: 函数线程装饰器没有返回值

funcThreadDecoratorResult: 函数线程装饰器有返回值
"""


class MyThread(threading.Thread):
    def __init__(self, func, args, kwargs):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = self.func(*self.args, **self.kwargs)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None


def funcThreadDecoratorNotResult(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        t.join()

    return wrapper


def funcThreadDecoratorResult(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = MyThread(func, args=args, kwargs=kwargs)
        t.start()
        t.join()
        return t.get_result()

    return wrapper


###一个例子....
@funcThreadDecoratorResult
def test1(b, c, d, a=100):
    print(b)
    print(c)
    print(d)
    print(a)
    print("test is ok ")


if __name__ == '__main__':
    test1(1, 2, 3)
