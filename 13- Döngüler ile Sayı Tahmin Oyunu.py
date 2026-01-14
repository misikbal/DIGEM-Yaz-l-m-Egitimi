from random import randint

from sayitahmin import tahmin

tutulan_sayi=randint(1,10)
hak=3
while True:
    tahmin_sayi=int(input("1-10 Arasında Sayı Tamininizi Yazınız:"))
    if hak==0:
        print("Hakkınız kalmadı")
        print(tutulan_sayi)
        break
    else:
        hak=hak-1
        if tutulan_sayi==tahmin_sayi:
            print("Tahminiz Doğru Tebrikler")
            break
        elif tutulan_sayi>tahmin_sayi:
            print("Daha büyük bir sayı giriniz")
        elif tutulan_sayi<tahmin_sayi:
            print("Daha küçük bir sayı giriniz")
        print(hak," hakkınız kaldı")

