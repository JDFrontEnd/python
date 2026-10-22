
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
#print(a[1]) e

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

""" 
Python - Slicing Strings - Cortes de cadenas

    Puedes devolver un rango de caracteres usando la sintaxis de cortes. Especifique el índice inicial y el índice final, separados por dos puntos, para devolver un parte de la cuerda.
"""
# Lleva los caracteres de la posición 2 a la posición 5 (no incluido):
b = "hello, world!"
# print(b[2:5]) ello
# Nota: El primer carácter tiene índice 0.
""" 
Corte desde el principio
    Al omitir el índice inicial, el rango comenzará en el primer carácter: 
"""
# Consigue los caracteres desde el principio hasta la posición 5 (no incluido):
b = "hello, world!"
# print(b[:5]) hello
""" 
Corte hasta el final
    Al omitir el índice final, el rango irá al final:
"""
# Lleva a los caracteres desde la posición 2 y hasta el final:
b = "Hello, World!"
# print(b[2:]) llo, world!
""" 
Indexación negativa
    Utiliza índices negativos para comenzar el corte desde el final de la cadena:
"""
# Descubre a los caracteres: De: "o" en "world!" (posición -5) Para, pero no incluyó: "d" en "world!" (posición -2):
b = "Hello, World!"
# print(b[-5:-2]) -5 pocision desde donde inicia la cadena contando de atras a delante -2 donde termina de atras adelante la posicion va desde 1 no desde 0, no existe un índice negativo 0, porque el 0 ya está reservado para el primer elemento desde el inicio

""" 
Python - Modify Strings - Modificar cadenas
    Python tiene un conjunto de métodos integrados que puedes usar en cadenas.
    
    Upper Case
    El método devuelve la cadena en mayúsculas:upper()
"""
a = "Hello, World!"
# print(a.upper())

""" Minúsculas
    El método devuelve la cadena en minúsculas:lower() """
# print(a.lower())

""" 
PRIMERA LETRA 
    convierte la primera letra en mayusculas
    capitalize()
"""
#print(a.capitalize())

"""
Eliminar espacios en blanco
    El espacio en blanco es el espacio antes y/o después del texto real, y muy a menudo quieres eliminar ese espacio. 
    El método elimina cualquier espacio en blanco desde el principio o el final:strip()
"""

a = " Hello, World!    "
# print(a.strip())

""" 
Reemplazar la cuerda

    El método replace() reemplaza una cadena por otra cadena:
"""

a = "Hello, World!"
#print(a.replace("H", "J"))

""" 
Split String - Cuerda partida
    El método split() divide la cadena en subcadenas si encuentra instancias del separador:
"""
a = "Hello, World!"
#print(a.split(",")) returns ['Hello', ' World!']

""" 
Python - Formato - Cadenas

    F-Strings

    Para especificar una cadena como una cuerda f, simplemente pon a delante de la cuerda literal, f y {} añadir corchetes como marcadores de posición para variables y otras operaciones.
"""

age = 36
txt = f"My name is John, I am {age}"


""" Un marcador de posición puede incluir un modificador para formatear el valor.

Un modificador se incluye añadiendo dos puntos seguido de un tipo de formato legal, como que significa número de punto fijo con 2 decimales::.2f """
price = 59
txt = f"The price is {price:.2f} dollars"
#print(txt)

""" 
Un marcador de posición puede contener código Python, como operaciones matemáticas:
"""

txt = f"The price is {20 * 59} dollars"

""" 
Escape Character

Un caracter de escape es una barra diagonal seguida del caracter que quieres insertar.\

Un ejemplo de carácter ilegal es una doble comilla dentro de una cadena rodeada de comillas dobles:

txt = "We are the so-called "Vikings" from the north."

El carácter escape te permite usar comillas dobles cuando normalmente no te dejarían:

"""
txt = "We are the so-called \"Vikings\" from the north."


# \'	Single Quote - comillas simples
# \\	Backslash - barra invertidad
# \n	New Line - salto de linea
# \r	Carriage Return	- retorno de carriage
# \t	Tab	
# \b	Backspace - retroceso
# \f	Form Feed - salto de pagina
# \ooo  Octal value - valor octal	
# \xhh	Hex value - 

""" 
Métodos de cuerdas

    Python tiene un conjunto de métodos integrados que puedes usar en cadenas.
    
    Nota: Todos los métodos de cadenas devolven nuevos valores. No cambian la cuerda original.

capitalize() convierte el primer caracter en mayucula 
casefold() convierte un str en minusculas
center() devuelve el str centrado
count()	Returns the number of times a specified value occurs in a string
encode() Returns an encoded version of the string
endswith() Returns true if the string ends with the specified value
expandtabs() Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

age = 20
print("edad:"+ str(age))
