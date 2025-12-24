#1. input() – Kullanıcıdan veri alma

#Amaç: Programın sadece kendi kendine değil, kullanıcıyla etkileşimde olması.



isim = input("Adın ne? ")
print("Memnun oldum", isim)

#📝 Açıklama:
#“Bilgisayarı konuşan bir arkadaş gibi düşünün. Siz bir şey söylüyorsunuz, o da cevap veriyor.”



#2. Tip dönüşümleri – int(), str()

#Problemin öğrenilmesi için örnek:

yas = input("Kaç yaşındasın? ")
print(yas + 5)

#Bu hata verecek. Çünkü yas bir string.

#Sonra çözümü göster:

yas = int(input("Kaç yaşındasın? "))
print("5 yıl sonra yaşın:", yas + 5)


#"Bilgisayara 12 yazsan bile bunu yazı (string) gibi görür. Matematik yapmak için sayıya çevirmeliyiz."


#3. Karşılaştırma Operatörleri

#== (eşit mi?)

#!= (eşit değil mi?)

#>, <, >=, <=


#🎯 Basit Örnek:

sayi = int(input("Tahmin et: Ben kaç sayısını tuttum? "))
print(sayi == 7)

#Sonuç True/False olarak çıkar, çocuklar eğlenir.


#4. if – else tekrar ama gerçek bir senaryoda

#“Öğrencilerin anlayacağı gerçek hayat örnekleri”

#🍔 Yemek Sipariş Sistemi

yemek = input("Ne yemek istersin? (pizza / hamburger): ")

if yemek == "pizza":
    print("Pizza 75 TL!")
elif yemek == "hamburger":
    print("Hamburger 60 TL!")
else:
    print("Menüde o yok :)")


#5. Basit Proje: Mini Hesap Makinesi

#Bu hem operatörleri tekrar ettirir hem de input-if kullanımını oturtur.

print("Mini Hesap Makinesine Hoşgeldiniz!")
sayi1 = int(input("Birinci sayıyı gir: "))
sayi2 = int(input("İkinci sayıyı gir: "))
islem = input("İşlem seç (+, -, *, /): ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    print("Sonuç:", sayi1 / sayi2)
else:
    print("Geçersiz işlem!")

#🧠 Burada öğrenci tüm öğrendiklerini tek bir kod içinde kullanmış olur.


#🎮 6. Eğlenceli Mini Proje (5 dk): Yaş Testi Oyunu

yas = int(input("Yaşın kaç? "))

if yas < 13:
    print("Sen bir çocuksun! 🍭")
elif yas < 18:
    print("Gençsin! ⚡")
else:
    print("Yetişkisin! 💪")