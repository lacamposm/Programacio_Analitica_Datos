#!/usr/bin/env python
# coding: utf-8

# # Tratamiento de datos.
# 
# **Tema:**
# 
# * Cruce de información - merge
# * Agrupamiento de categorías - groupby
# * Tablas pivote: cruzar categorías de filas y columnas.

# ## _Cruce de información._
# 
# El cruce de información es una operación esencial en el análisis de los datos. Usualmente, la posibilidad de realizar el cruce de dos o más fuentes de información es el primer paso para responder preguntas complejas acerca de los datos. Existen muchas formas de cruzar o combinar tablas de datos. El cruce de estos datos siempre tiene un propósito. Por tanto, se debe realizar un análisis de lo que se requiere antes de iniciar. Para esto, lo primero es conocer bien las fuentes de información que se van a relacionar.

# 
# ### *Uniones (Joins)*
# 
# Usando la librería pandas se pueden realizar 4 tipos de uniones para cruzar información entre dos fuentes de datos, ver Figura abajo. 
# * INNER JOIN: este tipo de cruce incluye solo los registros que coincieden en las dos tablas.
# * LEFT JOIN:  en este tipo de cruce se incluyen todos los registros de la primera tabla aunque no aparezcan coincidencias en la segunda. Cuando no hay coincidencias en la segunda tabla los campos correspondientes a esta aparecerán como nulos.
# * RIGHT JOIN: en este tipo de cruce se incluyen todos los registros de la segunda tabla aunque no aparezcan coincidencias en la primera. Cuando no hay coincidencias en la primer tabla los campos correspondientes a esta aparecerán como nulos.
# * OUTER JOIN O FULL JOIN: combina todos los registros de ambas tablas aunque no existan coincidencias en la otra tabla. 
# 
# ![Los tipos de uniones que se pueden ejecutar en pandas](https://letsdobigdata.files.wordpress.com/2016/03/joins.png) 
# 
# **Imagen tomada de wordpress.com**

# La combinación a usar depende del análisis que se requiera con los datos. Lo más común es realizar un cruce de tipo Inner Join, debido a que muestra los registros cuando aparecen relacionados en ambas tablas. Sin embargo, en 
# ocasiones se quiere saber que pasa con todos los registros de la primera tabla aunque no se tengan coincidencias. Alternativamente, quizá, lo menos usual es hacer combinaciones de tipo RIGHT o OUTER. Generalmente, estas son usadas cuando se quiere saber por qué no se tienen coincidencias, o cuáles registros no cumplen con la relación especificada.

# ### _Ejemplo: Infomación archivo de Excel `examen2.xlsx`_
# 
# 
# Para entender como funciona se necesita una tabla de inofrmación. Para esto, se va utilizar el archivo `examen2.xlsx`. Este archivo consta de seis tablas repartidas en diferentes hojas del libro de excel. El archivo contiene el registro anonimizado del examen de algoritmos y programación aplicado a todos los programas de Ingeniería en 2017-2. La información recolectada registró los resultados del examen de los estudiantes de la asignatura "algoritmos y programación" en el mencionado periodo académico. A este registro lo acompañan una tabla de los profesores y otra tabla de los grupos de cursos que se formaron. Además, se tiene un informe de calificaciones de los estudiantes antes de presentar dicho examen, referente a notas y fallas del primer y segundo corte. Finalmente, se cuenta con un registro de la citación al examen de cada estudiante. Para mayor claridad, a continuación se describe en detalle los sheets:

# ### Información del archivo `examen2.xlsx`
# 
# 
# ESTUDIANTE
# - **IDE:** identificador de estudiante (valor entero consecutivo)
# - **programa:** programa al que pertenece (texto {Ingeniería de sistemas, Ingeniería ambiental, Ingeniería mecánica, Ingeniería electrónica, Ingeniería industrial})
# - 
# PROFESOR
# - **IDP:** identificador de profesor (valor entero consecutivo)
# - **profesor:** nombre del profesor (texto)
# - **dedicación:** dedidcación de profesor en la U {TC, TM y Cátedra}
# - 
# GRUPO
# - **IDG:** número del grupo (texto, consecutivo del grupo)
# - **curso:** nombre del curso (texto)
# - **creditos:** número de créditos del curso (número entero positivo)
# - **nestd:** número de estudiantes inscritos en cada grupo (entero positivo)
# - **periodo:** periodo académico del año en que se dictó el curso {1,2, 3}
# - **año:**  año en que se dictó el curso (entero positivo)
# 
# LISTADO
# - **corte1:** nota en el primer corte (valor real [0.0, 5.0])
# - **corte2:** nota en el segundo corte (valor real [0.0, 5.0])
# - **prom:** promedio primeros dos cortes (valor real [0.0, 5.0])
# - **fallas:** cantidad de horas de falla (valor entero mayor o igual a cero)
# - **fallaP:** porcentaje de horas de falla (real [0.0, 100.0])
# 
# EXAMEN
# - **inicio:** hora inicio de examen (hora formato: '%H%M')
# - **final:** hora finalización de examen (hora formato: '%H%M')
# - **nota:** nota total (valor real [0.0, 5.0])
# - **p1, p2,...,p10:** resultado por pregunta, 10 preguntas (valor real [0.0, 5.0])
#  
# CITA
# - **nsala:** número de la sala en donde presenta el examen (valor entero consecutivo)
# - **sala:**  nombre de la sala en donde presenta el examen (texto)
# - **horaExamen:** hora programada para presentar examen (hora formato: '%H%M %pm')
# - **jornada:** jornada en la que presenta el examen (texto {día, noche})

# 
# ### _Actividad 1: Cargar información del examen_
# 
# 
# 1. Para esto se debe incluir la librería `pandas` y se recomienda importar la librería `numpy`
# 2. Definir una ruta y nombre del recurso (url del archivo).
# 3. Crear un DataFrame con cualquier tabla de las que estas disponibles en el recurso.
# 
# 
# ```Python
# # Importar las librerías básicas 
# import pandas as pd
# import numpy as np
# ```

# In[1]:


# celda de código para probar
import pandas as pd
import numpy as np


# #### _Ejercicio 1._
# 
# Cargue todas las hojas del libro en diferentes dataframes y explore la información. Compare las columnas de los dataframes con el diccionario de datos presentado arriba

# In[2]:


ls -l


# In[3]:


# celda de código para probar 
urlfile = 'datas/examen2.xlsx'
sheets = pd.read_excel(urlfile, sheet_name= None)
print(sheets.keys())


# In[4]:


get_ipython().run_line_magic('who', '')


# In[5]:


sheets = {"df_"+ key:value for key, value in sheets.items()}
locals().update(sheets)
##
for i in sheets.keys():
    print(i)


# In[6]:


def info_df(*dataframes):
    i = 0
    for df in dataframes:
      print("*"*80)
      print(f'Tamaño dataframe {list(sheets.keys())[i]}: {df.shape}')
      print("*"*80)
      print(df.info())
      print("*"*80)
      print("Cabeza del dataframe:")
      print(df.head())
      print("*"*80)
      i +=1
    return None


# In[7]:


info_df(*sheets.values())


# In[8]:


df_cita.head(2)


# In[9]:


df_estudiante.head(2)


# In[10]:


df_estudiante['IDE'].value_counts()


# In[11]:


df_examen.head(2)


# In[12]:


df_profesor.head()


# In[13]:


df_grupo.head(2)


# In[14]:


df_listado.head(2)


# ### Actividad 2. Preguntas que se pueden responder con estos datos
# 
# 
# Una vez se tiene un completo entendimiento de la información, y se conoce el procedimiento para cargar la información, se procede a abordar ciertas preguntas de intereś que surgen de los datos y se procede a analizar la posible solución. Seguramente, la solución a las siguientes preguntas requiere un cruce de información, un filtrado de los datos, un agrupamiento y quizá un ordenamiento de los datos resultantes.
# 
# 1. Cuáles son los profesores asignados a cada grupo, ordenado por profesor?
# 2. Cuáles son los estudiantes que tiene cada profesor por grupo y por programa académico?
# 2. Cuáles son los promedios de calificación en el primer y segundo corte que tienen cada uno de los profesores en los grupos de Ingeniería de Sistemas?
# 3. Qué estudiantes de cada programa han dejado de presentar el examen?
# 4. Cuáles de los estudiantes, que presentaron el examen, no aparecen en el listado?
# 
# 

# #### **Solución pregunta 1**
# 
# _Cuáles son los profesores asignados a cada grupo, ordenado por profesor?_
# 
# Para esto se deben relacionar las tablas de grupo y profesor. En este caso, no es casualidad que ambas tablas tienen una misma columna llamada __IDP__ y que además corresponden a el identificador del profesor.

# In[15]:


df_profesor["IDP"].value_counts()


# In[16]:


# Imprimimos nombres de las columna de los dataframes.
print(df_grupo.columns.values)
print(df_profesor.columns.values)


# Para combinar las fuentes de información el dataframe (que se utiliza como tabla izquierda) hace un llamado de la función _merge_, a la cual se le pasa el dataframe que funcionará como tabla derecha de la unión. Los parámetros importantes de la función _merge_ son los siguientes:
# * _right:_ (requerido) dataframe que funciona como tabla derecha.
# * _how:_ (opcional) indica el tipo de unión: {'left', 'right', 'outer', 'inner'} si no se especifíca el valor por omisión es 'inner'
# * _on:_ (opcional) especifica la columna por la que se hace la unión. Esta debe encontrarse en ambos dataframes. Si no se especifica la función busca la primera coincidencia en nombre y tipo de columna.
# * _left_on:_ (opcional) columna o nombres de columna para hacer la unión con el dataframe de la izquierda
# * _right_on:_ (opcional) columna o nombres de columna para hacer la unión con el dataframe de la derecha
# 
# 
# #### Resolver Pregunta 1. 
# 
# _Cuáles son los profesores asignados a cada grupo, ordenado por profesor?_
# 
# ```Python
# # 1. combinar 'df_profesor' y 'df_grupo'
# dfgp = df_grupo.merge(df_profesor)
# dfgp.sort_values('profesor', inplace=True)
# dfgp[['profesor', 'IDG', 'curso', 'nestud']]
# ```

# In[17]:


# 1. combinar 'df_profesor' y 'df_grupo'
dfgp = df_grupo.merge(df_profesor)
dfgp.sort_values('profesor', inplace=True)
dfgp[['profesor', 'IDG', 'curso', 'nestud']]


# In[18]:


df_grupo.head(2)


# In[19]:


df_profesor.head(2)


# In[20]:


# 1. combinar 'df_profesor' y 'df_grupo'
dfgp = df_grupo.merge(df_profesor)
dfgp.head()


# In[21]:


dfgp.sort_values('profesor', inplace=True)


# In[22]:


dfgp[['IDG', 'profesor']].head(10)


# #### **Solución pregunta 2**
# 
# _Cuáles son los estudiantes que tiene cada profesor por grupo y por programa académico?_
# 
# En esta caso podemos cruzar la tabla anterior con `df_estudiante`, pues son las tablas que tienen la información solicitada, pero debemos hacer uso de otra tabla para lograr hacer el puente y enlazar la información.
# 

# In[23]:


dfgp.head()


# In[24]:


dfel = df_estudiante.merge(df_listado) # Puente
dfel.head()


# In[25]:


dfge = dfel.merge(dfgp)
dfge.head()


# In[26]:


## A continuación una posible solución:
dfge.sort_values(['profesor','IDG','programa'], inplace=True)
df1 = dfge[['profesor','IDG','programa','IDE']]
df1.head()


# ### ***Solución pregunta 3***
# 
# _Cuáles son los promedios de calificación en el primer y segundo corte que tienen cada uno de los profesores en los grupos de Ingeniería de Sistemas?_

# In[27]:


df_temp = df_listado.merge(df1)
##
mask  = df_temp["programa"] == "Ingeniería De Sistemas"
mask1 = df_temp["profesor"] == "Apolo"
df_temp[mask & mask1][["corte1","corte2"]].mean()


# ## Agrupar datos con el método _groupby_
# 
# 
# En el Análisis de la información se suelen usar funciones de resumen, las cuales plantean el agrupamiento de ciertas características por categorías. Para una revisón de la función _groupby_ con ejemplos prácticos visite la página: [tutorialspoint](https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm)
# 
# 
# ### __Resumen de funciones para trabajar con series numéricas en pandas:__
# Lista de funciones de pandas y numpy para usar con variables numéricas en dataframes:
# 
# `count, sum, mean, mad, median, min, max, mode, abs, prod, std, var, skew, kurt, quantile, cumsum, sumprod, cummax, cummin`
# 
# 
# 
# 
# 

# In[28]:


## Ejemplo 1
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
df


# In[29]:


## Obtenemos los grupos y los índices de los registros de cada grupo.
df.groupby('Team').groups


# In[30]:


## Obtenemos los grupos y los índices de los registros de cada grupo.
df.groupby(['Team','Year']).groups


# In[31]:


df.groupby(['Team','Year']).indices


# In[32]:


## Dataframe con los grupo generados.
grouped = df.groupby('Year')

for name, group in grouped:
    print(name)
    print(group)


# In[33]:


## Dataframe con un grupo particular.
grouped = df.groupby('Year')
grouped.get_group(2014)


# In[34]:


## Cantidad de registros en cada grupo
grouped = df.groupby('Team')
grouped.size()


# In[35]:


df


# In[36]:


## Función de agregación
grouped = df.groupby('Year')
grouped['Points'].agg(np.mean)


# In[37]:


## Varias funciones de agregación para una columna luego de ser agrupados.
grouped = df.groupby('Team')
grouped['Points'].agg([np.sum, np.mean, np.std])


# In[38]:


## Transformación de datos por grupos.
grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
grouped.transform(score)


# In[39]:


## Aquellos grupos con 3 o más registros
df.groupby('Team').filter(lambda x: len(x) >= 3)


# ### Ejemplos de groupby con _examen2.xlsx_
# 
# Pruebe los siguientes ejemplos y analice el resultado:
# 
# ```python
# # ejemplos con groupby
# dfge.groupby(['profesor','IDG','programa'])[['IDE','corte1']].agg([np.size,np.std})
# dfge.groupby(['profesor','IDG','programa']).agg({'corte1': ['mean', 'min','max'], 'corte2': ['std','min','max']})
# dfge.groupby(['profesor','IDG','programa']).agg({'corte1': ['mad', 'median', 'mean']})
# dfge.groupby(['profesor','IDG']).agg({'programa': ['count', 'first','last','nunique', 'sum']})
# dfge.groupby(['profesor','IDG'])['programa'].describe()
# ```

# In[40]:


dfge.head(2)


# In[41]:


dfge["IDE"].value_counts() ## Todos los estudiantes son distintos


# In[42]:


# ¿Cuánto estudiantes tiene cada profesor?
dfge.groupby(["profesor"]).size().sort_values(ascending=False)


# In[43]:


## Obtenemos para cada columna seleccionada y para cada agrupación size = Tamaño, mean = media muestral y std = desviación estandar.
dfge.groupby(['profesor','IDG','programa'])[['corte1','corte2']].agg([np.size,np.mean,np.std])


# In[44]:


## Información de los grupos para la variable seleccionada y las distintas funciones de agragación.
dfge.groupby(['profesor','IDG']).agg({'programa': ['count', 'first','last','nunique', 'sum']})


# In[45]:


## Infomación de profesor y grupo para la variable categórica 'programa'.
dfge.groupby(['profesor','IDG'])['programa'].describe()


# In[46]:


## Infomación de profesor y grupo para la variable categórica 'programa'.
dfge.groupby(['profesor','IDG'])['corte1'].describe()


# In[47]:


# Grupos por profesor:
df1.groupby(['profesor'])['IDG'].agg(lambda x: set(x))


# ### ***Solución pregunta 3.***
# 
# _Cuáles son los promedios de calificación en el primer y segundo corte que tienen cada uno de los profesores en los grupos de Ingeniería de Sistemas?_
# 
# 
# Con lo que ya se conoce intente resolver

# In[48]:


## Solución pregunta 3.
df_groupby = dfge[dfge['programa']=='Ingeniería De Sistemas'].groupby('profesor')[['corte1','corte2']].mean()
df_groupby


# ### ***Solución de la pregunta 4***
# 
# _Qué estudiantes de cada programa han dejado de presentar el examen?_
# 
# 
# **Análisis:** Para esta pregunta la información esta en las tablas: 'examen' y 'estudiante'. Al combinar estas dos tablas es necesario forzar a que aparezcan todos los estudiantes incluso los que no presentaron examen. Luego se puede filtrar por aquellos estudiantes que no les aparece nota de examen y se organizan por programa.
# 
# 
# 
# 
# 

# **Hint**:
# 
# Realice los siguientes tres pasos:
# 
# 1. Enlace las 2 tablas del anaĺisis con `how=???`
# 2. Muestre la cantidad de faltantes por carrera con ``pd.groupby()``
# 3. Construya un dataframe donde se vean los faltantes, el total y % de faltantes.

# In[49]:


df_examen.head(2)


# In[50]:


df_examen.shape, df_estudiante.shape


# In[51]:


df_estudiante["IDE"].value_counts() ## No tenemos registros repetidos por IDE


# In[52]:


df_examen["IDE"].value_counts() ## Tenemos 2 registros repetidos por IDE


# In[53]:


df_examen[df_examen["IDE"] == 1900]


# In[54]:


df_examen[df_examen["IDE"] == 1681]


# In[55]:


df_estudiante.head(2)


# In[56]:


dfxe = df_estudiante.merge(df_examen, how = "left")
dfxe.info()


# In[57]:


dfxe.head(10)


# In[58]:


mask = dfxe["nota"].isna()


# In[59]:


## Serie de pandas a dataframe.
mask = dfxe["nota"].isna()
df_temp = dfxe[mask].groupby("programa")["IDE"].count().sort_values(ascending=True).to_frame()
print(df_temp.reset_index())


# In[60]:


## Una posible solución.
df3 = dfxe.groupby('programa')['IDE'].count().to_frame()
df1 = dfxe[mask]
print('Tamaño de tabla: ',df1.shape)
df2 = df1.groupby('programa')['IDE'].count().to_frame()
df2['total'] = df3['IDE']
df2['percent'] = 100*df2.IDE/df2["total"]
print(df2)


# ### ***Solución pregunta 5.***
# 
# _Cuáles de los estudiantes que presentaron el examen no aparecen en el listado?_
# 
# Con lo que ya conoce trate de resolver este punto.

# In[61]:


## Primero notemos que todos los estudiantes que presentaron el examen están en el listado
print("El tamaño del dataframe df_examen es:",df_examen.shape)
print("El tamaño del dataframe df_listado es:",df_listado.shape)
print("El tamaño del dataframe con inner join es:", df_examen.merge(df_listado).shape)


# In[62]:


## ¿Porqué aumenta el número de registros?
df_listado.merge(df_examen, how="left").shape


# In[63]:


# celda de código para probar


# ## _**Manejo de Tablas Pivote**_
# 
# 
# Las `Pivot table` son tablas de datos de resumen. Estas tablas permiten agrupar información para el análisis de datos. La agrupación de información es posible en filas y columnas, lo cual resulta muy útil para cruzar categorías de diferentes características. Con la información de cruce se calculan diferentes estadísticas, como por ejemplo: suma, promedio, desviación, varianza, entre otros para variables numéricas. Así como también, conteos, cantidad de valores únicos, moda, entre otras para variables de tipo categórico.
# 
# Antes de usar una `Pivot Table`, es necesario que se tenga una completa compresión de la estructura de sus datos, la descripción de cada una de las columnas que tiene y los posibles valores que estas puedan tomar y que va usar en el procesamiento de los datos. Luego de entender los datos, ahora debe comprender la pregunta que está intentando resolver mediante una `Pivot table`. 

# ### El método: `pivot_table`
# 
# A continuación se mencionan los parámetros más importantes de la función:
# * __dataframe:__ es necesario antes crear una tabla con todos los datos que se van a trabajar.
# * __index:__ lista de columnas que serán utilizadas para agrupar por filas
# * __columns:__ lista de columnas que se utilizarán para agrupar por columnas, con las categorias de las filas
# * __values:__ (opcional) lista de columnas que serán utilizadas para resumir la información
# * __aggfunc:__ Lista de funciones que se utilizan para agregar los valores. 
# * __fill_value:__ valor para reemplazar valores nulos
# * __margins:__ Para agregar subtotales a las filas y columnas, parciales o totales.
# 
# Para información adicional de pivot tables [python datascience notebook](https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html)
# 
# 

# In[64]:


import seaborn as sns
titanic = sns.load_dataset('titanic')


# In[65]:


titanic.head(2)


# In[66]:


titanic.groupby('sex')[['fare']].mean()


# In[67]:


titanic.groupby(['sex', 'class'])['survived'].agg('mean').unstack()


# In[68]:


titanic.pivot_table('survived', index='sex', columns='class')


# In[69]:


titanic['survived'].value_counts()


# In[70]:


age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')


# In[71]:


fare = pd.qcut(titanic['fare'], 2)
titanic.pivot_table('survived', ['sex', age], [fare, 'class'])


# In[72]:


titanic.pivot_table(index='sex', columns='class', aggfunc={'survived':sum, 'fare':'mean'})


# In[73]:


titanic.pivot_table('survived', index='sex', columns='class', margins=True)


# In[74]:


titanic.head()


# In[75]:


f = lambda x: abs(x.mean()-1)


# In[76]:


titanic.pivot_table(values = 'survived',index='sex', columns='class', margins=True,\
                    aggfunc=[np.mean, f])


# ### Ejemplo pivot_table 1
# 
# **Problema:** Se requiere saber el promedio de las notas del corte 1 y corte 2 agrupadas por profesor y número del grupo (en filas) y clasficadas por el nombre del programa (en columnas).

# In[77]:


print(dfel.head(2)) # Estudiante y listado
print(dfgp.head(2)) # Grupo y profesor


# In[78]:


df_merge = dfel.merge(dfgp)
df_merge.columns.values


# In[79]:


# celda para probar
df_merge.pivot_table(values = ['corte1','corte2'], index=['IDG',"profesor"],columns="programa",
                     fill_value = "S/E")


# ### Uso de pivot_table
# 
# Aplicamos la función sobre los datos preparados:
# 
# 
# ```python
# dfr = dfl.pivot_table(index=['profesor', 'IDG'], columns='programa', values=['corte1', 'corte2'], aggfunc=np.mean)
# dfr
# ```
# 
# 
# 

# Ahora le agregamos totales de fila y de columna a los resultados
# 
# ```python
# dfr = dfl.pivot_table(index=['profesor', 'IDG'], columns='programa', values=['corte1', 'corte2'], aggfunc=np.mean, margins='All',\
#                        margins_name='Total', dropna=True, fill_value=-1)
# dfr
# ```
# 
# 

# In[80]:


# celda de código para probar
#dfr = dfl.pivot_table(index=['profesor', 'IDG'], columns='programa', values=['corte1', 'corte2'],
#                      aggfunc=np.mean, margins='All',margins_name='Total', dropna=True, fill_value=-1)
#dfr


# ### Ejemplo pivot table 2
# 
# **Problema:** Ahora se quiere saber la cantidad de estudiantes a cargo de cada profesor agrupado por dedicación y profesor (en filas) clasificada por el nombre de programa (en columnas).
# 
# ```python
# dfr = dfl.pivot_table(index=['dedicacion','profesor'], columns='programa', values=['nestud'], aggfunc=np.sum, margins='All', margins_name='Total', dropna=True, fill_value=0)
# dfr
# ```
# 
# 

# In[81]:


# celda para probar
#dfr = dfl.pivot_table(index=['dedicacion','profesor'], columns='programa', values=['nestud'], 
#                      aggfunc=np.sum, margins='All', margins_name='Total', dropna=True, fill_value=0)
#dfr


# 
# ## ___Ejercicios.___
# 
# 
# Con los datos suminstrados se requiere resolver las siguientes inquietudes:
# 1. Se quiere hacer un ranking de profesores de acuerdo con el promedio de nota de sus estudiantes
# 2. Se quiere saber cuáles fueron los estudiantes que pasaron el examen con más o igual a 4.0, con qué profesor estaban, de qué jornada son y a qué grupo pertenecen
# 3. Saber cuáles fueron los promedios de examen por jornada y por carrera y ordenados por promedio. 
# 4. Se quiere comparar los estudiantes que presentaron el examen respecto al tiempo que tardaron. Comparar promedios de las calificaciones de los 40 más rápidos contra los 40 más lentos. 
# 5. Se quiere saber por profesor cuantos pasaron (nota >= 3) el examen y cuantos los perdieron. 
# 6. Se quiere organizar las preguntas de la más difícil a la más fácil de acuerdo a como respondieron en el examen.
# 7. Formule dos preguntas acerca de los datos en donde tenga que aplicar ordenamiento, filtrado, agrupación y cruce de datos.
# 8. Responda las preguntas que planteó en el punto anterior.

# ## Tarea: revisar:
# 
# ### 1. Manejo de datos duplicados 
# 
# Los dataframes tienen la posibilidad de detectar las filas duplicadas con la función: 
# 
# ```
# df.duplicated({columns})
# ```
# 
# Si no especifica {columns}, se busacarán duplicados teniendo en cuenta todas las columnas. Una vez detectados el dtaframe tiene un función para eliminar filas duplicadas, haciendo:
# 
# ```
# df = df.drop_duplicates()
# ```
# 
# También es posible eliminar filas que duplican solo algunos campos. Con el fin de dejar solo una ocurrencia.
# 
# ```
# df.drop_duplicates(['nombre', 'apellido', 'cédula'], keep='last')
# ```
# En este caso, como no todas las colomnas son iguales se conserva solo la última ocurrencia.
# 
# 
# ### 2. Manejo de datos perdidos o esperados
# 
# Son aquellos datos flatantes en la tabla que por alguna razón o error no se encuentran, o parecen con algún valor o etiqueta de no válido. 
# Para reemplazar datos perdidos en un dataframe `df` se usa la función:
# ```python
# promedio = df['nota'].mean()
# df['nota'].replace(np.nan, promedio)
# ```
# en donde la opción `promedio` busca el valor promedio de la columna (datos numéricos).
