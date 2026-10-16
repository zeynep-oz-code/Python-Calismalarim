# Amacımız; soru verilerini, kullanıcı cevaplarını ve puan hesaplama mantığını dağınık değişkenler
# yerine sınıflar (Classes) ve nesneler (Objects) içinde organize ederek yönetebilen, terminal
# veya arayüz tabanlı çalışan nesne yönelimli bir sınav sistemi oluşturmaktır.

#iki ana sınıf tasarlanır:
#1. question sınıfı : bu sınıfın tek bir sorumluluğu vardır: tek bir soruyu şıkları ve doğru cevabı tutmak.
#attributes:(__init__ ile gelenler)
#text:soru metni
#choices:şıklar listesi
#answer:doğru cevap

#2.quiz sınıfı: bu sınıf soruları yönetmekisırayla ekrana getirekiskoru tutumak ve sınavın bitip bitmediğini kontrol etmektir.
#attributes:(__init__ ile gelenler)
#questions: soruların listesi(yukarıda oluşturduğun soru nesnelerini içeren bir liste)
#questions_index: şu an kaçıncı soruda olduğunuzu tutan sayaç(genelde 0dan başlar)
#score: kullanıcının anlık puanı[genelde 0dan başlar]

class Question():
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def cevapKontrol(self,user_choice) :  
        return self.answer.lower() == user_choice.lower()

class Quiz():
    def __init__(self,questions , question_index=0 , score=0):
        self.questions = questions
        self.question_index = question_index
        self.score = score 

    def soruGetir(self):
        return self.questions[self.question_index]

# Soru nesnelerini oluşturuyoruz
q1 = Question("En popüler programlama dili hangisidir?", ["Python", "C#", "JavaScript", "Java"], "Python")
q2 = Question("Hangisi bir veri analizi kütüphanesidir?", ["Pandas", "Django", "Flask", "HTML"], "Pandas")
q3 = Question("Python hangi yıl çıkmıştır?", ["1990", "1995", "2000", "2010"], "1995")

# Bu soruları bir liste içine atıyoruz
sorularListesi = [q1, q2, q3]

# Quiz nesnesini oluşturuyoruz
quiz = Quiz(sorularListesi)

while quiz.question_index < len(quiz.questions):
    aktif_soru = quiz.soruGetir()

    print(f" Soru {quiz.question_index+1}: {aktif_soru.text}")
    for secenek in aktif_soru.choices :
        print(f"-{secenek}")

    kullanici_cevabi = input("Cevabınız: ")

    if aktif_soru.cevapKontrol(kullanici_cevabi) :
        print("Cevabınız Doğru")
        quiz.score+=10
    else :
        print("Cevabınız Yanlış")

    quiz.question_index += 1


print("Sınav bitti")
print(f"Toplam Puanınız: {quiz.score}")




    



  

