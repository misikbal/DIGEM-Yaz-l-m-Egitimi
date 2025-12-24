times=float(input("Otoparkta ne kadar süre kaldınız:"))
car_type=input("Araç Tipiniz Nedir (otomobil, motor, kamyon):")
vip=input("VIP misiniz? (e/h):")
no_ticket=input("Kayıp Bilet Var mı? (e/h):")

if car_type=="otomobil":
    clock_price=30
elif car_type=="kamyon":
    clock_price=60
elif car_type=="motor":
    clock_price=20
else:
    print("hatalı giriş! araç tipi bulunumadı")

if times<=1 and times>=0:
    total_price=0
    print("1 saaten az kaldığımız için ücret ödemiyorsunuz")

elif times>1:
    if times>10:
        if vip=="h" and no_ticket=="h":
            print("Araban otoparkta çok kaldı bu yüzden %20 zam yapılacak")
            total_price=(times*clock_price)*1.20
            print("Ödenecek Tutar:",total_price)
        elif vip=="e" and no_ticket=="h":
            total_price=(times*clock_price)*1.20*0.70
        elif no_ticket=="e":
            total_price=((times*clock_price)*1.20)+200
    
    elif vip=="e" and no_ticket=="h":
        total_price=(times*clock_price)*0.70
        print(total_price)
    elif vip=="h" and no_ticket=="h":
        total_price=times*clock_price
        print("Toplam Tutar:",total_price)
    elif no_ticket=="e":
        total_price=(times*clock_price) + 200
        print("200 lira ceza kesildi! ",total_price)

    
    else:
        print("hatalı bir işlem yaptınız")

else:
    print("Süre ile ilgili hatalı giriş yaptınız")