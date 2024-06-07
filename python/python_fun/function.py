def sayHello(name):
    print("Hello " + name)

sayHello("Dogu")


def total(num1,num2):
    return num1+num2

result = total(10,20)
print(result)

def add(a,b,c=3):
    return sum((a,b,c))
'''
eğer bir fonksiyonda parametreye bir değer atarsak,
kullanmasak bile kullanmisiz gibi, verdiğimiz değer kullanilir.
'''
print(add(10,20))
print(add(10,20,30))


'''
* -> tuple listesi demektir.
şöyle bir durumdan bahsedebiliriz. oluşturduğumuz fonksiyon kaç tane 
parametre alacak bunu bilmiyorsak, *params parametresini kullanabiliriz.
böylece her fonksiyon çağrildiğinda farkli şekillerde değerler 
ekleyebiliriz.
'''

def addM(*params):
    return sum((params))

print(addM(10,20))
print(addM(10,20,30))
print(addM(10,20,30,40))

'''
** -> dictionary listesi demektir.
'''

def displayUser(**params):
    print(type(params))  # dictionary tipinde
    for key,value in params.items():
        print("{}" is "{}".format(key,value))

print(displayUser(name="George"))
print(displayUser(name="John",age=24))
print(displayUser(name="Alice",age=32,email="alice@gmail.com"))


def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


myFunc(10,20,30,40,50,key1='value1',key2='value2')


myFunc('''istenen ilk değer a değeri''','''istenen ikinci değer b değeri''','''istenen üçüncü değer ve sonrasi *args değeri  -> liste tipinde''','''*args değerinden sonra key-value şeklindeki veri **kwargs değeri olur.''')
















