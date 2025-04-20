# 1)
"""  
Escribir un programa que solicite la edad del usuario.
Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

"""

edad = int(input("Ingrese su edad: "))

if edad >= 18 :
    print(f"Es mayor de edad")

print("")

# 2)
"""
Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”.

"""

nota = int(input("Ingresar nota: "))

if nota >= 6 :
    print(f"APROBADO")
else :
    print("DESAPROBADO")

print()

# 3)
"""
Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar.

"""

nro = int(input("Ingrese un Nro. Par: "))

if nro % 2 == 0 :
    print("Ha ingresado un número par")
else :
    print("Por favor, ingrese un número par")

print()

# 4)
"""
Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años.

"""

edad_persona = int(input("Ingrese su edad: "))

edad_menor = 12
edad_adolescente = 18
edad_adulto = 30

if edad_persona < edad_menor :
    print(f"Perteneces a la Categoría Niño")

elif edad_persona < edad_adolescente :
    print(f"Perteneces a la Categoría Adolescente")

elif edad_persona >= edad_adolescente and edad_persona < edad_adulto :
    print(f"Perteneces a la Categoría Adulto Jóven")

else :
    print(f"Perteneces a la Categoría Adulto")

print()

# 5)
"""
Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string. 

"""

password = input("Ingrese su Contraseña: ")

if len(password) >= 8 and len(password) <= 14 :
    print("Ha ingresado una contraseña correcta")
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print()

# 6)
"""
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
Definir la lista numeros_aleatorios de la siguiente forma: 

nros_aleatorios = [random.randint(1, 100) for i in range(50)]

Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
forma aleatoria. 

"""

from statistics import mode, median, mean
import random

# Genera 50 números aleatorios entre 1 y 100
nros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula la Moda, la Media y la Mediana de los números aleatorios
moda = mode(nros_aleatorios)
mediana = median(nros_aleatorios)
media = mean(nros_aleatorios)

# Muestra los Números Aleatorios y las estadísticas
print(f"Nros Aleatorios: {nros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana and mediana > moda :
    print("Hay Sesgo Positivo")

elif media < mediana and mediana < moda :
    print("Hay Sesgo Negativo")

elif media == mediana == moda :
    print("No hay Sesgo")

else:
    print("Sesgo no definido")

print()

# 7)
"""
Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. 

"""

texto = input("Ingrese una frase o palabra: ")

# Busca el último caracter de la palabra o frase ingresada y lo convierte a minúscula
ultimo = texto[-1].lower()

print(f"El último caracter de lo ingresado es {ultimo}")

if ultimo == 'a' or ultimo == 'e' or ultimo == 'i' or ultimo == 'o' or ultimo == 'u' :
    print(f"{texto}!")
else :
    print(f"{texto}")

# 8)
"""
Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

"""

nombre = input("Ingrese su nombre: ")

# input con Varias Líneas para Menú de Opciones
opcion = int(input(
    """
    ******************
     Menú de Opciones
    ******************

    1 - Nombre en MAYÚSCULA
    2 - Nombre en minúscula
    3 - Nombre con la 1® Letra Mayúcula
    0 - Para Salir
    
    Elegir la opción deseada: 
    *****************************
    """
) )

if opcion == 1 :
    print(f"{nombre.upper()}")
elif opcion == 2 :
    print(f"{nombre.lower()}")
elif opcion == 3 :
    print(f"{nombre.title()}")
else :
    pass

print()

# 9)
"""
Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

"""

escala_terremoto = float(input("Ingrese la Magnitud del Terrermoto: "))

leve = 3
perceptible = 4
moderado = 5
fuerte = 6
muy_fuerte = 7
extremo = 8

categoria_leve = "en la escala de Richter es Categoría 'MUY LEVE', casi imperceptible."
categoria_perceptible = "en la escala de Richter es Categoría 'LEVE', ligeramente imperceptible."
categoria_moderado = "en la escala de Richter es Categoría 'MODERADO', sentido por personas pero generalmente no causa daños."
categoria_fuerte = "en la escala de Richter es Categoría 'FUERTE', puede causar daños en estructuras débiles."
categoria_muy_fuerte = "en la escala de Richter es Categoría 'MUY FUERTE', puede causar daños significativos."
categoria_extremo = "en la escala de Richter es Categoría 'EXTREMO', puede causar graves daños a gran escala."


if escala_terremoto < leve :
    print(f"El Terromo escala {escala_terremoto} {categoria_leve} ")

elif escala_terremoto >= leve and escala_terremoto < perceptible  :
    print(f"El Terromo escala {escala_terremoto} {categoria_perceptible}")

elif escala_terremoto >= perceptible and escala_terremoto < moderado :
    print(f"El Terromo escala {escala_terremoto} {categoria_moderado} " ) 

elif escala_terremoto >= moderado and escala_terremoto < fuerte :
    print(f"El Terromo escala {escala_terremoto} {fuerte} ")

elif escala_terremoto >= fuerte and escala_terremoto < muy_fuerte :
    print(f"El Terromo escala {escala_terremoto} {categoria_muy_fuerte} ")

else :
    print(f"El Terromo escala {escala_terremoto} {categoria_extremo} ")

print()

# 10)

""""
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. 



"""
# Pide al usuario que ingrese el Hemisferio y toma sólo el primer caracter y lo convierte en Mayúscula
hemisferio = input("Indique si se encuentra en el Hemisferio Norte o SUR: ")[0].upper()

# Pide Mes y Día
mes = int(input("Ingresa el mes actual: "))
dia = int(input("Ingresa el dia en número: "))


if hemisferio == "N" :
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 22):
        estacion = "Verano"
    elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha No Válida. Vuelva a Ejecutar!"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 22):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha No Válida. Vuelva a Ejecutar!"
else:
    estacion = "Hemisferio No Válido. Vuelva a Ejecutar!"


print(f"""
    +------------------------------------+-------------------------------+-------------------------------+
    |     Período del año                | Estación en Hemisferio Norte  | Estación en Hemisferio Sur    |
    +------------------------------------+-------------------------------+-------------------------------+
    | 21 de diciembre al 20 marzo        |      Invierno                 |         Verano                |
    | 21 de marzo al 20 junio            |      Primavera                |         Otoño                 |
    | 21 de junio al 22 septtiembre      |      Verano                   |         Invierno              |
    | 23 de septiembre al 20 diciembre   |      Otoño                    |         Primavera             |
    +----------------------------+---------------------------------------+-------------------------------+
    
    Según Tabla de Estaciones te encuentras en {estacion}  
    
""")
