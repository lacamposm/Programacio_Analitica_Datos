#!/usr/bin/env python
# coding: utf-8

# # Funciones en Python,
# 
# **Temas:**
# 
# * Funciones en python
# * Manejo de errores en Python

# In[1]:


get_ipython().system('python --version')


# ## Definición de función
# 
# Una función es un bloque fundamental en la programación. Sirve para agrupar una serie de líneas de código que han sido concebidas para solucionar un problema específico. Una vez la función ha sido programada correctamente, es decir que resuelve el problema retornando la salida esperada para unas entradas dadas, se convierte en un bloque más complejo que se puede reutilizar en otros programas. La función trabaja como si fuera una nueva instrucción del lenguaje que es capaz de realizar una tarea un poco más compleja que las instrucciones que tenía antes. Lo ideal con las funciones es compartir y distribuir estas para un uso generalizado de la solución. 
# 
# En síntesis una función es una caja que tiene unas __entradas__, las cuales son procesadas para producir una __salida__. En la mayoría de situaciones el interés es simplemente como se puede usar la función, para lo cual solo se requiere el nombre, entradas (parámetros de la función) y salida (valor de retorno de la función).
# 
# 

# ## Crear una función
# 
# Para crear una función en pyhthon se sigue la siguiente sintaxis:
# 
# 
# ```python
# def nombre_funcion(parametro1, parametro2, ..., parametroN):
#     linea1
#     linea2
#     ...
#     lineaM
#     return valor
# ```
# En el esquema de función se identifican las siguientes partes:
# * __def__: es la palabra reservada de python para declarar una función, siempre tiene que escribirse. 
# * __nombre_funcion__: es un nombre válido que el programador quiera darle a la función para poderla usar en el futuro. Válido, es que no sea una palabra reservada, no sea vacia, no inicie con número o caracter especial. 
# * __parametros__: la lista de parámetros son las entradas de la función. Estas pueden ser una cantidad fija o variable, incluso puede no haber. Los parámetros pueden ser opcionales u obligatorios. Los parametros se escriben dentro de paréntesis redondos y se termina la línea con dos puntos ':'
# * __lineas__: las líneas representan a las líneas de código que se requieren para resolver el problema dado a la función. Pueden ser tantas como se necesiten. En este bloque, el cual debe llevar un nivel de sangria más, pueden ser llamadas otras funciones que esten definidas, incluso, se puede llamar la función a si misma.
# * __return__: es la palabra reservada en python para indicar que el valor de la salida ya fue calculado y que ya termina la función. Esta palabra no es requerida, pueden haber funciones que no tiene valor de salida. 
# * __valor__: es una variable que generalmente se crea dentro de la función y que se utiliza como la salida o el resultado de la función.
# 
# ### Ejemplo:
# 
# 
# ```python
# from datetime import datetime
# 
# def saludo_actual():
#     print('hola mundo: ', datetime.now())
# ```
# En este ejemplo se escribe una función sin entradas ni salidas, lo que hace simplemente es mostrar un saludo junto con la fecha y hora actual.
# 
# notas de interés
# * Para mostrar la fecha y hora actual dentro de la función se usa otra función llamada __now()__ y que está dentro de la librería llamada _datetime_, la cual se debe importar para que la función la reconozca. 
# * Tenga en cuenta que la definición de la función no significa que se ejecute. Por tanto se debe llamar la función de manera correcta en el bloque de código explícitamente. Para esto escriba el nombre de la función con los paréntesis:
# 
# ```python
# # llamado de la función:
# saludo_actual()
# ```

# In[2]:


# pruebe el ejemplo en esta celda de código
from datetime import datetime
 
def saludo_actual():
    print('hola mundo: ', datetime.now()) 


# In[3]:


saludo_actual()


# ## Parámetros o argumentos y valor de retorno de una función
# 
# En general las funciones requieren parámetros o argumentos, para no tener una función plana como la anterior, que siempre muestra los mismo. La idea es que el resultado de la función (salida) dependa de los valores conocidos (llamados entradas). 
# 
# ### Ejercicio
# 
# Se requiere una función para calcular el error relativo porcentual. El cual está definido cómo:
# 
# $$e_r = \frac{e}{X} 100\%$$ 
# 
# En donde $e_r$ es el error relativo, $e$ es el error cometido y $X$ es la cantidad que se está midiendo. 
# 
# Para este caso: 
# * ¿cuáles son las entradas?
# * ¿cuáles son las salidas?
# * ¿cómo es el proceso para convertir las entradas en las salidas del problema?
# 
# 
# 

# In[4]:


## resuelva el ejercicio en esta celda de código

## Entradas: e el error cometido y la cantidas X que se está midiendo
## Salida: e_{r}, el error relativo.


# ## Manejo de argumentos en funciones:
# 
# Antes de continuar con los ejercicios se debe revisar en la documentación de [docs python 4.7](https://docs.python.org/3.7/tutorial/controlflow.html#more-on-defining-functions) las siguientes secciones:
# 
# * 4.7.1. Default arguments value
# * 4.7.2. Keyword Arguments
# * 4.7.3. Special parameters (Versiones 3.8 en adelante.)
# * 4.7.4. Arbitrary Argument Lists
# * 4.7.7. Documentation Strings

# In[5]:


def fib(n):    # Serie Fibonacci hasta n.
    """Imprime la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
      print(a, end=' ')
      a, b = b, a+b
    print()


# Observe que la función no tiene return. En caso de no tenerlo se da un None en la función al hacer uso de print().

# In[6]:


fib(5)


# In[7]:


## No imprime nada.
fib(0)


# In[8]:


print(fib(0))


# In[9]:


## Es posible reasignar a otro nombre que luego puede ser usado como una función. 
## Esto sirve como un mecanismo general para renombrar:
f = fib
f(100)


# In[10]:


## La sentencia return devuelve un valor en una función.
def fib2(n):  # Serie Fibonacci hasta n.
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result

f100 = fib2(100)    # call it
print(f100)


# In[11]:


## return sin una expresión como argumento retorna None.
def fib2(n):  # Serie Fibonacci hasta n.
     """Return None."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return 

f100 = fib2(100)   # call it
print(f100)


# In[12]:


## return sin una expresión como argumento retorna None.
def fib2(n):  # Serie Fibonacci hasta n.
     """Return None."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b      

f100 = fib2(100)   # call it
print(f100)


# ### Default arguments value

# In[13]:


## Es una función que puede ser llamada con menos argumentos que los que permite.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[14]:


ask_ok()


# In[14]:


# Llamado 1, solo parámetro prompt
ask_ok('Do you really want to quit?')


# In[ ]:


# Llamado 2, parámetro prompt y retries.
ask_ok('OK to overwrite the file?', 2)


# In[ ]:


# Llamado 3, todos los parámetros.
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# In[15]:


## Los default arguments value son evaluados en el momento de la definición de la función, en el ámbito de la definición.
## Si ya se ha definido el parámetro, este no cambía. Para que se haga se debe especificar en la función.
i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[16]:


f(7)


# In[17]:


## La siguiente función acumula los argumentos que se le pasan en subsiguientes llamadas:
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[18]:


## Si no se quiere que el valor por omisión sea compartido entre subsiguientes llamadas, se pueden escribir la función así:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[19]:


f(2,[4,5,8])


# ### Keyword arguments

# In[20]:


## Las funciones también puede ser llamadas usando keywords arguments de la forma kwarg=value. 
## Por ejemplo, la siguiente función:
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end = ' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
## acepta un argumento obligatorio (voltage) y tres argumentos opcionales (state, action, y type). 
## Esta función puede llamarse de cualquiera de las siguientes maneras:


# In[21]:


parrot(1000)                                          # 1 Argumento posicional


# In[22]:


parrot(voltage=1000)                                  # 1 keyword argument.


# In[23]:


parrot(voltage=1000000, action='VOOOOOM')           # 2 keyword arguments.


# In[24]:


parrot(action='VOOOOOM', voltage=1000000)            # 2 keyword arguments.


# In[25]:


parrot('a million', 'bereft of life', 'jump')       # 3 Argumento posicional.


# In[26]:


parrot('a thousand', state='pushing up the daisies')  # 1 posicional, 1 keyword.


# In[27]:


## Llamadas invalidas.
#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argumen


# In[28]:


## Error posicional.
parrot('a thousand', 'pushing up the daisies', voltage = "100000")


# In[29]:


## Ningún argumento puede recibir más de un valor al mismo tiempo. Aquí hay un ejemplo que falla debido a esta restricción:
def function(a):
     pass
     
function(0, a=0)


# In[30]:


## Note que *arguments es una tupla y **keywords es un diccionario que almacena todos los keyword arguments
## excepto todos aquellos que sean un parámetro formal.
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print("arguments is type: ",type(arguments))
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print("-" * 40)
    print("keywords is type:", type(keywords))
    print("-" * 40)


# In[31]:


## Note que *arguments es una tupla y **keywords es un diccionario que almacena todos los argumentos nombrados
## excepto todos aquellos que sean un parámetro formal.
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# ### Special parameters

# ### Arbitrary Argument Lists

# In[32]:


## La función concatena string via /
def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")


# In[33]:


## Se debe usar como keyword argument si está despues de *args
concat("earth", "mars", "venus", sep=".")


# In[34]:


concat("earth", "mars", "venus", ".")


# In[35]:


## Debe ser posicional también
concat(sep=".","earth", "mars", "venus")


# ---
# 
# ## Ejercicio en clase: __funciones__
# 
# ---
# 
# Construir una función de `Python` que pinte la curva Senosoidal, a partir de un intervalo dado de valores (xInicial, xFinal) y que devuelva los correspondientes valores pintados
# 
# _Antes de iniciar se deben importar las librerias:_
# 
# ```python
# import matplotlib.pyplot as plt
# import numpy as np
# ```
# 
# ### 1. Definir entradas y salidas
# 
# 
# ### 2. Escribir la función con las entradas y salidas
# 
# ```python
# def pintarSeno(xInicial, xFinal) :
#     plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)))
#     return np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal))
# ```
# 
# ### 3. Llamar la función con diferentes valores
# 
# 
# 
# ```python
# x, y = pintarSeno(0, 6.28)
# ```

# In[36]:


# celda para librerias
import matplotlib.pyplot as plt
import numpy as np


# In[37]:


np.linspace()


# In[ ]:


help(np.linspace)


# In[38]:


np.linspace(0,5,)


# In[ ]:


np.sin(np.linspace(0,5))


# In[40]:


# celda para definir función
def pintarSeno(xInicial, xFinal) :
    plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)))
    return np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal))


# In[41]:


# celda para llamar función
x, y  = pintarSeno(0, 6.28)


# ### 4. Capturar el error en los valores de entrada
# 
# - imprima el tipo de dato que recibe la función
# 
# ```python
#     if(xInicial >= xFinal):
#         raise ValueError("Error en los valores: xFinal debe ser mayor que XInicial")
# ```
# 

# In[42]:


# celda para definir función
def pintarSeno(xInicial, xFinal) :
    if(xInicial >= xFinal):
      raise ValueError("Error en los valores: xFinal debe ser mayor que XInicial")
    plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)))
    return np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal))


# In[43]:


# celda para llamar función
x, y = pintarSeno(6.28,0)


# ### 5. Usar valores por omisión
# 
# Revisar los diferentes comportamientos de los parámetros:
# - Parámetros obligatorios y opcionales
# - Parámetros posicionales o por posición 
# - Definir parámetros por nombre
# - Cambiar el orden de los parámetros

# ### 6. Cómo hacer para imprimir todos los argumentos
# 
# 
# 
# ```python
# def tt(k, m=3, *arguments, **keywords):
#     print('Obligatorias: k =', k)
#     print('Opcionales:   m =', m)
#     print("-" * 20, 'args', "-" * 20)
#     for arg in arguments:
#         print(arg)
#     print("-" * 20, 'keys', "-" * 20)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
# 
# ```
# ### Ejercicio
# 
# - Analice los siguientes llamados a la función y pruebe otros comportamientos para comprender su funcionamiento.
# 
# 
# 
# ```python
# tt(1,2,3,4,5,6,7,x=8,y=9,z=10,a=11)
# ```
# 
# ```python
# tt(x=8, y=9, z=10, a=11, k=2)
# ```
# 
# ```python
# tt(1, 2, s='NA')
# ```
# 
# ```python
# tt(t=1, u=2, v=3)
# ```
# 
# ```python
# tt(1, m=2, s='SA', k=3)
# ```
# 
# ```python
# tt(1,2,3,4,5,6,7,x=8,y=9,z=10,a=11, x=6)
# ```
# 

# In[44]:


# celda para probar
def tt(k, m=3, *arguments, **keywords):
    """
    Descrip: Proporciona los parametros que son obligatorios, los opciones, además muestra los elementos ingresados
             por el usuario, más el diccionario con las nuevas variables.
    Argumentos: K: Obligatorio, m = 3 opcional, *arguments: Valores ingresados por el usuario, **keywords: Las nuevas variables
                ingresadas por el usuario.
    Output: Sin retorno
    """
    print('Obligatorias: k =', k)
    print('Opcionales:   m =', m)
    print("-" * 20, 'args', "-" * 20)
    for arg in arguments:
        print(arg)
    print("-" * 20, 'keys', "-" * 20)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[ ]:


tt()


# In[46]:


tt(5)


# In[47]:


tt(8,9)


# In[48]:


tt(8,9,3)


# In[49]:


tt(8,9,3,5,8)


# In[50]:


tt(1,2,3,4,5,6,7,x=8,y=9,z=10,a=11)


# In[51]:


tt(x=8, y=9, z=10, a=11)


# In[52]:


tt(x=8, y=9, z=10, a=11, k=2)


# In[53]:


tt(t=1, u=2, v=3)


# In[54]:


tt(1, 2, s='NA')


# In[55]:


tt(1, m=2, s='SA', k=3)


# In[56]:


tt(1,2,3,4,5,6,7,x=8,y=9,z=10,a=11, x=6)


# ### Ejercicio
# - Cree una función que reciba una cantidad arbitraria de parámetros numéricos y haga el promedio. En caso de no recibir parámetos que lance un error. Pruebe la función 
#     - sin parámetros, 
#     - con un parámetro,
#     - con muchos parámetros y de diferente tipo
# 

# In[75]:


def prom(*args):
  print(f'{"-"*20}\nBienvenido\n{"-"*20}')
  print("Esta programa calcula el promedio de la cantidad de números que usted desee")
  print("-"*80)
  if len(args) == 0:
    raise ValueError("Error en los valores: Debe ingresar al menos un valor")
  acum = 0
  for a in args:
        acum += a # acum = acum + a
  print("El promedio de los numeros", args, "es:")
  return round(acum/len(args),2)


# In[74]:


prom(5,4,1,2.5,6,7,8)


# ### 7. Documentar la función para el usuario
# 
# - Descripción + argumentos (Args:) + retorno (Return:) + lanzamiento de errores (Raise:)
# - Use la impresión de la documentación 
# 
# ```python
# print(my_function.__doc__)
# ```
# 
# 

# In[ ]:


# celda de código para probar
print (tt.__doc__)


# In[27]:


import pandas as pd
help(pd.DataFrame)


# ---
# ## 8. Crear nuevos parámetros en la función (**ejercicio fuera de clase**)
# ---
# 
# Aumentar la capacidad de personalizar la gráfica de la función 'pintarSeno'  agregando parámetros opcionales que permitan configurar:
# - Título de la gráfica 
# - Título del eje X
# - Título del eje Y
# - Color de la curva
# - Ancho de línea de la curva
# - Configurar hasta donde van los valores en los ejes x, y
# - Poner cuadrícula
# - Definir el tamaño de la figura
# 
# En el siguiente ejemplo se configuran todas las opciones de personalización solicitadas. Tome este ejemplo y convierta los valores fijos en parámetros.
# 
# ```python
# def pintarSeno(xInicial, xFinal) :
#     # color {rojo 'r', azul 'b', verde 'g', magenta 'm', cyan 'c', amarillo 'y', negro 'k'}
#     color = 'm'
#     # tamaño de la figura (ancho, alto)
#     fig = plt.figure(figsize =(14,8))
#     # pintado de la gráfica con color y ancho de línea
#     plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)), color, linewidth=3)
#     # titulo de la gráfica
#     plt.title('Titulo de la gráfica')
#     # título eje x
#     plt.xlabel('Eje X')
#     # título eje y
#     plt.ylabel('Eje Y')
#     # rango de los ejes [x_min, x_max, y_min, y_max]
#     plt.axis([12.56, 18.85, -2, 2])
#     # agregar cuadrícula a la gráfica
#     plt.grid()
#     # retornar los valores
#     return np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal))
# 
# x, y = pintarSeno(10, 20)
# ```

# In[33]:


# celda para probar
def pintarSeno(xInicial, xFinal) :
    # color {rojo 'r', azul 'b', verde 'g', magenta 'm', cyan 'c', amarillo 'y', negro 'k'}
    color = 'm'
    # tamaño de la figura (ancho, alto)
    fig = plt.figure(figsize =(14,8))
    # pintado de la gráfica con color y ancho de línea
    plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)), color, linewidth=3)
    # titulo de la gráfica
    plt.title('Titulo de la gráfica')
    # título eje x
    plt.xlabel('Eje X')
    # título eje y
    plt.ylabel('Eje Y')
    # rango de los ejes [x_min, x_max, y_min, y_max]
    plt.axis([12.56, 18.85, -2, 2])
    # agregar cuadrícula a la gráfica
    plt.grid()
    # retornar los valores
    return np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal))

x, y = pintarSeno(0, 20)


# ### Ambito de las variables
# Se debe tener ciudado con el uso de las variables fuera y dentro de las funciones cuando tienen el mismo nombre. A través de los ejemplos identifique qué es lo que sucede. Cuándo son la misma variable y cuándo son variables distintas.
# 
# #### Ejemplo 1:
# 
# 
# ```python
# def ff():
#     print('inside:', b, c)
#     a = 10
# 
# b = 13
# c = 3
# 
# ff()
# print('outside:',b, c, a)
# 
# ```
# 
# 
# 
# 

# In[ ]:


def ff():
    print('inside:', b, c)
    a = 10


# In[ ]:


ff()


# In[ ]:


a


# In[ ]:


b = 13 ## Variable global
c = 3 ## Variable global
ff()


# In[ ]:


print('outside:',b, c, a) # Variable local


# #### Ejemplo 2:
# 
# 
# ```python
# # comparado al anterior, por qué no funciona?
# def ff1():
#     print('inside ff1:', b, c)
#     d = 4
#     
# def ff2():
#     print('inside ff2:', b, c)
#     b = 23
#     d = 14
#     
# 
# b = 57
# c = 8
# 
# ff1()
# print('outside(1):',b,c)
# ff2()
# print('outside(2):',b,c,d)
# 
# ```
# 

# In[ ]:


def ff1():
    print('inside ff1:', b, c)
    d = 4

def ff2():
    print('inside ff2:', b, c)
    b = 23
    d = 14


# In[ ]:


ff1()


# In[ ]:


ff2()


# In[ ]:


print('outside(1):',b,c)


# In[ ]:


print('outside(2):',b,c,d)


# #### Ejemplo 3:
# Alcance de variables en funciones anidadas
# 
# ```python
# def ff1():
#     a = 48
#     def ff2():
#         a = 57
#         print('inside ff2:', a)
#     ff2()
#     print('inside ff1:', a)
#    
# a  = 39
# ff1()
# print('outside:', a)
# 
# ```
# 

# In[ ]:


# celda de código para probar
def ff1():
    a = 48
    def ff2():
        a = 57
        print('inside ff2:', a)
    ff2()
    print('inside ff1:', a)


# In[ ]:


a  = 39
ff1()


# In[ ]:


print('outside:', a)


# #### Ejemplo 4:
# 
# 
# ```python
# # ejemplo obtenido de https://www.datacamp.com/community/tutorials/scope-of-variables-python
# 
# name = 'Théo'
# 
# def change_name(new_name):
#     name = new_name
# 
# print(name)    
# 
# change_name('Karlijn')
# 
# print(name)
# 
# ```
# 

# In[ ]:


# celda de código para probar
name = 'Théo' ## Global

def change_name(new_name):
    name = new_name

print(name)    

change_name('Karlijn')

print(name)


# #### Ejemplo 5:
# Uso de la palabra reservada _global_
# 
# ```python
# # ejemplo obtenido de https://www.datacamp.com/community/tutorials/scope-of-variables-python
# name = 'Théo'
# 
# def change_name(new_name):
#     global name
#     name = new_name
# 
# print(name)
# change_name('Karlijn')
# print(name)
# ```
# 

# In[28]:


# celda de código para probar
name = 'Théo'

def change_name(new_name):
    global name
    name = new_name

print(name)
change_name('Karlijn')
print(name)


# #### Ejemplo 6:
# Modificación de listas dentro de una función
# 
# ```python
# def f(a, b):
#     x[1] = 7 
#     z = a+b
#     y = a-b
#     return z, y
# 
# x = [5, 6]
# w = 2
# print(f(x[0], x[1]))
# print(x)
# 
# ```
# 

# In[ ]:


# celda de código para probar
def f(a, b):
    x[1] = 7 
    z = a+b
    y = a-b
    return z, y

x = [5, 6]

print(f(x[0], x[1]))
print(x)


# ## Manejo de errores en python
# 
# __Errores de sintaxis__
#  Los errores de sintaxis son fáciles de arreglar puesto que solo hay que leer y comprender el mensaje que muestra el interpretador de python cuando se produce el error. 
# 
#  Los errores de lógica en la programación son más difíciles de encontrar puesto que el programa funciona y el interpretador no aporta mensajes en este sentido. Otro problema es cuando el algoritmo se queda en un ciclo infinito. En este caso se puede instalar un depurador para ejecutar el programa paso a paso, o también se pueden agregar mensajes de depuración para saber si el algoritmo está funcionando tal como se espera y de esta forma detectar alguna anomalía. 
# 
# __Aprender de los errores__
# 
#  Para aprender de los errores, en los siguientes algoritmos observe cual es el objetivo de cada uno y trate de hacerlos funcionar leyendo y arreglando los errores que muestra el compilador de python. También debe comentar que hace cada una de las líneas de código del algoritmo.
# ## Ejemplo de errores:
# - En operaciones no coinciden los tipos de datos
# - Los métodos no existen para el tipo de datos
# - División por cero
# - Error con el nombre de la variable
# - Errores de sintaxis
# - Error de estructura 
# - Errores en el sangrado de código
# 
# ## Ejercicio 
# - Lea cuidadosamente cada error que va apareciendo y corrija hasta que funcione perfectamente:
# - Verifique que el programa funciona bien con números entre 1 y 10, y que muestra el mensaje cuando el número no es válido
# 
# ```python
# print('El presente programa muestra la tabla de multiplicar de un número entre 1 y 10, de lo contrario dice que el número no es válido')
# x = input("ingrese un valor entero del 1 al 10: ")
# 
# if NOT(x <= 10 And x > 1) # nombre
#     printf("Error: el valor "+ str(x) + " ingresado no es válido") # str
#     else: # sangrado
#         mult = 1
#         while mult <= 10
#             print[mult,'x',x,'=',mult*x] 
#              mult = mult + 1  # sangrado
# 
# print('Fin del programa con éxito!!')
# ```

# In[ ]:


print('El presente programa muestra la tabla de multiplicar de un número entre 1 y 10, de lo contrario dice que el número no es válido')
x = int(input("ingrese un valor entero del 1 al 10: "))

if not(x <= 10 and x >= 1): # nombre
    print("Error: el valor "+ str(x) + " ingresado no es válido") # str
else:
  mult = 1
  while mult <= 10:
        print(mult,'x',x,'=',mult*x)
        mult = mult + 1  # sangrado

print('Fin del programa con éxito!!')


# ## Ejercicio
# 
# Realizar las siguientes funciones con su respectiva documentación y utilizando valores opcionales.
# 
# 1. Realizar una función que reciba el valor de día, mes y año, que retorne si la fecha resulta ser válida o no.
#     ```python
#     def validarFecha(dia, mes, año):
#     ```
# 
# 2. Realizar una función que recibe 3 vértices y retorna el área, el perímetro y si es triángulo rectángulo o no.
#     ```python
#     def infoTriangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
#     ```
# 
# 3. Aumentar la capacidad de la función 'pintarSeno'  con los parámetros opcionales como se especificó arriba.

# In[142]:


# EJERCICIO 1.
### Se considera que el usuario ingresa un número entero. #####

def validarFecha(day, moth, year):
  print(f"********************************************************************************************************************")
  print(f"********************************************************************************************************************")
  print(f'Este programa determina si la fecha ingresada está entre el 01 de enero del 2000 y hasta el 31 de diciembre del 2020')
  print(f"********************************************************************************************************************")
  print(f"********************************************************************************************************************")
  print(f'La fecha ingresa es: día --> {day}, mes --> {moth}, año --> {year}')
#### Debe ingresar un número con las condicones numéricas dadas.
  while (day>31) or (day<1):
    day = int(input("Error: Ingrese el día con un valor entre 1 y 31 "))
  while (moth<1) or (moth)>12:
    moth = int(input("Error: Ingrese el mes con un valor entre 1 y 12 "))
  while (year<2000) or (year>2020):
    year = int(input("Error: Ingrese el año con un valor entre 2020 y 2020"))
#### Condiciones de día 31 meses abril, junio, septiembre y noviembre
  while (day == 31) and (moth==2 or moth == 4 or moth == 6 or moth == 9 or moth == 11):
    moth = int(input("Error: El mes ingresado no tiene día 31. Ingrese un mes válido entre 1 y 12: "))
### Condicion día 30 de febrero no disponible.
  while (day == 30) and (moth == 2):
    moth = int(input("Error: Febrero no tiene día 30. Ingrese un mes válido entre 1 y 12: "))
### 
  while (year%4 !=0) and (day==29) and (moth==2):
    year = int(input("Error: El año ingreado no es bisiestro. Ingrese un año bisiesto entre el año 2000 y 2020: "))
  print(f"********************************************************************************************************************")
  print(f'La fecha: día --> {day}, mes --> {moth}, año --> {year}, es una fecha correcta')
  print(f"********************************************************************************************************************")


# In[143]:


validarFecha(20,13,2005)


# In[36]:


#  EJECICIO 3.
import matplotlib.pyplot as plt
import numpy as np

def pintarSeno(xInicial, xFinal, color = "m", ancho_linea = 1, tamano = (14,8), titulo = "Titulo de la gráfica", eje_x = "Eje X",\
               eje_y = "Eje Y", x_min = 12.56, x_max = 18.85, y_min = -2, y_max=2) :
    if xInicial >= xFinal:
      raise ValueError("Error en los valores: xInicial debe ser menor que xFinal")
    fig = plt.figure(figsize = tamano) # tamaño de la figura (ancho, alto)
    # pintado de la gráfica con color y ancho de línea
    plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)), color = color, linewidth = ancho_linea)
    plt.title(titulo) # titulo de la gráfica
    plt.xlabel(eje_x) # título eje x
    plt.ylabel(eje_y) # título eje y
    plt.axis([x_min, x_max, y_min, y_max]) # rango de los ejes
    plt.grid() # agregar cuadrícula a la gráfica
    # retornar los valores
    return np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal))

x, y = pintarSeno(10, 20, color="#FF0000", ancho_linea=10, tamano=(10,1), titulo = "MI TITULO PERSONAL!!!!", eje_x= "HOLA ", eje_y = "HOLAAAAAAAA")


# In[30]:


#  EJECICIO 3.
import matplotlib.pyplot as plt
import numpy as np

def pintarSeno(xInicial, xFinal, **keywords):
    if xInicial >= xFinal:
      raise ValueError("Error en los valores: xInicial debe ser menor que xFinal")
    dicc = {"color":"m", "ancho_linea":1, "tamano":(14,8), "titulo": "Titulo de la gráfica", "eje_x": "EJE X", "eje_y":"EJE Y",\
            "x_min": 12.56, "x_max" : 18.85, "y_min":-2, "y_max":2}
    for keys, values in keywords.items():
      dicc[keys] = values
    fig = plt.figure(figsize = dicc["tamano"]) # tamaño de la figura (ancho, alto)
    # pintado de la gráfica con color y ancho de línea
    plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)), color = dicc["color"], linewidth = dicc["ancho_linea"])
    plt.title(dicc["titulo"]) # titulo de la gráfica
    plt.xlabel(dicc["eje_x"]) # título eje x
    plt.ylabel(dicc["eje_y"]) # título eje y
    plt.axis([dicc["x_min"], dicc["x_max"], dicc["y_min"], dicc["y_max"]]) # rango de los ejes
    plt.grid() # agregar cuadrícula a la gráfica
    return 

pintarSeno(10, 20, color="g", ancho_linea=5, tamano=(20,5), titulo = "OTRA OPCIÓN", eje_x= " HOLAAAAAA", eje_y = ":) :)  :)")


# In[31]:


# celda para probar
def pintarSeno(xInicial, xFinal, color = "b", linewidth = 1, titulo = "Titulo de la gráfica", ) :
    # color {rojo 'r', azul 'b', verde 'g', magenta 'm', cyan 'c', amarillo 'y', negro 'k'}
    color = 'm'
    # tamaño de la figura (ancho, alto)
    fig = plt.figure(figsize =(14,8))
    # pintado de la gráfica con color y ancho de línea
    plt.plot(np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal)), color, linewidth=3)
    # titulo de la gráfica
    plt.title('Titulo de la gráfica')
    # título eje x
    plt.xlabel('Eje X')
    # título eje y
    plt.ylabel('Eje Y')
    # rango de los ejes [x_min, x_max, y_min, y_max]
    plt.axis([12.56, 18.85, -2, 2])
    # agregar cuadrícula a la gráfica
    plt.grid()
    # retornar los valores
    return np.linspace(xInicial, xFinal), np.sin(np.linspace(xInicial, xFinal))

x, y = pintarSeno(0, 20)

