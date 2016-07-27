from functools import reduce

def str2int(s):
#    def str2num(x, y):
#        return x*10+y
    str2integer = lambda x, y: x*10+y
    str2decimal = lambda x, y: x/10+y
        
    def char2num(s):
        return {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}[s]

    i = s.index(".")
    integer = reduce(str2integer, map(char2num, s[:i]))
    decimal = reduce(str2decimal, map(char2num, s[:i:-1]))/10

    print(integer)
    print(decimal)
    
    return integer + decimal

    #return reduce(str2num, map(char2num, s))

#print(str2int("123"))


def str2int_official(s):
    return reduce(lambda x, y: x+y/(10**len(str(y))), map(int, s.split('.')))

print(str2int_official("45678"))
