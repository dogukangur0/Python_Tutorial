# dosya oluşturmak içi open metodu kullanılır.

# open(file_name,access mode (default r))
# seek -> cursor konumu

f = open("textfile.txt","r",encoding="utf-8")

#print(f.read())

# dosya okuma mantığı cursor mantığına göredir. yani dosyayı okumaya başlar ve en son elemanı okuduktan sonra o satırın sonuna kadar gider
# eğer tekrar print ile dosya okuma işlemi yazdırırsak dosyanın sonuna gittiği için bir sonrakinde okunacak bir veri kalmaz.
# dosya okuma işlemi devam ettiği için eğer içeriye yeni veri eklenir ve dosya okuma işlemi yapılırsa son yapılan değişiklik ekrana bastırılır.
# böylece cursor sona alınmış olur.abs

# cursor başa almak için 
#f.seek(0) # ile başa alınır. tekrar okuma atapmak istediğimizde baştan başlayarak okuma sağlar.

#print(f.seek(10)) # 10.karakterden itibaren yazar 
#print(f.read())
# 1 satırdaki veri okunduktan sonra karakter sayma işlemi satırın sonuna kadar gider


print(f.readlines()) # readline -> her çalıştırıldığında satır okur.  readlines -> satırların hepsini liste halinde okur.

# f.closed -> dosyanın kapalı mı açık mı olduğunu söyler true,false

#f.close() -> dosyayı kapatmak için kullanılır  -> f.open ile tekrar açılır.