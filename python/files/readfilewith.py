with open("textfile.txt","r",encoding="utf_8") as f:
    print(f.read(10)) # 10.karaktere kadar okur
    print(f.tell()) # kaçıncı satırda olduğunu söyler
    print(f.read()) # okumaya kaldığı yerden devam eder.and
    print(f.tell()) # kaçıncı satırda kaldığını söyler
    
