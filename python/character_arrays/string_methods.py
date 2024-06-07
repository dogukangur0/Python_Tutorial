title = "Python programlama kursu"

result1 = title.upper()
result2 = title.lower()
result3 = title.title()       # kelimelerin baş harfi
result4 = title.capitalize()  # ilk kelimenin baş harfi

print(result1)
print(result2)
print(result3)
print(result4)


result5 = "abc".isupper()  # hepsi büyük harf mi ? islower() hepsi küçük harf mi ?
print(result5)


message = "   Hello   "
result6 = message.strip() # boşlukları kapatır
result7 = title.split()  # default olarak her boşluk olduğunda verileri ayrıştırır ve liste oluşturur.
result8 = title.split('a')  # her a karakterinden sonra verileri ayrıştırır ve liste oluşturur.

print(result6)
print(result7)
print(result8)  


result9 = title.index("programlama")
# title.startswith("a") a ile mi başlıyor ?  bool
# title.endswith("a") a ile mi bitiyor ?     bool
# title.replace("Python","Kotlin")
print(result9)


# title 'kursu' kelimesi içeriyor mu ?

result10 = title.find("kursu")  # bu değişken sonuç bulamazsa return -1 olarak ayarlar.
result11 = title.index("kursu") # bu değişken sonuç bulamazsa hata verir.