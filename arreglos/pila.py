#PILA EN PYTHON
#El último elemento que entra, es el primero que sale

stack = [1, 2, 3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop() #Como no se le da un valor, saca el último valor
print(stack)

stack.pop()
print(stack)