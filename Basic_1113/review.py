#!/usr/bin/env python
# -*- coding: utf-8 -*-

s=r"Let\'s go!"
print(s)

#ascii and unicode and utf-8 and byts

print("ABC".encode('ascii'))
print("中文".encode('utf-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# List and Tuple
Teammates=['Thomas', 'Alice', 'Bob']

Teammates.append('Carol')
print(Teammates)

Teammates.insert(1, 'David')
print(Teammates)

print(Teammates.pop(0))
print(Teammates)

t1=()
t2=(1,)

#dict and set

d = {'Alice':95, 'Bob':98, 'Carol':92}
print(d['Bob'])

if (d.get('Thomas', -1) < 0):
    print('%s: Thomas is not in the dic.\n' % 'WTF')

d.pop('Carol')
print(d)

s=set(list(range(0,10)))
print(s)

s.add(10)
print(s)

s.remove(0)
print(s)

#s_list = set(1,2,3,[4,5],6)
#print(s_list)

#string replace
s='this is string example....wow!!! this is really string'
print(s.replace('is','was'))

print(s.replace('is', 'was', 3))
