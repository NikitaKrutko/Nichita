#Option 1
#N1
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
sum = 0
count = 0
mas = []
for i in range(m):
    b = []
    for j in range(n):
        print('Write [',i,',',j,'] element')
        b.append(int(input()))
    mas.append(b)
print("Исходный массив")
for i in range(n):
    for j in range(n):
        print(mas[i][j], end="")
    print()
for i in range(m):
    for j in range(n):
        if (mas[i][j]>0) and i < j:
            count += 1
            sum += mas[i][j]
print(sum)
print(count)

# N2
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
mas = []
for i in range(m):
    b = []
    for j in range(n):
        print('Write [',i,',',j,'] element')
        b.append(int(input()))
    mas.append(b)
for i in range(m):
    for j in range(n):
        print(mas[i][j], end="")
    print()
for i in mas:
    for j in [i]:
        max_el = max(i)
        ind_max = i.index(max_el)
        min_el = min(i)
        ind_min = i.index(min_el)
        i[ind_max], i[0] = i[0], i[ind_max]
        i[ind_min], i[0] = i[0], i[ind_min]
for i in range(n):
    for j in range(n):
        print(mas[i][j], end="")
    print()

# Option 2
# N1
n = int(input("Введите значение строки и столбца: "))
a = []
for i in range(n):
    b = []
    for j in range(n):
        print('Write [',i,',',j,'] element: ')
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

firstsum = sum(a[0])
b = 0
for k in a:
    if sum(k) != firstsum:
        b += 1
        break

for k in range(0, n):
    if sum([row[k] for row in a]) != firstsum:
        b += 1
        break

if b == 0:
    print('Магический квадрат')
else:
    print('Не магический квадрат')

#N2
from random import *
n = int(input("Введите число: "))
m = int(input("Введите число: "))
a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(randint(1,9))
    a.append(b)
print("Исходный массив")
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
for i in a:
    i[0],i[3] = i[3],i[0]
print("Измененный массив")
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

#Option 3
#N1
from random import *
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
count = 0
mas = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(randint(1,9))
    mas.append(b)
for i in range(n):
    for j in range(n):
        print(mas[i][j], end="")
    print()
up = []
down = []

for i in range(n):
    for j in range(n):
        if i > j:
            down.append(mas[i][j])
        elif i < j:
            up.append(mas[i][j])

print(down,'\n',up)
if up == down:
    print("Симметрична")
else:
    print("Несимметрична")
