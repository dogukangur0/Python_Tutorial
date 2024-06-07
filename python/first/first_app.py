website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

courseLength = len(course)
print(courseLength)

wwwWebsite = website[7:10] # başlangıçtan al bittiği yerden bir sonraki yerde bitir.
print(wwwWebsite)

comWebsite = website[-3:] # tersten giderken en sondakini alacakken  değer girmeye gerek yok. Bittiği yere giderken o satırı yazman yeterli
print(comWebsite)

first_15_in_course = course[:15]
last_15_in_course = course[-15:]
print(first_15_in_course)
print(last_15_in_course)

terstenYazCourse = course[::-1]
print(terstenYazCourse)


name, surname, age, job = 'Bora','Yılmaz',32,'mühendis'

info = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}."
infoSecondPath = 'Benim adım {} {}, Yaşım {} ve mesleğim {}.'.format(name,surname,age,job)

print(info)
print(infoSecondPath)
