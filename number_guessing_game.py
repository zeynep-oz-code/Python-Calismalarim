
# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
# buldurmaya çalışın. (hak = 5)

# ** "random modülü" 
# ** 100 üzerinden puanlama yapın. Her soru 20 puan.
# ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
#    üzerinden hesaplansın.

import random
sayi=random.randint(1,100)
can = int(input("Kaç hak kullanmak isterseniz: "))
hak = can 
soru_basina_puan = 100 / can

while hak > 0 :
    tahmin= int(input("Sayıyı tahmin edin: "))

    if tahmin > sayi :
        print("Daha küçük sayı tahmin edin.")
        hak = hak - 1
        print(f"kalan hakkınız: {hak}")
    elif tahmin < sayi:
        print("daha büyük sayı tahmin edin.")
        hak = hak -1
        print(f"kalan hakkınız: {hak}")
    else :
        print("doğru tahmin!")
        toplam_puan= soru_basina_puan *hak
        print(toplam_puan)
        break


