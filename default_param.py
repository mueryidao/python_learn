def enroll(name, gender, age=6, city='QD'):
    print name, gender, age, city



#enroll('Thomas', 'F')
#enroll('Tom', 'F', 10)
#enroll("Jim", 'M', city='SH')


def calc(*numbers):
    for n in numbers:
        print n

    return

#list_my=[1,2,3]
#calc(*list_my)
#tuple_my=([3,4,5,6])
#calc(*tuple_my)

def person(*arg, **kw):
    print arg, kw

kw={'city':'QD', 'job':'Engineer'}
person('Thomas', 24, **kw)
person('Tome', 10, 100, x=10)

