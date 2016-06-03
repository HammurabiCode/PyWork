#coding=utf-8

'Work: 高阶函数的使用 sorted'

__author__ = 'Hammurabi'

def by_name(t) :
    return t[0]

def by_score(t) :
    return t[1]

if __name__ == '__main__' :
    strL = ['Tom', 'Jerry', 'Emily', 'Ann', 'Henry']
    numL = [199, 23, -123, -898]
    lRec = [('Vanessa', 99), ('Henry', 88), ('Joseph', 77), ('Terry', 87)]
    print sorted.__doc__
    print sorted(strL)
    print sorted(numL, key = abs, reverse = True)
    print sorted(lRec, key = by_name)
    print sorted(lRec, key = by_score, reverse = True)
