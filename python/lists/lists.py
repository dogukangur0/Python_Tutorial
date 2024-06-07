message = "Hello World"

print(type(message)) # str

list1 = message.split()
print(list1)
print(type(list1))
print(list1[0])   # -1
print(list1[1])   # -2


del list1[0]  # silme işlemi
