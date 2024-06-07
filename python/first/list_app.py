carList = ["BMW","Mercedes","Opel","Mazda"]
lenCarList = len(carList)
print(lenCarList)
print(carList[0])
print(carList[-1])

carList[-1] = "Toyata" # son indexi değiştir.

print(carList)

isMercedesEleman = "Mercedes" in carList # içerisinde mercedes var mı ?
print(isMercedesEleman)

print(carList[-2]) # -2 index
print(carList[:3]) # listenin ilk 3 elemanı

carList[-2:]=["Toyata","Renault"]  # son 2 eleman yerine bu değerleri ekle

carList = carList + ["Audi","Nissan"] # listenin sonuna bu değerleri ekle
print(carList)

del carList[-1] # listenin son elemanını sil
print(carList)

terstenListele = carList[::-1] # tersten listele
print(terstenListele)

