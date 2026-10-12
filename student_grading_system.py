# Bir sınıftaki öğrencilerin sınav notlarını (vize ve final) sisteme kaydeden, bu notlara göre geçme ortalamasını ve harf notunu hesaplayan, ardından tüm öğrencileri listeyle ekrana basan interaktif bir konsol (terminal) uygulaması yazmak.

# Yani dışarıdan kullanıcı verisi alacak, bu verileri fonksiyonlar aracılığıyla işleyecek, matematiksel hesaplamalar ve koşullar (if-else) yapıp sonuçları ekrana düzenli bir şekilde yazdıracaksın.


     
ogrenci_listesi = []

def ogrenci_ekle():

        while True:
            ad_soyad = input("Ögrencinin adını soyadını giriniz(Çıkış için 'q' yazınız.) ")
            if ad_soyad.lower() == 'q':
                break # iç döngüden çıkıp ana menüye döner.
                    
            vize_notu = int(input("Ögrencinin vize notunu giriniz: "))
            final_notu = int(input("Ögrencinin final notunu giriniz: "))

            ogrenci = {
            "ad": ad_soyad,
            "vize": vize_notu,
            "final": final_notu
            }

            ogrenci_listesi.append(ogrenci)


def harf_notu_hesapla(ortalama):
    if 0 <= ortalama < 50:
        return "FF"
    elif 50 <= ortalama < 65:
        return "DC"
    elif 65 <= ortalama < 80:
        return "BB"
    elif 80 <= ortalama <= 100:
        return "AA"

def not_ortalama_hesapla():
    print("\n" + "=" * 65)
    print(f"{'ÖĞRENCİ ADI SOYADI':<20} | {'VİZE':<6} | {'FİNAL':<6} | {'ORTALAMA':<8} | {'HARF'}")
    print("=" * 65)
    
    for ogrenci in ogrenci_listesi:
        ortalama = (ogrenci["vize"] * 0.4) + (ogrenci["final"] * 0.6)
        harf = harf_notu_hesapla(ortalama)
        
        # Sütunlar halinde düzgün bir tablo yazdırıyoruz
        print(f"{ogrenci['ad']:<20} | {ogrenci['vize']:<6} | {ogrenci['final']:<6} | {ortalama:<8.1f} | {harf}")
    
    print("=" * 65)


while True:
     print("----ÖGRENCİ NOT SİSTEMİ----")
     print("1-Ögrenci Ekle")
     print("2-Notları ve Ortalamaları Hesapla")
     print("3-Çıkış")

     choice = input("Hangi işlemi gerçekleştirmek istiyorusunuz (1/2/3):  ")


     if choice == "1":
          ogrenci_ekle()
     elif choice == "2":
          not_ortalama_hesapla()    
     elif choice == "3":
          print("Sistemden çıkış yapılıyor. İyi günler.")
          break
     else :
          print("Geçersiz Seçim!")
          
