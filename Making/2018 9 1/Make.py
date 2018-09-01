# -*- coding: utf-8 -*-  
import os
import random

'''
适用于开发Windows2.5D游戏的初级引擎

该py文件中设定的是制作游戏时调用的函数

Create.py中则是在设置完一切调用的函数之后生成游戏的py文件的

Use.py则是用户使用的交互（暂时不考虑开发图形界面）

Github: https://www.github.com/huxiao14/Scene
'''

class Player():
    def Create(serf,name,sex):   #创建角色,Save应为项目根目录
        global SAVE
        os.chdir(SAVE+'/bin/part')     #更换工作目录
        if os.path.exists(name+'.txt') == True:   #判断是否重复创建了角色,注意名字一样性别不同的角色不能创建的，否则会覆盖
            A = str(input('你确定要怎么做吗,角色'+name+'已经存在,该操作将会覆盖,确定请输入Y'))
            if A == 'Y':
                file = open(name+'.txt','w') #文件操作同下
                file.write(name+'\n')
                file.write(sex+'\n')
                file.close()
                print ('操作成功')
                return True #如果是覆盖角色的话函数会返回一个True值
            else:
                print ('操作没有完成') #没有发生覆盖或者储存会返回none
                return
        else:
            file = open(name+'.txt','w')
            file.write(name+'\n')
            file.write(sex+'\n')
            file.close()
            print ('操作成功')
            return False   #不是覆盖角色会返回False值

    def Delete(serf,name): #删除角色
        global SAVE
        os.chdir(SAVE+'/bin/part')
        if os.path.exists(name+'.txt') == True:
            if str(input('确定要删除'+name+'吗？请输入Y确认否则输入任意字符')) == 'Y':
                os.remove(name+'.txt') #删除文件
                print ('操作成功')
                return True
            else:
                print ('操作没有完成')
                return 
        else:
            print ('操作失败,找不到该角色')
            return False
    
    def Feature(serf,name,feature,*key):#此处的feature参数需为字典，字典的key是特征的类型，key参数是为了只导入字典中少量的数据,
                                        #参数前加上*可以变为可选参数，本函数就是类似于人设的设定
        global SAVE
        os.chdir(SAVE+'/bin/part')#注释接上上行，如果没有该角色名字的话不会报错而是会产生一个新的角色,角色默认为男
        A = os.path.exists(name+'.txt')
        if A == True:
            pass
        if A == False:
            file = open(name+'.txt','w')
            file.write(name+'\n')
            file.write('Male\n')
            file.close()
        file = open(name+'.txt')
        #os.system('pause')  写到这里先收工之后在读取字典时要用for遍历
        
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
    def Create(serf,name,save): #此处save应为上一级目录，创建项目
        os.chdir(save)
        os.makedirs(name+'/')
        os.chdir(save+'/'+name+'/')
        os.makedirs('bin/part')
        #os.makedirs 此处待补充更多目录
        A = save+name+'/'
        return A
'''
重要提示 important!
此处返回A是为了能把项目的根目录作为全局变量，因此在使用时必须以
B = Software().Create()的形式才能将A作为全局变量储存在B中
使用时名字请统一为SAVE

'''

#B = Software()
#SAVE = B.Create('Demo','E://P bian cheng wen jian/Python/Scene/')
#
#A = Player()  
#A.Create('Hu','Male') #测试Player.Create函数
#A.Delete('Hu')#测试Delete函数
os.system('pause')
