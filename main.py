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
