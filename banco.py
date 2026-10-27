user = {
    "usuario": "juan diego mesa",
    "passward": 123456789,
    "saldo": 0
}

""" user = {
    "user1": {}
    "user2": {}
    "user3": {}
} """


# funcion login usuario

def loginUser():
    global usuario
    usuario = input("ingrese su nombre de usuario: ")

    if usuario != user["usuario"]:
        print('"ALVERTENCIA"\n El nombre de usuario es incorrecto o no esta registrado, por favor ingrese el usuario correctamente')
        return loginUser()
    elif usuario == user["usuario"]:
        loginPassward()


# funcion login pasward
def loginPassward():
    global contraseña
    
    contraseña = int(input("ingrese su contraseña: "))
    if contraseña != user["passward"]:
        print("contraseña incorrecta")
        return loginPassward()
    elif contraseña == user["passward"]:
        action()

#funcion para retirear dinero
def Actionleave():
    global actionL
    actionL = int(input("cuanto deseas retirar: "))  
    user["saldo"] -= actionL
    print(f"dinero retirado: ${actionL}")
    print(f"su saldo restante: ${user['saldo']}")
    
    
#funcion para retirear dinero
def ActionTransfer():
    global actionT
    actionT = int(input("cuanto deseas transferir: "))  
    user["saldo"] -= actionT
    print(f"dinero transferido: ${actionT}")
    print(f"su saldo restante: ${user['saldo']}")
    
    
# funcion para consignar dinero
def ActionDeposit():
    global actionD
    actionD = int(input("cuanto deseas consignar: "))  
    user["saldo"] += actionD
    print(f"dinero consignado: ${actionD}")
    print(f"su saldo restante: ${user['saldo']}")
    
    
# funcion navegar al inicio o salir a la interfaz
def GoBack():
    global regresar
    regresar = input("Escribe 'salir' para salir de tu cuenta o 'inicio' para ir al menu de inicio: ")
    if regresar == "salir":
        return interfaz()
    elif regresar == "inicio":
        return action()
    
#action user
def action():
    global actionUser
    
    actionUser = input("que quieres hacer: (retirar, tranferir, consignar, salir) ")
    
    if actionUser == "retirar":
        Actionleave()
    elif actionUser == "tranferir":
        ActionTransfer()
    elif actionUser == "consignar":
        ActionDeposit()
    
    GoBack()
    
              

def interfaz():
    global accoutConfirmation
    accoutConfirmation = input("\n HOLA BIENVENIDO A BANK.PY \n ¿tienes una cuenta abierta?\n  si - no \\ ")
    
    if accoutConfirmation == "si":
        loginUser()
    else:
        print("si no tines cuenta crea una")
        

interfaz()