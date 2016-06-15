#coding=utf-8

'Work: OOP'

__author__ = 'Hammurabi'


class Student(object):
    def __init__(self, name = '', score = 0):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

if __name__ == '__main__':
    s1 = Student('Ann', 90)
    s1.print_score()
