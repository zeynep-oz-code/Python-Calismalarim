# Bankamatik Uygulaması
# Aşağıdaki bilgileri ve fonksiyonları içeren bir Python programı yazmanı bekliyoruz.

# 1. Başlangıç Verileri
# Programın başında bir kullanıcı hesabı tanımla (sözlük/dictionary veya değişkenler kullanabilirsin):

# Kullanıcı Adı: "Ahmet"

# PIN Kodu: "1234"

# Bakiye: 5000 (TL)

# 2. Yazmanı İstediğimiz Fonksiyonlar
# pin_kontrol(girilen_pin)

# Kullanıcının girdiği PIN doğru mu diye kontrol etsin.

# Doğruysa True, yanlışsa False döndürsün (return).

# bakiye_sorgula(bakiye)

# Mevcut bakiyeyi ekrana yazdırsın.

# para_yatir(bakiye, miktar)

# Gelen miktar pozitif ise bakiyeye eklesin ve güncel bakiyeyi return etsin.

# Miktar 0 veya negatifse uyarı verip mevcut bakiyeyi aynen döndürsün.

# para_cek(bakiye, miktar)

# Çekilmek istenen miktar bakiyeden büyükse "Yetersiz bakiye!" uyarısı versin ve bakiyeyi değiştirmeden döndürsün.

# Çekilmek istenen miktar uygunsa bakiyeden düşsün ve yeni bakiyeyi return etsin.

# 3. Ana Program Akışı (Döngü Yapısı)
# Program başladığında kullanıcıdan PIN Kodu istensin (En fazla 3 hak verilsin).

# PIN doğru girilirse bir Menü gösterilsin:

# Bakiye Sorgula

# Para Yatır

# Para Çek

# Çıkış Yap

# Kullanıcı 4 yazana kadar bu menü bir while döngüsü içinde tekrar etsin.
Kullanici_adi = "Zeynep"

PIN_Kodu = "1234"

Bakiye = 5000 

def pin_giris_kontrol():
    PIN_kodu = "1234"
    hak=3

    while hak > 0:
        girilen_PIN = input("PIN GİRİNİZ:")

        if girilen_PIN==PIN_kodu :
           return True
        else :
            hak -= 1
            print("YANLIŞ PIN!")
    if hak == 0 :
        print("HAKKINIZ BİTTİ")
        return False   

def  bakiye_sorgula(Bakiye):
    print(f"Mevcut bakiyeniz {Bakiye} TL" )
    return Bakiye    

def para_yatir(Bakiye):
    yatir_para_miktari = int(input (" yatırmak istediğiniz miktarı giriniz:"))
    Bakiye += yatir_para_miktari
    print(f"Hesabınıza {yatir_para_miktari} TL yatırıldı.Güncel bakiyeniz: {Bakiye} TL.")
    return Bakiye    


def para_cek(Bakiye):
    cek_para_miktari = int(input("çekmek istediğiniz miktarı giriniz:"))

    if cek_para_miktari<= Bakiye:
        Bakiye -= cek_para_miktari
        print(f"Hesabınızdan {cek_para_miktari} TL çekildi.Güncel bakiyeniz: {Bakiye} TL")
        return Bakiye
    else :
        print("Yetersiz bakiye!")
        return Bakiye    


if pin_giris_kontrol():
    print("PIN doğru. Menüye yönlendiriliyorsunuz.")

    while True:
            print("----MENU----")
            print("1- BAKİYE SORGULA")
            print("2- PARA YATIR")
            print("3- PARA ÇEK")
            print("4- ÇIKIŞ")
        
            choice= input("Select Operation (1-4): ").strip()

            if choice == "1":
                bakiye_sorgula(Bakiye)

            elif choice == "2":
               Bakiye = para_yatir(Bakiye)

            elif choice == "3":
                Bakiye = para_cek(Bakiye)

            elif choice== "4":
                print(f"İyi Günler Dileriz {Kullanici_adi} ." )
                break    

            else :
                print("geçersiz tuş")    

        
