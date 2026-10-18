import random
import time
import os

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


menu = {
    "papas": 1000,
    "pool": 2000,
    "festival": 800
}

ver_menu = input("para ver el menu escriba'ver menu' /")

if "ver menu" not in ver_menu:
    ver_menu = input("ERROR SYNTAS: por favor ingrese 'ver menu' /")
elif "ver menu" in ver_menu:
    print(menu)
    
orden = input("que quieres llevar ej: papas, pool /")
    
total = menu

if "papas" in orden:
    if orden == "papas":
        global pago
        pago = input(f"total a pagar: {total} ingrese el total a pagar: /")
    elif orden == "papas, pool" or orden == "pool, papas":
        total = menu["papas"] + menu["pool"]
        pago = input(f"total a pagar: {total} ingrese el total a pagar: /")    
    elif orden == "papas, festival" or orden == "festival, papas":
        total = menu["papas"] + menu["festival"]
        pago = input(f"total a pagar: {total} ingrese el total a pagar: /")
    elif orden == "papas, pool, festivas" or orden == "papas, festival, pool" or orden == "pool, papas, festival" or orden == "pool, festival, papas" or orden == "festival, papas, pool" or orden == "festival, pool, papas":
        total = menu["papas"] + menu["pool"] + menu["festival"]
        pago = input(f"total a pagar: {total} ingrese el total a pagar: /")    
elif "pool" in orden:    
    if orden == "pool":
        total == menu["pool"]
        pago = input(f"total a pagar: {total} ingrese el total a pagar: /")
    elif orden == "pool, festival" or orden == "festival, pool":
        total = menu["pool"] + menu["festival"]    
elif "festival" in orden:
    if orden == "festival":
        total = menu["festival"]
        pago = input(f"total a pagar: {total} ingrese el total a pagar: /")

if int(pago) == int(total):
    print("pago verificado, gracias por su compra")
    


"""     
width = 40
height = 12
gravity = 18.0
bounce = 0.78
fps = 20

balls = [
    {"x": 5.0, "y": 1.0, "vx": 9.0, "vy": 0},
    {"x": 25.0, "y": 3.0, "vx": -5.0, "vy": 0.0}
]

def render():
    grid = [["" for _ in range(width)] for _ in range(height)]
    for ball in balls:
        x = int(ball["x"])
        y = int(ball["y"])
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = "0"
            
    print("+" + "-" * width + "+")
    for row in grid:
        print("|" + "".join(row) + "|")
    print("+" + "-" * width + "+")
def update(dt):
    for ball in balls:
        ball["vy"] += gravity * dt
        ball["x"] += ball["vx"] * dt
        ball["y"] += ball["vy"] * dt
        if ball["x"] <= 0:
            ball["x"] = 0
            ball["x"] <= abs(ball["vx"])
            
        elif ball["x"] >= width - 1:
            ball["x"] = width - 1
            ball["x"] = -abs(ball["vx"])
            
        if ball["y"] >= height - 1:
            ball["y"] = height - 1
            ball["vy"] = -abs(ball["y"]) * bounce
            
        if ball["y"] <= 0:
            ball["y"] = 0
            ball["vy"] = abs(ball["y"])
    print("python physics simulator")
    print("press Ctrl+c to stop-")
    
try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        update(1 / fps)
        render()
        print("\nGravity:", gravity)
        print("Objects:", len(balls))
        time.sleep(1 / fps)
except KeyboardInterrupt:
    print("\nSimution: n stopped.")     """