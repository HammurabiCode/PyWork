#coding=utf-8

'Work: 装饰器'

__author__ = 'Hammurabi'

def log(func) :
    def f(*args, **kw):
        print 'begin'
        func(*args, **kw)
        print 'end'
    return f

def logWithArg(str) :
    print str
    def wrapper(func):
        def f(*args, **kw):
            print 'begin'
            func(*args, **kw)
            print 'end'
        return f
    return wrapper

def logBoth(ipt) :
    if callable(ipt):
        func = ipt
        def wrapper(*args, **kw):
            print 'begin'
            func(*args, **kw)
            print 'end'
            return
        return wrapper
    else:
        def decorator(func):
            def wrapper(*args, **kw):
                print ipt, 'begin'
                func(*args, **kw)
                print ipt, 'end'
                return
            return wrapper
        return decorator


@logBoth
def hello():
    print 'Hello World'

if __name__ == '__main__' :
    hello()
