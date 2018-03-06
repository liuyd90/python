#函数式编程
#-------------------------------------------------------------高阶函数----------------------------------------------------------------------------------
def add(x,y,f):
    return f(x)+f(y);
print(add(10,-20,abs))

# map(f,Iterable)
#f代表函数  ，后面是迭代 ，返回结果为Iterator

# reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)  返回单个数据

#filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]),返回复核条件的数据，去除不符合条件的

#

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(s) :
    return s[0].upper()+s[1:].lower();
l1 = ['adam', 'LISA', 'barT']
print( list( map(normalize,l1) ) );

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(l) :
    return reduce(lambda x,y :x*y,l);
print(prod([1,2,3,4,5,6]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
import math
def str2float (s) :
    int_part ,sec_part = s.split(".")
    return reduce(lambda x,y : x*10+y,map(int,int_part))+\
           reduce(lambda x,y :x*10+y,map(int,sec_part))*math.pow(10,-len(sec_part));
print(str2float("123.456"))

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

print(is_palindrome(232))

#假设我们用一组tuple表示学生名字和成绩：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(t) :
    return t[0];

#再按成绩从高到低排序：
def by_age(t) :
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=by_name))
print(sorted(L,key=by_age))

#-------------------------------------------------------------返回函数----------------------------------------------------------------------------------
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    def g() :
        n = 0;
        while True:
            n += 1;
            yield n
    it = g();
    def counter():
        return next(it)
    return counter

f = createCounter()
print(f(),f(),f())
#-------------------------------------------------------------匿名函数----------------------------------------------------------------------------------
#请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1
# L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda n: n%2 == 1, range (1,20)))

#-------------------------------------------------------------装饰器----------------------------------------------------------------------------------


#-------------------------------------------------------------偏函数----------------------------------------------------------------------------------
import functools
int2 = functools.partial(int,base=2)

print(int2("1010"))






