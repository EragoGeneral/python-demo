#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):

    count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1
		
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
print(bart.count)
print(Student.count)
lisa = Student('Lisa Simpson', 87)
print(lisa.count)
print(Student.count)
bart.print_score()
lisa.print_score()