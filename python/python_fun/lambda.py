def square(num):
    return num ** 2

# default olarak bir sayının karesi

# elimizde bir liste varsa her birini for içinde ayrı ayrı bulmak yerine
# map fonksiyonunu kullanabiliriz.

numbers = [1,2,3,4,5]

# map fonksiyonu 2 parametre alır. 
# ilk parametre fonksiyon adı. 
# ikinci parametre liste adı. 

#result = map(square,numbers) # bu sonuç bize adresi verir. 

# burada map bir listeye çevrilmeli ya da for döngüsünde çağrılmalı.

result = list(map(square,numbers))
print(result)

# lambda kullanımı 
result = list(map(lambda num : num**2,numbers))

# tanımlamış olduğumuz fonksiyona bir isim verir gibi de belirtebiliriz. 
# square = lambda num : num**2


# filter işlemi

def check_even(num):
    return num%2==0

result = list(filter(check_even,numbers))
result = list(filter(lambda num : num%2==0,numbers))
print(result)

# the power of lambda is better then when you use them as an anonymous function inside another function.


