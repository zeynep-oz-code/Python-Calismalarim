# Sayı Filtreleme ve Toplam:

# sayilar = [12, 5, 8, 20, 33, 44, 15, 60] #listesindeki 10'dan büyük ve 3'e tam bölünebilen sayıları ekrana yazdırıp toplamlarını hesaplayın.
# sum = 0
# for number in sayilar :
#     if number > 10 and number % 3 == 0 :
#         print(f"Eligible number : {number}")
#         sum+=number
# print(sum)


# Kelimeleri İşleme:

isimler = ["Ahmet", "Mehmet", "Ali", "Canan", "Ece"] #listesindeki her ismin karakter sayısını (uzunluğunu) ve 5 karakterden uzun olan isimleri ekrana yazdırın.

# for name in isimler :
#     length = len(name)
#     print(f"name : {name} and length : {length}")
#     if length > 5 :
#         print(name)

# Matematiksel Aralık (Range) İşlemleri:

# 1 ile 50 arasındaki sayılardan hem 3'e hem de 5'e tam bölünebilen sayıları ve bu sayıların kaç adet olduğunu bulun.
# count = 0
# for i in range(1,51):
#     if i%3 == 0 and i%5 == 0 :
#         print(f"match : {i}")
#         count +=1
# print(f"Total count : {count}")

# Metin Analizi:

# Kullanıcıdan alınan bir metindeki (string) sesli harflerin (a, e, ı, i, o, ö, u, ü) sayısını ve hangi harfler olduğunu ekrana yazdırın.

# text = input("enter a sentence: ").lower() #----> hem küçük hem de büyük harfleri tek seferde yakalamak için .lower() metodunu kullanabilirsin.
# vowels = "aeiou"
# found_vowels = [] #----->list to store found vowels
# for char in text: #----> eğer rwxtin içeriği ile işin varsa büyük harfleri değiştirmeyip sadece for satırına in text.lower() ekleyebilirsin.
#     if char in vowels:
#         found_vowels.append(char)
# print(f"orginal text: {text}")
# print(f"found vowels: {found_vowels}")
# print(f"total vowel count: {len(found_vowels)}")         

# Sözlük (Dictionary) Elemanlarını Listeleme:

ogrenciler = [{"ad": "Ali", "not": 75}, {"ad": "Ayşe", "not": 90}, {"ad": "Can", "not": 45}] #yapısındaki öğrencilerden notu 50'nin üzerinde olanların isimlerini ve durumunu (Geçti) for ile listeleyin.

for student in ogrenciler :
    if student["not"] >= 50:
        print(f"passed: {student['ad']}, note: {student['not']}")
        