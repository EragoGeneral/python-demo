import threading, multiprocessing
from multiprocessing import Pool, Process

		
'''		
#多线程的方式死锁，无法占满全部CPU

def loop():
    x = 0
    while True:
        x = x^1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
	
'''
def loop(i):
    x = 0 
    print('Thread - ', i)
    while True:
        x = x^1

def proc(i, cpu_count):
    print('Process: ', i)
    for i in range(cpu_count*2):
        t = threading.Thread(target=loop, args=(i,))
        t.start()

if __name__ == '__main__':
    cpu_count = multiprocessing.cpu_count()
    p = Pool(cpu_count)
    for i in range(cpu_count):
        p.apply_async(proc, args=(i, cpu_count))
    p.close()
    p.join()
