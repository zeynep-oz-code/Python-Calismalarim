#The purpose and work of the project: it is a quary tool checks whether the user can get a driver's license; if he can,which class of driver's license can apply according to the education.
#Scenario The basic rule for a person to obtain a driver's licence is that they must be at least 18 years old and have a health report.
#The education status of the people who meet these two basic conditions is considered. High school or universty graduate/ student can get a Class B license and primaty school
#graduate can get a Class A license. if  the conditions are not met, the system will inform the person of the reason for refusal.

#---The First Code I Wrote---
# get user age, health report and education level

# age = int(input("Enter your age: "))
# has_health_report= input("Do you have a health report?  (yes or no): ").lower().strip()
# education_level = input("Enter your education level (primary/middle/high/university): ").lower().strip()

# # validate main eligibility( age and health report)

# if age >= 18 and has_health_report== 'yes' :

#     if education_level in ['high school' ,'university' ] :
#         print(f" You can get a Class B driver's license.")
#     else :
#         print(f" You can get a Class A1 driver's license.")
# else:
#     print("\n[REJECTED] Application failed.")
#     print("Reason(s): ")

#     if age < 18 :
#         print("  You must be at least 18 years old.")

#     if has_health_report != 'yes':
#         print("  Health report is required.")    
# 
# --- Improved Code Using a List Structure---

age = int(input("Enter your age: "))
has_health_report = input("Do you have a health report? (yes or no): ").lower().strip()
education_level = input("Enter your education level (primary/middle/high/university): ").lower().strip()

reasons = []

if age < 18:
    reasons.append("You must be at least 18 years old.")

if has_health_report != 'yes':
    reasons.append("Health report is required.")

if len(reasons) == 0:
    if education_level in ['high school', 'university']:
        print("You can get a Class B driver's license.")
    else:
        print("You can get a Class A1 driver's license.")
else:
    print("\n[REJECTED] Application failed.")
    print("Reason(s):", reasons)    
   



