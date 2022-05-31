from cmath import pi
from tokenize import Exponent


first_name = input("Dame tu nombre: ")
last_name = input("Dame tu apellido: ")
full_name = first_name + " " + last_name
country = input("Dame tu pais: ")
city =  input("Dame tu ciudad: ")
age = int(input("Dame tu edad: "))
year = int(input("Dame el año: "))
is_married = True
is_true = True
is_light_on = False
multiple, variables, one, line = True, 0, "No es cierto", 0.27

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(multiple))
print(type(variables))
print(type(one))
print(type(line))

le = len(first_name)-len(last_name)

print(f"Diferencia: {le}")

num_one = int(input("Dame el primer número: "))
num_two = int(input("Dame el segundo número: "))

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = (num_one ** num_two)
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = float(input("Dame el radio del circulo: "))
area_of_circle = (radius ** 2)*pi
circum_of_circle = 2 * pi * radius
print(area_of_circle, circum_of_circle)