# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: check0.py
@time: 2018/4/19 下午9:02
"""


import os
import time
import filecmp
import shutil
path1 = '/Users/zhouqi/Desktop/g/0/0/1/'
path2 = '/Users/zhouqi/Desktop/g/0/0/2/'
path3 = '/Users/zhouqi/Desktop/g/0/0/3/'

def checkfile(file1,file2):

    return  filecmp.cmp(path1+file1,path2+file2)




while 1:

    count = 0  # 计数大文件夹下共有多少个小文件夹
    list   = []
    for filename in os.listdir(path1):
        # print filename
        if filename =='.DS_Store':
            pass
        else:
            count += 1
            list.append(filename)
    print (count)
    print list
    if count > 0 :
        for i in list :
            if os.path.isfile(path2+i):
                if checkfile(i,i) :
                    print 'same'
                    shutil.move(path1+i,path3+i)
                else:
                    print 'diff'
            else:
                print 'path2 is not this file'

    time.sleep(1)







if __name__ == '__main__':
    pass