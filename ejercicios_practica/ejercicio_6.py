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
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

cantidad_numeros_positivos = 0  # Inicializo el contador en 0
lista = []
positivos_y_cero = 0
negativos = 0
# for ... in range(....)
for i in range(inicio, fin + 1, 1):
    lista.append(i)
print('\n La lista a analizar es: ',lista)
for i in lista:
    if i < 0:
        negativos = negativos + 1
    else:
        positivos_y_cero = positivos_y_cero +1
print('\n La cantidad de numeros negativos es: ',negativos)
print('\n La cantidad de numeros positivos y el cero es: ',positivos_y_cero)
# Imprimir el valor de la cantidad de números positivos y negativos
print("\n terminamos!\n")
