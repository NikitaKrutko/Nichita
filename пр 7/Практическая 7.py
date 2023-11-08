from math import *
f = input("Назовите свою фигуру: ")
def pl():
    if f == "Квадрат":
        znach = float(input("Сторона квадрата: "))
        p = znach**2
        print(p)
    elif f == "Круг":
        znach = float(input("Радиус круга: "))
        p = pi*(znach**2)
        print(p)
    elif f == "Прямоугольный треугольник":
        znach = float(input("Катет 1: "))
        znach2 = float(input("Катет 2: "))
        p = (1/2)*(znach*znach2)
        print(p)
pl()


import random

guesses_made = 0
guesses_made2 = 0

name = input('Привет! Как тебя зовут?\n')
password = "72320728"
login = "Nichita"
while guesses_made2 < 3:
    writelog = input("Write your login: ")
    writepas = input("Write your password: ")
    guesses_made2 += 1
    if writelog != login or writepas != password:
        print("Минус одна попытка")
    else:
        break
if writepas == password and writelog == login:
    print("Можешь начинать")
else:
    print("Извини")
    exit()
number = random.randint(1, 30)
print('Отлично, {0}, я загадал число между 1 и 30. Сможешь угадать?'.format(name))

while guesses_made < 6:
    guess = int(input('Введи число: '))
    guesses_made += 1
    if guess < number:
        print('Твое число меньше того, что я загадал.')
    if guess > number:
        print('Твое число больше загаданного мной.')
    if guess == number:
        break
if guess == number:
    print('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(name, guesses_made))
else:
    print('А вот и не угадал! Я загадал число {0}'.format(number))

#Option 2
#N1
import math
a=int(input())
def triangle(a):
    return (a ** 2) * math.sqrt(3) / 4
def triangle6(a):
    return triangle(a) * 6
print(triangle6(a))

N2
for kol in range(3):
    print(int(input("Введите первую сторону"))*int(input("Введите вторую сторону")))

#Option 3
#N1
def g2(x, y):
    return x ** 2 + y ** 2


a1, b1 = map(float, input("Катеты первого треугольника a1, b1 = ").split())
a2, b2 = map(float, input("Катеты второго треугольника a2, b2 = ").split())
c1 = g2(a1, b1)
c2 = g2(a2, b2)
if c1 == c2:
    print("Гипотенузы равны")
else:
    print("Гипотенуза первого треугольника больше" if c1 > c2 else "Гипотенуза второго треугольника больше")

#N2
from itertools import accumulate


def sort(str):
    return tuple(accumulate(sorted(str)))[-1]


str = input("Введите строку: ")
print(sort(str))