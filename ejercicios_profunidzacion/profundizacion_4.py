# Bucles [Python]
# Ejercicios de profundización

# Autor: Edwin Yepez
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

temp_dataloger = [19.8, 21.6, 23, 20.8, 22.1, 21.3, 23.5, 27.6,
                  22.7, 23.6, 25.2, 26.4]

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
En este ejercicio se lo provee de una lista de temperaturas,
esa lista de temperaturas corresponde a los valores de temperaturas
tomados durante una temporada del año en Buenos Aires.
Usted deberá analizar dicha lista para deducir
en que temporada del año se realizó el muestreo de temperatura.
La variable con la lista de temperaturas se llama "temp_dataloger"
definida al comienzo del archivo

Debe recorrer la lista "temp_dataloger" y obtener los siguientes
resultados

1 - Obtener la máxima temperatura
2 - Obtener la mínima temperatura
3 - Obtener el promedio de las temperaturas

Los resultados se deberán almacenar en las variables
que ya hemos preparado para usted al comienzo del ejercicio

NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
el máximo y el mínimo utilizando los mismos métodos vistos
durante la clase (ejemplos_clase/ejemplo_5.py)
'''

print("Mi primer pasito en data analytics")
# Empezar aquí la resolución del ejercicio

temperatura_max = None      # Aquí debe ir almacenando la temp máxima
temperatura_min = None      # Aquí debe ir almacenando la temp mínima
temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

# Colocar el bucle aqui......
    # Verifico si el número ingresado es mayor al
    # máximo número ingresado hasta el momento
for numero in temp_dataloger:
    if (temperatura_max is None) or (numero > temperatura_max):
       temperatura_max = numero
for numero in temp_dataloger:
    if (temperatura_min is None) or (numero < temperatura_min):
       temperatura_min= numero
print('La temperatura maxima es: ',temperatura_max)
print('La temperatura minima es: ',temperatura_min)
for numero in temp_dataloger:
    temperatura_sumatoria = temperatura_sumatoria + numero
print('La sumatoria de todas las temperaturas es: ',temperatura_sumatoria)
temperatura_len = len(temp_dataloger)
temperatura_promedio = temperatura_sumatoria / temperatura_len
print('El promedio de las temperaturas es de: ',temperatura_promedio)
print('La maxima temperatura calculado por python: ',max(temp_dataloger))
print('La minima temperatura calculado por python: ',min(temp_dataloger))
print('La sumatoria calculada por Python es: ',sum(temp_dataloger))

#Al finalizar el bucle compare si el valor que usted calculó para
# temperatura_max y temperatura_min coincide con el que podría calcular
# usando la función "max" y la función "min" de python
# función "max" --> https://www.w3schools.com/python/ref_func_max.asp
# función "min" --> https://www.w3schools.com/python/ref_func_min.asp

# Al finalizar el bucle debe calcular el promedio como:
# temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

# Corroboren los resultados de temperatura_sumatoria
# usando la función "sum"
# función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

'''
Una vez que tengamos nuestros valores correctamente calculados debemos
determinar en que epoca del año nos encontramos en Buenos Aires utilizando
la estadística de años anteriores. Basados en el siguiente link realizamos
las siguientes aproximaciones:

verano -->      min = 19, max = 28
otoño -->       min = 11, max = 20
invierno -->    min = 8, max = 14
primavera -->   min = 10, max = 24

Referencia:
https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
'''

# En base a los rangos de temperatura de cada estación,
# ¿En qué época del año nos encontramos?
# Imprima el resultado en pantalla
# Debe utilizar temperatura_max y temperatura_min para definirlo
if(temperatura_min >= 19) and (temperatura_max <= 28):
    print('ESTAMOS EN VERANO!!')
elif(temperatura_min >= 11) and (temperatura_max <= 20):
    print('ESTAMOS EN OTOÑO!!')
elif(temperatura_min >= 8) and (temperatura_max <= 14):
    print('ESTAMOS EN INVIERNO!!')
elif(temperatura_min >= 10) and (temperatura_max <= 24):
    print('ESTAMOS EN PRIMAVERA!!')
