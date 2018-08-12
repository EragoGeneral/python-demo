# -*-  coding:utf-8  -*-

import os 
import sys

def find_file(name, path='.'):

    dir_list = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
    file_list = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]
    
    for x in file_list:
        if name in x:
            print(os.path.join(path, x))
    for x in dir_list:
        new_path = os.path.join(path, x)
        find_file(name, new_path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need one argument!')
    else:
        find_file(sys.argv[1])
			
			
			
			
			