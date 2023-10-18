#Option 1
#N1
a = []
for i in range(10):
    a.append(int(input("Введите число: ")))
print("Максимальный элемент: ", str(max(a)))
print("Массив в обратном порядке: ", str(list(reversed(a))))

#N2
import random
a = [random.random() for _ in range(10)]
sumel = sum(a)
srznach = sumel/len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] == srznach
print(a)

#Option 2
#N1
a = []
for i in range(10):
    a.append(int(input("Введите число: ")))
print("Минимальный элемент: ", str(min(a)))
print("Индекс минимального элемента: ", a.index(min(a)))

#N2
a = []
b = []
c = []
for i in range(4):
    a.append(int(input("Введите число: ")))
for n in a:
    if n > 0:
        b.append(n)
    else:
        c.append(n)
print(b, c)

#Option 3
#N1
a = []
for i in range(8):
    a.append(int(input("Введите число: ")))
maxel = max(a)
print("MaxElement: ", maxel)
k = 0
c = 0
z = 0
for x in a:
    if x > maxel:
        print(x, ">", maxel)
        k += 1
    elif x < maxel:
        print(x, "<", maxel)
        c += 1
    elif x == maxel:
        print(x, "=", maxel)
        z += 1
print("Больше: ", k)
print("Меньше: ", c)
print("Равно: ", z)

#N2
a = []
s = 0
for i in range(10) :
    a.append(int(input("Введите число: ")))
    if a[-1] > 5 :
        s += a[-1]
print(a)
print(s)