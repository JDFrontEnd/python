
""" Python Indentation """
 
""" La sangría se refiere a los espacios al inicio de una línea de código.

    Mientras que en otros lenguajes de programación la sangría en el código es para la legibilidad solo que la sangría en Python es muy importante.

    Python utiliza sangría para indicar un bloque de código. """
#if 5 > 2:
    #print("Five is greater than two!") 
    
""" Python te dará un error si te saltas la sangría: """
#if 5 > 2:
#print("Five is greater than two!")



""" 
Python Variables
    En Python, se crea una variable cuando le asignas un valor:
"""
x = 5
y = "Hello, World!"



""" 
Sentencias en Python -  Python Statements

    Declaraciones
        Un programa informático es una lista de "instrucciones" que debe ser "ejecutada" por un ordenador. En un lenguaje de programación, estas instrucciones se denominan sentencias. La siguiente afirmación imprime el texto "¡Python es divertido!" en la pantalla:
"""
# print("Python is fun!") ejemplo



""" 
Python Output / Print

    Texto impreso 
    Ya has aprendido que puedes usar la función para mostrar texto o valores de salida:print()
"""
# print("Hello World!")



""" 
Comillas dobles
    El texto en Python debe estar entre comillas. Puedes usar comillas dobles o comillas simples:"'
"""
# print("This will work!")
# print('This will also work!')



""" 
Impresión sin línea nueva
    Por defecto, la función termina con una nueva línea.print() 
    Si quieres imprimir varias palabras en la misma línea, puedes usar el parámetro:end
"""
# print("Hello World!", end=" ")
# print("I will print on the same line.")
#resultado Hello World! I will print on the same line.



"""
Variables Python
    Las variables son contenedores para almacenar valores de datos.
    Una variable se crea en el momento en que le asignas un valor por primera vez.
"""
x = 5
y = "John"

""" 
Las variables no necesitan declararse con ningún tipo en particular, e incluso pueden cambiar de tipo una vez que se hayan establecido.
"""
x = 4       # x is of type int
x = "Sally" # x is now of type str

""" 
Casting 
    Si quieres especificar el tipo de dato de una variable, esto se puede hacer mediante casting.
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

""" 
Variables Python - Consigue el tipo
    Puedes obtener el tipo de dato de una variable con la función.type() 
"""
x = 5
y = "John"
print(type(x))
print(type(y))

""" 
Variables Python - Case-Sensitive 
    Los nombres de variables son sensibles a mayúsculas y mayúsculas.
"""
#Esto generará dos variables:
a = 4
A = "Sally"
#A will not overwrite a

""" 
Variables Python - Nombres de variables 
    Una variable puede tener un nombre corto (como x e y) o un nombre más descriptivo (edad, nombre de coche, total_volume).
    Reglas para variables en Python:
    -debe comenzar con una letra o el carácter de guion bajo
    -no puede empezar con un número
    -solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _ )
    -son sensibles a mayúsculas minúsculas (edad, edad y edad son tres variables diferentes)
    -no puede ser ninguna de las palabras clave de Python.
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

""" 
Variables Python - Nombres de variables de varias palabras
    Los nombres de variables con más de una palabra pueden ser difíciles de leer. Hay varias técnicas que puedes usar para hacerlos más legibles:
"""
# Camel Case
myVariableName = "John"

# """ Pascal Case """
MyVariableName = "John"

# """ Snake Case """
my_variable_name = "John"

""" 
Variables Python - Asignar múltiples valores 
    Muchos valores a múltiples variables
        Python te permite asignar valores a varias variables en una sola línea:
"""
x, y, z = "Orange", "Banana", "Cherry"
#Nota: Asegúrate de que el número de variables coincida con el número de valores, o de lo contrario te dará un error.

""" 
Un valor para múltiples variables
        Y puedes asignar el mismo valor a varias variables en una sola línea: 
"""
x = y = z = "Orange"


""" 
Variables Python - Unpack a Collection 
    Si tienes una colección de valores en un , etc. Python te permite extraer los valores en variables. Esto se llama UNPACKING.listtuple
"""
# Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# apple
# banana
# cherry

""" 
Python - Global Variables 
    Variables que se crean fuera de una función (como en todos los ejemplos en las páginas anteriores) se conocen como variables globales. Las variables globales pueden ser utilizadas por todos, tanto dentro de Funciones y fuera.
    
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

Si creas una variable con el mismo nombre dentro de una función, esta variable será local y solo puede usarse dentro de la función. La variable global con el mismo nombre permanecerá como antes, global y con el valor original.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

La palabra clave global
Normalmente, cuando creas una variable dentro de una función, esa variable es local, y solo puede usarse dentro de esa función.

Para crear una variable global dentro de una función, puedes usar la palabra clave.global
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""




""" 
Tipos de datos en Python
    En programación, el tipo de dato es un concepto importante. Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacer cosas diferentes. Python tiene los siguientes tipos de datos integrados por defecto, en estas categorías:

    En Python, el tipo de dato se establece cuando asignas un valor a una variable:
"""
x = "Hello World"	#Text Type: str	

x = 20	#Numeric Types: int	
x = 20.5	#Numeric Types: float	
x = 1j	#Numeric Types: complex	

x = ["apple", "banana", "cherry"]	#Sequence Types: list	
x = ("apple", "banana", "cherry")	#Sequence Types: tuple	
x = range(6)	#Sequence Types: range	

x = {"name" : "John", "age" : 36}	#Mapping Type: dict	

x = {"apple", "banana", "cherry"}	#Set Types: set	
x = frozenset({"apple", "banana", "cherry"})    #Set Types: frozenset	

x = True	#Boolean Type: bool	

x = b"Hello"	#Binary Types: bytes	
x = bytearray(5)	#bBinary Types: ytearray	
x = memoryview(bytes(5))	#Binary Types: memoryview	

x = None	#NoneType
""" 
Establecer el tipo de dato específico
    Si quieres especificar el tipo de dato, puedes usar lo siguiente Funciones constructoras:
"""
x = str("Hello World")	#str	

x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	

x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	

x = dict(name="John", age=36)	#dict	

x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	

x = bool(5)	#bool	

x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	

x = memoryview(bytes(5))	#memoryview	



""" 
Conversión de tipos
    Puedes convertir de un tipo a otro con los métodos , , y :int()float()complex() 
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

#Nota: No puedes convertir números complejos en otro tipo de número.

""" 
Random Number
    Python no tiene una función para hacer un número aleatorio, pero Python tiene un módulo incorporado llamado random que puede usarse para crear números aleatorios:random()
    
    Importa el módulo aleatorio y muestra un número aleatorio del 1 al 9:
"""
# import random

# print(random.randrange(1, 10))




""" 
Python Casting 
    Especificar un tipo de variable
    Puede haber ocasiones en las que quieras especificar un tipo en una variable. Esto se puede hacer con el lanzamiento. Python es un lenguaje orientado a objetos y, como tal, utiliza clases para definir tipos de datos, incluidos sus tipos primitivos.

    Por tanto, el casting en python se realiza usando funciones constructoras:
    
    int() - construye un número entero a partir de un literal entero, un literal flotante (eliminando todos decimales), o un literal de cadena (siempre que la cadena represente un número entero)
    
    float() - construye un número float a partir de un literal entero, un literal float o un literal de cadena (siempre que la cadena represente un float o un entero)
    
    Str() - construye una cadena a partir de una gran variedad de tipos de datos, incluyendo cadenas, literales enteros y literales float
"""
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'




""" 
Python Strings

Las cuerdas son matrices - Strings are Arrays

    Como muchos otros lenguajes de programación populares, las cadenas en Python son matrices de caracteres unicode. Sin embargo, Python no tiene un tipo de dato de carácter, un solo carácter es simplemente una cadena con una longitud de 1. Los corchetes pueden usarse para acceder a elementos de la cuerda.

"""
a = "Hello, World!"
#print(a[1])

""" 
Bucle a través de una cuerda 
    Como las cadenas son arrays, podemos recorrer los caracteres de una cadena, con un bucle.for
"""
# for x in "banana":
#   print(x)

""" 
String Length - Longitud de cuerda
    Para obtener la longitud de una cadena, usa la función.len()
"""
a = "Hello, World!"
#print(len(a)) 13

""" 
Check String - Cuerda de control
    Para comprobar si una frase o carácter concreto está presente en una cadena, podemos usar La palabra clave .in
"""

txt = "la patada voladora del mocho"
#print("mocho" in txt)  True

txt = "el grito mortal del mudo!"
if "mudoo" in txt:
  print("si, el sordo escucho el grito del mucdo")

""" 
Check if NOT - Comprueba si no
    Para comprobar si una frase o carácter concreto NO está presente en una cadena, podemos usar La palabra clave .not in
"""
# Comprueba si "caro" NO está presente en el siguiente texto:
txt = "The best things in life are free!"
#print("expensive" not in txt) True