message = 'Helloo, my name is Zeynep Öz.'

message = message.upper() # => because it is a method, we must use parentheses even if it has no parameters. AND
# => The upper() method converts all the letters in the variable to uppercase and stores the result back in the variable.

print(message)

message = message.lower() # the lower() method converts all the letters to lowercase.
print(message)

message = message.title() # the title() method capitalizes the first letter of each word.
print(message)

message = message.capitalize() # the capitalize() method capitalizes only the first letter of the sentence and converst the rest to lowercase.
print(message)

message = message.strip() #the strip() method removes leading and trailing spaces from the text.
print(message)

# message = message.split() # the split() method splits a  string into a list using a separator.(separator=ayırıcı)
# print(message)
# print(message[4])

message = message.split(',') # If no parameter is provided, split() uses spaces as the default separator. If a parameter is provided, it splits the string using that separator. ( is provided=verilirse/sağlanırsa)
print(message)

message = ','.join(message) #the join() method the elements of a list into a string
print(message)

index = message.find('öz')
print(index)

index = message.find('words')
print(index)

message = message.replace('zeynep','Rumeysa') # the replace() method serches for the parameter and replaces it with the second parameter.
print(message)

message = message.replace('ö','o').replace(' ','-')
print(message)

message = message.center(50,'*')
print(message)

# you can learn about other string methods on W3Schools.

