
#-----------------------------调用函数---------------------------------------

# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
a = 20;
print(hex(a));

#-----------------------------定义函数---------------------------------------
# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
import math;
def quadratic(a, b, c):
    s = b*b-4*a*c;
    if s < 0 :
        print("此函数无解")
    if s == 0 :
        return -b/2/a
    if s >0 :
        return (-b+math.sqrt(s))/2/a,(-b-math.sqrt(s))/2/a;
print(quadratic(1,3,-4))

#-----------------------------函数的参数---------------------------------------
#默认参数
def my_pow(x,y=2):
    s = 1;
    while y > 0 :
        s  =  s * x;
        y -=1;
    return s;

print(my_pow(3),my_pow(3,4))

# 可变参数
def my_calc(*numbers):
    return sum(n for n in numbers);
print(my_calc(1,2,3),my_calc(1,2,3,4),my_calc(*[1,2,4,5,7]))
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#关键字参数
def persion(name,age,**kw):
    print("name",name,"age",age,"kw",kw)
persion("lili",23,city="北京",height=170,weight=65)
extra = {"city":"北京","height":170,"weight":65}
persion("lili",23,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数
#只接收city和job作为关键字参数，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person_2(name, age, *, city, job):
    print(name, age, city, job)
person_2("lily",25,city="北京",job="IT")
person_2("lily",25,city="北京",job="IT")

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

#计算两个数的乘积，可接收一个或多个数并计算乘积：
def product(*number):
    s = 1;
    if number is ():
        raise TypeError
    for n in number:
        s = s * n;
    return s;
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

#-----------------------------递归函数---------------------------------------
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
