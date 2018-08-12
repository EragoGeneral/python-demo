import os,sys

def get_abspath(s):
    PATH='.'
    a=os.path.abspath('.')
    for root,dirs,files in os.walk(PATH):
         for file in files:
              if s in file:
                 print((os.path.abspath(os.path.join(root,file))).replace(a,''))
				 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Need one argument!')
    else:       
        get_abspath(sys.argv[1])