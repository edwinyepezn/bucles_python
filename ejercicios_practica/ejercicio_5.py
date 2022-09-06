# Bucles [Python]
# Ejercicios de práctica

# Autor: Edwin Yepez
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0
for i in range(inicio, fin + 1 , 1):
    sumatoria = i + sumatoria
    
print('La sumatoria de los numeros enteros entre: ' ,inicio, ' y ' ,fin, ' es: ' ,sumatoria )


# for ... in range(....)

# Imprimir el valor de la sumatoria

print("terminamos!\n\n")


# Otra manera de resolver:

sumatoria = 0
lista = []
for i in range(inicio, fin + 1, 1):
    lista.append(i)
print('La lista de numeros a sumar es: ',lista)
for i in lista:
    sumatoria = sumatoria + i
print(sumatoria)
