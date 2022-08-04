#!/usr/bin/env python
# coding: utf-8

# #  Introducción Libreria `Pandas`
# 
# **Tema:**
# 
# * **Series de Pandas**: Definición y algunos métodos
# * **DataFrames de Pandas**: Definición y construcción.

# # Librería `pandas`
# 
# 
# Será nuestra librería base para trabajar con los `dataframe`, es decir, una estructura de datos bidimensional, donde las columnas serán las variables o características y las filas serán los registro. Es una librería que trabaja a la par con muchas de las librerías de **Python**. Puede consultar más información en la página oficial de [`pandas.`](https://pandas.pydata.org/docs/index.html)

# In[1]:


## Librerías requeridas
import numpy as np
import pandas as pd


# ## Series
# 
# Vamos a explorar la estructura de serie en `pandas`. Debemos al final estar
# familiarizados en cómo almacenar y manipular datos indexados unidimensionales.
# 
# La serie es una de las estructuras de datos esenciales en `pandas`. Todos los elementos se almacenan en la serie y hay etiquetas con las que se puede recuperarlos. Una forma sencilla de pensar una serie en `pandas` son las columnas de datos. El primero es el índice especial, muy parecido a las llaves o keys de un diccionario. Mientras que el segundo son los datos reales. Es importante tener en cuenta que la columna de datos tiene una etiqueta propia y se puede recuperar.

# In[2]:


estudiantes = ["Maria", "Juan", "Alejandra"]
pd.Series(estudiantes)


# El resultado es una serie de `pandas`, los índices son dados automaticamente siguiendo en orden de los números naturales. Además `pandas` identificó el tipo de datos de esta serie como "object" y estandariza el tipo de dato buscando el que mejor corresponda.

# In[3]:


estudiantes = {"Maria":"Química",
               "Juan": "Sociales",
               "Alejandra": "Matemáticas"}


# In[4]:


## En el caso de tener un diccionario las claves o keys serán los índices y los valores la asignación a dicho índice
pd.Series(estudiantes)


# In[5]:


serie = pd.Series(estudiantes)


# In[6]:


serie[0], serie[1], serie[2]


# In[7]:


## Con este método podemos obtener los índices de la Serie de Pandas.
serie.index


# In[8]:


for i in serie.index:
  print(f'El índice {i} tiene el valor {serie[i]}')


# In[9]:


# El índice se genera automaticamente desde 0 hasta el número de entradas en la lista.
numeros = [1,2,3]
pd.Series(numeros)


# In[10]:


# En las series de pandas puede usted mismo asignar los valores a los índices.
pd.Series(numeros, index=["Uno","Dos","Tres"])


# In[11]:


serie_1 = pd.Series(["Química", "Matemáticas", "Química","Sociales"], index= ["Maria", "Juan", "Carlos","Alison"])
serie_1


# In[12]:


serie_2 = pd.Series(["Química", "Matemáticas", "Química", None], index= ["Maria", "Juan", "Carlos","Alison"])
serie_2


# In[13]:


serie_2.isna()


# In[14]:


serie_3 = pd.Series([1,2,3,None], index= ["Maria", "Juan", "Carlos","Alison"])
serie_3


# In[15]:


serie_3.isna()


# In[16]:


notas_clase = {99: 'Matemáticas',
              100: 'Química',
              101: 'Inglés',
              102: 'Sociales'}
serie_4 = pd.Series(notas_clase)
#serie_4[0] # Se generará un error, pues no tenemos el índice 0.


# In[17]:


serie_4[99]


# _Nota:_
# 
# Para el caso en que los índices NO sean los dados por default (es decir iniciando desde el 0 y hasta n-1, donde n en el número de ingresos de la Serie), se puede hacer el llamado por la etiqueta del índice o por la ubicación numérica.
# 

# In[18]:


serie_1


# In[19]:


[serie_1[i] for i in serie_1.index]


# In[20]:


[serie_1[i] for i in range(len(serie_1))]


# In[21]:


serie_1["Maria"], serie_1[0]


# In[22]:


## Recordemos la serie_1
serie_1


# In[23]:


## el método pd.Series.unique(), permite obtener los valores únicos en la serie.
serie_1.unique()


# In[24]:


serie_2


# In[25]:


## Podemos anexar a una Serie otra Serie
serie_1.append(serie_2)


# In[26]:


## Podemos hacer el llamado de los elementos en la Serie, se retornarán los elementos que coinciden con ese índice
serie_1.append(serie_2)['Carlos']


# In[27]:


## Observe que el método .unique(), proporciona la información sobre si tenemos presencia de valores faltantes.
pegado = serie_1.append(serie_2)
pegado.unique()


# In[28]:


## Reemplazar un valor en un índice.
pegado["Maria"] = "Artes"
pegado


# In[29]:


## Eliminar un índice
pegado.drop("Carlos")


# In[30]:


## Eliminar una lista de índices
pegado.drop(["Carlos","Juan"])


# In[31]:


## Note que la Serie original con los métodos anteriores no se ve afectada.
pegado


# In[32]:


## Ingresar un nuevo registro.
pegado["Persona_sin_nombre"] = "Culinaría"
pegado


# In[33]:


## Observe que en esta caso tenemos un error, esto debido a que no podemos ingresar un nuevo registro de manera numérica.
# pegado[10] = "Culinaría" ## Error en esta linea
pegado


# In[34]:


## Eliminar los registros faltantes.
pegado.dropna()


# In[35]:


## Eliminar los registros duplicados (por default se queda con el primer registro encontrado.)
pegado.drop_duplicates()


# In[36]:


## Serie booleana
pegado.isna()


# 
# ## Dataframes.
# 
# DataFrame es el corazón de la biblioteca de `pandas`. La estructura de datos DataFrame es el objeto principal en el que se trabaja en el análisis de datos y tareas de limpieza.
# 
# El DataFrame es conceptualmente un objeto de serie bidimensional, donde hay un índice y múltiples columnas, cada columna con una etiqueta. De hecho, la distinción entre una columna y una fila es realmente sólo una
# distinción conceptual. Un  DataFrame es una matriz etiquetada de dos ejes.
# 
# Ahora, seguir la guía de [towards data science: dataframes](https://towardsdatascience.com/pandas-dataframe-a-lightweight-intro-680e3a212b96)

# In[37]:


registro1 = pd.Series({"Nombre": 'Alicia',
                     "Asignatura": 'Física',
                     "Puntuación": 85})
registro2 = pd.Series({'Nombre': 'Andrés',
                       'Asignatura': 'Química',
                       'Puntuación': 82})
registro3 = pd.Series({'Nombre': 'Helen',
                       "Asignatura": 'Biología',
                       "Puntuación": 90})


# In[38]:


## Al igual que una Serie, en caso de no espeficar el index, este será la enumeración que se da en las Series.
df = pd.DataFrame([registro1,registro2,registro3])
df


# In[39]:


df = pd.DataFrame([registro1,registro2,registro3], 
             index=["estudiante1","estudiante2","estudiante3"])
df


# In[40]:


## Note el tipo que de objeto que tenemos en una Serie
type(registro1)


# In[41]:


type(df)


# In[42]:


# Podemos formar un dataframe apartir de una lista con diccionarios, cada uno será un registro del dataframe.
estudiantes = [{'Nombre': 'Alicia',"Asignatura": 'Física', 'Puntuación': 85},
               {'Nombre': 'Andrés',"Asignatura": 'Química', 'Puntuación': 82},
               {'Nombre': 'Helen',"Asignatura": 'Biología', 'Puntuación': 90}]
pd.DataFrame(estudiantes, index=["estudiante1","estudiante2","estudiante3"])


# In[43]:


# Podemos formar un dataframe apartir de una diccionario con keys los nombres de las columnas y una lista con los registros.
datos = {"Estudiantes": ["Luis","Andres","Sandra","Patricia", "Elizabeth"],
         "Notas": [2.5,3,4,4.9,4.3],
         "Resultado": ["no_aprobo", "aprobo", "aprobo", "aprobo", "aprobo"]}
pd.DataFrame(datos)


# In[44]:


## Podemos ingresar una columna en el pandas DataFrame.
df['Nueva'] = 50
df


# In[45]:


## Es posible anexar un registro nuevo a un Pandas DataFrame, esto no modifica el data frame original.
df.append({"Nombre":"Luisa","Asignatura":"Artes","Puntuación":"100","Nueva":"45"},ignore_index=True)


# In[46]:


## Podemos anexar un dataFrame a otro donde se encuentren las mismas columnas
df.append(df)


# In[47]:


## Podemos recuperar el tamaño del DataFrame, al ser una lista podemos solicitar el número de registros (indice 0)
## así como el número de columnas (índice 1)
df.shape, df.shape[0], df.shape[1]


# ## Conclusiones:
# 
# 
# Revisamos como importar la librería `pandas`. Se conocieron los objetos de datos: `Series` y `dataframes`. Para cada uno de ellos se mostró la forma de construirlos y algunas consultas básica.

# ## Para tener en cuenta:
# 
# 
# Las Series de `pandas` tienen muchos más métodos de los presentados acá, vale la pena que explore muchos de ellos. Puede ver una información detallada [acá.](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
