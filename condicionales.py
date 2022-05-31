calificacion = int(input("Introduce tu calificacion del AZ-900: "))

if calificacion < 700:
    print("Veees, por no estudiar") #Si es menor a 700 pasa esto
elif calificacion > 1000:
    print("Mientes!!!!! No puedes sacar más de 1000")
else:
    print("Felicidades, pasa por tu certificado")

edad = int(input("Introduce tu edad: "))
if edad >= 18 and edad <= 100:
    print("Bienvenid@ al mamitas")
elif edad >100:
    print("Si vienes acompañad@ de tus abuelitos, si te podemos fiar")
elif edad < 0:
    print("Ni que fueras viajero del tiempo")
else: 
    print("No puedes llevarte esos cigarros")

#EN PYTHON NO HAY SWITCH CASE