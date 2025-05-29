# Definición de Funciones


"""
Actividad 1: FACTORIAL DE UN NÚMERO
"""

# Factorial usando iteracción
def factorial (n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


# Factorial usando Recursión
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * (factorial_recursivo(n-1))
        


# Factorial Recursivo Usando IF Ternario
def fact_version_corta(n):
    return 1 if n == 0 else n * (fact_version_corta (n-1))


if __name__ == "__main__" :
    print(factorial(5))
    print(factorial_recursivo(5))
    print (fact_version_corta(5))



def mostrar_factoriales(nro) :
    for i in range(1, nro+1) :
        print(f"El Factorial de {i} es {fact_version_corta(i)}")



"""
Actividad 2: FIBONACCI
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__" :
    print(fibonacci(4))



def mostrar_fibonacci(nro) :
    for i in range(0, nro+1) :
        print(f"El Fibonacci de {i} es {fibonacci(i)}")



"""
Actividad 3: POTENCIA
"""

def potencia(base, exponente): 
    if exponente == 0: 
        return 1 
    else: 
        return base * potencia(base, exponente - 1) 
    

def mostrar_potencia(base, exponente):
    print(f"El Resultado de {base} elevado a la {exponente} es {potencia(base,exponente):.2f}")


"""
Actividad 4: DECIMAL A BINARIO
"""


def decimal_a_binario(n): 
    if n == 0: 
        return "" 
    else: 
        return decimal_a_binario(n // 2) + str(n % 2)
    
def mostrar_decimal_a_binario(nro):
    print(f"El Número Decimal {nro} convertido a Binario es {decimal_a_binario(nro)}")


"""
Actividad 5: PALÍNDROMO
"""

# Validar Cadena sin Espacios ni Tildes
def es_cadena_sin_espacios_ni_tildes(mensaje):
    tildes = "áéíóúÁÉÍÓÚ"
    cadena_valida = False

    while not cadena_valida:
        cadena = input(mensaje)
        cadena_valida = True

        # Verificamos si hay espacios
        for letra in cadena:
            if letra == " ":
                print(f"ERROR: La cadena {cadena} no debe contener espacios.")
                cadena_valida = False
                break

        # Verificamos si hay tildes
        for letra in cadena:
            if letra in tildes:
                print(f"ERROR: La cadena {cadena} no debe contener tildes.")
                cadena_valida = False
                break

    return cadena


# Verificar si es Palíndromo
def es_palindromo(palabra) :
    if len(palabra) <= 1:
        return True
    
    palabra = palabra.lower()
    
    if palabra[0] != palabra[-1] :
        return False
    
    return es_palindromo(palabra[1:-1])


"""
Actividad 6: SUMA DE DÍGITOS
"""

def suma_digitos(nro):
    if nro < 10:
        return nro
    else:
        return (nro % 10) + suma_digitos(nro // 10)


"""
Actividad 7: PIRÁMIDE
"""

def contar_bloques(nro):
    if nro == 1:
        return 1
    else:
        return nro + contar_bloques(nro-1)
    

def mostrar_piramide(nro, nivel=1, simbolo = "* "):
    print()
    if nivel > nro:
        return
    else:
        # Caclula cuantos espacios hay que poner antes del primero símbolo en ese nivel para que quede centrada
        espacios = nro - nivel
        linea = " " * espacios + simbolo * nivel
        # Quita el espacio final e imprime la línea
        print(linea.rstrip())  
        mostrar_piramide(nro, nivel + 1)


"""
Actividad 8: CONTAR DÍGITO
"""
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        veces = 1 if numero % 10 == digito else 0
        return veces + contar_digito(numero // 10, digito)





"""
Otras Funciones
"""


# Validar Número Entero

def leer_entero_validado (mensaje, min = float('-inf'), max = float('inf')) :
    n = int(input(f"{mensaje}"))

    while n < min or n > max :
        n = int(input(f"ERROR, {mensaje}"))

    return n

def segundos_a_horas(segundos) :
    return round(segundos / 3600, 2)


# Validar Número Decimal

def leer_decimal_validado (mensaje, min = float('-inf'), max = float('inf')) :
    n = float(input(f"{mensaje}"))

    while n < min or n > max :
        n = float(input(f"ERROR, {mensaje}"))

    return n


# Validar Dígito

def leer_digito_validado(mensaje):
    digito_valido = False

    while not digito_valido:
        entrada = input(mensaje)

        if entrada.isdigit() and len(entrada) == 1:
            digito = int(entrada)
            digito_valido = True
        else:
            print(f"ERROR: {mensaje}")

    return digito