kullanici_listesi = []

def kayit_ol() :
    kullanici_ad = input("Adınızı giriniz.")
    kullanici_soyad = input("Soyadınızı giriniz.")
    kullanici_hesap_no = input("Hesap numaranızı giriniz.")
    kullanici_pin = input("4 Haneli PIN oluşturunuz.")

    kullanici = {
        "ad":  kullanici_ad,
        "soyad" :kullanici_soyad,
        "hesap_no":kullanici_hesap_no,
        "pin":kullanici_pin,
        "bakiye":0.0,
        "gecmis": [
            "Hesap oluşturuldu."    # İŞLEM GEÇMİŞİNİ TUTACAĞIMIZ LİSTE
        ],

    }

    kullanici_listesi.append(kullanici)

def para_yatir(aktif_kullanici):
        miktar = float(input("Yatırmak istediğiniz tutar:"))
        aktif_kullanici["bakiye"] += miktar
        aktif_kullanici["gecmis"].append(f"+{miktar} TL yatırıldı.")
        print(f"İşlem başarılı! Güncel bakiyeniz: {aktif_kullanici['bakiye']} TL. " )

def para_cek(aktif_kullanici):
        miktar = float(input("Çekmek istediğiniz miktar: "))

        if miktar <= aktif_kullanici["bakiye"]:
           aktif_kullanici["bakiye"] -= miktar
           aktif_kullanici["gecmis"].append(f"-{miktar} TL çekildi.")
           print(f"İşlem başarılı! Güncel bakiyeniz: {aktif_kullanici["bakiye"]} TL.")
        else:
           print("Yetersiz bakiye.")


def para_transferi(aktif_kullanici):
        alici_hesap_no = input("ALıcı hesabın hesap numarasını giriniz.")
        gonderilen_miktar = float(input("Göndermek istediğiniz miktarı yazınız."))

        if alici_hesap_no == aktif_kullanici["hesap_no"] :
           print("Hata : Kendi hesabınıza para gönderimi yapamazsınız")
           return
        
        if aktif_kullanici["bakiye"] < gonderilen_miktar :
           print("Yetersiz bakiye!")
           return

        aliciyi_bulduk_mu = False
        for diger_kullanici in kullanici_listesi:
           if diger_kullanici["hesap_no"] == alici_hesap_no :
              aliciyi_bulduk_mu = True

              aktif_kullanici["bakiye"] -= gonderilen_miktar
              aktif_kullanici["gecmis"].append(f"-{gonderilen_miktar} TL transfer edildi ({alici_hesap_no}).")

              diger_kullanici["bakiye"] += gonderilen_miktar
              diger_kullanici["gecmis"].append(f"+{gonderilen_miktar} TL transfer alındı. ({aktif_kullanici['hesap_no']})")

              print(f"İşlem başarılı. {gonderilen_miktar} TL başarıyla gönderildi.")
              break

        if not aliciyi_bulduk_mu :
           print("Hata: Hesap numarası bulunamadı!")  

def islem_gecmisi(aktif_kullanici):
    for islem in aktif_kullanici["gecmis"]:
        print(f"-{islem}")

        
def giris_yap() :
        girilen_hesap_no = input("Hesap numaranızı giriniz.")
        girilen_pin = input("4 Haneli şifrenizi giriniz.")

        for kullanici in kullanici_listesi :
          if  kullanici["hesap_no"] == girilen_hesap_no and kullanici["pin"] == girilen_pin :
             print("Giriş başarılı.")

             while True:
                print("-----Hesap işlemleri-----")
                print("1-Bakiye Sorgula")
                print("2-Para Yatır")
                print("3-Para Çek")
                print("4-Para Transferi")
                print("5-İşlem Geçmişi")
                print("6-Çıkış Yap")

                choice = input("İşlem Seçiniz(1-6): ")

                if choice == "1":
                   print(f"Güncel bakiyeniz {kullanici['bakiye']} TL")
                elif choice == "2":
                   para_yatir(kullanici)
                elif choice == "3":
                   para_cek(kullanici)
                elif choice == "4":
                   para_transferi(kullanici)
                elif choice == "5":
                   islem_gecmisi(kullanici)
                elif choice == "6":
                  print(f"Hesaptan çıkış yapılıyor.İyi günler dileriz {kullanici['ad']} {kullanici['soyad']}.")
                  break
                else :
                   print("Geçersiz işlem.")

# --- ANA PROGRAM DÖNGÜSÜ ---
while True:
  print("\n=== BANKA YÖNETİM SİSTEMİ ===")
  print("1- Kayıt Ol")
  print("2- Giriş Yap")
  print("3- Çıkış Yap")

  secim = input("Seçiminiz (1-3): ")

  if secim == "1":
    kayit_ol()
  elif secim == "2":
    giris_yap()
  elif secim == "3":
    print("Bankadan çıkış yapılıyor. İyi günler!")
    break
  else:
    print("Geçersiz seçim, lütfen tekrar deneyin.")


                   










                


