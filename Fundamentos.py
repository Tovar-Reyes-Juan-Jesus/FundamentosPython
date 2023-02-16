def nuevoTema(tema): #funcion en python : no tenemos un tipo de dato de retorno, usamos la palabra de def
    #despues el nombre del parametros no recibe el tipo de parametros. se usa el ":" para iniciar como la llave (UTF8)
    #despues de identificar que los dos puntos ":" usar la palabra reservada llamada "pass" para una funcion para que este vacia.

    print("\n ======", tema, "=========\n")

#hecho por Juan de jesus Tovar Reyes 09/02/2023
#Este es un comentario de una linea
nuevoTema("Operador aritmetico")
print("operador division entera (10 // 3)", 10 // 3)
print("operador potencia (5 ** 3): ", 5 ** 3) #Operador **



'''este es un comentario 
de varias 
lineas'''
nuevoTema("Operador Logicos")
print("Operador and (True and False): ", True and False)
#Actividad : Imprimir la tabla de verdad de los operadores logicos.

#Operador con and
print("Operador and (True and True): ", True and True)
print("Operador and (True and False): ", True and False)
print("Operador and (False and False): ", False and False)
print("Operador and (False and True): ", False and True)

#Operador con or
print("Operador or (True or True): ", True or True)
print("Operador or (True or False): ", True or False)
print("Operador or (False or False): ", False or False)
print("Operador or (False or True): ", False or True)

#Operador con not
print("Operador not ( not True): ", not True)
print("Operador not ( not False): ", not False)

nuevoTema("Operador de Comparacion")
print("2 == 3", 2 == 3)
#Actividad: Agregar los demas operadores de comparacion

#Menor que
print("2 < 3", 2 < 3)
#Menor o Igual
print("2 <= 3", 2 <= 3)
#mayor que
print("2 > 3", 2 > 3)
#Mayor o igual
print("2 >= 3", 2 >= 3)
#Diferente de
print("2 != 3", 2 != 3)

nuevoTema("Variables")
variable1 = 10
_variable2 = 6.2456
Variable3 = "Juancho"
dosPalabras = "Hola" #No hay afecto en el codigo de que se vean asi
dos_palabras = "Hello"

print(variable1, _variable2, Variable3, dos_palabras, dosPalabras) #no hay limites de parametros, donde son variables validas

a, b, c = 10, 5.16, "palabra"
print(a, b, c)
#python no tiene un numero maximo en numero entero, depende de la memoria de ram en la computadora.
#Actividad
nuevoTema("Enteros")
w=105
x= 9999999999999999999999999999999999999
y= -5
z = 0b0111011100
h= 0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

#la precision de python con los flotantes son de 15 decimales.
nuevoTema("Flotantes")
x = 1297.50
print(x, type(x))
y = 0.66757
print(y,type(y))

#numero imaginario se representa con una j de imaginario,
nuevoTema("Numero Complejos")
x = -46j
y = 12+ 45j
z = 2j
print(x, type(x))
print(y, type(y))
print(z,type(z))

nuevoTema("Booleanos")
lis = [8]
print(lis,"es", bool(lis))
t = () #con parentesis es una duplas
print(t,"es", bool(t))
new = 'hello'
print(new,"es",bool(new))
num = 99
print(num,"es", bool(num))
comp = 1 + 0j
print(comp,"es",bool(comp))
val = None #es equivalente a un NULL en python es recomendable tenerlo o usarlo.
print(val,"es",bool(val))
#python no existen ni se hacen arreglos, que se puede usar las listas. #nonepine

nuevoTema("LISTAS") #no son arreglos
a = [10, 20.5, "python list"]
print(a)
print(a[1])
a[0] = "hola"
print(a)

#las tuplas son como las listas pero nos inmutables ya no se puede cambiar el valor.
nuevoTema("TUPLAS")
t = (25, "tupla", 1+10j, 3.1416)
print(t)
print(t[2])
print("t[0:2]", t[0:2]) #esta es una sintaxis con un rango.
print("t[1:4]", t[1:4])
#t[1] = 34 Operacion no valida en duplas.

#seguir con SETS, Diccionario y cadenas.

nuevoTema("SETS")
a = {50,20,30,10,40}
print("a = ",a)
print(type(a))

nuevoTema("DICCIONARIOS")
d = {1:'val1',2:'val2'}
print(type(d))
print("d[1] = ",d[1])
print("d[2] = ",d[2])

nuevoTema("CADENAS")

s = "Esto es una simple linea de caracteres."
print(s)

s2 = '''Una multilineas
 de caracteres. '''

print(s2)

#print("hi")
