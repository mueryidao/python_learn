dic={'a':1, 'b':2, 'c':3, 'd':4}

for k in dic:
    print dic[k]

for v in dic.itervalues():
    print v

for k, v in dic.iteritems():
    print k,v

from collections import Iterable

print isinstance('abc', Iterable)
print isinstance(dic, Iterable)


for i, value in enumerate(['A', 'B', 'C']):
    print i, value
