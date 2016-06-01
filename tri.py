# coding=utf-8

'Calculate YangHui Triangles.'

__author__ = 'Hammurabi'

def triangles():
    'Generator of Yanghui Triangles'
    l = [1]
    while True:
        yield l
        l = [1] + [l[i + 1] + l[i] for i in range(0, len(l) - 1)] + [1]

if __name__ == '__main__' :
    g = triangles()
    n = 0
    while n < 10:
        n = n + 1
        print next(g)
