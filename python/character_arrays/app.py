title = "Python ile Programlama Dersleri"

# title değişkeni içerisindeki karakter sayısı ?
lenTitle = len(title)
print(lenTitle) # 31

# title içerisinden Python kelimesini al
takePython = title[0:6]
print(takePython)

# ilk 5 ve son 5 karakteri al

first5 = title[0:6]
last5 = title[-6:]
print(first5+" "+last5)

# title tersten yaz
last5 = title[::-1]
print(last5)

# string format kullanımı 
print("First Exam: ")
firstExam = int(input())
print("Second Exam: ")
secondExam = int(input())
avarage = (firstExam+secondExam)/2
title = f"Dogukan Gur isimli öğrencinin 1. notu {firstExam}, 2.notu {secondExam} ve not ortalaması {avarage} olarak hesaplanmıştır"

print(title)