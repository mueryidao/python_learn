#!/usr/bin/env python

import math

#isinstance is build-in function to check the type
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x;
    else:
        return -x;

#None function
def nop():
    pass

#一元二次方程
def quadratic(a, b, c):
    d = b*b - 4*a*c
    if (d > 0):
        print('two answers\n')
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1, x2
    elif(d == 0):
        print('one answer\n')
        x = -b/(2*a)
        return x
    else:
        print('no answer')
        return False

# location parameter: x and n value is determined by the location
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# default value parameter:
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
def add_end(L=[]):
    L.append('END')
    return L
def add_end_ok(L=None):
    if L is None:
        #L 作为形参也需要初始化?
        L = []
        L.append('END')
        return L

# variable parameter
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum

# key word parameter
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# name key word parameter
def person_name(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
def person_name_2(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)
#命名关键字参数city具有默认值，调用时，可不传入city参数, 不能传入city的其他值，会作为位置参数处理报错
def person_name_3(name, age, *, city='QD', job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)

#递归函数
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

# 尾递归优化
def fact_optimize(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(n-1, num*product)

# 汉诺塔实现
# 现在有个n个盘子，a,b,c三个塔。
# 把n个盘子抽象成两个盘子，n-1 和 底下最大的1
#
# n = (n-1) + 1
# 1. 把n-1移到缓冲区
# 2. 把1移到终点
# 3. 把缓冲区的n-1移到终点
#
# 1如何实现：
# move(N, 起点，缓冲区， 终点)
# 起点是a， 终点是b， 缓冲区是c，N=n-1
# move(n-1, a, c, b)
# 2如何实现
# move(1, a, b, c)
# 3
# move(n-1, b, a, c)
# if(N==1):
# a -> c

def hanoi(n, a, b, c):
    if n == 1:
        print(a, ' -> ', c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)

    

# if this python file is used as module, the __name__ will not be __main__
if __name__ == '__main__':

    #quadratic(3, 4, 5)

    # test default value parameter
    #print(add_end())

    # test variable parameter
    #nums = [1,2,3]
    #print(calc(*nums))                              #可变参数转化
    #print(calc(nums[0], nums[1], nums[2]))

    #test key word parameter
    person('Thomas', 28, city='QingDao')
    person('Bob', 30, gender='M', job='engineer')

    extra = {'city':'QD', 'job':'engineer'}
    person('Alice', 24, **extra, gender='F')

    # test name key word parameter
    person_name_2('Carol', 26, city='QD', job='engineer')
    person_name_3('David', 26, job='engineer')

    # test hanoi
    hanoi(2, 'A', 'B', 'C')


    






