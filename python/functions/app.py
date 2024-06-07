#Q1
name = input("Enter name:")
count = int(input("How many times will it be printed ? "))


def yazdir(name,count):
    i = 0
    while i<count:
        print(name)
        i+=1

yazdir(name,count)



def calculateRectangleArea(x,y):
    return x*y

def calculateRectanglePerimeter(x,y):
    return 2*(x+y)

print(calculateRectangleArea(2,6))
print(calculateRectanglePerimeter(2,6))


def yaziTura():
    import random
    number = random.random()

    if number > 0.5:
        return "Tura"
    else:
        return "False"

print(yaziTura())

