"""
*******************************************************************************
作者：gxyang
时间：2020.11.17 11：34
改进：
      相对于基础版本：1、拓展了   计算注释行、空行    功能
                      2、优化了使用界面，增加了   目录、各个功能的命令接口
时间：2020.11.18 20.26
改进：
      1、修改了计算行数、空行的漏洞
      2、加入了 一些保护代码，防止因用户输入错误而导致程序崩掉
*******************************************************************************
"""
import os
def wc(o,p):
    while True:
        try:
            f=open(p,'r',encoding="utf-8")
        except FileNotFoundError as e:
            print("您输入的文件目录有问题或文件不存在,请检查以下问题后再次输入：")
            print('1、文件目录是否有误或是否存在\n2、文件名称是否有错误或是否存在')
            o,p=get_file()
        else:
            break
    L=0                                    #定义行数为L
    C=0                                 #定义字符数
    W=0                                      #定义单词数
    Z=0                                 #定义注释行数   假设用*作为注释符
    K=0                         #定义空行数
    for line in f.readlines():
        for i in line:
            if i==' ':
                W+=1                    #若读到空格或换行符则单词数W+1
            elif i=='*':
                Z+=1
                C+=1
            elif i=='\n':
                C=C
            else:
                C+=1
        if len(line)==1:
            K=K+1
        else:
            W=W+1
    f.seek(0)
    for j in f.read():
        if j=='\n':
            L=L+1
    L=L+1
    if j[len(j)-1]=='\n':
        K=K+1
    while True:
        if o=='wc.exe -l':
            print("行数：%d"%L)
            break
        elif o=='wc.exe -z':
            print("注释行：%d"%Z)
            break
        elif o=='wc.exe -k':
            print("空行：%d"%K)
            break
        elif o=='wc.exe -c':
            print("字符数：%d"%C)
            break
        elif o=='wc.exe -w':
            print("单词数：%d"%W)
            break
        else:
            o,p=input("您输入的命令不存在，请重新输入：").split(',')
    f.close()
print('********************************************')
print('命令目录：')
print('wc.exe -c,\\file.txt       统计字符数')
print('wc.exe -w,\\file.txt       统计单词数')
print('wc.exe -l,\\file.txt       统计行数')
print('wc.exe -z,\\file.txt       统计注释行数')
print('wc.exe -k,\\file.txt       统计空行数')              
print('********************************************')
def get_file():
    context=input('输入文件所在目录:')
    while True:
        try:
            order,file=input('请输入命令：').split(',')
        except:
            print('请检查输入命令是否有误后再次输入，注意 逗号、空格、反斜杠')
        else:
            break
    path=context + file
    return order,path
while True:
   order,path=get_file()
   wc(order,path)
   b=input('如果想退出请输入break；否则，请回车：')
   if b=='break':
      break
os.system('pause')
