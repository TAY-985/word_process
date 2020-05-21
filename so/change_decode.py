#-*-coding:utf-8 -*-
import os
folder =r"E:\毕设\sougou_before2" #存储文本的目录

listDir = os.listdir(folder)#获取所有的子目录
print(listDir)
for files in listDir:
    #dataDir = [os.path.join(dataDir,i) for i in os.listdir(dataDir)]#获取绝对路径
    #for words in files:
        #pos,filename = os.path.split(words)
        i=1
        oldfile=open(folder+'\\'+files,'r',encoding='ansi')
        newFile = open(r'E:\毕设\sougou_before3'+'\\'+os.path.basename(folder+'\\'+files),'w',encoding='utf-8')#建立新文件
        try :
            newFile.write(oldfile.read().decode('gbk','ignore').encode('utf-8'))
        except:
            newFile.write(oldfile.read().decode('gbk','ignore').encode('utf-8'))
        oldfile.close()
        newFile.close()
        i=i+1
 #       os.remove(words)#删除旧文件
