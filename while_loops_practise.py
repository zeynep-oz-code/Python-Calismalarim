
# 1. Kullanıcı Giriş Simülasyonu (Max 3 Hak)

# Doğru kullanıcı adı ve şifreyi tanımlayın (Örn: "admin" / "123")
# Kullanıcıya 3 giriş hakkı tanıyın. 
# Yanlış girdikçe kalan hakkını ekrana basın. Hakkı biterse hesabı kilitleyin.

correct_username = "admin"
correct_password = "123"
attempts = 3

while attempts > 0 :
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == correct_username and password == correct_password :
            print("Login successful!")
            break
        else :
            attempts -= 1
            print(f"wrong credentials. Remaining attemps: {attempts}")    

if attempts == 0:
    print("Account blocked.")


# 2. Sayı Tahmin Oyunu

# Hedef bir sayı belirleyin (Örn: 42).
# Kullanıcı doğru sayıyı tahmin edene kadar döngüyü sürdürün.
# Her tahminde "Daha büyük bir sayı girin" veya "Daha küçük bir sayı girin" şeklinde yönlendirin.

target = 42
guess = 0

while guess != target :
    guess = int(input("Guess the number: "))

    if guess<target :
        print("Enter a higher number.")
    elif guess>target :
        print("Enter a lower number.")
    else :
        print("Correct guess!")



# 3. Sonsuz Veri Ekleme ve Ortalama Hesaplama ('q' ile Çıkış)

# Kullanıcı 'q' tuşuna basana kadar sürekli sayı girmesini isteyin.
# Girilen sayıları bir listede toplayın.
# 'q' girildiğinde döngüyü sonlandırıp girilen sayıların ortalamasını ekrana basın.

numbers = []

while True :
    entry = input("Enter a number ('q' to calculate avarage): ")

    if entry == 'q':
        break
    else :
        numbers.append(float(entry))
       
if len(numbers) > 0 :
    avarage = sum(numbers) / len(numbers)
    print(f"Avarage:  {avarage}")

else:
    print("No number entered.")


# 4. Basit Hesap Makinesi

# Kullanıcıdan iki sayı ve bir işlem seçimi (+ veya -) alın.
# İşlemi yapıp sonucu ekrana basın.
# İşlem bittiğinde "Devam etmek istiyor musunuz? (e/h)" diye sorun.
# Kullanıcı 'e' dışında bir şey girerse döngüyü sonlandırın.

while True:
 number1= float(input("Enter first number: "))
 number2= float(input("Enter second number: "))
 op = input("Operation (+/-): ")

 if op == '+':
  print(f"Result: {number1 + number2}")
 elif op == '-':
  print(f"Result: {number1 - number2}")
 else:
  print("Invalid operation. Selecet + or -.") 

 again = input("Do you want to continue?  (yes or no): ") .lower()

 if again != 'yes':
   print("Program terminated.")
   break


# 5. ATM / Bakiye Yönetimi

# Başlangıç bakiyesini 1000.0 olarak belirleyin.
# Kullanıcıya 4 seçenekli bir menü gösterin:
# 1- Bakiye Sorgula, 2- Para Yatır, 3- Para Çek, 4- Çıkış
# Kullanıcı 4'ü seçene kadar menüyü `while` döngüsü ile tekrar ekrana getirin.

balance = 1000.0

while True:
    print("----MENU----")
    print("1- Check Balance")
    print("2- Deposit Money")
    print("3- Withdraw Money")
    print("4- Exit")

    choice= input("Select Operation (1-4): ").strip()

    if choice == '1':
        print(f"Balance: {balance}")
    elif choice == '2':
        amount = float(input("Amount to deposite: "))
        balance += amount
        print(f"New Balance: {balance}TL")  
    elif choice == '3':
        amount = float(input("Amount to withdraw: ")) 
        if amount  > balance :
            print("Insufficient balance.")
        else :
            balance -= amount
            print(f"Remaining Balance: {balance}TL")
    elif choice == '4':
        print("Good bye")
        break
    else :
        print("Invalid choice!")