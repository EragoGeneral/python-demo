#! /user/local/env python3
# -*-  coding:utf-8  -*-

class Screen(object):

    # get方法需要有 selef 参数
    @property
    def width(self):
        return self._width
    # set 方法注解用 get方法名+.setter，且set方法名与get方法名一样
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

		
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
