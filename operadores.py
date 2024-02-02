# Ejemplo de Map, transforma una lista de números a sus cuadrados
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados))

# Ejemplo de filter, filtra números pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))

# Ejemplo de reduce, suma los elementos de una lista
from functools import reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)

# Ejemplo de distinct, elimina elementos duplicados de una lista
numeros = [1, 2, 2, 3, 3, 4, 5, 5]
unicos = list(set(numeros))
print(unicos)
