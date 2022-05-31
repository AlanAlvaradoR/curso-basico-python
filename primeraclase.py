import numpy as np 

##Variables empiezan con minuscula y clases empiezan con mayúscula

#miNombre = input("Mete tu nombre aquí: ")     

##Tres formas de imprimir variables en pantalla

#print(f"Hola {miNombre}")    ##Si no se le coloca la f al inicio imprime texto en vez de la variable
#print("Hola " + miNombre)
#print("Hola {}".format(miNombre))

##Concatenar en print

#edad = input("Mete tu edad aquí: ")
#print("Hola " + miNombre + " tu edad es: " + edad)

##Tipos de datos

pi = 3.1416     ##Tipo de dato flotante
miNombre = "Alan"  ##String
#edad = 25       ##int

##Operaciones básicas

#print(edad + 10)
#print(edad - 10)
#print(edad * 10)
#print(edad / 10)
#print(edad % 10)  ##Módulo para obtener residuo de la división
#print(edad // 10) ##División entera, redondea al entero más cercano
#print(edad ** 2) ##Exponencial - Devolver la base elevada al cuadrado

#edad = int(input("Mete tu edad: ")) ##Aquí se necesita el int para que se convierta o castee el string a int y poder usarlo

#if edad < 18 and edad > 0:
#    print("Eres menor de edad")
#elif edad >= 18 and edad < 100:
#    print("Eres mayor de edad")
#elif edad >= 100 and edad < 150:
#    print("Eres inmortal")
#elif edad < 0:
#    print("No existes!!!")
#elif edad == 0:
#    print("Eres un bebé")
#else:
#    print("Pon algo serio!!!!!🤬")

#comida = input("¿Qué comida te gusta?")
#tipoPizza = input("¿Qué tipo de pizza te gusta?")


#if comida == "pizza":
#    if tipoPizza == "peperoni":
#        print("Me gusta la pizza de peperoni")
#    else:
#        print("Me gusta todo tipo de pizza")
#else:
#    print("No me gusta la pizza")


##Ejemplo if y else en una sola linea

#animal = "perro"
#color = "negro"

#if color == "negro" : print("Es mi perro")
#else: print("No es mi perro")


##Listas, tupla y diccionario

lista = [1,2,3,4,5,6,7,8,9,10]  ##Son mutables (se pueden modificar)
tupla = (1,2,3,4,5,6,7,8,9,10)   ##No son mutables (no se puede modificar ya que son como constantes)
diccionario = {           ##Como una lista con indice y valor
    1: "uno",
    2: "dos",
    3: "tres"
}

lista2=[
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

#print(lista)
#print(tupla)
#print(diccionario)

#print(lista[0])  ##imprimir el primer valor de la lista
#print(tupla[9])   ##imprimir el último valor de la tupla

lista.append(11)  ##comando para agregar un valor al final de una lista mutable
#print(lista[0:len(lista):2])  ##imprimir desde 0 hasta el tamaño de la lista de 2 en 2
#print(np.array(lista2))

for x in lista:
    print(x)
