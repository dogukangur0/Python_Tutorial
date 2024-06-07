brands = ["audi","bmw","ferrari","mercedes"]

myObj = enumerate(brands,1) # (iterable,start)

print(type(myObj))  # enumerate
print(list(myObj))  


for brand in enumerate(brands,1):
    print(brand)



# zip  


number = [1,2,3,4,5]
student = ["Hary","Jack","Leonardo","Leo","Eric"]


print(list(zip(number,student)))

for stu in zip(number,student):
    print(stu)