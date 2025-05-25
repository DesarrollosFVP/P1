import math


# Definición de Funciones


"""
Actividad 1: Imprimir Hola Mundo!
"""

def imprimir_hola_mundo () :
    return "Hola Mundo!"



"""
Actividad 2: Saludar
"""

def saludar_usuario(nombre) :
    return f"\nHola {nombre}!"


"""
Actividad 3: Información Personal
"""

"""
    Pide al usuario que ingrese datos según los campos dados en una lista.
    Devuelve un diccionario con esos datos.
"""

def pedir_datos(lista) :
    datos = {}

    for i in lista :

        # Hace algo SIEMPRE hasta que se corte con un break
        while True :
            dato = input(f"Ingrese su {i}: ").strip()

            if i == 'edad' :
                if dato.isdigit() and int(dato) > 0 :

                    datos[i] = int(dato)
                    break
                
                else :
                    print("La edad debe ser un entero positivo.")

            else :

                if dato :
                    datos[i] = dato
                    break
                else :
                    print(f"{i.capitalize()} no puede estar vacío")

    return datos


def informacion_personal (nombre, apellido, edad, residencia) :
    print (f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")



"""
Actividad 4: Cálculo de Area y Perímetro de Círculos
"""

def leer_decimal_validado (mensaje, min = float('-inf'), max = float('inf')) :
    n = float(input(f"{mensaje}"))

    while n < min or n > max :
        n = float(input(f"ERROR, {mensaje}"))

    return n


def calcular_area_circulo(radio) :
    return round(math.pi * (radio ** 2), 2)


def calcular_perimetro_circulo(radio) :
    return round(2 * math.pi * radio, 2)





"""
Actividad 5: Pasar Segundos a Horas
"""

# Validar Números
def leer_entero_validado (mensaje, min = float('-inf'), max = float('inf')) :
    n = int(input(f"{mensaje}"))

    while n < min or n > max :
        n = int(input(f"ERROR, {mensaje}"))

    return n

def segundos_a_horas(segundos) :
    return round(segundos / 3600, 2)




"""
Actividad 6: Tabla de Multiplicar
"""

def tabla_multiplicar(numero) :
    print(f"\n**************")
    for i in range(1,11) :
        print(f" {i} X {numero} =  {i*numero}")    
    print(f"**************")



"""
Actividad 7: Operaciones Básicas
"""

def operaciones_basicas(a,b) :
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    if b != 0 :
        division = a / b
    else :
        division = "No se puede dividir por Cero"


    return (suma, resta, multiplicacion, division)




"""
Actividad 8: Masa Corporal
"""

def calcular_imc(peso, altura) :
    return round(peso / (altura ** 2),2)


"""
Actividad 9: Grados Celsius a Fahrenheit
"""

def celsius_a_fahrenheit(celsius) :
     return round((celsius * 9/5) + 32, 2)


"""
Actividad 10: Calcular Promedio
"""

def calcular_promedio(a, b, c) :
    return round((a+b+c)/3, 2)




"""
Otras Funciones
"""
