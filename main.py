import random

name = "juan" #str text
# print(type(name))

age = 24 #int number
# print(type(age))

student = True #bool boleano
# print(type(student))

learning = "python"

#operadores matematicos
a = 4 + 7 
b = 4 * 1
c = 4 / 5

#Many Values to Multiple Variables
x, y, z = "orange", "banana", "cherry"

#One Value to Multiple Variables
x = y = z = "orange"

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

x = 1 # int
y = 2.8 # float
z = 1j # complex

NumImpar = random.randrange(1, 20, 3)
NumPar = random.randrange(2, 20, 2)

L1 = NumImpar
L2 = NumPar
L3 = L1
L4 = L2

Ar = L1 * L2
Per = (L1 + L2)*2

print(f"Lado par es de: {L2}, lado impar es de: {L1},  el area es: {Ar},  el perimetro es: {Per}")

#rectangulo
pR = (L1 + L2)*2
aR = L1 * L2
vR = L1 * L2 * aR
print(f"rectangulo: -area: {aR} -perimetro: {pR} -volumen: {vR}")

a = random.randrange(1, 20)

L1 = L2 = L3 = L4 = a

# cuandrado
pC = L1 * 4 
aC = L1 * 2
vC = L1 * L2 * L3
print(f"cuadrado: -area: {aC} -perimetro: {pC} -volumen: {vC}")

#triangulo
pT = L1 + L2 + L3
aT = (L1 * L2) / 2
vT = L1 * L2 * L3
print(f"triangulo: -area: {aT} -perimetro: {pT} -volumen: {vT}")

    
"""calculo de edad""" 
    
name = input("Cual es tu nombre? ") 
age = int(input("cual es tu edad? "))

if age < 18:
    print(f"Hola, {name} eres menor de edad")
elif age >= 18 and age <= 65:
    print(f"hola, {name} eres mayor de edad")
else:
    print(f"Hola, {name} eres adulto mayor")   
    
    
    
""" calculadora """

print("calculadora")
number1 = int(input("ingrese el primer valor de la operacion: "))
operador = input("ingrese el operador matematico (suma: +, resta: -, multiplicacion: *, division: /): ")
number2 = int(input("ingrese el segundo valor de la operacion: "))


if "+" in operador:
    print(f"Resultado: {number1 + number2}")
elif "-" in operador:
    print(f"Resultado: {number1 - number2}")
elif "*" in operador:
    print(f"Resultado: {number1 * number2}")
elif "/" in operador:
    print(f"Resultado: {number1 / number2}")



a = "Hell0, World!"
b = a.split(",")
c = a[-6:-1], a[:6]
print(b[1] + b[0])
print(c)


hoy = 23
octuber = "octubre"
print(f"hoy es {hoy} de {octuber}")



id = 118735173
nombre = "santo tomas"
apellido = "santo"
edad = 24
print(f"hola, {nombre + " " + apellido} tu cedula es {id} y tienes {edad} años")




TRM = 3240
dolares = 120
print(f"para la TRM de hoy es: ${TRM} total es de ${TRM * dolares}")

saldo = 10000

tranferencia = int(input("ingrese el monto a tranferir:"))
saldo = tranferencia - saldo
print(f"saldo total: ${saldo * TRM}")

retiro = int(input("ingrese el monto a tranferir:"))
saldo = retiro - saldo
print(f"saldo total: ${saldo * TRM}") 

consignacion = int(input("ingrese el monto a tranferir:"))
saldo = consignacion + saldo
print(f"saldo total: ${saldo * TRM}")  
