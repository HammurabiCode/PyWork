# coding=utf-8

from tri import triangles

def testMain() :
    print triangles.__doc__
    g = triangles()
    n = 0
    while n < 10 :
        print next(g)
        n += 1

if __name__ == '__main__' :
    testMain()