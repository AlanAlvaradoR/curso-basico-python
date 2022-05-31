#Arreglo o lista
lista = [1, 2, 3, 4, 5]

lista.append(0) #Poner un elemento al final de la lista
print(lista)

lista.extend(lista) #Agregar una lista (o un iterable) a la lista
print(lista)

lista = lista[::-1] #Invertir una lista (se usa más para iterables)
print(lista)

lista.reverse() #Invertir una lista
print(lista)

lista.insert(0, 10) #Insertar un elemento en una posición especifica (posicion, valor)
lista.insert(5,11)
print(lista)

lista.remove(0) #Elimina un elemento de la lista (busca el primer elemento con el valor dado y lo elimina)
lista.remove(0)
print(lista)

print(lista.pop(1)) #Igual que .remove pero este lo devuelve
print(lista)

print(lista.count(3)) #Cuenta la cantidad de veces que aparece un elemento en la lista

print(lista.index(10)) #Devuelve la posición de un elemento enla lista
print(lista.index(11))

lista.sort() #Ordena la lista
print(lista)

lista.sort(reverse=True)  #Otra forma de invertir una lista
print(lista)

lista2 = lista.copy() #Copiar una lista (superficial, no funciona con sub-elementos)
print(lista)

lista.clear() #Limpiar la lista
print(lista)

lista2 = [] #Crear una lista vacia o la puede limpiar xd
print(lista2)