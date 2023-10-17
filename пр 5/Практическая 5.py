#Number 1
a = input()
k = 0
words = a.split()
for word in words:
    if word[0].lower()=="е":
        k += 1
print("Количество: ", k)

#Number 6
a = str(input())
if "а" in a:
    b = a.replace("а", "")
else:
    print("Try again")
print(b, len(a)-len(b))

#Number 12
s = input().split()
for i in s:
    if i[-1] == "я":
        print(i)

#Number 15
a = input()
print(a.count("т"))

#Number 14
s = input().split()
for i in s:
    if i[0] == "а":
        print("Начинаются на а: ", i)
    elif i[-1] == "я":
        print("Заканчиваются на я: ", i)
    else:
        print("Не подходит по правилам: ", i)
#Number 10
a = input()
print(a.upper())
