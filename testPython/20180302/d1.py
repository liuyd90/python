# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------------------
#输出和输入
print("hello world");
print("1024 * 768 =",1024*768)
# name = input("请输入姓名：");
# print("您的姓名是：",name);
#-----------------------------------------------------------------------------------------
# string
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

#格式化
name = 'hello, %s';
print(name %("liu"));
#------------------------------------------------------------------------------------------

# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[0],classmates[-1]);  #0表示第一个，-1从后面数第一个
classmates.append("Lucy");#在后面追加一个
classmates.insert(1,"Lili") #z在指定位置添加一个
print(classmates);
classmates.pop();#删除最后一个
classmates.pop(1);#删除指定位置的一个
classmates[1]="Bobj";#替换指定位置
print(classmates);
#-----------------------------------------------------------------------------------------
# if
height = 1.75
weight = 80.5
bmi  = weight/(pow(height,2));
if bmi <= 18.5:
    print("过轻");
elif bmi <= 25:
    print("正常");
elif bmi <= 28:
    print("过重");
elif bmi <= 32:
    print("肥胖");
else:
    print("严重肥胖")

#----------------------------------------------------------------------------
#求解：axx+bx+c=0（a≠0），

import math;
def quadratic(a,b,c):
    s = pow(b,2)-4*a*c;
    if s <0 :
        print("无解")
    elif s == 0 :
        return -b/2/a;
    else:
        return (-b+math.sqrt(s))/2/a ,(-b-math.sqrt(s))/2/a;
print(quadratic(1,3,-4))




