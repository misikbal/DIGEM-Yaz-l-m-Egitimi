meyveler=["çilek","kivi","fark etmiyor","domates","muz","ananas"]
print("berivan en fazla ",meyveler[2]," meyvesini seviyor")
print("taha en fazla ",meyveler[-1]," meyvesini seviyor")

toptanci=input("Hangi Meyveyi almak isityorusunuz?")
meyveler.append(toptanci)
print(meyveler)

ayarlar=("Ses","Türkçe","Dark Mode","deneme.com")
print(ayarlar[2])

ayarlar.append("x.com")


kütüphane=[   
{
    "ad":"Ali",
    "soyad":"Yılmaz",
    "yas":20,
    "sehir":"İstanbul",
    "okul":"İstanbul Üniversitesi",
    "tc":"12345678901"
},
{
    "ad":"Ayşe",
    "soyad":"Kaya",
    "yas":25,
    "sehir":"Ankara",
    "okul":"Ankara Üniversitesi",
    "tc":"12345678902"
}
]
kütüphane.remove(kütüphane[1])
print(kütüphane)
add_user=input("Yeni Kullanıcı Adınızı Giriniz:")
add_surname=input("Yeni Kullanıcı Soyadınızı Giriniz:")
add_age=int(input("Yeni Kullanıcı Yaşınızı Giriniz:"))
add_city=input("Yeni Kullanıcı Şehirinizı Giriniz:")
add_school=input("Yeni Kullanıcı Okulunuzu Giriniz:")
add_tc=input("Yeni Kullanıcı TC Kimlik Numaranızı Giriniz:")
kütüphane.append({
    "ad":add_user,
    "soyad":add_surname,
    "yas":add_age,
    "sehir":add_city,
    "okul":add_school,
    "tc":add_tc
})
print(kütüphane)