hesapA = {
    'ad' : 'Xyz',
    'hesapNo' : '12345',
    'bakiye' : 200,
    'ekhesap' : 100
}

hesapB = {
    'ad' : 'Abc',
    'hesapNo' : '13215',
    'bakiye' : 400,
    'ekhesap' : 200
}


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap['bakiye']>miktar):
        print("Para çekebilirsiniz")
    else:
        toplam = hesap['bakiye']+hesap['ekhesap']
        if(toplam>=miktar):
            ekHesapKullanimi = input('ek hesap kullan: (e/h)')
            if(ekHesapKullanimi=='e'):
                print("Para çekebilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir")
        else:
            print("Bakiye yetersiz")
paraCek(hesapA,250)