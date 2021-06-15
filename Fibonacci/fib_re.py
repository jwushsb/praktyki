
def fib(x):
    if x < 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def dl_fib(x):
    return((fib(y) for y in range(x)))

print(fib(7))