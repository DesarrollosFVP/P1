# 1)
"""
Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
range. 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 1")
print("************************************\n")


# Se crea Lista
lista_multiplo_4 = list(range (4, 101, 4))


print(f"Lista Múltimplo de 4: \n{lista_multiplo_4}\n" )


# 2)
"""
Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
indexing con números negativos! 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 2")
print("************************************\n")


# Se crea Lista con 5 elementos
lista_5_elementos = ["Hola", 1, True, "Ejercicio 2", lista_multiplo_4]

print(f"El Penúltimo Elemento de la Lista según Video es: {lista_5_elementos[3]}")
print(f"\nEl Penúltimo Elemento de la Lista con Número Negativo es: {lista_5_elementos[-2]}")


# 3)
"""
Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
ejemplo: 
        lista_vacia = [] 

"""

print("\n************************************")
print("         ACTIVIDAD Nº 3")
print("************************************\n")

# Se Crea Lista Vacía
lista_vacía = []

# Se Agregan elementos a la Lista vacía - Uno a la vez
lista_vacía.append("Hola")
lista_vacía.append("Bienvenido")
lista_vacía.append("Adios")


print (f"La Lista Vacía se convirtió en: : {lista_vacía}")


# 4)
"""
Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
en los videos o bien investigar cómo funciona el indexing con números negativos! 
animales = ["perro", "gato", "conejo", "pez"] 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 4")
print("************************************\n")

animales = ["perro", "gato", "conejo", "pez"]

# Muestra Lista Original
print (f"La Lista Original es: : {animales}")

# Se Reemplaza el 2º Valor de la Lista usando como se muestra en Video
animales[1] = "loro"

# Se Reemplaza el Último Valor de la Lista usando Nro. Negativo
animales[-1] = "oso"


# Muestra Resultado
print (f"\nLa Lista Modificada es: {animales}")


# 5)
"""
Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove (max(numeros))
print(numeros)

"""
print("\n************************************")
print("         ACTIVIDAD Nº 5")
print("************************************\n")

# Se Crea una Lista de Números aleatorios
numeros = [8, 15, 3, 22, 7]
print (f"{numeros}")

# Busca el Número más Grande con la función max
# Elimina el Número más Grande con el método remove
numeros.remove (max(numeros))

# Muestra por Pantalla la Lista Modificada
print(numeros)
print (f"Se eliminó el Número Más Grande la Lista Original")



# 6)
"""
Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
pantalla los dos primeros

"""

print("\n************************************")
print("         ACTIVIDAD Nº 6")
print("************************************\n")

# Se Crea Lista con Nros del 10 al 30 incluído con saltos de 5
lista_10_a_30 = list(range(10,31,5))

print (f"La Lista Original es: {lista_10_a_30}")

# Muestra los 2 Primeros Valores de la Lista
print (f"\nLos 2 Primeros Valores de la Lista son: {lista_10_a_30[0]} y {lista_10_a_30[1]} ")


# 7)
"""
Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
cualesquiera.

autos = ["sedan", "polo", "suran", "gol"] 

"""

print("\n************************************")
print("         ACTIVIDAD Nº 7")
print("************************************\n")


autos = ["sedan", "polo", "suran", "gol"] 
print (f"La Lista Original es: {autos}")

# Reemplaza los valores centrales por otros valores
autos[1] = "up"
autos[2] = "amarok"

print (f"\nLa Lista Modificada es: {autos}")


# 8)
"""
Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
directamente. Imprimir la lista resultante por pantalla. 

"""

print("\n************************************")
print("         ACTIVIDAD Nº 8")
print("************************************\n")


# Se Crea Lista Vacía llamada dobles
dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print (f"\nLa Lista Modificada es: {dobles}")


# 9)
"""
Dada la lista “compras”, cuyos elementos representan los productos comprados por 
diferentes clientes: 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

a) Agregar "jugo" a la lista del tercer cliente usando append. 
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
c) Eliminar "pan" de la lista del primer cliente.  
d) Imprimir la lista resultante por pantalla 

"""

print("\n************************************")
print("         ACTIVIDAD Nº 9")
print("************************************\n")


# Lista Original
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
print(f"Lista Original: {compras}")

# a) Se agrega elemento "jugo" a la lista del 3º cliente usando append
compras[2].append("jugo")
print(f"\nLista Modificada por punto a: {compras}")

# b) Reemplazar fideos por tallarines en la lista del 2º cliente
compras[1][1] = "tallarines"
print(f"\nLista Modificada por punto b: {compras}")

# c) Eliminar pan en la lista del 1º cliente
compras[0].remove("pan")
print(f"\nLista Modificada por punto c: {compras}")

# d) Muestra Lista Final
print(f"\nLista Final por punto d: {compras}")


# 10)
"""
 Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 

● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 

Imprimir la lista resultante por pantalla.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 10")
print("************************************\n")

# Se Crea Lista Anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Muestra Lista Anidada
print(f"Lista Anidada: {lista_anidada}")