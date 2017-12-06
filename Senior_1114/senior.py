#!/usr/bin/env python

# 分片
# 分片包含左值不包含右值

a=[1,2,3,4,5,6,7,8,9]
b=(1,2,3,4,5,6,7,8,9)

# 迭代
# dict的迭代

d={'a':1, 'b':2, 'c':3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,":",v) 

from collections import Iterable
from collections import Iterator

# isinstance 是否是可迭代的Interable
print(isinstance(d, Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对
for i,value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#列表生成式

print([i*i for i in range(1,11)])

print([m+n for m in 'ABC' for n in 'XYZ'])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[]
[L2.append(s.lower()) for s in L1 if isinstance(s, str)]

print(L2)

# 生成器

g=(x*x for x in range(1,11))
for n in g:
    print(n)

#fib
def fib(max):
    n, a, b=0,0,1
    while n < max:
        yield b
        print(b)
        a,b = b, a+b
        n=n+1
    return 'done'

# 迭代器
# 以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象

t = (1,)
t = (x*x for x in range(1,11))
print(isinstance(t, Iterator))

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter([]),Iterator)

# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。








if __name__ == '__main__':
    g = fib(10)
    while True:
        try:
            x = next(g)
        except StopIteration as e:
            print('Generator return value', e.value)
            break;
    pass

