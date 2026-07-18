name = 'Zeynep'
surname = 'Öz'
age = 21

# print('My name is {} {}'.format(name,surname))
# print('My name is {1} {0}'.format(name,surname))
# print('My name is {s} {n}'.format(n=name,s=surname))
print('My name is {} {} and I am {} years old.'.format(name,surname,age)) #age için tür değişimi yapmamıza gerek kalmadı.

result = 200/700
print('the result is {r:1.3}' .format(r=result)) #r den sonra ilk sayı noktadan önce; ikinci sayı ise noktadan sonra kaç basamak yazacağını söyler ve yuvarlar.

print(f'My name is {name} {surname} and I am {age} years old.') # aynı işlemi yapar. yeni gelen bir özellik
