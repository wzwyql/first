#!/usr/bin/env python3
# coding:utf-8

class Student(object):
    count = 0
    books = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
    pass

s = Student('Saotao', 25)
s.books.extend(["python","java"])
print('student\'s name is: %s, age is: %d' %(s.name,s.age))
print('student book list: %s' %s.books)

