#Option 1
#N1
from math import *
def vir(x,n):
    if n == 0:
        return 1
    else:
        return (x**n)/factorial(n)
print(vir(int(input()), int(input())))

#Option 2
n=int(input('Введите любое число: '))


def f(n):
    i = 2
    while n % i != 0:
        if i >= n ** 0.5:
            return True
        i += 1
    return False
n = int(input())
if f(n) or n == 2:
    print('YES')
else:
    print('NO')