# #Number 1
a = int(input())
b = int(input())
for i in range(a, b+1):
    print(i, end=" ")

#Number 6
a = int(input())
fac = 1
for i in range(2, a+1):
    fac *= i
print(fac)

#Number 2
a = int(input())
b = int(input())
if a > b:
    for i in range(a, b - 1, -1):
        print(i, end=" ")
else:
    for i in range(a, b+1):
        print(i, end=" ")

#Number 7
a = int(input())
sum = 1
curr = 1
for i in range(2, a + 1):
    curr *= i
    sum += curr
print(sum)