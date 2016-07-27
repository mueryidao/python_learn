L=(x*x for x in range(1,11))


def fib(max):
    n, a, b=0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

for n in fib(6):
    print(n)

g = fib(6)

while True:
    try:
        x=next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value.', e.value)
        break
