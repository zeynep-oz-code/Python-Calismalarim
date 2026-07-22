students = ['Ahmet', 'Zeynep', 'Murat', 'Elif']
scores = [85, 100, 70, 85]
cities = "İstanbul,Ankara"

# 1- "Mehmet" ismini students listesinin sonuna ekleyiniz.
students.append("Mehmet")
#print(students)

# 2- "Selin" değerini students listesinin başına (0. indekse) ekleyiniz.
students.insert(0,"Selin")
#print(students)

# 3- "Murat" ismini students listesinden siliniz.
students.remove("Murat")
# print(students)

# 4- "Zeynep" isminin indeksi nedir?
index =students.index("Zeynep")
#print(index)

# 5- "Ahmet" ismi students listesinin bir elemanı mıdır?
#print("Ahmet" in students)

# 6- students liste elemanlarını ters çevirin.
students.reverse()
#print(students)

# 7- students liste elemanlarını alfabetik olarak sıralayınız.
students.sort()
#print(students)

# 8- scores listesini rakamsal büyüklüğe göre sıralayınız.
scores.sort()
print(scores)

# 9- cities = "İstanbul,Ankara" karakter dizisini (string) virgüllerden ayırarak bir listeye çeviriniz.
result = cities.split(',')
print(result)
# 10- scores dizisinin en büyük ve en küçük elemanı nedir?
val1= min(scores)
val2 =max(scores)
print(val1,val2)

# 11- scores dizisinde kaç tane 85 değeri vardır?
print(scores.count(85))

# 12- scores dizisinin tüm elemanlarını siliniz.
scores.clear()
print(scores)

# 13- Kullanıcıdan alacağınız 3 tane meyve bilgisini bir listede saklayınız (input kullanarak).
fruits=[]

f1 = input("1.fruit: " )
f2 = input("2.fruit: " )
f3 = input("3.fruit: " )
fruits.append(f1)
fruits.append(f2)
fruits.append(f3)
print(fruits)

