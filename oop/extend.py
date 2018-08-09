#!/usr/bin/env python3
# -*-  coding:utf-8  -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eating...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog();
dog.run()

cat = Cat()
cat.run()

def run_twice(aaaaa):
    aaaaa.run()
    aaaaa.run()

run_twice(dog)
run_twice(cat)

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())

#print(type(dog))
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))

print(dir(Tortoise()))

string = 'AAA20180809bcd'
print(dir(string))
print(string.__len__())
print(string.__contains__('0809'))
print(string.index('0809'))
print(string.upper())

print(dir(dog))



class MyObject(object):
    def __init__(self):
        self.x = 9
        def power(self):
            return self.x * self.x

obj = MyObject()
hasattr(obj, 'x')
print(obj.x)
hasattr(obj, 'y')
setattr(obj, 'y', 19)
hasattr(obj, 'y')
print(getattr(obj, 'y'))
print(obj.y)

