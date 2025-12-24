sayi1=int(input("1.Sayınızı Giriniz:"))
sayi2=int(input("2.sayınızı giriniz:"))
islem=input("Hangi İşlemi Yapacaksınız: + - * /:")


if islem=="+" or islem=="toplama":
    print("Toplam:",sayi1+sayi2)
elif islem=="-":
    print("Çıkarma:",sayi1+sayi2)
elif islem=="*":
    print("Çarpma:",sayi1*sayi2)
elif islem=="/":
    if sayi2==0:
        print("Sıfıra bölünemez")
    else:
        
        print("Bölme:",round(sayi1/sayi2,2))
else:
    print("Geçersiz İşlem")