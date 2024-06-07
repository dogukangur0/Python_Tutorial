ogrenciler = {
    '120':{
        'isim' : 'Mehmet',
        'yas' : '25' ,
        'telefon' : '12345'
    },
    '125':{
        'isim' : 'Ahmet',
        'yas' : '15' ,
        'telefon' : '12325'
    }
}

ogrenciId = input("Öğrenci ID numarası gir:")
ogrenciIsim = input("Öğrenci isim gir:")
ogrenciYas = input("Öğrenci yaş gir:")
ogrenciTelefon = input("Öğrenci telefon gir:")

ogrenciler[ogrenciId] = {
    'isim' : ogrenciIsim,
    'yas' : ogrenciYas,
    'telefon' : ogrenciTelefon 
    }

print(ogrenciler)

ogrenciId = input("Öğrenci ID numarası gir:")
ogrenci = ogrenciler[ogrenciId]
print(ogrenci)
