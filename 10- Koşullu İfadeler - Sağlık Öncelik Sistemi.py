yas=int(input("Yaşınız:"))
kronik=input("Kronik Bir Hastalığınız Var mı? e/h:")
hamile=input("Hamile Misiniz? e/h:")
acil=input("Acil Bir Durum Var mı? e/h:")

if acil=="e":
    print("1. seviye öncelikli hastasınız")
elif hamile=="e":
    print("2. seviye öncelikli hastasınız")
elif yas>=65 or kronik=="e":
    print("3. seviye öncelikli hastasınız")
else:
    print("4. seviye öncelikli hastasınız")
