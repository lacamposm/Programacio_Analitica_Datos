#!/usr/bin/env python
# coding: utf-8

#  # Manipulación de cadenas de texto.
# 
# 
# **Tema:**
# 
# * Concatenar y partir.
# * Buscar y reemplazar.
# * Archivos de texto.
# * Verficaciones con cadenas.
# * Otras operaciones con cadenas.

# 
# # ***Cadenas de caracteres.***
# 
# Las cadenas de caracteres (strings) son un tipo de dato especial en los diferentes lenguajes de programación, y en _python_ no es la excepción. Las caracteristicas de una cadena de caracteres son las siguientes:
# - Funcionan como un arreglo, en donde cada caracter es un elemento del arreglo, y la longitud de una cadena es fija. 
# - El primer caracter está en la posición cero
# - Dependiendo de su contenido se pueden convertir a otros tipos de datos, por ejemplo números enteros y reales, fechas, y valores lógicos.
# - Permite representar archivos, enlaces, entidades, personas, categorías, etc
# - Se pueden definir variables de cadena usando comillas dobles o sencillas
# - Las cadenas además de visualizar caracteres alpha-numéricos, signos, operadores, emojis, etc, también pueden representar caracteres especiales que no se muestran, como por ejemplo: fin de línea (\n), tabulador (\t), entre otros
# 
# ## ***Operaciones básicas***
# 
# Las cadenas pueden ser vacias, tener solo un caracter o ser tan largas como se pueda. Para definir cadenas en python es lo mismo usar comillas dobles o sencillas
# 
# 
# ```python
# cad0 = ''                 # cadena vacia
# cad1 = 'Hola, mundo'      # definición con comilla sencilla
# cad2 = "Hello, world"     # definición con comilla doble
# cad3 = '''
# Esto es una cadena de 
# caracteres de multiples
# líneas de texto
# '''                       # definición de una cadena multilineas
# print(cad0)
# print(cad1)
# print(cad2)
# print(cad3)
# ```
# 
# 
# 

# In[1]:


# Pruebe el código en esta celda
cad0 = ''                 # cadena vacia
cad1 = 'Hola, mundo'      # definición con comilla sencilla
cad2 = "Hello, world"     # definición con comilla doble
cad3 = '''
Esto es una cadena de 
caracteres de múltiples
líneas de texto
'''                       # definición de una cadena multilineas
print(cad0)
print(cad1)
print(cad2)
print(cad3)


# 
# ### Cadenas crudas y unicode
# Observe el comportamiento de las siguientes líneas y concluya cual es la diferencia
# 
# ```python
# cad4 = "C:\\User\fulanito\taller.ipynb"
# print(cad4)
# cad5 = r"C:\\User\fulanito\taller.ipynb"
# print(cad5)
# cad6 = "C:\\User\fulanito\taller\nuevo.ipynb"
# print(cad6)
# ```
# 
# 
# 

# In[2]:


# Pruebe el código en esta celda
cad4 = "C:\\User\fulanito\taller.ipynb"
print(cad4)
cad5 = r"C:\\User\fulanito\taller.ipynb"
print(cad5)
cad6 = "C:\\User\fulañito\taller\nuevo.ipynb"
print(cad6)


# ### Cadenas como arreglos
# 
# Efectivamente, las cadenas de texto funcionan de manera similar a los arreglos o listas:
# 
# 
# 
# ```python
# print('Tamaño cadena:    ', len(cad1))     
# print('Primer caracter:  ', cad1[0])
# print('Último caracter: ', cad1[-1])
# print('El resto sería:   ', cad1[1:-1])
# 
# # Extraer cualquier subcadena a otra variable
# tmp = cad[4:10]
# print('Subcadena [4,10]: ', tmp)
# 
# # NO ES POSIBLE cambiar elementos directamente
# cad1[0] = 'h'       # error
# cad1[1:5] = 'news'  # error
# ```
# 
# 

# In[3]:


cad1


# In[4]:


# Pruebe el código en esta celda
print('Tamaño cadena:    ', len(cad1))     
print('Primer caracter:  ', cad1[0])
print('Último caracter: ', cad1[-1])
print('El resto sería:   ', cad1[1:-1])


# In[5]:


# Pruebe el código en esta celda
# NO ES POSIBLE cambiar elementos directamente
#cad1[0] = 'h'       # error


# In[6]:


#cad1[1:5] = 'news'  # error


# ### Recorrido y existencia como arreglo:
# 
# También es posible verficar la existencia de una sub-cadena o caracter dentro de una cadena con el operador __in__
# 
# Prube una a una:
# ```Python
# 'ola' in cad1
# ',' in cad1
# ```
# El recorrido como si fuera un vector de elementos usando __for__
# 
# ```Python
# for c in cad1:
#     print('-->', c)
# ```
# Usando __enumerate__
# 
# ```Python
# # muestra el índice de cada caracter
# for i, c in enumerate(cad1):
#     print(i, '-->', c)
# ```
# 
# 
# 
# 
# 
# 
# 

# In[7]:


cad1


# In[8]:


# Pruebe el código en esta celda
'ola' in cad1


# In[9]:


',' in cad1


# In[10]:


# muestra el índice de cada caracter
for i, c in enumerate(cad1):
    print(i, '-->', c)


# In[11]:


# muestra el índice de cada caracter almacenados en un diccionario.
dicc = {i:c for i,c in enumerate(cad1)}
for i, c in dicc.items():
    print("Indice:",i, '-->', "Caracter:",c)


# ### ***Concatenar***
# 
# * Para concatenar se usa el operador + 
# * Para generar múltiples copias de la cadena se usa el operador *
# 
# 
# ```python
# str1 = "analítica"
# str2 = 'datos'
# str3 = str1 + ' de ' + str2            # operación de concatenar 
# print('Cadena: ', len(str3), str3)     # imprimir tamaño y cadena
# print('Multiplicar: ', str1*5)         # operación de multiplicar
# print('Combinar: ', (str1+' ')*5)      # combinar para mejorar el resultado
# ```
# Para concatenar otros tipos de datos a una cadena se tienen dos formas
# 
# ```python
# entero = 34
# real = 146.38
# s1 = 'el valor: ' + str(entero) + ' es: ' + str(real)
# print(s1)
# s2 = 'el valor: %d es: %f' %(entero, real)
# print(s2)
# 
# ```
# 
# 
# 

# In[12]:


# Pruebe el código en esta celda
str1 = "analítica"
str2 = 'datos'
str3 = str1 + ' de ' + str2            # operación de concatenar 
print('String:', len(str3), str3)     # imprimir tamaño y cadena
print('Multiplicar: ', str1*5)         # operación de multiplicar
print('Combinar: ', (str1+' ')*5)      # combinar para mejorar el resultado


# In[13]:


entero = 34
real = 146.38
s1 = 'el valor: ' + str(entero) + ' es entero y el valor:' + str(real) + ' es real no entero.'
print(s1)
s2 = 'el valor: {:d} es entero y el valor {:.3f} es real no entero'.format(entero, real) 
## {:.3f} número de decimales después de la coma.
print(s2)


# In[14]:


print(type(cad1))


# ### ***Partir y unir una cadena*** 
# 
# Las funciones de __split__ y __join__ parten y unen una cadena respectivamente
# 
# 
# ```python
# str1 = 'porque como poco coco como, poco coco compro'
# lst1 = str1.split()                # partir cadena usando el caracter espacio
# print('lista1:', lst1)
# lst2 = str1.split(',')                # partir cadena usando el caracter espacio
# print('lista2:', lst2)
# str2 = ''.join(lst1)                  # función para unir a partir de un vector
# print(str2)
# 
# ```
# __nota:__
# Vuelva a generar una cadena a partir del vector, pero con espacios
# 
# 

# In[15]:


# Pruebe el código en esta celda
str1 = 'porque como poco coco como, poco coco compro'
lst1 = str1.split()                # partir cadena usando el caracter espacio
print('lista1:', lst1,"--->", type(lst1))


# In[16]:


lst2 = str1.split(',')                # partir cadena usando el caracter espacio
print('lista2:', lst2)


# In[17]:


lst3 = str1.split("o")                # partir cadena usando el caracter "o"
print(f'lista3: {lst3}')


# ### ***Otro ejemplo de unir cadenas***
# 
# Utilizando la función __join()__ y la técnica de listas por comprensión
# 
# ```python
# str3 = ''.join(e+' ' for e in lst1)  # unir la cadena poniendo un espacio
# print(len(str1), str1)             
# print(len(str3), str3)
# print(str1 == str3)                 # comparar las dos cadenas
# ```
# 
# 

# In[18]:


lst1


# In[19]:


# Pruebe el código en esta celda
str3 = ''.join(e+' ' for e in lst1)
str4 = ''.join(e for e in lst1)  # unir la cadena poniendo un espacio
print(len(str1), str1)             
print(len(str3), str3)
print(len(str4), str4)


# In[20]:


print(str1 == str3)


# ***¿por qué no da igual?***

# In[21]:


print([x for x in str1])


# In[22]:


print([x for x in str3])


# ### ***Ejemplo:*** Gráfica de la longitud de las palabras
# 
# Suponga que se quiere procesar una cadena para producir una gráfica de la longitud de las palabras que contiene. El siguiente código resuelve el problema, observe cada línea con cuidado e interprete su funcionamiento.
# 
# ```python
# lpal = [len(s) for s in str1.split(' ')]
# print(str1)
# print('longitud palabras: ', lpal)
# 
# #generar el gráfico usando matplotlib
# import matplotlib.pyplot as plt
# # plot bar recibe valores de x, y
# plt.bar(list(range(len(lpal))), lpal)
# # cambia las etiquetas del eje X
# plt.xticks(list(range(len(lpal))), lst1)
# plt.xlabel('Palabras')
# plt.ylabel('Cantidad de letras')
# plt.title('TAMAÑO DE LAS PALABRAS')
# plt.grid()
# ```
# 
# 
# 
# 

# In[23]:


lpal = [len(s) for s in str1.split(' ')]
print(str1)
print('longitud palabras: ', lpal)


# In[24]:


str1


# In[25]:


str1.split()


# In[26]:


lpal


# In[27]:


# Pruebe el código en esta celda
lpal = [len(s) for s in str1.split()]

for word, leng in zip(str1.split(),lpal):
  print("Longitud palabra:", word,"====>",leng)


# In[28]:


list(range(len(lpal)))


# In[29]:


len(lpal), lpal


# In[30]:


# Pruebe el código en esta celda

import matplotlib.pyplot as plt
# plot bar recibe valores de x, y
plt.bar(list(range(len(lpal))), lpal)
# cambia las etiquetas del eje X
plt.xticks(list(range(len(lpal))), str1.split())
plt.xlabel('Palabras',)
plt.ylabel('Cantidad de letras')
plt.title('TAMAÑO DE LAS PALABRAS')
plt.grid()


# ### ***Ejercicio:***
# 
# Escriba una función que reciba una cadena de texto y que muestre una gráfica con el tamaño de las palabras

# In[31]:


def plot_long_word(string):
    import matplotlib.pyplot as plt
    lpal = [len(s) for s in string.split()]
    plt.bar(list(range(len(lpal))), lpal)
    plt.xticks(list(range(len(lpal))), string.split())
    plt.xlabel('Palabras')
    plt.ylabel('Cantidad de letras')
    plt.title('TAMAÑO DE LAS PALABRAS')
    plt.grid()

plot_long_word("Hola a todos, mi nombre es Andrés Campos")


# ### ***Buscar y reemplazar***
# 
# 
# ```python
# # str1 viene de una celda de código de arriba
# print(str1.find('co'), str1)   # buscar la cadena 'co' en la frase
# 
# # encontrar todas las ocurrencias de 'co' y ponerlas en un arreglo
# x = str1.find('co')
# ind = []
# while x != -1:
#     ind.append(x)
#     x = str1.find('co', x+1)   # se busca a partir del x+1 uno después del anterior
# print(ind)                     # imprime todos los índices donde aparece 'co'
# 
# #verificamos la cuenta de 'co' en la frase
# print('Cuenta "co":', str1.count('co'))
# 
# # ahora la idea es reemplazar 'co' por 'COS'
# str2 = str1.replace('co', 'COS')
# # que pasa si se busca y no hay ocurrencias?
# print(str2.find('de'), str2)
# 
# ```
# 
# 
# 

# In[32]:


# str1 viene de una celda de código de arriba
print(str1.find('co'), str1)   # buscar la cadena 'co' en la frase


# In[33]:


# ¿Qué sucede acá?
print(str1.find('co',8,30), str1)


# In[34]:


# ¿Y acá?
print(str1.find('co',-5), str1)


# In[35]:


# encontrar todas las ocurrencias de 'co' y ponerlas en un arreglo
x = str1.find('co')
ind = []
while x != -1:
    ind.append(x)
    x = str1.find('co', x+1)   # se busca a partir del x+1 uno después del anterior
print(ind)                     # imprime todos los índices donde aparece 'co'


# In[36]:


# Veamos que cumple lo exigido.
for i,idx in enumerate(ind):
  print(f':)...En el índice {idx} encontramos la ocurrencia {i+1} y el inicio del substring: {str1[idx]+str1[idx+1]}\n')


# In[37]:


# verificamos la cuenta de 'co' en la frase
print('Cuenta "co":', str1.count('co'))


# In[38]:


str1


# In[39]:


str1.replace('co', 'COS')


# In[40]:


# ahora la idea es reemplazar 'co' por 'COS'
str2 = str1.replace('co', 'COS',5)
# que pasa si se busca y no hay ocurrencias?
print(str2.find('co'), str2)


# In[41]:


str1.replace("ma","COS")


# #### ***Ejemplo 4. Detectar un subconjunto de caracteres***
# 
# Supongamos que tenemos la siguiente frase 
# 
# 
# ```python
# str1 = 'TOMÁS de niño, pidió públicamente perdón, disculpándose después muchísimo más Íntimamente.'
# ```
# 
# Ahora queremos buscar y reemplazar todos los caracteres especiales propios del español que están en el siguiente _string_
# 
# 
# ```python
# stildes = 'áéíóúñÁÉÍÓÚÑ'
# ```
# Se quiere contar cuántos caracteres de la segunda cadena hay en la primera
# 
# 
# 
# ```python
# str2 = ''.join('&' if c in stildes else c for c in str1)
# print(str2)
# ```
# Ahora piense en otra forma de resolver el ejemplo anterior.
# 
# 
# 
# 

# In[42]:


# Pruebe el código en esta celda
str1 = 'TOMÁS de niño, pidió públicamente perdón, disculpándose después muchísimo más Íntimamente.'
stildes = 'áéíóúñÁÉÍÓÚÑ'


# In[43]:


('&' if c in stildes else c for c in str1)


# In[44]:


str2 = ''.join('&' if c in stildes else c for c in str1)
print(str2)


# ## ***Ejercicio 1***
# 
# Suponga que necesitamos una función, a la cual se le pasa una cadena texto, en donde se requiere que se cambie todos los caracteres especiales que aparecen en una cadena por otros que los van a reemplazar. La función recibe: 
# 1. la cadena de texto a procesar, 
# 2. la cadena de caracteres especiales que queremos reemplazar
# 3. la cadena de caracteres que van a reemplazar a los especiales
# 
# La función retorna la primera cadena donde se cambia los caracteres especiales por los de reemplazo. 
# 
# _Ejemplo:_ si la función se llama reemplazo y se llama así:
# 
# `reemplazo('Sí són éstos es fácil', 'áéíóú', 'aeiou')`
# 
# retorna
# 
# `Si son estos es facil`
# 
# 

# ### ***Solución 1***
# 
# Es importante que intente resolver el ejercicio por su cuenta. Una vez resuelto el ejercicio anterior, compare la solución propia frente a la solución que el docente le propone:
# 
# 
# 
# ```Python
# def replaceSPA(cad, esp, rem):
#     ## código docente
#     return answer
# # ejemplo de uso
# ssym  = 'áéíóúüñÁÉÍÓÚÜÑ'
# srep  = 'aeiouunAEIOUUN'
# str1 = 'Angélica y María estudian Lingüística para NIÑOS'
# 
# print(replaceSPA(str1, ssym, srep))
# output: ---> 'Angelica y Maria estudian Linguistica para NINOS'
# ```
# 
# 

# In[45]:


# Una posible solución:
def replaceSPA(cad, esp, rem):
    s2 = ''.join(rem[esp.find(c)] if c in esp else c for c in cad)
    return s2
# ejemplo de uso
ssym  = 'áéíóúüñÁÉÍÓÚÜÑ'
srep  = 'aeiouunAEIOUUN'
str1 = 'Angélica y María estudian Lingüística para NIÑOS'

print(replaceSPA(str1, ssym, srep))


# ### ***Leer archivos de texto***
# 
# Los archivos de tipo texto se pueden leer en python de varias formas, por ejemplo
# * De un solo golpe, es decir, todo el texto,
# * Línea por línea, o
# * Una cantidad fija de caracteres
# 
# Para esto, lo primero es crear un variable de tipo archivo con la ruta y nombre del archivo de texto. luego se puede leer de las formas descritas arriba.
# 
# Antes de arrancar se debe crear el archivo: __`fragmento.txt`__
# 
# #### ***Ejemplo 1: leer archivo de un solo golpe.***
# 
# ```python
# # abre archivo de texto en modo lectura y lo asigna a la variable 'pfile1'
# pfile1 = open('datas/framento.txt', 'r')
# texto = pfile1.read()                  # lee todo el archivo completo
# print('tamaño total:', len(texto))     # imprime el tamaño del texto leido
# print('Texto del arhivo:\n', texto)    # imprime el contenido del archivo
# pfile1.close()                         # cerrar el archivo
# ```
# Para poder ejecutar este ejemplo debe tener el archivo en fichero `datas` con el nombre fragmento.txt. Aunque también puede cambiar el código para poner otra ruta y otro nombre de archivo que sea válido.
# 

# In[46]:


create_file = open("datas/prueba.txt","x") ## Creamos el archivo prueba.txt


# In[47]:


file_w = open("datas/prueba.txt", "w")         # Archivo en modo esritura.
file_w.write("Título".center(100,"="))         # Escribimos en el archivo
file_w.close()                                 # Cerramos el archivo
##
f = open("datas/prueba.txt", "r")              # Leemos todo el archivo completo
print(f.read())
f.close()


# In[48]:


# Pruebe el código en esta celda
f = open("datas/prueba.txt", "r")
texto = f.read()
print('tamaño total:', len(texto))     # imprime el tamaño del texto leido
print('Texto del arhivo:\n', texto)    # imprime el contenido del archivo
f.close()


# In[49]:


f = open("datas/prueba.txt", "a")
for i in range(10):
  f.write(f'\nLinea {i+2} Python es lo mejor para DS')
f.write("\n"+"".center(100,"="))
f.close()
##
f = open("datas/prueba.txt","r")
print(f.read())
f.close()


# In[50]:


## Leemos la primera linea del archivo
f = open("datas/prueba.txt", "r")
linea_1 = f.readline()
print(linea_1)
f.close()


# In[51]:


## Leemos TODAS las lineas del archivo
f = open("datas/prueba.txt", "r")
print(type(f.readlines()))
f.close()


# In[52]:


## Leemos TODAS las lineas del archivo
f = open("datas/prueba.txt","r")
##
for i,linea in enumerate(f.readlines()):
    print("ELEMENTO",i+1,"---->",linea)
f.close()


# In[53]:


# Pruebe el código en esta celda
# abre archivo de texto en modo lectura y lo asigna a la variable 'pfile1'
f = open('datas/prueba.txt', 'r')
texto = f.read()                  # lee todo el archivo completo
print('tamaño total:', len(texto))     # imprime el tamaño del texto leido
print('Texto del arhivo:\n', texto)    # imprime el contenido del archivo
f.close()                         # cerrar el archivo


# #### ***Ejercicio 2***
# 
# Leer archivo de texto línea por línea
# 
# 
# ```Python
# # abre archivo de texto en modo lectura y lo asigna a la variable 'f2'
# f2 = open('datas/fragmento.txt', 'r')
# for linea in f2:         # iterar por cada una de las líneas del archivo
#     print('--', linea)             # hacer algo con la línea... imprimirla
# f2.close()               # cerrar el archivo
# ```
# Para poder ejecutar este ejemplo debe tener un archivo en la ruta actual del notebook con el nombre archivoTexto.txt. Aunque también puede cambiar el código para poner otra ruta y otro nombre de archivo que sea válido.
# 

# In[54]:


# Pruebe el código en esta celda
f2 = open('datas/fragmento.txt', 'r')
for linea in f2:         # iterar por cada una de las líneas del archivo
    print('--', linea)             # hacer algo con la línea... imprimirla
f2.close()               # cerrar el archivo


# #### ***Ejemplo 3***
# Leer archivo de texto un tamaño fijo cada vez
# 
# 
# ```python
# # abre archivo de texto en modo lectura y lo asigna a la variable 'pfile3'
# pfile3 = open('archivoTexto.txt', 'r')
# dato = pfile3.read(20)          # lee 20 caracteres (incluidos caracteres especiales)
# print(dato)
# 
# ```
# Cómo se sabe cuál es el tamaño de un archivo {__seek, tell__}
# 
# ```python
# pfile3.seek(0,2)                # moverse a el final del archivo
# size = pfile3.tell()            # leer la posición actual del archivo, es decir el tamaño
# print('El tamaño del archivo es:', size)
# ```
# ¿Cómo leer los últimos n caracteres de un archivo?
# 
# ```python
# pfile3.seek(size-20,0)          # moverse a el final del archivo
# dato = pfile3.read(20)          # leer los últimos 20 caracteres del archivo
# print(size, dato)
# pfile3.close()                  # cerrar el archivo
# ```
# > Para poder ejecutar este ejemplo debe tener un archivo en la ruta actual del notebook con el nombre archivoTexto.txt. Aunque también puede cambiar el código para poner otra ruta y otro nombre de archivo que sea válido.
# 

# In[55]:


# Pruebe el código en esta celda
# abre archivo de texto en modo lectura y lo asigna a la variable 'pfile3'
f3 = open('datas/fragmento.txt', 'r')
dato = f3.read(20)          # lee 20 caracteres (incluidos caracteres especiales)
print(dato)


# In[56]:


# Pruebe el código en esta celda
f3.seek(0,2)                # moverse a el final del archivo
size = f3.tell()            # leer la posición actual del archivo, es decir el tamaño
print('El tamaño del archivo es:', size)


# In[57]:


# Pruebe el código en esta celda
f3.seek(size-5,0)         # moverse a el final del archivo
dato = f3.read(20)          # leer los últimos 20 caracteres del archivo
print(size, dato)
f3.close()                  # cerrar el archivo


# ## ***Introducción a Minería de texto en `Python`***
# 
# Los siguientes ejemplos se utilizan en el contexto de procesamiento de cadenas de texto. Como siempre, la idea es probar las líneas de código una por una, hacerle modificaciones y seguir probando, y seguir aprendiendo.
# 
# ```Python
# texto1 = 'El Infierno está lleno de buenas intenciones y el Cielo de buenas obras'
# # filtrar las palabras con más de 3 letras
# lst1 = texto1.split()
# w = []
# for word in lst1:
#     if len(word) > 3:
#         w.append(word)
# print(w)
# ```
# Uso de la técnica de comprensión y las funciones ***istitle() y endswith()*** 
# ```Python
# # 1. filtrar las palabras con más de 3 letras
# w = [word for word in texto1.split() if len(word) > 5]
# print(w)
# 
# # 2. filtrar las palabras que inician en mayúscula
# w1 = [word for word in texto1.split() if word.istitle()]
# print(w1)
# 
# # 3. filtrar las palabras que terminan en 's'
# w2 = [word for word in texto1.split() if word.endswith('s')]
# print(w2)
# ```
# 
# 

# In[58]:


# Pruebe el código en esta celda
texto1 = 'El Infierno está lleno de buenas intenciones y el Cielo de buenas obras'
# filtrar las palabras con más de 3 letras
lst1 = texto1.split()
w = []
for word in lst1:
    if len(word) > 3:
        w.append(word)
print(w)


# In[59]:


# 1. filtrar las palabras con más de 3 letras
w = [word for word in texto1.split() if len(word) > 3]
print(w)


# In[60]:


[word if len(word)>2 else word+" Gol..." for word in texto1.split()]


# In[61]:


# 2. filtrar las palabras que inician en mayúscula
w1 = [word for word in texto1.split() if word.istitle()]
print(w1)


# In[62]:


"carlo".endswith("s")


# In[63]:


texto1


# In[64]:


# 3. filtrar las palabras que terminan en 's'
w2 = [word for word in texto1.split() if word.endswith('s')]
print(w2)


# ### Encontrar palabras únicas usando set()
# 
# ```python
# text3 = 'To be or not to be'
# text4 = text3.split(' ')
# print(text4)
# print(len(text4))
# 
# w3 = set(text4)
# print(w3)
# print(len(w3))
# 
# w4 = set([word.lower() for word in text4])
# print(w4)
# 
# ```
# 

# In[65]:


# Pruebe el código en esta celda
text3 = 'To be or not to be'
text4 = text3.split(' ')
print(text4)
print(len(text4))


# In[66]:


w3 = set(text4)
print(w3)
print(len(w3))


# In[67]:


w4 = set([word.lower() for word in text4])
print(w4)


# ### ***Resumen de Funciones para preguntar sobre el contenido del texto.***
# 
# ***Más detalles [aqui](https://www.w3schools.com/python/python_ref_string.asp)***
# 
# ```python
# a = '1 o 5 the note of this course'
# # Verificar si la cadena inicia con un patrón
# a.startswith('1')
# # Verificar si la cadena termina con un patrón
# a.endswith('5')
# # Verificar si la cadena tiene un 'valor'
# 'o' in a
# # Verificar si la cadena esta en mayúscula
# a.isupper()
# # Verificar si la cadena está en minúscula
# a.islower()
# # Verificar si la cadena esta en forma de Título
# a.istitle()
# # Verificar si la cadena está compuesta por solo caracteres
# a.isalpha()
# # Verificar si la cadena es de caracteres numéricos
# a.isdigit()
# # Verificar si la cadena se compone solo de caracteres alfa-numéricos
# a.isalnum()
# ```

# In[68]:


# Pruebe el código en esta celda
a = '1 o 5 the note of this course'
# Verificar si la cadena inicia con un patrón
a.startswith('1')


# In[69]:


# Verificar si la cadena termina con un patrón
a.endswith('5')


# In[70]:


# Verificar si la cadena tiene un 'valor'
'o' in a


# In[71]:


# Verificar si la cadena esta en mayúscula
a.isupper()


# In[72]:


# Verificar si la cadena está en minúscula
a.islower()


# In[73]:


# Verificar si la cadena esta en forma de Título
a.istitle()


# In[74]:


# Verificar si la cadena está compuesta por solo caracteres
a.isalpha()


# In[75]:


# Verificar si la cadena es de caracteres numéricos
a.isdigit()


# In[76]:


# Verificar si la cadena se compone solo de caracteres alfa-numéricos
a.isalnum()


# ## __Ejercicio 2__
# 
# Hay ciertas operaciones de verificación y de análisis del que se suelen usar. Resolver para los siguientes requerimientos:
# - Verificar si una cadena que representa el nombre de un archivo finaliza con la extensión "pdf". Ej: `nom = 'C:\\trabajo1.pdf'`
# - Verificar si una cadena que representa el correo de alguien está en minúscula. Ej: `correo = 'jvictorinog@ucentral.edu.co'`
# - Verficar si una cadena que representa un número solo tiene caracteres numéricos y por tanto se puede convertir a numérico sin problema. Ej: `x = "18416"`, `y = "-707"`, `z = "-3.1416"`
# - Verficar si una cadena que representa una frase está límpia de caracteres especiales, es decir que solo tiene caracteres alfanuméricos. Ej: `desc = "El dólar se cotizó 4185, el máximo histórico`
# 
# 
# 
# 

# ### ***Solución 2.***
# 
# Resuelva el ejercicio anterior. Una vez resuelto, compare su solución frente a la propuesta. 
# 
# 

# In[77]:


# Pruebe el código en esta celda
nom = 'C:\\trabajo1.pdf'
ext = nom[-3:]
print(ext)
print(nom.endswith('pdf'))


# In[78]:


correo = 'jvictorinog@ucentral.edu.co'
ind = correo.find('@')
print('@' in correo)
q = correo.count('@')
print(ind, q, correo[ind])


# ### ***Resumen de métodos que operan con cadenas.***
# 
# ```python
# b = '11111Sitting in on lectures: In general we are happy for guests to sit-in on lectures if they are a member of the Stanford community (registered student, staff, and/or faculty). \n If the class is too full and we are running out of space, we ask that you please allow registered students to attend. Due to high enrollment, we cannot grade the work of any students who are not officially enrolled in the class.111'
# 
# # convertir a mayúsculas
# b.upper()
# # convertir a minúsculas
# b.lower()
# # partir el texto por el caracter espacio ' '
# b.split(' ')
# # davuelve una lista con todas las líneas de una cadena. 
# b.splitlines()
# # reune los caracteres de un arreglo de cadenas de texto
# s = "-";
# seq = ("a", "b", "c"); 
# print(s.join(seq))
# # devuelve una copia de la cadena en la cual se han eliminado todos los caracteres del final de la cadena (si omite el parámetro se eliminarán los espacios en blanco). 
# x = b.rstrip('1')
# print(x)
# # Devuelve una copia de la cadena en la cual todos los caracteres del inicio y del final han sido eliminados de la misma (si omite el parámetro se eliminarán los espacios en blanco)
# y = b.strip('1')
# print(y)
# 
# ```
# 

# In[79]:


# Pruebe el código en esta celda
b = '''11111Sitting in on lectures: In general we are happy for guests to sit-in on 
lectures if they are a member of the Stanford community 
(registered student, staff, and/or faculty). \n If the class is too full and we 
are running out of space, we ask that you please allow registered students to attend. 
Due to high enrollment, we cannot grade the work of any students who are not officially 
enrolled in the class.111'''


# In[80]:


# convertir a mayúsculas
b.upper()


# In[81]:


# convertir a minúsculas
b.lower()


# In[82]:


b.split()


# In[83]:


# davuelve una lista con todas las líneas de una cadena. 
b.splitlines()


# ### ***Convertir texto a lista de caracteres.***
# 
# ```python
# 
# text5 = 'If the class is too full and we are running out of space'
# list(text5)
# 
# ```
# 

# In[84]:


# Pruebe el código en esta celda
text5 = 'If the class is too full and we are running out of space'
list(text5)


# # ***TALLER PRÁCTICO.***
# 
# El __objetivo__ de esta práctica es desarrollar los ejercicios con los conocimiento que se han visto en el curso hasta el momento. La idea no es usar todavía librerías para minería de texto.El trabajo esta diseñado para hacerlo en grupo, en donde la idea es compartir los conocimientos para que todos los integranetes del puedad comprender una solución final a una problemática.
# 
# Para esta práctica se entregan dos archivos de texto:
# * __fragmento.txt__ corresponde a un archivo que tiene un fragmento del libro de 100 años de soledad
# * __stopWordsSPA.txt__ Corresponde a un listado de las palabras, las cuales carecen de significado por si solas. En general la lista la componen los: artículos, preposiciones, conjunciones, pronombres, etc.
# 
# Por favor usar diferentes bloques de código para resolver cada uno de los ejercicios. La idea es volver a usar los bloques en código en los diferentes ejercicios.
# 

# ### 1. Contar
# La idea de este ejercicio es leer dos archivos de texto que se entregaron _fragmentos.txt_ y _stopWordsSPA.txt_ y contar: carácteres, palabras y frases que tienen. Una vez lo resuelva escríbalo en forma de función (def)
# 
# 
# ```python
# pf = open('fragmento.txt', 'r')
# texto = pf.read()
# fpal = texto.split()
# ffra = texto.split('.')
# print(len(texto), len(fpal), len(ffra))
# 
# ```
# 
# 
# 

# In[85]:


# resuelva aquí el punto 1:
pf = open('datas/fragmento.txt', 'r')
texto = pf.read()
fpal = texto.split()
ffra = texto.split('.')
print(len(texto), len(fpal), len(ffra))


# ### 2. Buscar
# La idea en este ejercicio es buscar la palabra 'todo' en el archivo _fragmento.txt_. Generar una lista con las posiciones en el texto en donde aparece la palabra dada. Contar cuantas veces aparece la palabra sola (completa) y cuántas veces aparece acompañada (como parte de otra palabra). Al final generar una función (def) que recibe como parámetro el archivo y la palabra, y la función retorna la lista de posiciones y la cantidad de veces que aparece sola y la cantidad de veces que aparece dentro de otra palabra.
# 
# _Resultados:_
# - Lista de posiciones: [1014, 1479, 6443, 8049, 12777, 13634, 14647, 15322, 15841, 17473, 18314, 30741, 39600, 44841, 47842, 48200, 49714, 51218]
# - Palabra todo completa: 10 veces
# - Palabra todo dentro de otras palabras: 9 veces
# 

# In[86]:


# resuelva aquí el punto 2:


# ### 3. Buscar en conjunto
# Buscar todas las 'stop words' en el archivo _fragmento.txt_ y **contarlas**. Las stop words son las palabras que aparecen en el archivo llamado _stopWordsSPA.txt_. Escribirlo en forma de función (def) que recibe como parámetros los dos archivos y devuelve el conteo.

# In[87]:


# resuelva aquí el punto 3:


# ### 4. Formato tipo título
# Leer los primeros 1762 caracteres del archivo _fragmento.txt_ y convertir todas las palabras del archivo a mayúsculas la primera letra de cada palabra y el minúscula el resto, excepto las palabras que aparecen en el archivo _stopWordsSPA.txt_. 
# 
# 

# In[88]:


# resuelva aquí el punto 4:


# ### 5. Ranking de palabras
# Con el archivo _fragmento.txt_ genere un conteo de la frecuencia de cada una de las palabras, excepto las que aparecen en _stopWordsSPA.txt_. Luego determine el Top 20 de las palabras más usadas en el documento. Finalmente, con las 20 palabras que más aparecen haga una gráfica de pulsos o de barras.
# 

# In[89]:


# resuelva aquí el punto 5:

