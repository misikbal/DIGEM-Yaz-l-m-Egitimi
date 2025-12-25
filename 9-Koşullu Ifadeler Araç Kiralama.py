yas = int(input("Yaş: "))
ehliyet = int(input("Ehliyet yılı: "))
hasar = input("Geçmiş hasar var mı? (evet/hayır): ")

if yas >= 25:
    if ehliyet >= 5:
        if hasar == "hayır":
            print("Araç kiralanabilir")
        else:
            print("Kiralanamaz")
    else:
        print("Kiralanamaz")
elif yas >= 23:
    if ehliyet >= 3:
        print("Ek depozito ile kiralanabilir")
    else:
        print("Kiralanamaz")
else:
    print("Kiralanamaz")