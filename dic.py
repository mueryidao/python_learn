dic={'Thomas':95, 'Zhisheng':97, 'Simon':92}

if 'Thomas' in dic:
    print dic['Thomas']

if dic.get('Thomas'):
    print 'exist!'
if dic.get('Tom', -1):
    print 'No exist!'

set1 = set([1,2,3])
set2 = set([4,5,6,7])



set1.add(4)

set2.remove(6)
print set1
print set2

print set1&set2
print set1|set2
