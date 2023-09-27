a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

n = int(input())
if n <= 9:
    for i in range(1, n+ 1):
        for a in range(1, i+1):
            print(a, sep="",end="")
        print()
else:
    print("Try again")

n = int(input())
z = 0
for i in range(1, n+1):
    z += i**3
    print(i, i ** 3, z)
print(z)


























