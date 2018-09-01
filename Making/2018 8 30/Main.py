#copy from Scene/Main.py
import os
import random
#适用于开发Windows2.5D游戏的初级引擎

class Player():
    def Create(serf,Name,Sex,Save):   #创建角色,Save应为项目根目录
        os.chdir(Save+'/bin/part')     #更换工作目录
        if os.path.exists(Name+'.txt') == True:   #判断是否重复创建了角色,注意名字一样性别不同的角色不能创建的，否则会覆盖
            A = str(input('你确定要怎么做吗,角色'+Name+'已经存在,该操作将会覆盖,确定请输入Y'))
            if A == 'Y':
                file = open(Name+'.txt','w') #文件操作同下
                file.write(Name+'\n')
                file.write(Sex+'\n')
                file.close()
                print ('操作成功')
                return True #如果是覆盖角色的话函数会返回一个True值
            else:
                print ('操作没有完成') #没有发生覆盖或者储存会返回none
                return
        else:
            file = open(Name+'.txt','w')
            file.write(Name+'\n')
            file.write(Sex+'\n')
            file.close()
            print ('操作成功')
            return False   #不是覆盖角色会返回False值

    def Delete(serf,Name,Save): #删除角色
        os.chdir(Save+'/bin/part')
        if os.path.exists(Name+'.txt') == True:
            os.remove(Name+'.txt')
            print ('操作成功')
            return True
        else:
            print ('操作失败')
        return False


class Model():
    pass


class Map():
    pass


class Tool():
    pass

class Episode():
    pass

class Menu():
    pass

class Software():
    def Create(serf,Name,Save): #此处Save应为上一级目录，创建项目
        os.chdir(Save)
        os.makedirs(Name+'/')
        os.chdir(Save+'/'+Name+'/')
        os.makedirs('bin/part')
        #os.makedirs 此处待补充更多目录
        return

#B = Software()
#B.Create('Demo','E://P bian cheng wen jian/Python/Scene/')
#A = Player()  
#A.Create('Hu','Male','E://P bian cheng wen jian/Python/Scene/Demo/') #测试Player.Create函数
#A.Delete('Hu','E://P bian cheng wen jian/Python/Scene/Demo/')#测试Delete函数
os.system('pause')
