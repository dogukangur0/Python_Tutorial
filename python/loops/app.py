
start  = int(input("Enter the start value:"))
finish = int(input("Enter the finsh value:"))
value = start
liste = []
while value<finish:
    if(value%2==0):
        liste.append(value)
    value = value+1
print(liste)

i = 100
while i > 0:
    print(i)
    i-=1


a=1
liste = []
while  a<6:
    x = int(input(f"{a}.sayiyi giriniz:"))
    liste.append(x)
    a+=1

liste.sort()
print(liste)




username = input("Enter username:")

while username == "":
    username = input("Enter username:")

print(username)