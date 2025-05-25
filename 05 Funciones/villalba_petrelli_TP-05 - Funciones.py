import utils

# Programa Principal

# 1)
"""
Crear una función llamada imprimir_hola_mundo que imprima porpantalla el mensaje: “Hola Mundo!”.
Llamar a esta función desde el programa principal
"""
print("\n************************************")
print("         ACTIVIDAD Nº 1")
print("************************************\n")


# Llama a Función imprimir_hola_mundo
print (utils.imprimir_hola_mundo())

# 2)
"""
Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
Llamar a esta función desde el programa principal solicitando el nombre al usuario

"""
print("\n************************************")
print("         ACTIVIDAD Nº 2")
print("************************************\n")

# Llamada a Función saludar_usuario
nombre = input("Ingrese su nombre: ")
print(utils.saludar_usuario(nombre))



# 3)
"""
Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
Pedir los datos al usuario y llamar a esta función con los valores ingresados.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 3")
print("************************************\n")


# Lista con los campos que queremos pedir
lista_de_datos_a_pedir = ['nombre', 'apellido', 'edad', 'residencia']

# Pedimos los datos al usuario
datos_personales = utils.pedir_datos(lista_de_datos_a_pedir)

# Llamamos a la función con los datos ingresados
utils.informacion_personal(
    datos_personales['nombre'],
    datos_personales['apellido'],
    datos_personales['edad'],
    datos_personales['residencia']
)



# 4)
"""
Crear dos funciones: calcular_area_circulo(radio)
que reciba el radio como parámetro y devuelva el área del círculo.
calcular_perimetro_circulo(radio)
que reciba el radio como parámetro y devuelva el perímetro del círculo.
Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

"""
print("\n************************************")
print("         ACTIVIDAD Nº 4")
print("************************************\n")

# Llama a la Función para Validar el número ingresado
radio = utils.leer_decimal_validado("Ingrese el radio: ", 0)

# Imprime los cálculos realizados
print (f"\nEl área del círculo es {utils.calcular_area_circulo(radio)}")
print (f"\nEl perímetro del círculo es {utils.calcular_perimetro_circulo(radio)}")



# 5)
"""
Crear una función llamada segundos_a_horas(segundos)
que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
Solicitar al usuario los segundos y mostrar el resultado usando esta función

"""
print("\n************************************")
print("         ACTIVIDAD Nº 5")
print("************************************\n")

# Se Crea una Lista de Números aleatorios

# Llama a Función para Validar el Número
segundos = utils.leer_entero_validado("Ingrese la cantidad de segundos: ", 0)


print(f"\nEl equivalente a {segundos} segundos es {utils.segundos_a_horas(segundos)} horas.")


# 6)
"""
Crear una función llamada tabla_multiplicar(numero)
que reciba un número como parámetro y que imprima la tabla de multiplicar de ese número del 1 al 10.
Pedir al usuario el número y llamar a la función.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 6")
print("************************************\n")

# Llama a Función para Validar el Número
tabla_de_multiplicar = utils.leer_entero_validado("Ingrese que Tabla de Multiplicar desea ver: ", 0)

utils.tabla_multiplicar(tabla_de_multiplicar)


# 7)
"""
Crear una función llamada operaciones_basicas(a, b)
que reciba dos números como parámetros y devuelva una tupla con el resultado de
sumarlos, restarlos, multiplicarlos y dividirlos.
Mostrar los resultados de forma clara

"""

print("\n************************************")
print("         ACTIVIDAD Nº 7")
print("************************************\n")


# Llama a Función para Validar el Número Validado
nro_1 = utils.leer_decimal_validado("Ingrese un Número: ", 0)
nro_2 = utils.leer_decimal_validado("Ingrese otro Número: ", 0)

resultados = utils.operaciones_basicas(nro_1, nro_2)

print()
print (f" {nro_1} + {nro_2}  =  {resultados[0]}")
print (f" {nro_1} - {nro_2}  =  {resultados[1]}")
print (f" {nro_1} X {nro_2}  =  {resultados[2]}")
print (f" {nro_1} / {nro_2}  =  {resultados[3]}")


# 8)
"""
Crear una función llamada calcular_imc(peso, altura)
que reciba el peso en kilogramos y la altura en metros,
y devuelva el índice de masa corporal (IMC).
Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales

"""

print("\n************************************")
print("         ACTIVIDAD Nº 8")
print("************************************\n")

# Llama a Función para Validar el Número Validado
peso = utils.leer_decimal_validado("Ingrese su Peso: ", 0)
altura = utils.leer_decimal_validado("Ingrese su Altura: ", 0)

print(f"\nEn base a su altura de {altura} metros y su peso de {peso} Kg. su Masa Muscular es de: {utils.calcular_imc(peso, altura)}")


# 9)
"""
Crear una función llamada celsius_a_fahrenheit(celsius)
que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 9")
print("************************************\n")


# Llama a Función para Validar el Número Validado
celsius = utils.leer_decimal_validado("Ingrese la Temperatura en Grados Celsius: ", 0)

print(f"{celsius}º Celsius son equivalentes a {utils.celsius_a_fahrenheit(celsius)}º Fahrenheit")


# 10)
"""
Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta función.

"""

print("\n************************************")
print("         ACTIVIDAD Nº 10")
print("************************************\n")


# Llama a Función para Validar el Número Validado
a = utils.leer_decimal_validado("Ingrese un Nro: ", 0)
b = utils.leer_decimal_validado("Ingrese otro Nro: ", 0)
c = utils.leer_decimal_validado("Ingrese otro Nro: ", 0)

print(f"El Promedio de {a}, {b} y {c} es {utils.calcular_promedio(a, b, c)}")