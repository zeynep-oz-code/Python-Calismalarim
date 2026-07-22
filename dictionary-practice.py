students = {}



student_id = input("Student ID: ")
first_name = input("First Name: ")
last_name = input("Last Name: ")
phone = input("Phone Number: ")

students[student_id] = {
    'first_name': first_name,
    'last_name': last_name,
    'phone': phone
}


student_id = input("Student ID: ")
first_name = input("First Name: ")
last_name = input("Last Name: ")
phone = input("Phone Number: ")

students[student_id] = {
    'first_name': first_name,
    'last_name': last_name,
    'phone': phone
}


print(students)



search_id = input("Enter Student ID to search: ")


student_info = students[search_id]

print("\n--- Student Details ---")
print("First Name :", student_info['first_name'])
print("Last Name  :", student_info['last_name'])
print("Phone      :", student_info['phone'])

#you can use the update() method.