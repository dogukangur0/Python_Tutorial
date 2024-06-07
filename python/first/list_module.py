names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

names.append("Cenk") # listenin sonuna cenk eklendi
print(names)

names.insert(0, "Sena") # listenin başına sena eklendi
print(names)

#names.remove("Deniz") # listenin sonuna deniz çıkarıldı.
#print(names)

denizIndex = names.index("Deniz")
print(denizIndex)

result = "Ali" in names
if result == 1:
    print("Ali var")
else:
    print("Ali yok")

names.reverse()
print(names)

names.sort() # liste elemanlarını alfabetik sıralar
print(names)



str = "Chevrolet,Dacia" # stringini listeye çevir

result = str.split(",") # arada , olduğu için , baz alınarak çevrilir.

print(result)


maxYears = max(years) # maximum
print(maxYears)
minYears = min(years) # minimum
print(minYears)
count1998years = years.count(1998)
print(count1998years)

years.clear() # remove
print(years)

print("3 tane marka bilgisi giriniz:")
first=input("1.marka bilgisi giriniz:")
second=input("2.marka bilgisi giriniz:")
third=input("3.marka bilgisi giriniz:")

myList = []
myList.append(first)
myList.append(second)
myList.append(third)
print(myList)
