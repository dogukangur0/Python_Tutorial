fruits = {"apple","banana","pear"}

# results = fruits[0] # şeklinde indexler okunmaz

result = "apple" in fruits # True

fruits.add("orange")  # random added to set class, not last index -> random

# remove ve discard fonksiyonları set içerisinden istenilen elemanı siler. remove kullanılırken eğer eleman yoksa hata döner #
# pop komutu da set içerisinden random bir eleman siler. (paremetre almaz)
print(fruits)
