import threading

#创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    print('to do task 1')
    do_task_1()
    print('to do task 2')
    do_task_2()

def do_task_1():
    std = local_school.student
    print('doing task 1')
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def do_task_2():
    std = local_school.student
    print('doing task 2')
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bok', ), name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()

