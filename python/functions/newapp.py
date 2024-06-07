accounts = [
    {
        "name":"Dogukan",
        "account_no":123456,
        "bakiye":10000,
        "ekHesap":5000,
        "username":"dogukan",
        "password": "12345"
    },
    {
        "name":"Dgkn",
        "account_no":987654,
        "bakiye":20000,
        "ekHesap":2000,
        "username":"dgkn",
        "password":12345
    }
]
name = ""
password = ""

def login():
    username = input("Username giriniz: ")
    password = int(input("Password giriniz: "))

    isLogged = False

    for account in accounts:
        if account["username"] == username and account["password"] == password:
            print("Hoşgeldiniz")
            isLogged = True
            menu(account)
    if not (isLogged):
        print("username ya da parola yanlış!")
        
login()
    
def menu(account):
    print("\n")
    print(f"Hoşgeldiniz {account["name"]}")
    print("1-Bakiye Sorgulama")
    print("2-Para Çekme")
    print("3-Para Yatırma")
    
    islem = input("Yapmak İstediğiniz İşlemi Seçiniz: ")

    if islem == "1":
        bakiyeSorgula(account)
    elif islem == "2":
        paracek(account)
    else:
        print("Hatalı Seçim Yaptınız")


def bakiyeSorgula(account):
    print(f"Merhaba {account["name"]} hesabınızın bakiyesi {account["bakiye"]}")
    

def paracek(account):
    miktar = input("Ne kadar para çekmek istediğinizi yazınız lütfen : ")
    if miktar > account["bakiye"]:
        print("Hesabınızda istediğiniz miktar kadar para bulunmamaktadır.")
        secim = input("Ek hesabı kullanmak ister misiniz ? (e/h)")
        if secim == "e":
            ekHesapMiktar = int(input("Ek hesabın ne kadarını kullanmak istersiniz ? :"))
            if ekHesapMiktar > account["ekHesap"]:
                print("Ek hesabınız da çekmek istediginiz tutar bulunmamaktadır.")
                anotherIslem = input("Başka bir işlem yapmak ister misiniz (e/h) ? :")
                if anotherIslem == "e":
                    menu(account)
            else:
                total = miktar + ekHesapMiktar
                if total > account["bakiye"]+account["ekHesap"]:
                    print("Yeterli miktarda para bulunmamaktadır.")
                    anotherIslem = input("Başka bir işlem yapmak ister misiniz (e/h) ? :")
                    if anotherIslem == "e":
                        menu(account)
                else:
                    account["bakiye"] -= miktar
                    account["ekHesap"] -= ekHesapMiktar
                    print(f"Para çekme işlemi başarılı hesabınızda kalan para bakiye: {account["bakiye"]}  /// ekHesap : {account["ekHesap"]}") 
        elif secim == "h":
            anotherIslem = input("Başka bir işlem yapmak ister misiniz (e/h) ? :")
            if anotherIslem == "e":
                menu(account)
    else:
        account["bakiye"] -= miktar
        print(f"Para çekme işlemi başarılı hesabınızda kalan para {account["bakiye"]}") 







        
        


            
