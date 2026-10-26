user = {
    "usuario": "Juan Diego Mesa",
    "passward": 123456789,
    "saldo": 0
}

#saldo = user["saldo"]






# funcion login usuario

def loginUser():
    global usuario
    usuario = input("ingrese su nombre de usuario: ")

    if usuario != user["usuario"]:
        print('"ALVERTENCIA"\n El nombre de usuario es incorrecto o no esta registrado, por favor ingrese el usuario correctamente')
        return loginUser()
    elif usuario == user["usuario"]:
        loginUser(True)


# funcion login pasward
def loginPassward():
    global contraseña
    if loginUser() == True:
        contraseña = int(input("ingrese su contraseña: "))
    if contraseña != user["passward"]:
        print("contraseña incorrecta")
        return loginPassward()
    elif contraseña == user["passward"]:
        loginPassward(True)


def login():
    global actionUser
    global regresar
    
            actionUser = input("que quieres hacer: (retirar, tranferir, consignar, salir) ")
            if actionUser == "retirar":
                montoRetirar = int(input("cuanto deseas retirar:"))
                user["saldo"] -= montoRetirar
                print(f"dinero retirado: ${montoRetirar}")
                print(f"su saldo restante: ${user['saldo']}")
                regresar = input("Escribe 'salir' para salir de tu cuenta o 'inicio' para ir al menu de inicio: ")
                if regresar == "salir":
                    return interfaz()
                elif regresar == "inicio":
                    return actionUser
            elif actionUser == "tranferir":
                tranferencia = int(input("ingrese un monto a tranferin"))
                user["saldo"] -= tranferencia
                print(f"dinero transferido: ${tranferencia}")
                print(f"su saldo total es: ${user['saldo']}")
                regresar = input("Escribe 'salir' para salir de tu cuenta o 'inicio' para ir al menu de inicio: ")
                if regresar == "salir":
                    return interfaz()
                elif regresar == "inicio":
                    return actionUser
            elif actionUser == "consignar":
                consignacion = int(input("cuanto desea consignar"))
                user["saldo"] += consignacion
                print(f"dinero consignado: ${consignacion}")
                print(f"su saldo total es: ${user['saldo']}")
                regresar = input("Escribe 'salir' para salir de tu cuenta o 'inicio' para ir al menu de inicio: ")
                if regresar == "salir":
                    return interfaz()
                elif regresar == "inicio":
                    return actionUser

def interfaz():
    global accoutConfirmation
    accoutConfirmation = input("\n HOLA BIENVENIDO A BANK.PY \n ¿tienes una cuenta abierta?\n  si - no \\ ")
    
    if accoutConfirmation == "si":
        login()
    else:
        print("si no tines cuenta crea una")
        

interfaz()