salaryAli = 5000
salaryAhmet = 4000
tax = 0.27

print(salaryAli -  (salaryAli*tax))
print(salaryAhmet -  (salaryAhmet*tax))

# Rules for Defining Variables

# Cannot start with a number
number1 = 10
print(number1)
number1=20
print(number1)
number1 += 30
print(number1)

# Variables are case-sensitive

age = 20
AGE = 30
print(age)
print(AGE)

# Avoid using Turkish characters

_age =20

x = 1            # int
y = 2.3          #float
name = "Zeynep"  #string
isStudent = True #bool

 # x,y,name,isStudent = (1,2.3,"Zeynep",True)

a = 10
b = 20
print(a+b) #30

c = '10'
d = '20'
print(c+d) #1020

firstName = "Zeynep"
lastName = " Öz"
print(firstName + lastName) # Zeynep Öz
