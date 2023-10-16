#Number 1
a = int(input())
b = int(input())
if a > b:
    print("Наибольшее", a)
else:
    print("Наибольшее", b)

#Number 6
a = int(input())
if a % 7 == 0:
    print("Кратно 7")
else:
    print("Не кратно 7")

#Number 11
a = int(input("Введите ваш возраст: "))
if a < 18:
    print("Вам запрещен вход на сайт:(")
else:
    print("Добро пожаловать:)")

#Number 16
a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print("Да, оно кратно 5 и 3")
elif a % 3 == 0 and a % 5 !=0:
    print("Кратно только 3")
elif a % 3 != 0 and a % 5 == 0:
    print("Кратно только 5")
else:
    print("Попробуйте еще раз")

#Number 10
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Yes")


