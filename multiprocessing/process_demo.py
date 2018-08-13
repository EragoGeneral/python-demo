﻿from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s), paranet process %s...' % (name, os.getpid(), os.getppid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')