# 1)
"""
Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 1")
print("************************************\n")

print("*********")
#Sumo un número más porque el último NO lo incluye
for cont in range(101):
    print("Nro: ",cont)
print("*********")

# 2)
"""
Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 2")
print("************************************\n")

entero = int(input("Ingresar un número entero: "))

# Se convierte el número a Valor Absoluto por si el usuario indicó un nro. Negativo
entero = abs(entero)

# Inicializo el contador en 0 para resetear el ejercicio anterior
cont = 0

# Si el número ingresado es 0 coloco el contador en 1 como un caso especial porque si lo coloco dentro del while con >= entraría en un bucle infinito
if entero == 0:
    cont = 1
else:
    while entero > 0 :
        entero = entero // 10
        cont +=1

print(f"El número ingresado contiene {cont} dígitos")


# 3)
"""
Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 3")
print("************************************\n")

# Ingresa 2 Valores por el usuario como indica el enunciado
# Se convierte a flotante por si el usuario ingresa un número con decimal
entero_1 = float(input("Ingrese un Valor: "))
entero_2 = float(input("Ingrese un Valor: "))

# Convierte el número a un tipo Entero por si el usuario ingresó un nro decimal
entero_1 = int(entero_1)
entero_2 = int(entero_2)

# Inicializa la variable de la sumatoria de los nros en Cero.
sumatoria = 0

# Si el Primer nro es menor o igual ejecutará un for sino se invertiran los nros
if entero_1 <= entero_2 :
    for elemento in range(entero_1+1, entero_2) :
        sumatoria += elemento

else :
    for elemento in range(entero_2+1, entero_1) :
        sumatoria += elemento

print (f"La suma de los números ingresados es: {sumatoria}")


# 4)
"""
Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 4")
print("************************************\n")
nro = int(input("Ingresa un nro: "))

sumatoria = 0

while nro != 0 :
    sumatoria += nro
    nro = int(input("Ingresa otro nro ó 0 para Salir: "))

print("\n************************************")
print("  El Total Acumulado es de", sumatoria)
print("************************************")


# 5)
"""
Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 5")
print("************************************\n")

# Se importa Módulo RANDOM de la Librería Estandar de Python
import random

# Se genera Nro. Aleatorio entre 0 y 9
nro_aleatorio = random.randint(0,9)

# Se inicializa el intento en 1 porque al menos lo intentará una vez
intento = 1

print("*************************************************************'")
print("      ADIVINA EL NÚMERO QUE ESTOY PENSANDO ENTRE 0 Y 9")
print("*************************************************************\n'")
nro = int(input("Ingresa el Número entre 0 y 9: "))


while nro != nro_aleatorio :
    print("\nFALLASTE!!!")
    print("INTENTA DE NUEVO!")
    nro = int(input("Ingresa otro Número entre 0 y 9: "))
    intento += 1
    

print("\nFELICITACIONES!!!!\nEl Número que estaba pensando es el", nro_aleatorio)
print("Lo adivinaste en el", str(intento) + "º intento")

input("\nPresiona una tecla ENTER para continuar\n")


# 6)
"""
Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente

"""

print("\n************************************")
print("         ACTIVIDAD Nº 6")
print("************************************\n")

# Se inicializa la variable con el Valor más Alto para poder ir en orden decreciente
pares = 100

print ("Los Números Pares comprendidos entre 0 y 100 en Orden Decreciente son: \n")

# Se utiliza un for porque se conoce la cantidad
# Se usa la variable pares-2 como valor inicial para que empiece desde 98 y no de 100 ya que no está incluído
# Se usa 0 como valor final porque es el último número par y no se lo toma en cuenta
# Se coloca menos -2 al final para que vaya decrementando de a 2 y así tome todos los nros pares
for cont in range(pares-2, 0, -2) :
    print("Número:", cont )



# 7)
"""
Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 7")
print("************************************\n")

sumatoria = 0
entero_positivo = int(input("Ingrese un Número Entero Positivo: "))

# Si el usuario No puso un Nro Mayor a 0 le volverá a pedir hasta que ingrese un Nro Entero Positivo
while entero_positivo <= 0 :
    entero_positivo = int(input("Ingrese un Número Entero Positivo Mayor a 0: "))


for cont in range(1, entero_positivo) :
    sumatoria += cont


print (f"La Suma de TODOS los Números entre 0 y {entero_positivo} es {sumatoria}")
print (f"\n*** Aclaración importante: 0 y {entero_positivo} NO están incluídos***")


# 8)
"""
Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

"""

print("\n************************************")
print("         ACTIVIDAD Nº 8")
print("************************************\n")

# Se inicializan todos los contadores en 0
cont_pares = 0
cont_impares = 0
cont_negativos = 0
cont_positivos = 0

# Se utiliza un for sabiendo que serán 100 números y como comenzará en 1 también se suma uno para que llegue al 100
for cont in range (1, 101) :
    nro = int(input("Ingrese un Número Entero: "))

    if nro > 0 :
        if nro % 2 == 0 :
            cont_positivos +=1
            cont_pares +=1

        else :
            cont_positivos +=1
            cont_impares +=1    

    elif nro < 0 :
        if nro % 2 == 0 :
            cont_negativos +=1
            cont_pares +=1

        else :
            cont_negativos +=1
            cont_impares +=1    

    else :
        print("\n\t\tEl Nro 0 No es Par ni Impar. Tampoco es Positivo ni Negativo\n")



print(f"\nDe los Nros. ingresados hay {cont_pares} Nros. Pares")

print(f"De los Nros. ingresados hay {cont_impares} Nros. Impares")

print(f"De los Nros. ingresados hay {cont_positivos} Nros. Positivos")

print(f"De los Nros. ingresados hay {cont_negativos} Nros. Negativos")



# 9)
"""
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). 

"""

print("\n************************************")
print("         ACTIVIDAD Nº 9")
print("************************************\n")


# Se inicializa la Suma en 0
sumatoria = 0

# Se utiliza un for sabiendo que serán 100 números y como comenzará en 1 también se suma uno para que llegue al 100
for cont in range (1, 101) :
    nro = int(input("Ingrese un Número Entero: "))
    sumatoria += nro

# Se realiza el Cálculo de la Media diviviendo la Suma Total entre la Cantidad de Nros ingresados
print (f"\nLa Media de los Valores ingresados es {sumatoria/cont}")



# 10)
"""
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 10")
print("************************************\n")



nro = int(input("Ingrese un Número: "))

# Se guarda el número ingresado por el usuario en otra variable para trabajar luego
nro_original = nro

# Se inicializa la variable que contendrá el número invertido
nro_invertido = 0

# Si el nro original es Negativo se Multiplica por -1 para hacerlo Positivo
if nro_original < 0 :
    nro *= -1

# Mientras el Nro sea Mayor a 0
# Saca el último dígito con el Resto de la división
# Al Nro Invertido lo Multiplica por 10 y al resultado le suma el dígito obtenido en el paso anterior
# Al Nro ingresado por el Usuario lo divide por 10 y devuelve sólo la parte entera porque el Resto ya se lo llevó al Nro. Invertido
while nro > 0 :
    digito = nro % 10
    nro_invertido = nro_invertido * 10 + digito
    nro = nro // 10


# Si el nro original era Negativo le agrega el Signo Negativo al Nro Invertido ya que trabajamos con Nro Positivo
if nro_original < 0 :
    nro_invertido *= -1

print (f"\nEl Número Invertido de {nro_original} es {nro_invertido}")