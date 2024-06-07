# string formatları

# string concat

name = "Dogukan"
surname = "Gur"
age = 23

# string format
message = "My name is {} {}. I'm {} years old.".format(name,surname,age)
message1 = "My name is {0} {1}. I'm {2} years old.".format(name,surname,age)
message2 = "My name is {n} {s}. I'm {a} years old.".format(n=name,s=surname,a=age)
print(message)
print(message1)
print(message2)

# f-string

message = f"My name is {name} {surname}. I'm {age} years old."
print(message)

