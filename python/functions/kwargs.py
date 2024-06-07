'''
def display_function(*args):
    print(args)
    print(type(args))   # tuple

display_function()

def display_function(**kwargs):
    print(kwargs)
    print(type(kwargs)) # dict

display_function()
'''


def displayUser(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

displayUser(username="Dogukan",age=24)



def myFunc(a,b,c,d,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(kwargs)

myFunc(1,2,3,4,5,6,7,name="Dogukan",surname="Gur",age=24,language="Python")

