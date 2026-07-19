# 1-  "Python", "Java", "C++", "JavaScript" elemanlarına sahip bir 'programlama_dilleri' listesi oluşturunuz.
# 2-  Oluşturduğunuz liste kaç elemanlıdır?
# 3-  Listenin ilk elemanını ve son elemanını ekrana yazdırınız.
# 4-  "C++" değerini "Go" ile değiştiriniz.
# 5-  "Java" listenin bir elemanı mıdır? Kontrol ediniz.
# 6-  Listenin -3 indeksindeki değer nedir?
# 7-  Listenin ilk 2 elemanını (slicing kullanarak) alın.
# 8-  Listenin son 2 elemanı yerine "Ruby" ve "Swift" değerlerini ekleyin.
# 9-  Listenin üzerine "C#" ve "Kotlin" değerlerini ekleyin (Listeyi genişletin).
# 10- Listenin ilk elemanını silin.
# 11- Liste elemanlarını alfabetik olarak sıralayınız.
# 12- Liste elemanlarını tersten yazdırınız.
# 13- Aşağıdaki verileri tek bir liste (iç içe liste - nested list) içinde saklayınız:

    # filmA: Inception 2010, (8.8, "Bilim Kurgu")
    # filmB: Interstellar 2014, (8.6, "Bilim Kurgu")
    # filmC: The Dark Knight 2008, (9.0, "Aksiyon")

# 14- Oluşturduğunuz bu yeni filmler listesini ekrana yazdırınız.
#1
programming_languages = ["Python", "Java", "C++", "JavaScript"]
print(programming_languages)  

#2
length =len(programming_languages)                                                   
print(length)                                                   

#3
print(programming_languages[0],programming_languages[length-1]) #=> son elemanı yazdırmak için -1 de yazdırabilirsin tersten gitmiş olur.

#4
programming_languages[2] = "Go"

#5
print("Java" in programming_languages)
print("C#" in programming_languages)

#6
print(programming_languages[-3])

#7
print(programming_languages[0:2])

#8
programming_languages[-1] = "Ruby"
programming_languages[-2] = "Swift"
print(programming_languages)

#veya daha kullanışlısı
# programming_languages[-2:] = ["Ruby", "Swift"]
# print(programming_languages)

#9
programming_languages = programming_languages + ["C#" , "Kotlin"]
print(programming_languages)

# veya programlama_dilleri.extend(["C#", "Kotlin"])

#10
del programming_languages[0]
print(programming_languages)
#veya
# programming_languages.pop(0)
# print(programming_languages)

#11
programming_languages.sort()
print(programming_languages)

#12
print(programming_languages[::-1])

#13
#flat list
movie1 = ["Inception", 2010, (8.8, "science fıction")]
movie2 = ["Interstellar", 2014, (8.6, "science fıction")]
movie3 = ["The Dark Knight", 2008, (9.0, "action")]

#nested list
movie = [movie1,movie2,movie3]

#14
print(movie)
print(movie[2])
print(movie[1][0])
print(movie[2][2])



