#!/usr/bin/env python
# coding: utf-8

# # Estructuras de datos en python
# 
# 
# **Temas:**
# 
# * Listas
# * Tuplas
# * Conjuntos
# * Diccionarios

# ## 1. Listas
# 
# Una lista es un tipo de estructura de datos que alamacena una secuencia de elementos, los cuales quedan ordenados en relación a  un índice utilizado para accederlos. Este tipo de estructura permite almacenar y mezclar todo tipo datos, como: enteros, decimales, cadenas, otras listas, y objetos.
# 
# Una lista vacía (sin elementos en su interior) puede ser declarada en python de la siguiente forma:
# 
# ```python
# lst_uno = []
# lst_dos = list()
# print(lst_uno)
# print('cantidad elementos en lista: ',len(lst_uno))
# ```
# 
#  Las listas pueden contener elementos del mísmo o diferente tipo.
# 
# 
# ```python
# lst_ent = [1, 2, 3, 4, 5]
# lst_real = [1.0, 2.1, 4.8, 6.2]
# lst_fecha = ["Martes", 29, 'de Enero', 2019]
# ```
# * Generar secuencias o listas con valores iniciales...

# In[1]:


# celda de código para practicar
lst_uno = []
lst_dos = list()
print(lst_uno)
print('cantidad elementos en lista:',len(lst_uno), type(lst_uno))


# ### Agregar elementos a una lista.
# 
# Usted puede agregar un elemento a una lista vacía o a una lista que ya tenga elementos a partir de la función **append()**. Esta función requiere como argumento el elemento que usted quiere añadir a la lista.
# 
# 
# 
# ```python
# lst_uno.append('primero')
# lst_uno.append('segundo')
# lst_uno.append([2,5])
# print(lst_uno)
# print('cantidad elementos en lista: ',len(lst_uno))
# ```
# Luego de imprimir la lista, usted puede darse cuenta que el último elemento que se agregó fue una lista. Fijese bien que este se agrega a partir de la función *append* como un único elemento.
# 
# En caso de que se requiera añadir a una lista los elementos de otra lista como elementos independientes, deberá utilizar la función **extend()**
# 
# 
# ```python
# lst_uno.extend([4,6,7])
# print(lst_uno)
# lst_uno.extend([122]*5)
# ```

# In[2]:


# celda de código para practicar
lst_uno.append('primero')
lst_uno.append('segundo')


# In[3]:


lst_uno.append([2,5])
print(lst_uno)
print('cantidad elementos en lista: ',len(lst_uno))


# In[4]:


lst_uno.extend([4,6,7])
print(lst_uno)


# In[5]:


[122]*5


# In[6]:


[[1,2]]*8


# In[7]:


lst_uno.extend([122]*5)
print(lst_uno)


# In[8]:


## Otra forma de usar .extend()
lst_uno[len(lst_uno):] = ["maestria", "analítica", "datos"]
lst_uno


# In[9]:


# celda para probar
print(lst_uno)


# #### Ejercicio 1: 
# 
# Suponga usted que tiene que ir a mercar y debe ir anotando el nombre de los productos y el respectivo precio de todo lo que quiere llevar. El propósito de esta actividad es saber cuanto debe pagar antes de llegar a la caja. Cada vez que usted ingrese un producto a su canasta, deberá anotar el nombre y el valor del producto. Una vez haya finalizado sus compras deberá conocer la cantidad de productos y el total a pagar. ¿Cómo piensa resolver el problema?

# In[10]:


# Solución del ejercicio 1.
# inicialización de variables

lst_val_prod = []
lst_nom_prod = []
total_prod = 0.0


# ### Métodos para recorrer una lista
# Existen varios métodos en `Python` para recorrer una lista:
# 1. Usando los índices mediante un ciclo _while_
# 2. Usando los índices mediante un ciclo _for_
# 3. Usar un ciclo _for_ con los elementos 

# In[11]:


print(lst_uno)


# In[12]:


## Proporciona el índice del primer elemento con ese nombre.
lst_uno.index("primero")


# In[13]:


for elem in lst_uno:
  print("-"*80)
  print(f'El elemento --> {elem}, tiene índice en Python de {lst_uno.index(elem)} y es el elemento {lst_uno.index(elem)+1}')
print("-"*100)


# ### 1.2 **Acceder a los elementos de una lista.**
# 
# El acceso a los elementos de la lista se realiza a través de sus índices. En `Python` los índices de una lista van desde 0 hasta el tamaño de la lista -1. Por ejemplo de la siguiente lista se puede obtener acceso a los elementos 3, 4 y 6 de la siguiente forma:
# 
# 
# 
# ```python
# lst_anim = ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Pez', 'Hamster', 'Tortuga']
# ```
# 
# |lst_anim |\[| Perro | Gato | Pájaro | Conejo | Pez | Hamster | Tortuga | \]
# 
# |--- ||:---: | :---: | :---: | :---: | :---: | :---: | :---: | ---
# 
# |índices |+| 0 | 1 | 2 | 3 | 4 | 5 | 6 |  |
# 
# |índices |-| -7 | -6 | -5 | -4 | -3 | -2 | -1 |  |
# 
# ```python
# # Elemento: 3, índice del elemento: 2.
# print(lst_anim[2])
# # Elemento: 4, índice del elemento: 3.
# print(lst_anim[3])
# # Elemento: 6, índice del elemento: 5.
# print(lst_anim[5])
# ```
# 
# También puede modificar el valor de alguno de los elementos de la siguiente forma:
# 
# ```python
# # Modificando el elemento 4 que tiene por índice 3.
# lst_anim[3] = 'Jirafa'
# print(lst_anim)
# ```

# In[14]:


# celda de código para practicar
lst_anim = ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Pez', 'Hamster', 'Tortuga']
lst_anim


# In[15]:


# Elemento: 3, índice del elemento: 2.
print(lst_anim[2])
# Elemento: 4, índice del elemento: 3.
print(lst_anim[3])
# Elemento: 6, índice del elemento: 5.
print(lst_anim[5])


# In[16]:


# Modificando el elemento 4 que tiene por índice 3.
lst_anim[3] = 'Jirafa'
print(lst_anim)


# ### 1.3 Funciones recurrentes para listas.
# 
# A continuación se muestran otros métodos para las listas en `python`.
# 
# ```python
# 
# lst_anim = ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Pez', 'Hamster', 'Tortuga']
# print(lst_anim)
# # Remueve los elementos de la lista de acuerdo al argumento pasado a la función.
# lst_anim.remove('Pájaro')
# print(lst_anim)
# # Devuelve el número del indice del elemento que se pasa como argumento a la función.
# lst_anim.index('Conejo')
# # Devuelve la cantidad de veces que se repite el elemento que se pasa como argumento en la función.
# lst_anim.count('Pez')
# # Invierte el orden de los elementos de la lista.
# lst_anim.reverse()
# print(lst_anim)
# # Inserta un elemento en la posición inidicada. Lo argumentos para la función 
# #son el indice donde se quiere insertar y el elemento a insertar.
# lst_anim.insert(2,'Caballo')
# print(lst_anim)
# # Remueve el elemento de la lista que se pasa como argumento (índice del elemento)
# # a la función. La función pop devuelve el elemento removido. 
# anim = lst_anim.pop(2)
# print(anim)
# # Remueve todos los elementos de la lista.
# lst_anim.clear()
# print(lst_anim)
# ```
# - Generar ciclos para recorrer listas (función zip)
# - Buscar un elemento en una lista (operador in)

# In[17]:


# pruebe una por una las instrucciones de arriba
lst_anim = ['Perro', 'Gato', 'Pájaro', 'Conejo', 'Pez', 'Hamster', 'Tortuga']
print(lst_anim)


# In[18]:


# Remueve los elementos de la lista de acuerdo al argumento pasado a la función.
lst_anim.remove('Pájaro')
print(lst_anim)


# In[19]:


# Devuelve el número del indice del elemento que se pasa como argumento a la función.
lst_anim.index('Conejo')


# In[20]:


# Devuelve la cantidad de veces que se repite el elemento que se pasa como argumento en la función.
lst_anim.count('Pez')


# In[21]:


# Invierte el orden de los elementos de la lista.
lst_anim.reverse()
print(lst_anim)


# In[22]:


# Inserta un elemento en la posición inidicada. Lo argumentos para la función son el indice donde se quiere insertar y el
# elemento a insertar.
lst_anim.insert(2,'Caballo')
print(lst_anim)


# In[23]:


# Remueve el elemento de la lista que se pasa como argumento (índice del elemento) a la función. La función pop devuelve 
# el elemento removido. 
anim = lst_anim.pop(2)
print(anim)
print(lst_anim)


# In[24]:


# Remueve todos los elementos de la lista.
lst_anim.clear()
print(lst_anim)


# ### Manipular sublistas.
# 
# En algunos casos al trabajar con listas para la resolución de problemas es necesario extraer partes de la lista original. Python ofrece esta posibilidad  con la siguiente estructura:
# 
# ```python
#   nom_lista[<indice inicio> : <indice final + 1>]
# ```
# **Ejemplos:**
# 
# ```python
# 
# l1 = list(range(-20,20,2))
# print(l1)
# l2 = l1[2:8]   # Lista con los elementos del índice 2 hasta el 7
# print(l2)
# l2 = l1[1:]    # Lista con los elementos del índice 1 hasta el final de la lista
# print(l2)
# l2 = l1[:5]    # Lista con los elementos desde el inicio hasta el índice 4
# print(l2)
# l2 = l1[:]     # Lista con todos los elementos
# print(l2)
# l2 = l1[15:15] # Lista con los elementos del índice del 15 al 15 (vacía)
# print(l2)
# ```

# In[25]:


# pruebe las instrucciones una por una
l1 = list(range(-20,20,2))
print(l1)


# In[26]:


l2 = l1[2:8]   # Lista con los elementos del índice 2 hasta el 7
print(l2)


# In[27]:


l2 = l1[3:]    # Lista con los elementos del índice 1 hasta el final de la lista
print(l2)


# In[28]:


l2 = l1[:5]    # Lista con los elementos desde el inicio hasta el índice 4
print(l2)


# In[29]:


l2 = l1[:]     # Lista con todos los elementos, además puede crear una copy de la lista.
print(l2)


# In[30]:


l2 = l1[15:15] # Lista con los elementos del índice del 15 al 15 (vacía)
print(l2)


# ### Ejercicio 2
# 
# Usted también puede modificar los elementos de una lista usando sublistas. Revise con cuidado cada una de las siguientes líneas de código, trate de predecir lo que va a suceder y valide cada uno de los comportamientos presentados. El insertar, modificar y eliminar sublistas también se hace a partir de los índices de los elementos de la lista.
# 
# ```python
# letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'ñ', 'o']
# print(letras)
# letras[1:4] = ['k']               # Se sustituye la sublista ['b', 'c', 'd'] por ['k'], solo reemplazara el elemento 1 de la lista
# print(letras)
# letras[1:4] = [1, 2]              # Se sustituye la sublista ['k', 'c' , 'd'] por [1, 2], reemplazará 2 elementos de la lista
# print(letras)
# letras[3:4] = [76]                # Se sustituye la sublista ['g'] por [76], reemplazará 1 elemento de lista
# print(letras)
# letras[6:6] = ['%', '&']          # Se inserta la sublista ['%', '&'] a partir de la posición 6 de la lista
# print(letras)
# letras[0:3] = []                  # Se elimina la sublista ['a', 1, 2] a partir de la posición 0 hasta la 2
# print(letras)
# letras[-100:-50] = ['q','a','z']  # Se inserta ['q','a','z']. Python acepta valores de índices fuera del rango. Para este caso se insertará la sublista al inicio
# print(letras)
# letras[120:140] = ['q','a','z']   # Se inserta ['q','a','z']. Python acepta valores de índices fuera del rango. Para este caso se insertará la sublista al final
# print(letras)
# del letras[10]                    # Borrará el elemento que tiene por índice 10 de la lista
# print(letras)
# del letras[8:]                    # Borrará los elementos a partir del índice 8 hasta el final de la lista
# print(letras)
# ```
# 
# 

# In[31]:


# celda de código para practicar
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'ñ', 'o']
print(letras)


# In[32]:


# Se sustituye la sublista ['b', 'c', 'd'] por ['k'], solo reemplazara el elemento 1 de la lista
letras[1:4] = ['k']  
print(letras)


# In[33]:


# Se sustituye la sublista ['k', 'c' , 'd'] por [1, 2], reemplazará 2 elementos de la lista
letras[1:4] = [1, 2]   
print(letras)


# In[34]:


# Se sustituye la sublista ['g'] por [76], reemplazará 1 elemento de lista
letras[3:4] = [76]                
print(letras)


# In[35]:


# Se inserta la sublista ['%', '&'] a partir de la posición 6 de la lista
letras[6:6] = ['%', '&']          
print(letras)


# In[36]:


# Se elimina la sublista ['a', 1, 2] a partir de la posición 0 hasta la 2
letras[0:3] = []                  
print(letras)


# In[37]:


# Se inserta ['q','a','z']. Python acepta valores de índices fuera del rango. Para este caso se insertará la sublista al inicio
letras[-100:-50] = ['q','a','z']
print(letras)


# In[38]:


# Se inserta ['q','a','z']. Python acepta valores de índices fuera del rango. Para este caso se insertará la sublista al final
letras[120:140] = ['q','a','z']
print(letras)


# In[39]:


# Borrará el elemento que tiene por índice 10 de la lista
del letras[10]
print(letras)


# In[40]:


# Borrará los elementos a partir del índice 8 hasta el final de la lista
del letras[8:]
print(letras)


# ## list comprehension
# 
# 
# Las comprensiones de listas ofrecen una forma rápida y concisa para la creación de listas. Esto consiste en la codificación de una ***expresión*** seguida de la cláusula ***for*** a la cual se le puede añadir cláusulas ***if*** o ***for*** en caso de que sea requerido.
# 
# La comprensión de listas se destacan en `Python` para crear nuevas listas. Cada elemento es el resultado de algunas operaciones aplicadas sobre la lista (secuencia u objeto iterable) a partir de una condición u otros ciclos.
# 
# La estructura básica de una comprensión de lista es:
# 
# 
# ```
#  lista = [expresion for elemento in objeto_iterable]
# ```
# 
# 
# 
# La forma general de crear una lista con la estructura cíclica for es:
# 
# 
# 
# ```python
# # Lista de los números enteros del 1 al 10
# nums = []
# 
# for i in range(1,11):
#   nums.append(i)
# print(nums)
# 
# ```
# 
# Usted podría realizar esto con una comprensión de listas. Ejemplo:
# 
# 
# ```python
# nums = [num for num in range(1,11)]
# print(nums)
# ```

# In[41]:


# celda de código para practicar
nums = []

for i in range(1,11):
  nums.append(i)
print(nums)


# In[42]:


nums = [num for num in range(1,11)]
print(nums)


# ### Comprensión de listas con estructuras condicionales.
# 
# Ahora analice los siguientes ejemplos que estan construidos a partir de comprensión de listas. Interprete y documente el código que se muestra para cada ejemplo indicando que hace cada instrucción.
# 
# ```python
# # Pruebe una por una las instrucciones en esta celda.
# nums = list(range(-10,10))
# num_txt = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']
# # Comprensión de listas
# l1 = [n**2 for n in nums]
# print(l1)
# # Comprensión de listas con funciones de python
# vocales = [v.lower() for v in ['A','E','I','O','U']]
# l2 = [abs(n) for n in nums]
# print(l2)
# # Comprensión de listas con if
# l3 = [n**2 for n in nums if n%2==0]
# print(l3)
# # Comprensión de listas con if y else
# texto = 'El almuerzo suelo acompañarlo con 3 manzanas y 10 peras'
# texto2 = [txt if not txt.isnumeric() else num_txt[int(txt)-1] for txt in texto.split(' ')]
# print(texto2)
# string = " "
# texto3 = string.join(texto2)
# print(texto3)
# # Comprensión de listas con multiple if
# modulo = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
# print(modulo)
# ```

# In[43]:


# celda de código para practicar
nums = list(range(-10,10))
num_txt = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']
print(nums)
print("-"*83)
print(num_txt)


# In[44]:


l1 = [n**2 for n in nums]
print(l1)


# In[45]:


l1 = [andres**2 for andres in nums]
print(l1)


# In[46]:


# Comprensión de listas con funciones de Python
vocales = [v.lower() for v in ['A','E','I','O','U']]
vocales


# In[47]:


l2 = [abs(n) for n in nums]
print(l2)


# In[48]:


# Comprensión de listas con if
l3 = [n**2 for n in nums if n%2==0]
print(l3)


# In[49]:


texto = 'El almuerzo suelo acompañarlo con 3 manzanas y 10 peras'
texto.split(' ')


# In[50]:


"almuerzo".isnumeric()


# In[51]:


num_txt


# In[52]:


# Comprensión de listas con if y else
texto = 'El almuerzo suelo acompañarlo con 3 manzanas y 10 peras'
texto2 = [txt if not txt.isnumeric() else num_txt[int(txt)-1] for txt in texto.split(' ')]
print(texto2)


# In[53]:


string = " "
texto3 = string.join(texto2)
print(texto3)


# In[54]:


# Comprensión de listas con multiple if
modulo = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(modulo)


# ### Comprensión de listas anidadas.
# 

# In[55]:


# Vamos a construir una matriz en un lista de listas. (Tomado de la documentación oficial.)
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
         [9, 10, 11, 12],
          ]
matrix


# In[56]:


get_ipython().run_cell_magic('time', '', '## Supongamos de deseamos transponer la matriz, es decir filas en columnas y viceversa\ntranspuesta = []\nfor i in range(4):\n    filas = []\n    for row in matrix:\n        filas.append(row[i])\n    transpuesta.append(filas)\n\nprint(transpuesta)\n')


# La lógica del código anterior es la siguiente:
# 
# Se deben recorrer las 4 columnas de la matriz, luego, en cada recorrido se toma las filas de la matriz y se toma el primer elemento, este, se va consigando en la lista `filas=[]` luego se agrega dicha lista en la lista `transpuesta=[]`. Al cabo de recorrer todos las columnas se obtiene la matriz buscada.
# 
# Al realizar la misma tarea con una list comprehensions, tenemos:

# In[57]:


get_ipython().run_cell_magic('time', '', '[[filas[i] for filas in matrix] for i in range(4)]\n')


# En esta caso la lógica del código es la siguiente:
# 
# Como debemos crear las filas como una lista tenemos el siguiente códido
# 
# ```python
# [filas[i] for filas in matrix]
# ```
# Note que la anterior `comprensión de lista` recorre todos los elementos de la lista `matrix` y se queda con el primer elemento de cada una de las listas internas. Para cada valor fijo de `i` se obtiene una fila de la matriz buscada.
# 
# Como necesitamos obtener la lista final, hacemos el recorrido tantas veces como columnas tiene la matriz y así generamos la matriz busada.
# 
# Puede pensar que el primer `for` que se necesita recorrer, es el último en la `list comprehensions`

# ## __Revisión de información en la WEB__
# 
# * Tuplas.
# * Conjuntos.
# * Diccionarios.
# 
# `Lectura_3` del curso de Introducción a `Pyhton`.
# 
# Finalmente seguir la guía de [Estructuras de datos en Python Docs](https://docs.python.org/3/tutorial/datastructures.html)

# ## __Ejercicio 3__
# 
# Resolver los siguientes problemas sin utilizar las funciones que ya están definidas en estas estructuras. La idea es hacer un recorrido completo por los valores de las estructuras y responder apropiadamente:
# 
# - __Problema 1__ Se plantea la necesidad de buscar un valor en una lista o tupla e indicar la posición en la que se encuentra.
# - __Problema 2__ Ahora se quiere saber cuántas veces aparece un determinado valor en una lista
# - __Problema 3__ Se quiere saber cuál de los valores en una lista, tupla es el que se presenta con mayor frecuencia.

# In[58]:


## Problema 1.
def find_position(lista_or_tuple, value):
  pos = 0
  if value in lista_or_tuple:
    for values in lista_or_tuple:
      pos +=1
      if value == values:
        return pos
  else:
    print("El valor no está en la lista")

find_position((1,2,6,5,8),6)


# In[59]:


## Problema 2.
def count_element(lista, value):
  count = 0
  for values in lista:
    if value == values:
      count+=1
  return count 
count_element([2,5,8,5,9,5,7,5-89,28,8], 8)


# In[60]:


## Problema 3.
def most_frecuency(lista_or_tuple):
  max, L  = 0, []
  for value in lista_or_tuple:
    if value not in L:
      L.append(value)
      temp = count_element(lista_or_tuple,value)
      if temp > max:
        max = temp
        moda = value
  return moda

most_frecuency([8,5,9,5,7,5-89,28,8,5])


# ### Pruebas de tiempo

# In[61]:


import random
import numpy as np

prueba = random.choices(np.linspace(0,9,10), k = 5000000)


# In[62]:


get_ipython().run_cell_magic('time', '', 'most_frecuency(tuple(prueba))\n')


# In[63]:


get_ipython().run_cell_magic('time', '', 'prueba.count(0.0)\n')


# In[64]:


get_ipython().run_cell_magic('time', '', 'count_element(prueba,0.0)\n')


# ---
# # Ejercicio en clase
# ---
# 
# ### Problema de las votaciones
# 
# A continuación tenemos un diccionario con el nombre del candidato y el número que le corresponde. También, se tienen seis mesas de votación en donde se registra el voto por cada candidato usando el respectivo número. Cuando se registra cero, corresponde a votos en blanco. El objetivo es contar la votación de cada candidato para saber como proceder de acuerdo con las siguientes reglas:
# 
# 1. Si el voto en blanco consigue la mayor votación se debe convocar otras elecciones con otros candidatos
# 2. Si un candidato supera más del 50% de la votación, quitando los votos en blanco. Gana las elecciones
# 3. En caso contrario, los dos candidatos con mayor votación pasan a segunda vuelta.
# 
# Hacer un programa que determine cual es el resultado final de las elecciones de acuerdo con las reglas establecidas siguiendo los pasos del pensamiento computacional.
# 
# 

# In[65]:


candidatos = {'José Arcadio': 101, 'Aureliano': 75, 'Úrsula': 143, 'Amaranta': 56, 'Rebeca': 9, 'blanco': 0}
mesa1 = [75,143,75,56,0,9,0,75,9,9,143,75,75,0,101,101,75,56,101,56,0,56,0,101,56,143,101,56,56,101,0,56,0,0,0]
mesa2 = [0,0,0,101,0,101,0,143,0,56,0,143,9,101,56,101,56,75,0,0,101,101,101,0,0,56,75,0,56,0,75,75,0,0,101,143,75,143,56,101]
mesa3 = [56,143,0,0,9,101,9,75,101,9,101,0,143,75,0,0,143,75,143,0,101,56,56,75,56,0,75,9,0,75,75,0,0,0,101,101,0,101,0,75,0,0,0,101,9]
mesa4 = [75,0,0,143,0,101,0,0,75,101,75,0,101,56,0,0,101,9,0,0,56,56,75,0,143,143,101,101,101,75,0,143,101,0,0,75,101,143,101,0,\
         75,101,75,75,0,56,143,101,101,0]
mesa5 = [0,0,0,0,75,101,101,143,9,75,143,0,75,56,75,143,0,56,101,0,101,9,9,75,101,0,101,0,0,101,143,101,101,56,0,0,0,0,75,75,101,\
         101,101,101,101,9,75,143,0,56,143,143,75,56,101]
mesa6 = [101,143,101,101,101,9,101,9,9,75,75,75,75,101,101,75,56,101,143,75,101,9,101,143,101,101,101,101,101,101,101,75,101,75,101,\
         101,75,75,143,75,101,9,56,9,75,101,143,143,143,101,75,101,101,101,143,101,101,101,101,9]


# In[66]:


mesas = [mesa1, mesa2, mesa3, mesa4, mesa5, mesa6]

print("-"*60)
for key, values in candidatos.items():
  for i, j in enumerate(mesas):    
    print(f'El candidato {key} en la mesa {i+1} tuvo {j.count(values)}')
  print("-"*60)


# In[67]:


candidatos.keys()


# In[68]:


for i in candidatos.keys():
  print(i)


# In[69]:


candidatos.values()


# In[70]:


for key, value in candidatos.items():
  print(key,value)


# In[71]:


# celda para resolver los ejercicios

## Función que cuenta los votos por mesa.
def count_votes(*arguments, candidatos):
  '''
  Solución al problema ejercicio en clase. Función que cuenta los votos por mesa.
  Input : *arguments: Listas de la información frente a la votación por mesa. (Cada mesa es una lista.)
          candidatos: diccionario con las etiquetas de los candidatos y el número asignado que enlaza con los valores en las listas.
  Output: Diccionario con el total de votas de cada candidato.
  '''
  dicc = dict() ## Creamos un diccionario vacio.
  for key, value in candidatos.items():
    count = 0
    for mesa in arguments:
      count += count_element(mesa,value)
    dicc[key] = count
  return dicc

prueba1 = count_votes(mesa1,mesa2,mesa3,mesa4,mesa5,mesa6,candidatos=candidatos)
prueba1


# In[72]:


## Función que da los resultados de la elección luego de tener los totales por candidato.
def arg_max_dicc(dicc):
  max , total =  0, 0
  for key, value in dicc.items():
    if value > max:
      max = value
      key_max = key
    total += value
  if key_max == "blanco":
    return print("Se deben repetir las elecciones con diferentes candidatos, pues ganó el voto en BLANCO")
  else:
    if dicc[key_max] > (total-dicc["blanco"])/2:
      return print("El ganador con más del 50% quitando los votos en blanco es:", key_max, "pues obtuvo", dicc[key_max], "de", total-dicc["blanco"])
    else:
      [dicc.pop(key) for key in ["blanco", key_max]]
      max1 = 0
      for key, value in dicc.items():
        if value > max1:
          max1 = value
          key_max1 = key
      dicc_final = dict(zip([key_max,key_max1], [max,max1]))
      return print("Pasan a segunda vuelta:", dicc_final)

arg_max_dicc(prueba1)


# In[73]:


lista1 = "hola"
lista2 = [1,2,3,4]

dict(zip(lista1,lista2))


# In[74]:


def result_votaciones(*arguments, candidates):
  dic = count_votes(*arguments, candidatos = candidates)
  return arg_max_dicc(dic)

result_votaciones(mesa1,mesa2,mesa3,mesa4,mesa5,mesa6,candidates=candidatos)


# In[75]:


prueba2 = {"C1": 40, "blanco":31, "C2": 28,"C3":1 }
arg_max_dicc(prueba2)

