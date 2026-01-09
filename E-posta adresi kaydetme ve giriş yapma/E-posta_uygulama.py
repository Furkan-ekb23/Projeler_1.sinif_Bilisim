liste = []

while True:
    email = input("Lütfen eklemek istediğiniz E-posta adresini giriniz (Bitirmek için 0): ")
    if email == "0":
        break
    liste.append(email)

while True:
    a = input("\nLütfen sisteme kayıtlı E-posta adresini giriniz: ")
    
    if a in liste:
        b = input("Lütfen şifrenizi giriniz: ")
        if b == "Furki1212":
            print("E-posta adresiniz ve şifreniz doğru.")
            print("Giriş başarılı.")
            break
        else:
            print("Şifre yanlış. Lütfen tekrar deneyin.")
    else:
        print("E-posta adresi bulunamadı. Lütfen tekrar deneyin.")