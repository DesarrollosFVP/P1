import utils

# Programa Principal

# 1)
"""
Crea una función recursiva que calcule el factorial de un número.
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

"""
print("\n************************************")
print("         ACTIVIDAD Nº 1")
print("************************************\n")


# Llama a Función para Pedir un Nro
nro = utils.leer_entero_validado("Ingresa un Número Entero: ", 1)

# Llama a la Función para Mostrar los Factoriales hasta el número ingresado
utils.mostrar_factoriales(nro)


# 2)
"""
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

"""
print("\n************************************")
print("         ACTIVIDAD Nº 2")
print("************************************\n")

# Llama a Función para Pedir un Nro
nro = utils.leer_entero_validado("Ingresa un Número Entero: ", 1)

# Llama a la Función para Mostrar los Fibonacci hasta el número ingresado
utils.mostrar_fibonacci(nro)



# 3)
"""
Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
utilizando la fórmula n**𝑚 = n * n**(m-1).
Prueba esta función en un algoritmo general

"""

print("\n************************************")
print("         ACTIVIDAD Nº 3")
print("************************************\n")


# Llama a Función para Pedir un Nro
base = utils.leer_decimal_validado("Ingresa un Número: ")
potencia = utils.leer_entero_validado("Ingresa el Exponente al que desea elevar el Número anterior: ", 0)

# Llama a Función para Mostrar el Resultado
utils.mostrar_potencia(base, potencia)




# 4)
"""
Crear una función recursiva en Python que reciba un número entero positivo en base decimal
y devuelva su representación en binario como una cadena de texto.

Convertir el número 10 a binario: 
10 ÷ 2 = 5     resto: 0   
 5 ÷ 2 = 2     resto: 1   
 2 ÷ 2 = 1     resto: 0   
 1 ÷ 2 = 0     resto: 1   
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010". 

"""
print("\n************************************")
print("         ACTIVIDAD Nº 4")
print("************************************\n")

# Llama a Función para Pedir un Nro
nro = utils.leer_entero_validado("Ingresa un Número Entero: ", 1)

utils.mostrar_decimal_a_binario(nro)



# 5)
"""
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes,
y devuelva True si es un palíndromo o False si no lo es. 

     Requisitos: 
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()

"""
print("\n************************************")
print("         ACTIVIDAD Nº 5")
print("************************************\n")

# Llama a la Función para ingresar una cadena
cadena = utils.es_cadena_sin_espacios_ni_tildes("Ingresa una cadena sin Espacios ni Tildes: ")

# Muestra si es Verdadero o Falso
print(f"La cadena {cadena} es Palíndromo? {utils.es_palindromo(cadena)}")



# 6)
"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba
un número entero positivo y devuelva la suma de todos sus dígitos.

     Restricciones: 

- No se puede convertir el número a string.
- Usá operaciones matemáticas (%, //) y recursión. 

Ejemplos: 
suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
suma_digitos(9)      → 9 
suma_digitos(305)    → 8   (3 + 0 + 5)

"""

print("\n************************************")
print("         ACTIVIDAD Nº 6")
print("************************************\n")

# Llama a Función para Pedir un Nro
nro = utils.leer_entero_validado("Ingresa un Número Entero Positivo: ", 1)

# Llama a la Función para Sumar los dígitos del Número
print(f"La suma de los digitos del Número {nro} es igual a {utils.suma_digitos(nro)}")


# 7)
"""
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
 
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
pirámide. 
 
      Ejemplos: 

contar_bloques(1)   → 1         (1) 
contar_bloques(2)   → 3         (2 + 1) 
contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

"""

print("\n************************************")
print("         ACTIVIDAD Nº 7")
print("************************************\n")


# Llama a Función para Pedir un Nro
nro = utils.leer_entero_validado("Ingresa el Número de Bloques que se colocarán en el Nivel más Bajo de la Pirámide: ", 1)

# Muestra la Pirámide según Número indicado por usuario
utils.mostrar_piramide(nro)

# Llama a la Función para Contar los Bloques que Necesita
print(f"\nSi la Base de la Pirámide tiene {nro} bloques entonces se necesitarán en Total {utils.contar_bloques(nro)} bloques para Construir la Pirámide completa")


# 8)
"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba
un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

      Ejemplos: 

contar_digito(12233421, 2)   → 3   
contar_digito(5555, 5)       → 4   
contar_digito(123456, 7)     → 0   


"""

print("\n************************************")
print("         ACTIVIDAD Nº 8")
print("************************************\n")

# Llama a Función para Pedir un Nro
nro = utils.leer_entero_validado("Ingresa un Número Entero Positivo: ", 1)
digito = utils.leer_digito_validado("Ingresa un Dígito entre 0 y 9: ")

print(f"\nEl Dígito {digito} está incluído {utils.contar_digito(nro, digito)} veces dentro del número {nro}")