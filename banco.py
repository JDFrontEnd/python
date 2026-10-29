user = {
    "usuario": "juan diego mesa",
    "passward": 123456789,
    "saldo": 0
}

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
    print(user["saldo"])
    actionL = int(input("cuanto deseas retirar: ")) 
    if actionL - user["saldo"] > 0:
        print("Error: saldo insufisiente")
        return Actionleave()
    elif actionL == user["saldo"] or actionL > user["saldo"] or actionL - user["saldo"] == 0: 
        user["saldo"] -= actionL
        print(f"dinero retirado: ${actionL}")
        print(f"su saldo restante: ${user['saldo']}")
    GoBack()
    
#funcion para retirear dinero
def ActionTransfer():
    global actionT
    print(user["saldo"])
    actionT = int(input("cuanto deseas transferir: "))  
    if actionT - user["saldo"] > 0:
            print("Error: saldo insufisiente")
            return ActionTransfer()
    elif actionT == user["saldo"] or actionT > user["saldo"] or actionT - user["saldo"] == 0: 
        user["saldo"] -= actionT
    print(f"dinero transferido: ${actionT}")
    print(f"su saldo restante: ${user['saldo']}")
    GoBack()
    
    
# funcion para consignar dinero
def ActionDeposit():
    global actionD
    print(user["saldo"])
    actionD = int(input("cuanto deseas consignar: "))  
    user["saldo"] += actionD
    print(f"dinero consignado: ${actionD}")
    print(f"su saldo restante: ${user['saldo']}")
    GoBack()
    
    
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
    
    print(f"Saldo actual: {user['saldo']}")
    actionUser = input("que quieres hacer: (retirar, transferir, consignar, salir) ")
    
    
    if actionUser != "retirar" and actionUser != "transferir" and actionUser != "consignar" and actionUser != "salir":
        print("¡Error!, copie correctamente el comando")
        return action()
    elif actionUser == "retirar":
        Actionleave()     
    elif actionUser == "transferir":
        ActionTransfer()   
    elif actionUser == "consignar":
        ActionDeposit()
    elif actionUser == "salir":
        interfaz()
    

def interfaz():
    global accoutConfirmation
    print("<===============================================================================>")
    accoutConfirmation = input("\n \t \t \tHOLA BIENVENIDO A BANK.PY \n \t \t \t¿tienes una cuenta abierta?\n \t \t \t \t si - no -> ")
    
    if accoutConfirmation != "si" and accoutConfirmation != "no":
        print("¡Error!, copie correctamente el comando")
        return interfaz()
    elif accoutConfirmation == "si":
        loginUser()
    elif accoutConfirmation == "no":
        print("si no tines cuenta crea una")
        

interfaz()