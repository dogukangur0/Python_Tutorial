cities = ["kocaeli","ankara","istanbul"]
numbers = [41,6,34]

print(cities[numbers.index(41)])
print(numbers[cities.index("ankara")])


# dictionary

plakalar = {
    "kocaeli":41,
    "ankara":6,
    "istanbul":34,
    "izmir":42
}

print(plakalar)

plakalar["izmir"] = 35  # daha sonra bu şekilde güncelleme yapabiliriz.


print(plakalar) 


students = {
    101 : {
        "ad":"Yiğit",
        "soyad":"Bilgi",
        "dogumyili":2010,
        "notlar":(40,80,90)
    },
    102 : {
        "ad":"Ada",
        "soyad":"Bilgi",
        "dogumyili":2012,
        "notlar":(80,80,80)
    },
    103 : {
        "ad":"Murat",
        "soyad":"Bilgi",
        "dogumyili":2017,
        "notlar":(70,70,70)
    }
}

numara = int(input("Numara : "))
student = students[numara]
avarage = (student["notlar"][0]+student["notlar"][1]+student["notlar"][2])/3

print(f"{numara} numaralı {student["ad"]} {student["soyad"]} ismindeki öğrencinin yaşı {2024-student["dogumyili"]} ve not ortalaması {avarage}.")





students = {
    101 : {
        "name":"Dogukan",
        "surname":"Gur",
        "birth":2000,
        "notes" : (40,60,100)
    },
    102 : {
        "name":"Melis",
        "surname":"Yilmaz",
        "birth":2003,
        "notes" : (50,60,80)
    },
    103:{
        "name":"Ahmet",
        "surname":"Simsek",
        "birth":2000,
        "notes" : (40,60,100)
    }
}

student_no = int(input("Enter the student number "))

studentName = students[student_no]["name"]
studentSurname = students[student_no]["surname"]
studentAge = 2024 - students[student_no]["birth"]
studentAvarage = (students[student_no]["notes"][0]+students[student_no]["notes"][1]+students[student_no]["notes"][2])/3

print(f"{student_no} numaralı {studentName} {studentSurname} ismindeki öğrencinin yaşı {studentAge} ve not ortalaması {studentAvarage}")




