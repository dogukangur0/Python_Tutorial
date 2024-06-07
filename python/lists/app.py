# 1.
listCars = ["Toyata","BMW","Renault","Mercedes"]

print(len(listCars)) # 4

print(listCars[0]+" "+listCars[-1])

listCars[2] = "Togg"

print(listCars)

result = "Togg" in listCars
print(result)

print(listCars[0:2])

listCars = listCars + ["Ford","Citroen"]
print(listCars)

del listCars[-1]
print(listCars)

#2.

ogrenciYigit = ["Yigit","Bilgi",2010, [70,80,90]]
ogrenciAda = ["Ada","Bilgi",2011, [70,70,80]]
ogrenciAli = ["Ali","Bilgi",2017, [60,60,90]]

currentYear = 2024
calculateAgeYigit = currentYear - ogrenciYigit[2]
calculateAgeAda = currentYear - ogrenciAda[2]
calculateAgeAli = currentYear - ogrenciAli[2]
print(f" {ogrenciYigit[0]} is {calculateAgeYigit} years old,{ogrenciAda[0]} is {calculateAgeAda} years old and {ogrenciAli[0]} is {calculateAgeAli} years old")

calculateAvarageYigit = (float)(ogrenciYigit[3][0]+ogrenciYigit[3][1]+ogrenciYigit[3][2])/3
calculateAvarageAda = (float)(ogrenciAda[3][0]+ogrenciAda[3][1]+ogrenciAda[3][2])/3
calculateAvarageAli = (float)(ogrenciAli[3][0]+ogrenciAli[3][1]+ogrenciAli[3][2])/3 
print(f"Chilren avarages are {ogrenciYigit[0]} is {calculateAvarageYigit},{ogrenciAda[0]} is {calculateAvarageAda} and {ogrenciAli[0]} is {calculateAvarageAli}")