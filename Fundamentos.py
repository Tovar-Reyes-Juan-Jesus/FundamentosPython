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

nuevoTema("SETS o Conjuntos")
#el orden no es definido y solo permiten elementos en su tipo.
#se declaran entre llaves
a = {50,20,30,40,10,50}#son elementos unicos y no se repiten a la hora de ejecutar 
print("Conjunto a = ",a,type(a))
print(type(a))

nuevoTema("DICCIONARIO")
#es un par ordenado el valor puede ser de cualquier valor ya sea la clave y el valor.
d = {1:"valor1","Valor2":2j} #sintaxis: Clave_:_Valor
print(d, type(d))
print("d[Valor2] = ",d["Valor2"])


nuevoTema("CADENAS")
#son tipo secuenciales que pueden hacer cualquiera agregar un elemento en especifico.

cadena1 = "Cadena con comillas dobles"
cadena2 = 'Cadena con comillas simples'

print(cadena1,type(cadena1))
print(cadena2,type(cadena2))

cadenaMultilinea = ''' Esta es una cadena de varias lineas     con     tabulares y
            saltos
de
linea''' #cadena formateada donde tal cual se pone es como se imprime solo si esta en un print

print(cadenaMultilinea)

print("Segmentacion de cadenas")

print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1]) #con numeros negativos regresa el valor al ultimo ala izquierda.
print(cadena1[0:18:1])#son saltos donde brinca o sancada para definir los caracteres donde son .
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1= "hola"
cadena4= (cadena1 + " ") * 5 #estamos multiplicando 5 veces, donde se repiten.
print(cadena4)

#para poder saltar o omitir cierto caracteres.
#parametros con valor.
#una cadena no la puedes cambiar, lo que puede cambiar es la variable.
cadena5 = cadena4.upper()
print(cadena5)