#1
def printScreen(name,number):
    print(name*number)

printScreen("Dogu\n",3)

#2
def addList(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

print(addList(10,20,30,40,50,60))

#3
num1 = int(input('sayi1:'))
num2 = int(input('sayi2:'))
def findNumber(num1,num2):
    for num in range(num1,num2+1):
        if num > 1:
            for i in range(2,num):
                if(num%2==0):
                    break
            else:
                print(num)

findNumber(num1,num2)

#4

def tamBolen(sayi):
    liste = []
    for i in range(2,sayi):
        if(sayi % i == 0):
            liste.append(i)      
    return liste


sayi = int(input('sayi:'))
print(tamBolen(sayi))

