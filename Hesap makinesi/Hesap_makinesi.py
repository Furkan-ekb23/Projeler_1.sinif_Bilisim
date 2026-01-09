sayi1 = int(input("1. sayıyı gir: "))
sayi2 = int(input("2. sayıyı gir: "))

print("İşlemler")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")

secim = int(input("Seçimin: "))

if secim == 1:
    print("Sonuç:", sayi1 + sayi2)
elif secim == 2:
    print("Sonuç:", sayi1 - sayi2)
elif secim == 3:
    print("Sonuç:", sayi1 * sayi2)
elif secim == 4:
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Hata: 0'a bölünemez")
else:
    print("Geçersiz seçim")