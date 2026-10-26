""" maquina de golocinas """

menu = {
    "papas": 1000,
    "pool": 2000,
    "festival": 800
}
 

def MenuFun():
    ver_menu = input("para ver el menu escriba'ver menu' /")
    if ver_menu != "ver menu":
        print("ERROR: para ver el menu ingrese correctamente 'ver menu'")
        return MenuFun()
    elif ver_menu == "ver menu":
        print(menu)
MenuFun()
    
orden = input("que quieres llevar ej: papas, pool /")
    
total = menu

pago = 10

if "papas" in orden:
    if orden == "papas":
        total = menu["papas"]
        pago = int(input(f"total a pagar: {total} ingrese el total a pagar: /"))
    elif orden == "papas, pool" or orden == "pool, papas":
        total = menu["papas"] + menu["pool"]
        pago = int(input(f"total a pagar: {total} ingrese el total a pagar: /"))  
    elif orden == "papas, festival" or orden == "festival, papas":
        total = menu["papas"] + menu["festival"]
        pago = int(input(f"total a pagar: {total} ingrese el total a pagar: /"))
    elif orden == "papas, pool, festivas" or orden == "papas, festival, pool" or orden == "pool, papas, festival" or orden == "pool, festival, papas" or orden == "festival, papas, pool" or orden == "festival, pool, papas":
        total = menu["papas"] + menu["pool"] + menu["festival"]
        pago = int(input(f"total a pagar: {total} ingrese el total a pagar: /"))   
elif "pool" in orden:    
    if orden == "pool":
        total == menu["pool"]
        pago = int(input(f"total a pagar: {total} ingrese el total a pagar: /"))
    elif orden == "pool, festival" or orden == "festival, pool":
        total = menu["pool"] + menu["festival"]    
        pago = int(input(f"total a pagar: {total} ingrese el total a pagar: /"))
elif "festival" in orden:
    if orden == "festival":
        total = menu["festival"]
        pago = int(input(f"total a pagar: {total} ingrese el total a pagar: /"))

if pago != total:
    pago = int(input(f"El total a pagar es incorreto: {total} ingrese el total a pagar: /"))
    

if pago == int(total):
    print("pago verificado, gracias por su compra")