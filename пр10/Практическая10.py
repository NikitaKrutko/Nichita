from random import randint
n=int(input())
m=int(input())
a=[]
for i in range(n):
    b=[]
    for j in range(m):
        b.append(randint(1,100))
    a.append(b)
with open('C:/Users/alyon/Desktop/GitProjects(nikita)/Nichita/пр10/Nikita_Krutko_vvod.txt', 'w') as file:
    for i in a:
        for j in i:
            file.write(str(j))
            file.write(' ')
        file.write("\n")
with open('C:/Users/alyon/Desktop/GitProjects(nikita)/Nichita/пр10/Nikita_Krutko_vvod.txt', 'r') as file:
    b=[]
    for i in file:
        c=[]
        s=i.split()
        for j in s:
            c.append(j)
        b.append(c)
for i in b:
    minim=i.index(min(i))
    maxim=i.index(max(i))
    i[maxim],i[0]=i[0],i[maxim]
    i[minim],i[-1]=i[-1],i[minim]
with open('C:/Users/alyon/Desktop/GitProjects(nikita)/Nichita/пр10/Nikita_Krutko_vivod.txt', 'w') as file:
    for i in b:
        for j in i:
            file.write(str(j))
            file.write(' ')
        file.write("\n")
