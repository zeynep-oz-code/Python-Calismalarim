#project Logic: Evaluates discount rates with logical operators(and,or) according to the age, 
#student status and day type entered by user and calculates the final ticket amount.

#1. get user inputs for age,student status and day.
age = int(input("Enter your age: "))
is_student = input("Are you student? (yes or no) :").lower().strip()
day = input("Enter day type (weekday or weekend) :").lower().strip()

#2. define base price 

if day == "weekend" :
    base_price = 120
else :
    base_price=100 

#3. check eligibility for student or age discount

if age < 18 or is_student == "yes" :
    discount = 0.20 # 20% discount for student and youths.
    
else :
    discount = 0.0

#4.calculate final ticket price   

final_price = base_price *(1-discount)

#5.display ticket summary and total cost
print(f"Your ticket price: {final_price} $")
       
        