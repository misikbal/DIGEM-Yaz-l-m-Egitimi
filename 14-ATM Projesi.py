kullancilar={
    "kerem":{"sifre":"123","bakiye":160},
    "berivan":{"sifre":"6057","bakiye":20000},
    "mizgin":{"sifre":"1946","bakiye":100000}
}

username=input("kullanıcı adınızı giriniz:")

if username in kullancilar:
    
    hak=3
    while hak>0:
        sifre=input("Şifrenizi giriniz")
        if sifre==kullancilar[username]["sifre"]:
            print("Hesaba giriş yapıldı")
            break
        else:
            print("şifreniz yanlış")
            hak=hak-1
    if hak==0:
        print("Kartınız Bloke Olmuştur Hayırlı Uğurlu olmasın")
    else:
        bakiye=kullancilar[username]["bakiye"]
        while True:
            print("""
            (1) Bakiye Görüntüle
            (2) Para Çek
            (3) Para Yatırma
            (4) Çıkış
            
            """)

            secim=input("Seçiminizi Yapınız:")

            if secim=="1":
                
                print(bakiye)
            elif secim=="2":
                miktar=int(input("kaç para çekmek istiyorsunuz:"))
                
                if miktar<=bakiye:
                    bakiye=bakiye-miktar
                    print("Kalan Bakiyeniz:",bakiye)

                else:
                    print("Bakiyeniz Yeterli Değil")
            elif secim=="3":
                
                miktar=int(input("Kaç Para Yatıracaksınız:"))
                bakiye=bakiye+miktar

                print("Toplam Bakiyeniz",bakiye)
            elif secim=="4":
                print("güle güle")
                break
