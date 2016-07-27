def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x > 0:
        return x
    else:
        return -x

def nop():
    pass

def multi():
    x = 10
    y = 20
    return x, y

print my_abs(-20)
#print my_abs('A')
print multi()[-1]
