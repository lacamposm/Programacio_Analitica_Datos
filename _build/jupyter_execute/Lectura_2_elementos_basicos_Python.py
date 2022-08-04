#!/usr/bin/env python
# coding: utf-8

# # Introducción a Python - elementos básicos del lenguaje

# ## Metodología
# 
# Para iniciar en programación se deben aprender algunos conceptos básicos como son los pilares del pensamiento computacional, y para codificar conceptos como: variables, expresiones, condicionales, ciclos, entre otros. Sin embargo, la habilidad de programar para resolver problemas se adquiere mediante la práctica constante. 
# - La experiencia en la solución de diferentes problemas es un factor fundamental que ayuda a la solución de otros problemas que son parecidos o un poco más complejos. Es decir, que aprender a programar es incremental y se puede realizar mediante el entendimiento de ejemplos. 
# - Tenga en cuenta que entre más ejemplos logre apropiar mayores habilidades y técnicas adquiere. Por consiguiente, aprender a programar deber ser una responsabilidad individual y una actividad consciente, puesto que es la persona misma, quien puede experimentar sus conocimientos, habilidades y limitaciones cuando se enfrenta a distintos problemas. 
# 
# La metodología propuesta en este curso tiene como objetivo que el estudiante practique con ejemplos guíados que ayuden de manera incremental a mejorar sus habilidades en la solución de problemas mediante algoritmos. Para esto se proponen las siguientes actividades en las clases tipo taller:
# * Realizar con tiempo la lectura del material propuesto para la clase.
# * En el desarrollo del taller se deben seguir los ejemplos planteados, hacer que funcionen, autoevaluar su entendimiento, preguntar en que otros escenarios se puede usar.
# * Cuando se propongan actividades, es el momento de verificar si se entendió, primero intente resolverlo solo, recurra al material dado, si no es suficiente busque ayuda en la red o con otros compañeros
# * Tómese el tiempo para desarrollar el taller, vaya de acuerdo con el ritmo más apropiado. Siga los diferentes ejemplos, entienda su funcionamiento y modifiquelos conscientemente. La idea, es que las modificaciones que realiza sirvan para autoevaluar su entendimiento.
# * Cuando tenga dificultades, primero siempre trate de solucionarlas usted mismo, para esto, repase material conocido (por tanto es importante mantener el material organizado incluso el que consigue por sus propios medios). Si no logró resolver sus dificultades busque ayuda en compañeros, monitor y/o profesor. Se recomienda que no aplace la solución a sus inquietudes.

# ## **Elementos básicos de Python.**
# 
# 
# Este tutorial esta escrito en un **Notebook** de *Python*. El notebook es proporcionado por Anaconda usando un módulo llamado *Jupyter* o por *Google Drive* mediante una aplicación llamada **Colaboratory**. El  **Notebook** tiene tres componentes CODE, TEXT y OUTPUT. 
# * CODE: espacio para escribir un programa usando el lenguaje de python
# * TEXT: espacio para escribir texto con formato, es posible agregar fórmulas, imágenes, tablas, entre otros muchos elementos. Ideal para documentar los trabajos y reportar resultados.
# * OUTPUT: este espacio se genera debajo de un componente de código, cuando este último se ejecuta. Muestra los resultados del programa o los errores en dado caso. Los resultados de la ejecución pueden ser numéricos, texto, gráficas, imágenes, etc.
# 
# Para información de referencia en elementos básicos del lenguaje visite: [Covantec cap3](https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion3/) o más información de otros elementos: [Aquí](https://entrenamiento-python-basico.readthedocs.io/es/latest/)
# 
# ### **1. Instrucciones**
# 
# Para observar instrucciones aritméticas, se usa Python como calculadora.
# 
# Para escribir las instrucciones en Python, genere un espacio de código y escriba la operación. Tenga en cuenta que los operadores requieren un orden y en general deben tener dos valores a cada lado. Por ejemplo:
# 
# Operación | Siginificado | Resultado
# :---: | :---: | :---:
# 5032 + 7624 + 365  | sumar valores | 13021
# 18213 - 9567.5  | restar valores | 8645.5
# 13.3 * 8.52  | multiplicación |  113.316
# 35698.7 / 798.23 | división |  44.72232314
# 23 / 8 | División | 2.875
# 23 // 8 | División entera | 2
# 23 % 8 | Módulo de la división | 7
# 13\*\*2 | Potenciación | 169
# 
# En un bloque de código pruebe una a una las operaciones de la tabla y verifique el resultado
# 

# In[1]:


# Pruebe una por una las operaciones de la tabla en esta celda
5032 + 7624 + 365


# In[2]:


# Resta
18213 - 9567.5


# In[3]:


# Multiplicación
13.3 * 8.52


# In[4]:


35698.7/798.23


# In[5]:


23 / 8


# In[6]:


#  División entera : Se obtiene solamente el cociente de la división
23 // 8


# In[7]:


# Resto de la división
23 % 8


# #### Comentarios
# Note que los comentarios en las celdas de código de python inician con el caracter llamado almohadilla '#'. 
# 
# 
# 
# ```python
# # Esto tiene formato de código
# # y estas líneas son comentarios
# """ cuando se quieren comentarios de
#     varias líneas en un bloque de código
#     se pueden usar comillas dobles
# """
# x = int(5)  # para tomar un valor entero
# 
# ```

# In[8]:


# bloque de código para probar
# Esto tiene formato de código
# y estas líneas son comentarios
""" cuando se quieren comentarios de
    varias líneas en un bloque de código
    se pueden usar comillas dobles
"""
x = int(5)  # para tomar un valor entero


# ### **2. Variables.**
# 
# 
# Además de las operaciones básicas, lo interesante de la calculadora es cuando se maneja memoria. Para guardar los resultados de las operaciones en memoria se utilizan las **variables**. Estas **variables** también son útiles para guardar todos los valores que se necesiten. Ejemplos son:
# * x = 3
# * x1 = -2
# * x2 = 6.28
# * y = 4\*x\*\*2
# * u = 45
# 
#  En el espacio de código cada vez que escriba cada una de estas líneas  ejecute la celda y observe el resultado.
# 
#  Ahora, con los valores de las variables anteriores se prueba la siguiente ecuación:
# 
# $$Z = 4x^3y - 2x^2y^2 + 10xy^3 + 5x$$
# 
# 
# Es más eficiente utilizar variables que escribir los valores de $x$ y $y$ cada vez que se requiere un valor de la función $Z = f(x,y)$. Determine el valor de $Z$ cuando $x=3.5$ y $y=0.7$, pruebe en un bloque de código:
# 
# * x = 3.5
# * y = 0.7
# * Z = 4 \* x\*\*3 \* y - 2 \* x\*\*2 \* y\*\*2 + 10\*x \* y\*\*3 + 5\*x
# 
# El resultado debe ser: 137.55

# In[9]:


# Pruebe la declaración de variables en esta celda
x = 3.5
y = 0.7
Z = 4 * x**3 * y - 2 * x**2 * y**2 + 10*x * y**3 + 5*x
Z


# ## Imprimir en Python
# 
# Es posible que haya notado que el notebook automaticamente imprime la última operación o la variable que se escriba en la línea final. Pero si se quiere imprimir varias veces en un segmento de código se puede usar la función __print__ o la función __display__. 
# 
# Observe las diferentes formas de imrpimir con la función __print__:
# 
# 
# ```python
# print() # imprime línea en blanco
# x =  -256/117
# print(x) # imprime valor de x, además del cambio de línea
# print('Tipo:', type(x), 'Valor:', x, 'Sin signo:', abs(x)) # imprime 6 veces en la misma línea 
# 
# a = 1
# b = 22
# c = 333
# d = 4444
# print(a,'\n',b,'\n',c,'\n',d) # imprimir valores en cada linea
# 
# #agregar un poco de formato para alinear los valores en la presentación
# print('Tabla de valores\n a = %5d\n b = %5d\n c = %5d\n d = %5d'%(a,b,c,d))
# ```
# 
# Se recomienda revisar algo más de documentación para el manejo de la función print en el siguiente enlace: [Print Function](https://realpython.com/python-print/)

# In[10]:


# bloque de código para probar
print() # imprime línea en blanco

x =  -256/117
print(x) # imprime valor de x, además del cambio de línea

print("Tipo:", type(x), 'Valor:', x, 'Sin signo:', abs(x)) # imprime 6 veces en la misma línea 

a = 1
b = 22
c = 333
d = 4444
print(a,'\n',b,'\n',c,'\n',d) # imprimir valores en cada linea

# agregar un poco de formato para alinear los valores en la presentación
print('Tabla de valores\n a = %5d\n b = %5d\n c = %5d\n d = %5d'%(a,b,c,d))

# Otro formato.
print(f'Tabla de valores\n a = {a}\n b = {b}\n c = {c}\n d = {d}')


# ### Precedencia de operadores
# 
# No todos los operadores tienen la misma jerarquía. La multiplicación, división, módulo y división entera tienen el mismo nivel de precedencia, al igual que la suma y la resta. Pero estos últimos tienen menor precedencia sobre los primeros. Es decir, por ejemplo, que primero es la multiplicación sobre la suma:
# 
# ```Python
# # No es lo mismo
# a = 2
# b = 3
# c = 5
# (a * b) + c
# a * (b + c)
# # Sin usar parentesis que sucede?
# ```
# La recomendación es usar parentesis si no se está seguro. Para profundizar en este tema puede consultar [Precedencia en python](https://www.interactivechaos.com/manual/tutorial-de-python/precedencia-de-operadores)

# In[11]:


# celda de código para probar
# No es lo mismo
a = 2
b = 3
c = 5
print((a * b) + c)
print(a * (b + c))
# Sin usar parentesis que sucede?


# ### Probar el nivel de precedencia de la potencia
# 
# ```Python
# x = 3
# y = 2
# z = 5
# (x**y)*z 
# x**(y*z)
# (z/x)**y
# z/(x**y)
# ```
# ¿Cuál es el nivel de precedencia del operador potencia? es igual?

# In[12]:


# celda de código para probar
x = 3
y = 2
z = 5
print((x**y)*z, x**(y*z), (z/x)**y, z/(x**y))


# ## **3. Tipos de datos.**
# 
# Los tipos de datos básicos que se pueden identificar en un programa son:
# * Numéricos: (valores enteros o que pertenecen a los números reales).
# * Lógicos (Son aquellos que pueden tomar por valor solamente __verdadero__ o __falso__).
# * Caracter (Caracter o cadena de caracteres).
# 
# 
#  A diferencia de otros lenguajes de programación como C o Java que son fuertemente tipados, Python es un lenguaje de programación de **tipado dinámico**. Esto quiere decir que si una variable ha sido declarada en este lenguaje, en cualquier momento usted podrá cambiarle el tipo sin ninguna restricción.
# 
#  Lo anterior quiere decir que Python no le exige que defina el tipo de dato de la variable. La asignación del tipo es de forma automática. Sin embargo, usted puede validar el tipo de dato asignado.
# 
# Para profundizar sobre los tipos de datos que maneja Python u obtener documentación se recomienda el siguiente enlace: [Python Data Types](https://docs.python.org/3/library/datatypes.html)
# 
# 
# ```python
# num_entero = 1
# print(type(num_entero))
# # Tipo de dato real
# num_real = 1.0
# print(type(num_real))
# # verdadero
# v = True
# print(v)
# # Falso
# f = False
# print(f)
# ```

# In[13]:


# Pruebe los tipos de dato en esta celda
num_entero = 1
print(type(num_entero))
# Tipo de dato real
num_real = 1.0
print(type(num_real))
# verdadero
v = True
print(v)
# Falso
f = False
print(f)


# ### Capturar valores de entrada:
# 
# Resulta muy útil interactuar con el usuario del programa para que este sea más flexible. Una forma es pedirle que ingrese valores por la consola de texto usando la función __input__:
# 
# 
# ```Python
# # leer de la consola y guardar en la variable valor
# valor = input('Ingrese un valor entero positivo:')
# # imprimir el tipo que recibe y el valor
# print('tipo: ', type(valor), 'contenido:', valor)
# ```
# 
# El siguiente bloque de código produce un error, por que es necesario convertir el valor de entrada para que se pueda usar en operaciones aritméticas. Por ejemplo:
# 
# 
# ```python
# # solicite al usuario ingresar un valor real por la consola de texto
# valor2 = input('Ingrese un valor real positivo (por ejemplo 0.25):')
# # observe el tipo de dato 
# print('tipo: ', type(valor2), 'contenido:', valor2)
# # intente operar con el valor obtenido
# area = valor2 * valor2
# print('area = ', area)
# ```

# In[14]:


# leer de la consola y guardar en la variable valor
valor = input('Ingrese un valor entero positivo:')
# imprimir el tipo que recibe y el valor
print('tipo: ', type(valor), 'contenido:', valor)


# Ahora intente ejecutar el siguiente bloque y compare con el anterior, qué fue lo que sucedió?
# 
# ```python
# # ahora convierta el valor a float
# fvalor = float(valor2)
# # intente operar con el valor convertido
# area = fvalor*fvalor
# print('area = ', area)
# 
# ```

# In[15]:


# celda de código para probar
# solicite al usuario ingresar un valor real por la consola de texto
valor2 = input('Ingrese un valor real positivo (por ejemplo 0.25):')
# observe el tipo de dato 
print('tipo: ', type(valor2), 'contenido:', valor2)
# intente operar con el valor obtenido
area = valor2 * valor2
print('area = ', area)


# ### manejo de strings
# 
# 
# ```Python
# # Caracter
# c = 'a'
# print(type(c))
# 
# # Cadena de caracteres. Puede definirse con comilla ' ' o " "
# cna_caracteres = 'Fundamentos de programación para analítica de datos'
# print(cna_caracteres)
# 
# # Cadena de caracteres con cambios de línea
# cna_caracteres = '''Fundamentos de programación.
# Maestría en analítica de datos'''
# 
# print(cna_caracteres)
# print(type(cna_caracteres))
# ```

# In[16]:


# Pruebe los tipos de dato en esta celda
# Caracter
c = 'a'
print(type(c))


# In[17]:


# Cadena de caracteres. Puede definirse con comilla ' ' o " "
cna_caracteres = 'Fundamentos de programación para analítica de datos'
print(cna_caracteres)


# In[18]:


# Cadena de caracteres con cambios de línea
cna_caracteres = '''Fundamentos de programación.
Maestría en analítica de datos'''
print(cna_caracteres)
print(type(cna_caracteres))


# ### Otras opciones con strings
# 
# 
# ```Python
# # longitud de cadena de caracteres contando espacios
# long_cnd = len(cna_caracteres)
# print(long_cnd)
# 
# # Contatenar texto
# cnt_texto = 'Esta es una forma ' + 'de ' + 'hacer ' + 'texto concatenado en Python '
# print(cnt_texto)
# 
# cnt_texto += 'y también en otros lenguajes'
# print(cnt_texto)
# 
# x = 'manzanas'
# y = 'limones'
# # %s Define el tipo de dato cadena o caracter y %i entero 
# z = 'A mi me gusta comer %s y %s, por lo menos %i de cada una'%(x,y,3)
# print(z)
# ```
# 
# ¿Cómo concatenar valores que no son cadenas?

# In[19]:


# Pruebe los tipos de dato en esta celda
# longitud de cadena de caracteres contando espacios
long_cnd = len(cna_caracteres)
print(long_cnd)


# In[20]:


# Contatenar texto
cnt_texto = 'Esta es una forma ' + 'de ' + 'hacer ' + 'texto concatenado en Python '
print(cnt_texto)


# In[21]:


x = 'manzanas'
y = 'limones'
# %s Define el tipo de dato cadena o caracter y %i entero 
z = 'A mi me gusta comer %s y %s, por lo menos %i de cada una'%(x,y,3)
print(z)


# En caso de de ser necesario usted puede convertir un tipo de dato a otro. No es necesario que declare una variable nueva para esto, también puede reasignar el tipo:
# 
# ```python
# # Conversión de entero a float
# num = 5
# print('num tipo: ', type(num))
# print('valor de num: ', num)
# 
# num = float(num)
# print('num tipo: ', type(num))
# print('valor de num: ', num)
# 
# # Conversión de caracter a entero
# ctr = '10'
# print('ctr tipo: ', type(ctr))
# print('valor de ctr: ', ctr)
# 
# ctr = int(ctr)
# print('ctr tipo: ', type(ctr))
# print('valor de ctr: ', ctr)
# ```
# Si quiere profundizar alrededor de las opciones con cadena de caracteres, acceda al siguiente link: [Strings and Character Data in Python](https://realpython.com/python-strings/)

# In[22]:


# Pruebe la conversión de tipos de datos en esta celda
# Conversión de entero a float
num = 5
print('num tipo: ', type(num))
print('valor de num: ', num)


# In[23]:


num = float(num)
print('num tipo: ', type(num))
print('valor de num: ', num)


# In[24]:


# Conversión de caracter a entero
ctr = '10'
print('ctr tipo: ', type(ctr))
print('valor de ctr: ', ctr)


# In[25]:


ctr = int(ctr)
print('ctr tipo: ', type(ctr))
print('valor de ctr: ', ctr)


# En Python como en otros lengujes se pueden hacer evaluaciones lógicas entre variables. Se debe recordar el funcionamiento de las tablas de verdad. A continuación se mencionan como ejemplo las tablas de verdad con los diferentes operadores lógicos de conjunción, disyunción y negación.
# 
# a | no a ¬(a)
# :---: | :---:
#  verdadero (V) | Falso (F)
#  falso (F) | verdadero (V)
# 
# a | b | a y b | a o b | 
# :---: | :---: | :---: | :---:
#  verdadero (V) | verdadero (V)  | verdadero (V) |  verdadero (V)
#  verdadero (V) | falso (F) | falso (F) | verdadero (V)
#  falso (F) | verdadero (V) | falso (F) | verdadero (V)
#  falso (F) | falso (F) | falso (F) | falso (F)
# 
# 
# 
# Los operadores lógicos o booleanos básicos son **not** (no),  **and** (y) **or** (o). 
# 
# 
# Operador lógico | Expresión lógica | Significado
# :---: | :---: | :---:
# not (not), !  | no p (not p) | negación de p
# y (and), & | p y q (p and q) | conjunción de p y q
# o (o), $|$  | p o q (p o q) | disyunción de p y q
# 
#  Al final de cada linea imprima si es una conjunción o disyunción.
# 
# 
# ```Python
# # Evaluar falso y verdadero
# print(f and v)
# # Evaluar falso o verdaero
# print(f or v)
# # Evaluar verdadero y verdadero
# print(v and v)
# # Evualuar verdadero y no falso
# print(v and not f)
# ```
# 
# Tenga en cuenta que los operadores también tienen precedencia. De nuevo la recomendación es usar paréntesis.

# In[26]:


# Evaluar falso y verdadero
print(f and v)
# Evaluar falso o verdaero
print(f or v)
# Evaluar verdadero y verdadero
print(v and v)
# Negaciíon de la negación
print(not f)
# Evualuar verdadero y no falso
print(v and not f)


# A continuación se mencionan otro tipo de expresiones lógicas o booleanas en donde su valor final solo puede tomar **verdadero** (True) o **falso** (False).  Las expresiones lógicas se forman a partir de una posible combinatoria de constantes lógicas, variables lógicas y otras expresiones lógicas tales como **not, and y or** y los *operadores relacionales* (de relación o comparación) $=, <, >, <=, >=, !=$ tomando la forma: *expresion_1* **operador de relación** *expresión_2*.
# 
# 
# ```python
# # Comparaciones entre números enteros
# print(3 < 6)
# print(0 > 1)
# print(4 == 2)
# print(8 <= 5)
# print(5 != 5)
# ```
# 
# Valide las demás opciones que existen sobre los operadores lógicos en Python en el siguiente link: [Python - Basic Operators](https://www.tutorialspoint.com/python/python_basic_operators.htm)

# In[27]:


# Pruebe las expresiones entre números enteros en esta celda
print(3 < 6)
print(0 > 1)
print(4 == 2)
print(8 <= 5)
print(5 != 5)


# ## **4. Entrada, proceso y salida.**
# 
# 
# Recordando la estructura de un algoritmo, este se encuentra divido de forma general en tres partes: Entrada, Proceso y Salida. Como ejemplo, en un algoritmo que soluciona una receta de cocina se infiere que esta tendrá:
# 
# *Entrada:* Ingredientes y utensilios.
# 
# *Proceso:* Elaboración de la receta en la cocina.
# 
# *Salida:*  Terminación del plato (por ejemplo, cordero).
# 
# 
# Las **entradas** de cualquier algortimo estan sujetas al contexto del problema planteado. Estas le proporcionan al algoritmo los elementos necesarios para realizar su validación una vez este se ha construido.
# 
# Las **salidas** corresponden al resultado posterior a la ejecución del algoritmo. Las salidas deben corroborarse contra el contexto del problema para ver si estas cumplen como solución total (algoritmo general) o de forma parcial (algoritmo de algun subproblema) a la solución del problema.
# 
# Las **entradas** y **salidas** en Python de forma básica pueden ser representadas en variables. También pueden ser en archivos.
# 
# **Ejemplo**:  Calcular un vector  unitario $\vec{u}$ que tenga el mismo sentido que $ \vec{v} = <-10, 20$. La fórmula de un vector unitario esta dada por: $$ u =\frac{1}{||v||}v  $$
# 
# ```python
# # Variables para las entradas
# v_x = -10
# v_y = 20
# # Variables para las salidas
# u_x = 0
# u_y = 0
# # Proceso
# mod_v = (v_x**2 + v_y**2)**(1/2)
# u_x = v_x / mod_v
# u_y = v_y / mod_v
# # Salidas
# print('u = <',u_x,', ',u_y,'' )
# 
# # Entradas desde un archivo
# archivo = open("hello.txt", 'w')
# archivo.name
# 
# # Entradas por teclado
# teclado = input('Ingrese un valor por teclado: ')
# print(teclado)
# 
# # Convertir la entrada por teclado en el momento de lectura
# teclado = int(input('Ingrese un numérico por teclado: '))
# print(type(teclado), teclado)
# ```

# In[28]:


# Pruebe el algoritmo en esta celda
# Entradas desde un archivo
archivo = open("hello.txt", 'w')
archivo.name


# ## **5. Estructuras condicionales.**
# 
# Estas estructuras de permite modificar el orden en el cual se ejecutan las instrucciones de un algoritmo. 
# 
# Las **estructuras condicionales** como su nombre lo indica, evaluan una condición. Dentro de esa estructura condicional se pueden escribir un conjunto de instrucciones. Las instrucciones que se encuentren en su interior se ejecutarán si y solo si la condición evaluada resulta verdadera.
# 
# El primer tipo de estructura condicional que puede utilizar se muestra a continuación. 
# 
# ```python
# edad_maria = 56
# edad_alberto = 47
# 
# # Si María es mayor en edad que Alberto entonces:
# if (edad_maria > edad_alberto):
#   print('María tiene más años que Alberto.')
# # De lo contrario:
# else:
#   print('Alberto tiene mas años que María.')
# ```

# In[34]:


# Pruebe las estructuras condicionales en esta celda
edad_maria = 56
edad_alberto = 47

# Si María es mayor en edad que Alberto entonces:
if (edad_maria < edad_alberto):
  print('María tiene más años que Alberto.')
# De lo contrario:
else:
  print('Alberto tiene mas años que María.')


# También se le podría incluir otra condición a evaluar (puede ser de conjunción, disyunción y/o negación).
# 
# ```python
# edad_maria = 56
# edad_alberto = 47
# altura_maria = 1.56
# altura_alberto = 1.70
# 
# # Si María es mayor en edad que Alberto entonces:
# if (edad_maria > edad_alberto):
#   print('María tiene más años que Alberto')
#   
#   if (altura_maria > altura_alberto):
#     print('Adicionalmente, es más alta que Alberto.')
#   
#   else:
#     print('Sin embargo Alberto es más alto.')
#   
# # De lo contrario:
# else:
#   print('Alberto tiene mas años que María.')
#   
#   if (altura_maria < altura_alberto):
#     print('Adicionalmente, es más alto que María.')
#   
#   else:
#     print('Sin embargo María es más alta.')
#  
# ```

# In[35]:


# Pruebe las estructura condicionales anidadas en esta celda

edad_maria = 56
edad_alberto = 47
altura_maria = 1.56
altura_alberto = 1.70

# Si María es mayor en edad que Alberto entonces:
if (edad_maria < edad_alberto):
  print('María tiene más años que Alberto')

  if (altura_maria > altura_alberto):
    print('Adicionalmente, es más alta que Alberto.')

  else:
    print('Sin embargo Alberto es más alto.')

# De lo contrario:
else:
  print('Alberto tiene mas años que María.')

  if (altura_maria < altura_alberto):
    print('Adicionalmente, es más alto que María.')

  else:
    print('Sin embargo María es más alta.')


# In[29]:


#### Ingreso de información del usuario.
edad_maria = int(input("Ingrese la edad de María en años: "))
edad_alberto = int(input("Ingrese la edad de Alberto en años: "))
altura_maria = int(input("Ingrese la altura de María en centímetros: "))
altura_alberto = int(input("Ingrese la altura de Alberto en centímetros: "))
####
if (altura_maria == altura_alberto):
  print("-----------------------------------------------------------------------------------------")
  print(f'María y alberto tiene una estatura de {altura_alberto}, la cual es la misma misma altura')
  print("-----------------------------------------------------------------------------------------")
else:
  print("-----------------------------------------------------------------------------------------")
  print(f'María mide {altura_maria} y Alberto mide {altura_alberto}, asi, tiene distinta estatura')
  print("-----------------------------------------------------------------------------------------")


# #### Ejercicio:
# 
# Utilizando el ejemplo para captura de datos por teclado, solicite el ingreso de la altura y la edad para María y Alberto e incluya las condiciones necesarias que le permitan determinar si los dos tienen la misma altura.

# In[30]:


### Una posible solución (Puede ser mejorada)
print(f'{100*"-"}\n{30*"-"} Bienvenido al programa {30*"-"}\n{100*"-"}')
print("Se le va solicitar los datos de altura y edad.")
print(f'{100*"-"}')
#####
persona = input("Ingrese 1 si usted es María o 2 si es Alberto: ")
if (type(int(persona)) == int) and (int(persona) == 0 or int(persona) == 1):
  if int(persona)== 1:
    print("Bienvenida María")
    altura_maria = int(input("María ingresa tu altura en cm: "))
    edad_maria = int(input("María ingresa tu edad en años: "))
    print("Bienvenido Alberto")
    altura_alberto = int(input("Alberto ingresa tu altura en centímetros: "))
    edad_alberto = int(input("Alberto ingresa tu edad en años: "))
  else: 
    print("Bienvenido Alberto")
    altura_alberto = int(input("Alberto ingresa tu altura en centímetros: "))
    edad_alberto = int(input("Alberto ingresa tu edad en años: "))
    print("Bienvenida María")
    altura_maria = int(input("María ingresa tu altura en cm: "))
    edad_maria = int(input("María ingresa tu edad en años: "))
else:
  print("Debe ingresar 1 si usted es María o 2 si usted es Alberto")
#######
if altura_maria == altura_alberto:
  print("****************************************************************************")
  print(f'La altura de María y Alberto es la misma. Ambos miden: {altura_alberto} cm.')
  print("****************************************************************************")
else:
  print("****************************************************************************")
  print("María y ALberto tienen alturas distintas")
  print("****************************************************************************")


# #### Tarea: revisar este tutorial
# 
# Puede ampliar sus conocimientos alrededor de las estructuras condicionales en el siguiente link: [Conditional Statements in Python](https://realpython.com/python-conditional-statements/)

# ## **6. Estructuras cíclicas**
# 
# La estructura ciclica (también llamadas estructura con bucle o repeticiones)  permiten que se ejecute repetidamente un conjunto de instrucciones, bien sea bajo un número pre-determinado de veces o hasta que se verifique y se cumpla una determinada condición.
# 
# Para esto existen dos tipos de estructuras: con **for** (número predeterminado) y **while** (con verificación y se cumplimiento de una condición).
# 
# El **ciclo for** tiene la siguiente estructura:
# 
# ```Python
# for <variable> in range(<inicio>, <fin>, <incremento>):
#        <instrucciones...>    
# ```
# 
# En donde ***variable*** corresponde al contador del ciclo, el cual inicia en el valor dado en ***inicio*** y termina con el valor dado en ***fin***. Adicionalmente se puede indicar de forma **opcional**  el valor incremental de la variable cada vez que se ejecute el ciclo (por defecto es 1).  En total el ciclo se ejecuta ***fin-inicio*** veces. Las ***instrucciones*** que a partir de una sangría a la derecha dentro de la instrucción **for**, son las que se repiten. Una vez se han ejecutado todas las instrucciones del ciclo, la variable (contador) se incrementará de acuerdo al valor definido o por defecto en uno (si no especifica incremento).
# 
# 
# Revise el siguiente ejemplo:
#  
# Problema: generar la tabla de multiplicar de un número entre dos y diez
# 
# * **Entrada**: Número de dos a 10.
# * **Salida**: La tabla del número.
# 
#  **Proceso**: imprimir la tabla de un número dado.
# 
#   1.  leer numero de entrada.
#   2.  Configurar un ciclo de 1 a 10.
#   3.  Imprimir cada línea de la tabla .
# 
# ```Python
# x = int(input('Ingrese un valor en el intervalo [2,10]: '))
# for y in range(1,11):  
#   print(x, 'x', y, '=', x*y)  
# ```
# Puede complementar sus conocimientos de estructuras cíclicas con for en el siguiente link: [lPython "for" Loops (Definite Iteration)](https://realpython.com/python-for-loop/)

# In[31]:


##
for i in range(1,10,1):
  print(i)


# In[32]:


# Pruebe la estructura cíclica con for en esta celda
x = int(input('Ingrese un valor en el intervalo [2,10]: '))
for y in range(1,11):  
  print(x, 'x', y, '=', x*y)


# Ahora use un doble ciclo para imprimir las tablas desde el 5 hasta el 12.
# 
# ```python
# for x in range(5,13,1):
#     for y in range(1, 11):
#         print(x, 'x', y, '=', x*y)
#     print('-------------')
# ```

# In[33]:


# Pruebe la estructura cíclica con for anidado en esta celda
for x in range(5,13,1):
    for y in range(1,11):
        print(x, 'x', y, '=', x*y)
    print('-------------')


# El **ciclo while** tiene la siguiente estructura:
# 
# ```python
# while <expresión lógica>: 
#        <instrucciones...>
# ```
# En donde ***expresión lógica*** corresponde a la condición del ciclo, si esta se cumple el ciclo se repite y en caso contrario, el ciclo se termina. 
# 
# 
# En la programación de ciclos es importante identificar y diseñar de manera adecuada las siguientes partes:
# 
# 
# 1.   **Inicialización**: corresponde a una variable, la cual hace parte de la condición del ciclo. Esta variable toma un valor antes de iniciar el ciclo.
# 2.   **Condición**: Es la responsable de llevar el control del ciclo. Por medio de esta se determina cuando se repite y cuando termina el ciclo. Esta condición se evalua cada vez que se hace una repetición e involucra a la variable del ciclo.
# 3. **Incremento**: En general, corresponde a un cambio en el valor de la variable del ciclo. La clave es que la variable dentro del ciclo, en el momento apropiado, se modifique a algún valor que produzca un cambio en la condición. De tal manera que esta condición no se cumpla y termine el ciclo.
# 
# Como ejemplo, se requiere un fragmento de código que permita el validar la nota que corresponde a la calificación de un estudiante de la Universidad Central. La nota es válida si y solo si se encuentra entre un rango de 0 a 5.
# 
# 
# ```python
# nota = float(input('Ingrese una calificación: '))            # 1. inicialización
# 
# while nota < 0 or nota > 5:                                  # 2. condición
#   nota = float(input('Error: ingrese un valor de 0 a 5: '))  # 3. incremento o cambio de valor 
# print('La nota es:', nota)                                   # salida
# 
# ```
# Puede ampliar sus conocimientos en estructuras cíclicas con while en el siguiente link: [Python "while" Loops (Indefinite Iteration)](https://realpython.com/python-while-loop/)

# In[34]:


# Pruebe la estructura cíclica con while en esta celda
nota = float(input('Ingrese una calificación: '))            # 1. inicialización

while nota < 0 or nota > 5:                                  # 2. condición
  nota = float(input('Error: ingrese un valor de 0 a 5: '))  # 3. incremento o cambio de valor 
print('La nota es:', nota)


# In[35]:


for i in range(1,6):
  print(i)


# In[36]:


####
count = 0
for num in range(1,6):
  nota = float(input(f"Ingrese la nota {num}:"))
  count = count + nota
####
prom = count/num
if (prom<3):
  print(f'La nota obtenida es: {round(prom,2)}. Luego PERDIÓ el curso')
else:
  print(f'La nota obtenida es: {round(prom,2)}. Luego APROBÓ el curso')


# Ahora construya un programa en el cual se pueda tomar las 5 notas de un estudiante, calcular el promedio y saber si el estudiante aprobó la asignatura. Para aprobar la asignatura, el resultado del promedio de las 5 notas ingresadas debe ser mayor o igual a  3.0.

# In[37]:


# Construya el programa que da solución al enunciado anterior en esta celda
print("------------------------------------------------------------------")
print("Este programa determina si usted aprobó o no la asignatura")
print("------------------------------------------------------------------")
i = 1 # Inicializamos un contador.
notafin = 0 # Inicializamos un acumulador.
while i<=5:
  nota = float(input(f'Ingrese la {i} calificación: '))
  i+=1 ## i = i +1
  notafin+=nota
if (notafin/5) >= 3.0:
  print("--------------------------------------------------------------")
  print(f'Su nota final fué de {round((notafin/5),2)} y por lo tanto aprobó el curso... :)')
  print("--------------------------------------------------------------")
else:
  print("------------------------------------------------------------------")
  print(f'Su nota final fué de {round((notafin/5),2)} y por lo tanto NO aprobó el curso... :(')
  print("------------------------------------------------------------------")


# In[38]:


### Se considera que el usuario ingresa un número entero. #####
print(f"********************************************************************************************************************")
print(f"********************************************************************************************************************")
print(f'Este programa determina si la fecha ingresada está entre el 01 de enero del 2000 y hasta el 31 de diciembre del 2020')
print(f"********************************************************************************************************************")
print(f"********************************************************************************************************************")
####
print("Debe ingresar tres números: El primero corresponde al dia, el segundo al número del mes y el tercero al año")
print(f"********************************************************************************************************************")
####
day = int(input("Ingrese el número de día: "))
moth = int(input("Ingrese el número del mes: "))
year = int(input("Ingrese el número del año: "))
####
print(f"********************************************************************************************************************")
print(f'La fecha ingresa es: día --> {day}, mes --> {moth}, año --> {year}')
####
while (year<2000) or (year>2020):
  year = int(input("Error: Ingrese un año válido: "))


# ## Ejercicio:
# 
# En un determinado programa se ingresan 3 valores que corresponden a día, mes y año. Dados estos 3 valores el programa debe verificar si la fecha que conforman estos tres números es válida o no. Para ser válida se debe verificar que la fecha esté entre 1 de enero de 2000 y el 31 de diciembre de 2020. Al final convierta el programa en una función llamada: validar_fecha(dia, mes, año).
# 
# Para este ejercicio tenga en cuenta que los meses tienen diferente cantidad de días y que en el año biciesto febrero tiene 29 días. 

# In[39]:


for num in range(2000,2021,1):
  print(f' La división modulo 4 de {num} es {num%4}\n')


# In[40]:


### Se considera que el usuario ingresa un número entero. #####
print(f"********************************************************************************************************************")
print(f"********************************************************************************************************************")
print(f'Este programa determina si la fecha ingresada está entre el 01 de enero del 2000 y hasta el 31 de diciembre del 2020')
print(f"********************************************************************************************************************")
print(f"********************************************************************************************************************")
####
print("Debe ingresar tres números: El primero corresponde al dia, el segundo al número del mes y el tercero al año")
print(f"********************************************************************************************************************")
####
day = int(input("Ingrese el número de día: "))
moth = int(input("Ingrese el número del mes: "))
year = int(input("Ingrese el número del año: "))
####
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


# In[41]:


for i in range(2000,2021,1):
  print(f'{i%4}')


# ## Problemas a resolver:
# 
# Los siguientes ejercicios tienen como objetivo prácticar la elaboración de algoritmos para resolver los problemas propuestos. Intente realizarlos sin buscar la solución en internet. El segundo punto esta diseñado para resolverlo de manera incremental.
# 
# 1. Haga un programa que recibe 3 valores numéricos válidos y se encarga de mostrar los tres valores ordenados de menor a mayor.
# 2. Dada la longitud de 3 lados (l1, l2, l3) de un triángulo determine su tipo, es decir si este es equilatero, isósceles o escaleno. 
#    * Ahora resuelva el problema anterior, pero suponga que no tenemos los 3 lados sino los vértices en 2D: (x1, y1, x2, y2, x3, y3)
#    * Ahora resuelva el tipo de triángulo pero suponga que tenemos los vértices en 3D (x1, y1, z1; x2, y2, z2; x3, y3, z3) 
#    * Suponga que ahora se quiere saber si el triángulo formado por los tres vértices en 3D es un triángulo rectángulo
# 

# In[42]:


# pruebe los programas en esta celda

