

username=input("Kullanıcı Adınızı Giriniz:")
password=input("Şifrenizi Giriniz:")

dogru_username="admin"
dogru_password="123456"

if username ==dogru_username:
    if password==dogru_password:
        print("Login Success")
    else:
        print("Password is wrong")
else:
    print("Username is wrong")
        
