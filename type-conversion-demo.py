# calculate the area and circumference of a circle given its radius. (pi:3.14)

pi=3.14

radius =float(input("radius: ")) # => the input() function returns a string. we need to convert it to a number.
area = pi * (radius ** 2)
circumference = 2 * pi * radius

print("area:",area)
print("circumference:",circumference)

