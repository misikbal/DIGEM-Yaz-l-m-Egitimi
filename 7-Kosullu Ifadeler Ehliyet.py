print("**** Ehliyet Alma Programı ****")
yas=int(input("Yaşınızı Giriniz:"))
saglık=input("Sürüş İçin Engeliniz Var mı? e/h:")
ilkSinav=int(input("Teorik Sınavdan Kaç Aldınız?:"))
uygulamaSinavi=input("Uygulama Sınavını Geçtiniz mi? e/h:")

if yas>=18:
    print("Yaşınız Uygun")
    if saglık=="h":
        print("Sağlık Engelniz Yoktur")
        if ilkSinav>=70:
            print("Teorik Sınav Notunuz Uygundur")
            if uygulamaSinavi=="e":
                print("Ehliyet Almaya Hak Kazandınız")
            else:
                print("Uygulama Sınavından Kaldınız")
        else:
            print("Teorik Sınavdan Yeterli Not Alamadınız")
    else:
        print("Sağlık Durumunuz Uygun Değildir")
else:
    print("Yaşınız Küçük")