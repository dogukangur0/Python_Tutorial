a = ["elma","armut"]
b = ["protakal","üzüm"]

a = b

print(a[0])



listA=[10,20]
listB = listA.copy()  # kopyalama 2.yöntem
# listB = list(listA)   # kopyalama 2.yöntem

print(listA,listB)

listB[0] = 34

print(listA,listB)