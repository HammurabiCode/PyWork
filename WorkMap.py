#coding=utf-8

'Work: 高阶函数的使用 map reduce'

__author__ = 'Hammurabi'

def normalize(name) :
    '将name的首字母大写,其余字母小写'
    return name.title()

def prod(L) :
    '计算列表L的积'
    return reduce(lambda x, y: x*y, L)

def prodStr(L):
    return reduce(lambda x, y:str(x)+' * '+str(y), L)

def str2float(s):
    i, xiaoshu = s.split('.')
    xiaoshu = xiaoshu[::-1] + '0'
    return reduce(lambda x, y: x * 10 + y, map(int, i))+reduce(lambda x, y:x*0.1+y, map(int,xiaoshu))

if __name__ == '__main__':
    L1 = ['adam', 'LISA', 'barT']
    print L1, map(normalize, L1)

    l = [3, 5, 7, 9]
    print prodStr(l),' = ', prod(l)

    strFloat = '1231.1323123'
    if float(strFloat) == str2float(strFloat) :
        print str2float.__name__, 'is right!'