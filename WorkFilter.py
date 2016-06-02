#coding=utf-8

'Work: 高阶函数的使用 filter'

__author__ = 'Hammurabi'

def numberGenerator():
    n = 1
    while True:
        n += 2
        yield n

def not_dividable(n):
    return lambda x: x%n > 0

def prime():
    n = 2
    yield n
    it = numberGenerator()
    while True:
        n = next(it)
        yield n
        it = filter(not_dividable(n), it)


def isPalidrome(n):
    return str(n) == str(n)[::-1]



if __name__ == '__main__':
    l = [12321, 3232, 98789]
    print filter(isPalidrome, l)
