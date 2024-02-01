# Ejemplo de Map, transformo una lista de números a sus cuadrados
numeros = [1, 2, 3, 4, 5]
cuadrados = map(lambda x: x ** 2, numeros)
print(list(cuadrados))

# Ejemplo de filter, filtra números pares de una lista
numeros = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # Output: [2, 4]
