from threading import *

class MyThread(Thread):
    def __init__(self,name,*args):
        super(MyThread,self).__init__(name = name)#调用父类的init，设置线程的名称
        self.data = args
    def run(self):
        print(self.name,self.data)
MyThread("abc", [x for x in range(10)]).start()