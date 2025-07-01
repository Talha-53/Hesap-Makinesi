def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("İşlemler: +, -, *, /")

    while True:
        try:
            sayi1 = float(input("Birinci sayı: "))
            islem = input("İşlem (+, -, *, /) veya çıkmak için 'q': ")
            if islem == 'q':
                print("Çıkılıyor...")
                break
            sayi2 = float(input("İkinci sayı: "))

            if islem == '+':
                sonuc = sayi1 + sayi2
            elif islem == '-':
                sonuc = sayi1 - sayi2
            elif islem == '*':
                sonuc = sayi1 * sayi2
            elif islem == '/':
                if sayi2 == 0:
                    print("Hata: Bir sayı sıfıra bölünemez.")
                    continue
                sonuc = sayi1 / sayi2
            else:
                print("Geçersiz işlem.")
                continue

            print(f"Sonuç: {sonuc}")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")


hesap_makinesi()
