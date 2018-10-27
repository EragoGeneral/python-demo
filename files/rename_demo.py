#coding:utf8
import os;

def rename():
        i=1
        baseDir = "C:\\study\\workspace\\python\\python-demo\\network\\tmp\\"
        #path="F:\test";        
        while i <= 27:
            path = baseDir + str(i)
            i = i + 1
            filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
            for files in filelist:#遍历所有文件
                #i=i+1
                Olddir=os.path.join(path,files);#原来的文件路径                
                if os.path.isdir(Olddir):#如果是文件夹则跳过
                        continue;
                filename=os.path.splitext(files)[0];#文件名
                filetype=os.path.splitext(files)[1];#文件扩展名
                newname=os.path.join(path,str(int(filename)+1000)+filetype);#新的文件路径
                os.rename(Olddir,newname)#重命名
                #print(newname)
            print(i) 
rename()