# ============================================================
# ATM PROJESİ - Banka Otomasyon Sistemi Simülasyonu
# Bu projede dictionary, while döngüsü, if-elif-else ve input kullanımı gösterilmektedir.
# ============================================================

# Kullanıcı veritabanı: Her kullanıcının şifresi ve başlangıç bakiyesi tutulur
# Dictionary içinde dictionary yapısı kullanılmıştır (iç içe dictionary)
kullancilar={
    "kerem":{"sifre":"123","bakiye":160},
    "berivan":{"sifre":"6057","bakiye":20000},
    "mizgin":{"sifre":"1946","bakiye":100000}
}

# Kullanıcıdan kullanıcı adı alınır
username=input("kullanıcı adınızı giriniz:")

# Kullanıcı adı sistemde kayıtlı mı kontrol edilir (in operatörü ile)
if username in kullancilar:
    
    # Şifre deneme hakkı: 3 yanlış denemede kart bloke olur
    hak=3
    # Şifre kontrol döngüsü - hak bitene kadar devam eder
    while hak>0:
        sifre=input("Şifrenizi giriniz")
        # Girilen şifre, kullanıcının kayıtlı şifresi ile eşleşiyor mu?
        if sifre==kullancilar[username]["sifre"]:
            print("Hesaba giriş yapıldı")
            break  # Doğru şifre - döngüden çık, ATM menüsüne geç
        else:
            print("şifreniz yanlış")
            hak=hak-1  # Her yanlış denemede hak 1 azalır
    
    # Tüm haklar tükendiyse kart bloke mesajı
    if hak==0:
        print("Kartınız Bloke Olmuştur Hayırlı Uğurlu olmasın")
    # Şifre doğru girildiyse ATM işlem menüsüne geç
    else:
        # Kullanıcının bakiyesi yerel değişkene alınır (işlemler için)
        bakiye=kullancilar[username]["bakiye"]
        # Sürekli menü döngüsü - kullanıcı çıkış seçene kadar devam eder
        while True:
            # ATM ana menü ekranı (çok satırlı string)
            print("""
            (1) Bakiye Görüntüle
            (2) Para Çek
            (3) Para Yatırma
            (4) Çıkış
            
            """)

            secim=input("Seçiminizi Yapınız:")

            if secim=="1":
                # Seçim 1: Mevcut bakiyeyi ekranda göster
                print(bakiye)
            elif secim=="2":
                # Seçim 2: Para çekme işlemi
                miktar=int(input("kaç para çekmek istiyorsunuz:"))
                # Bakiye yeterli mi kontrol et
                if miktar<=bakiye:
                    bakiye=bakiye-miktar  # Bakiyeden düş
                    print("Kalan Bakiyeniz:",bakiye)
                else:
                    print("Bakiyeniz Yeterli Değil")
            elif secim=="3":
                # Seçim 3: Para yatırma işlemi
                miktar=int(input("Kaç Para Yatıracaksınız:"))
                bakiye=bakiye+miktar  # Bakiyeye ekle
                print("Toplam Bakiyeniz",bakiye)
            elif secim=="4":
                # Seçim 4: Çıkış - döngüden break ile çıkılır
                print("güle güle")
                break
