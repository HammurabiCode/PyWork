#coding=utf-8

'Work: inheritance & poly'

__author__ = 'Hammurabi'


class Animal(object):
    def run(self):
        print 'Animal is running'

class Cat(Animal):
    def run(self):
        print 'Cat is running'

class Dog(Animal):
    def run(self):
        print 'Dog is running'

class Clock(object):
    def run(self):
        print 'Ticker...'

def runTwice(ani):
    ani.run()
    ani.run()

if __name__ == '__main__':
    d = Dog()
    c = Cat()
    t = Clock()
    runTwice(d)
    runTwice(t)
    print isinstance(d, Dog)
    print isinstance(d, Animal)
