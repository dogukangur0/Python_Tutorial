carInformations = {
    "carBrand" : "Mercedes",
    "carYear" : 2023,
    "carColor" : "Black",
    "carImage" : "image.jpg"
}

# access items

result = carInformations["carBrand"]
result = carInformations["carColor"]
result = carInformations.get("carYear")

result = carInformations.keys()   # dictionary içerisindeki key bilgilerini listeler.
result = carInformations.values() # dictionary içerisindeki value bilgilerini listeler.

result = carInformations.items()  # key-value verilerini birlikte listeler.

# update items

result = carInformations["carBrand"] = "BMW"
result = carInformations.update({"carBrand":"Audi"})
result = carInformations.update({"carYear":2024})
result = carInformations.update({"carEngine":2.0})

# delete items

carInformations.pop("carEngine")

carInformations.popitem()  # fonksiyon içerisine parametre göndermeye gerek yok, otomatik olarak son elemanı siler.
carInformations.clear()    # liste içerisindeki tüm elemanları siler
print(carInformations)