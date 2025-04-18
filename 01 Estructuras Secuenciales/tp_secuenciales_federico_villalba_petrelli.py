# Actividad 1
print ("Hola Mundo!")

# Actividad 2
nombre = input("Cuál es tu nombre? ")
print(f"Hola {nombre}!")

# Actividad 3
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
lugar_residencia = input ("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# Actividad 4
radio = float(input("Indique el radio del círculo: "))
pi = 3.1415
area = pi * radio**2
perimetro = 2 * pi * radio

print(f"El área del círculo es: {area}" )
print(f"El perímetro del círculo es: {perimetro}" )

# Actividad 5
segundos = int(input("Indique la cantidad de segundos: "))
horas = float(segundos/3600)
print(f"{segundos} segundos equivalen a {horas} horas")

# Actividad 6
nro = int(input ("Ingrese un número: "))
print(f"*****************************" )
print(f"  Tabla de Multiplicar de {nro}" )
print(f"*****************************" )
print(f"  {nro} x 1   =  {nro*1}" )
print(f"  {nro} x 2   =  {nro*2}" )
print(f"  {nro} x 3   =  {nro*3}" )
print(f"  {nro} x 4   =  {nro*4}" )
print(f"  {nro} x 5   =  {nro*5}" )
print(f"  {nro} x 6   =  {nro*6}" )
print(f"  {nro} x 7   =  {nro*7}" )
print(f"  {nro} x 8   =  {nro*8}" )
print(f"  {nro} x 9   =  {nro*9}" )
print(f"  {nro} x 10  =  {nro*10}" )

# Actividad 7
nro1 = int(input ("Ingrese un número entero distinto de 0: "))
nro2 = int(input ("Ingrese otro número entero distinto de 0: "))
print(f"*****************************" )
print(f"  OPERACIONES ENTRE {nro1} Y {nro2}" )
print(f"*****************************" )
print(f"  {nro1} + {nro2}   =  {nro1+nro2} " )
print(f"  {nro1} - {nro2}   =  {nro1-nro2} " )
print(f"  {nro1} * {nro2}   =  {nro1*nro2} " )
print(f"  {nro1} / {nro2}   =  {float(nro1/nro2)} " )

# Actividad 8
altura = float(input("Indique su altura: "))
peso = float(input("Indique su peso: "))
masa_corporal = peso / altura**2
print(f"Su masa corporal es de: {masa_corporal}")

# Actividad 9
temp_celsius = float(input("Ingrese la temperatura en grados celsius: "))
temp_fahrenheit = 9/5 * temp_celsius + 32
print(f"{temp_celsius}º celsius equivalen a {temp_fahrenheit}º fahrenheit")

# Actividad 10
nro1 = int(input ("Ingrese un número: "))
nro2 = int(input ("Ingrese otro número: "))
nro3 = int(input ("Ingrese otro número: "))
promedio = float((nro1+nro2+nro3)/3)
print(f"El Promedio de los números {nro1}, {nro2} y {nro3} es: {promedio}")