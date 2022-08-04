#!/usr/bin/env python
# coding: utf-8

# # Operaciones básicas con dataframes
# 
# **Temas:**
# 
# 
# * Cargar información con `pandas`
# * Acceso
# * Ordenamiento 
# * Filtrado
# * Guardar información con `pandas`

# 
# ## _Ubicación actual, cambio de ubicación._
# 

# Piense que ahora está en su computador, de hecho lo está, es una maquina virtual donde usted puede trabajar con un interprete de código `Python`.

# In[1]:


pwd ## Fichero de ubicación actual


# _Nota:_
# 
# Dependiendo de donde esté trabajando, debe tener en cuenta su ubicación actual (pwd) y apartir de allí cambiar de fichero si lo necesita (cd), piense que entra ingresando con lo hace normalmente al moverse en ficheros dentro de otros ficheros.

# In[2]:


ls -l ## Listar ficheros y documentos de la ubicación actual


# In[3]:


#%%capture
#!pip install --upgrade xlrd


# ## __Dataframes__
# 
# ¿Qué es un dataframe?
# 
# ¿Cuál es la estructura de un dataframe? filas, columnas, encabezados de columna, tipos de datos. 
# 
# Acá puede consultar un resumen de lo presentado [towards data science: dataframes.](https://towardsdatascience.com/pandas-dataframe-a-lightweight-intro-680e3a212b96)

# ## __1 - Cargar información con pandas__
# 
# 
# ![pandas](https://miro.medium.com/max/1400/0*WprttYz2ksxsdXBH)
#  
# Pandas proporciona facilidades para la recuperación simple de datos de una variedad de fuentes como objetos de pandas. Para este notebook se usarán varios conjunto de datos del fichero `datas`. Importe la librería de **Pandas** y **NumPy**.
# 
# 
# ```Python
# # importando librerías 
# import pandas as pd
# import numpy as np
# ```

# In[4]:


# importando librerías 
import pandas as pd
import numpy as np


# ## Cargando datos en un DataFrame a partir de archivos.
# 
# La librería `pandas` facilita la obtención de datos desde diferentes tipos de fuentes. Algunas fuentes de datos pueden estar en archivos de extensiones **.csv**, **.txt**, **.json**, **.xls**  y de **xlsx**. A continuación usted podrá cargar un archivo de excel. 
# 
# Como recomendación, procure dejar en una celda independiente para la lectura de los datos. Esta lectura tiene un costo de carga en recursos de máquina que puede impactar su trabajo y el entorno de `Python` si se esta ejecutando continuamente.
# 
# ```Python
# url_datos = 'datas/examen2.xlsx' # url local del archivo a leer
# df_Excel= pd.ExcelFile(url_datos) # lectura del archivo
# df_Excel # ¿Qué obtenemos?
# ```

# In[5]:


# celda de código para probar 
url_datos = 'datas/examen2.xlsx' # url local del archivo a leer
df_Excel= pd.ExcelFile(url_datos)
print(df_Excel)


# En el uso anterior del método `.ExcelFile()` hemos traido el archivo, pero aún no un dataframe de `pandas`, más información del método [acá.](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html)

# In[6]:


# Todos los sheets del archivo
df_Excel.sheet_names, type(df_Excel.sheet_names)


# In[7]:


# Podemos obtener todas los sheest, ahora como pandas-DataFrame
sheets = []
for sheet in df_Excel.sheet_names:
    sheets.append(df_Excel.parse(sheet))
    print("*"*80)
    display(df_Excel.parse(sheet)) ## display(dataframe/serie) despliega el pandas-DataFrame

#sheets ## Tenemos todos los pandas-DataFrame en la lista sheets.


# In[8]:


sheets[-1]


# Otra manera de leer archivos xlsx, o xls, es con el método `read_excel()`, note que en este caso solo trae por default el primer sheet, en caso de desear traer un sheet particular se debe proporcionar su nombre (o posición). El método tiene muchos parámetros, la información ampliada la puede encontrar en la [documentación oficial.](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
# 
# ```Python
# df_datos = pd.read_excel(url_datos)                      
# df_ind_col = pd.read_excel(url_datos, 'profesor')   # lectura del archivo especificando la hoja
# ```
# No siempre es necesario especificar el nombre de la hoja del archivo. Pandas por defecto tomará la primera. Ahora usted en una nueva celda puede llamar los DataFrame creados a partir de la lectura de los archivos.

# In[9]:


df_datos = pd.read_excel(url_datos)                 # lectura del archivo 
df_ind_col = pd.read_excel(url_datos, 'profesor')   # lectura del archivo especificando la hoja


# In[10]:


display(df_datos)


# In[11]:


df_ind_col


# _Ejercicio._
# 
# Pruebe algunos de los parametros de `read_excel()` y deje los comentarios que le sean relevantes.

# In[12]:


#help(pd.read_excel)


# In[13]:


#pd.read_excel(url_datos, "profesor", index_col = [0,2]) ## Podemos establecer una columna como índice. Será de uso en los merges.
#pd.read_excel(url_datos, "profesor", header= 0, names = ["col1","col2"]) # Podemos cambiar el nombre de las columnas.
#pd.read_excel(url_datos, "examen", names = ["col1","col2"])
#pd.read_excel(url_datos, "examen", header= 10) # Del sheet "examen", el registro 11 será la cabecera.
#pd.read_excel(url_datos, [0,1,2,3,4,5]) # En este caso podemos obtener todos sheets como un diccionario.
#pd.read_excel(url_datos, "profesor", skipfooter=5, skiprows=[1,2]) ## Eliminar los últimos 5 registros y los 2 primeros (Index=0)
### Diccionario con keys los nombres de los sheets.


# In[14]:


pd.read_excel(url_datos, None)["cita"]


# ### Cargar un archivo CSV.
# 
# Defina el nombre del DataFrame sobre el cual va a cargar los datos del archivo e invoque la instrucción *read_csv* de lectura de archivos **.csv**.
# 
# ```Python
# URL_pais = 'datas/pais.csv'
# 
# dfp = pd.read_csv(URL_pais, sep=',', ## El separador por default es ",".
#                   encoding='utf-8') ## Tipo de codificación del archivo (reconodimiento de caracteres especiales en la lectura)
# 
# print('País (Registros, columnas):', dfp.shape)
# print('País (nombre columnas):', dfp.columns)
# print('País (tipos):', dfp.dtypes)
# dfp.head()
# ```

# In[15]:


# celda de código para probar
URL_pais = 'datas/pais.csv' 
dfp = pd.read_csv(URL_pais, sep = ",", encoding='utf-8') ## El separador por default es ","
dfp


# In[16]:


print('País (Registros, columnas):', dfp.shape)


# In[17]:


print('País (nombre columnas):', dfp.columns)


# In[18]:


for i, colum in enumerate(dfp.columns.values): ## enumerate: enumera un objeto iterable.
  print(i,colum)


# In[19]:


print('País (tipos):\n', dfp.dtypes)


# In[20]:


dfp.head()


# ### _Ejercicio._
# 
# Defina el nombre del DataFrame sobre el cual va a cargar los datos del archivo e invoque la instrucción *read_csv* de lectura de archivos **.csv**.
# 
# ```Python
# URL_iris = 'data/iris.csv' # URL de acceso al archivo
# ```
# Luego
# 
# ```Python
# dfi = pd.read_csv(URL_iris, sep=',', encoding='utf-8')
# ```
# 
# 
# * Hacer lo mismo que en el ejemplo anterior para los datos de 'iris' definiendo una función.
# 
# ```Python
# # argumentos de la función:
# # URL donde se encuentra el archivo
# # separardor que utiliza el archivo
# # tipo de codificación del archivo (reconocimiento de caracteres especiales en la lectura)
# ```
# 

# In[21]:


URL_iris = 'datas/iris.csv' # URL de acceso al archivo
dfi = pd.read_csv(URL_iris, sep=',', encoding='utf-8')
dfi


# In[22]:


dfi.head(10)


# In[23]:


dfi.tail(2)


# In[24]:


# argumentos de la función:
# URL donde se encuentra el archivo
# separardor que utiliza el archivo
# tipo de codificación del archivo (reconocimiento de caracteres especiales en la lectura)
def info_df(url,codificacion, sep1=","):
    df = pd.read_csv(url, encoding=codificacion, sep = sep1)
    print(df.shape)
    print(df.columns)
    print(df.head())
    print(df.dtypes)
    return df


# In[25]:


info_df('datas/iris.csv','utf-8')


# In[26]:


print(dfi.columns)
print(dfi.dtypes)


# In[27]:


def info_df(url, coding, sep = ","):
    df = pd.read_csv(url)
    print("*"*100)
    print('País (Registros, columnas):', df.shape)
    print("*"*100)
    print('País (nombre columnas):', df.columns)
    print("*"*100,'\nPaís (tipos):')
    print(df.dtypes)
    print("*"*100)
    display(dfp.head())

info_df('datas/iris.csv','utf-8')


# ## Información de un dataframe
# 
# - Forma: `dfp.shape`
# - Nombre las columnas: `dfp.columns`
# - Tipos de datos de las columnas: `dfp.dtypes`
# - Tipo de dato del data frame o de una serie: `type`
# - Despliegue del dataframe: `display(dfp)` 
#     - Despliegue de los primeros registros: `display(dfp.head(10))`
#     - Despliegue de los últimas registros: `display(dfp.tail(12))`
#     - Despliegue de una muestra aleatorea de 8 registros: `display(dfp.sample(8))`

# ### _Ejercicio._
# 
# Haga uso de las funciones y métodos anteriores, pruébelos todas en las siguientes lineas de código. Amplie la función creada del ejercicio anterior

# In[28]:


# Celda para probar el código.
print("El tamaño del dataframe es:",dfp.shape)
print("El número de resgistrso es:", dfp.shape[0],)
print("El número de columnas es:", dfp.shape[1])


# In[29]:


dfp.columns


# In[30]:


# Tenemos un array (como elemento de Numpy)
dfp.columns.values


# In[31]:


dfp.dtypes ## Serie de pandas


# In[32]:


display(dfp)


# In[33]:


display(dfp.head(10))


# In[34]:


display(dfp.tail(12))


# In[35]:


## Muestra aleatoria del dataframe
display(dfp.sample(8))


# ### _Ejercicio._
# 
# Pruebe el siguiente código:
# 
# ```Python
# URL_datos = 'datas/examen.xlsx'                    # URL local del archivo a leer
# dfe = pd.read_excel(URL_datos)                     # lectura del archivo 
# dfx = pd.read_excel(URL_datos, 'examen1')          # lectura del archivo especificando la hoja
# ```
# 
# * Corregir el error al momento de cargar la hoja especificada del archivo.
# * Utilice un método adecuado para determinar todos los sheets del archivo.
# * Realizar una función para mostrar la información del dataframe: forma, columnas, tipos de datos y muestra de los elementos.
# 

# In[36]:


ls -l datas/


# In[37]:


URL_datos = 'datas/examen.xlsx'                         # URL local del archivo a leer
dfe = pd.read_excel(URL_datos)
#dfx = pd.read_excel(URL_datos, 'examen1')               # lectura del archivo 
dfe


# In[38]:


# Solución del error
dfx = pd.read_excel(URL_datos, None) ## Obtenemos un dict(), donde las keys son los sheets-names


# In[39]:


for key in dfx.keys():
  print(key)


# In[40]:


dfx["examen"] ## Como el valor de la key "examen"


# In[41]:


# Despúes de observar el diccionario tenemos el nombre de la hoja.
dfx = pd.read_excel(URL_datos, 'examen')
dfx


# In[42]:


URL_datos = 'datas/examen.xlsx'                    # URL local del archivo a leer
dfe = pd.read_excel(URL_datos)                     # lectura del archivo 
dfx = pd.read_excel(URL_datos, 'examen')          # lectura del archivo especificando la hoja


# In[43]:


for value in pd.read_excel(URL_datos, None).values():
  print(value)


# ### _Ejercicio._
# 
# Revise el fichero datas, y cargue los demás archivos, en caso que se tenga un nuevo tipo de archivo, busque el método adecuado para cargarlo como un pandas-DataFrame y haga uso de la función construida en el ejercicio anterior.
# 
# **Hint:** Con el siguiente código puede ver todos los archivos en la ruta indicada.
# 
# ```Python
# import glob
# 
# list_of_files = glob.glob("datas/*")
# list_of_files
# ```

# In[44]:


import glob

list_of_files = glob.glob("datas/*")
list_of_files


# In[45]:


df_json = pd.read_json('datas/downloaded_medals.json')
df_json


# In[46]:


df_text = pd.read_table('datas/stopWordsSPA.txt', header = None, names = ["Manual1"])
df_text


# In[47]:


df1 = pd.read_excel('datas/downloaded_medals.xls')
df1


# In[48]:


df_medals = pd.read_csv('datas/Medals.csv',encoding='utf-8', encoding_errors="ignore")
df_medals


# In[49]:


df_Ath = pd.read_csv('datas/Athelete_Country_Map.csv', encoding='utf-8', encoding_errors="ignore")
df_Ath.head()


# In[50]:


df_Ath = pd.read_csv('datas/downloaded_medals.csv', encoding='utf-8')
df_Ath.head()


# In[51]:


df_text = pd.read_table('datas/fragmento.txt',)
df_text


# 
# ## __2. Acceso al Dataframe__
# 
# 
# Dentro de las operaciones que se requieren para trabajar un Dataframe se resaltan las siguientes:
# 
# * Seleccionar las columnas que se quieren ver
# * Seleccionar un subconjunto de los registros utilizando el índice (primeras, últimas, intervalo), 
# * Obtener índice y cambiar el índice de la tabla

# ### Acceso al dataframe
# 
# - Acceder a determinadas columnas: `display(dfp[['Pais', 'moneda', 'Pobla']])`
# - Acceso al registro de índice 96:  `display(dfp.loc[96])`
# - Acceso al registro de índice 96 y la columna 'moneda': `display(dfp.loc[96, 'moneda'])
# - Acceso a los registros 96 a 98 y columna 'moneda': `display(dfp.loc[96:98, 'moneda'])`
# - Acceso a los registros 96 a 98 y las columnas 'Pais' y 'moneda': `display(dfp.loc[96:98, ['Pais','moneda']])`
# - Mas información acerca del uso del [método **loc**.](
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html)
# - Mostrar solo valores únicos de una columna: `dfp.moneda.unique()`, otro ejemplo: `dfp.C.unique()`

# ### _Ejercicio._
# 
# Haga uso de las funciones y métodos anteriores, pruebelos todos en las siguientes lineas de código.

# In[52]:


dfp.columns


# In[53]:


display(dfp[['Pais']])
print(type(dfp[['Pais']]))


# In[54]:


display(dfp['Pais'])
print(type(dfp['Pais']))


# In[55]:


dfp.head(2)


# In[56]:


lst = ['Pais', 'moneda', 'Pobla']
dfp[lst]


# In[57]:


dfp.columns


# In[58]:


get_ipython().run_cell_magic('time', '', 'lista2 = [x for x in dfp.columns if x not in lst]\ndfp[lista2]\n')


# In[59]:


display(dfp.loc[96]) ## Serie de Pandas. Registro 96


# In[60]:


display(dfp.loc[96, 'moneda'])


# In[61]:


display(dfp.loc[96:98, 'moneda'])


# In[62]:


display(dfp.loc[96:98, ['Pais','moneda']])


# In[63]:


## Valores únicos de la columna "moneda" del dataframe.
dfp["moneda"].unique()


# In[64]:


## Valores únicos de la columna "moneda" del dataframe.
dfp.moneda.unique()


# In[65]:


## Valores únicos de la columna "C" del dataframe.
dfp.C.unique()


# In[66]:


for i,columns in enumerate(dfp.columns):
  print(i,columns)


# In[67]:


dfp.index.values


# ### Seleccionar columnas
# 
# El método para seleccionar columnas de un dataframe más usado es hacer una lista con los nombres de las columnas en el orden que se quiere, así como se muestra en el siguiente ejemplo:
# 
# 
# ```Python
# URL_datos = 'datas/examen.xlsx'                    # URL local del archivo a leer
# dfe = pd.read_excel(URL_datos)                     # lectura del archivo 
# 
# ```
# 
# ```Python
# print(dfe.columns)
# sel_columns = ['IDE', 'IDG', 'profesor', 'nota']
# dfe1 = dfe[sel_columns]
# display(dfe1)
# ```
# Se puede usar directamente sin declarar la lista
# 
# 
# ```Python
# dfe1 = dfe[['IDE', 'IDG', 'profesor', 'jornada', 'nota']]
# ```
# 
# 
# 
# 
# 

# In[68]:


URL_datos = 'datas/examen.xlsx'                    # URL local del archivo a leer
dfe = pd.read_excel(URL_datos)                     # lectura del archivo  


# In[69]:


print(dfe.columns)
sel_columns = ['IDE', 'IDG', 'profesor', 'nota']
dfe1 = dfe[sel_columns]
display(dfe1)


# ### Seleccionar registros.
# 
# El método [__iloc__](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html) resulta útil para seleccionar registros y columnas de un DataFrame, como se muestra en el siguiente ejemplo:
# 
# 
# 
# ```Python
# print(dfe1.iloc[0])   # imprime el primer registro
# print(dfe1.iloc[1])   # imprime el segundo registro
# print(dfe1.iloc[-1])  # imprime el último registro
# ```
# 
# __iloc__ funciona como una lista de dos dimensiones, con el primer espacio se accede a las filas y con el segundo a las columnas
# 
# 
# 
# ```Python
# s1 = dfe1.iloc[:,-1]
# print(type(s1))
# s1
# ```
# Pruebe los siguientes ejemplos y verifique el tipo de estructura que devuelve cada operación:
# 
# ```Python
# dfe1.iloc[0:5]            # Primeras cinco filas
# dfe1.iloc[:, 0:5]         # Primeras cinco columnas
# dfe1.iloc[[0,2,1]]        # Primera, tercera y segunda filas
# dfe1.iloc[:, [0,2,1]]     # Primera, tercera y segunda columnas
# ```
# 
# * Usar las funciones head, tail y sample para ver una muestra de los datos del DataFrame

# In[70]:


print(dfe1.iloc[0])   # imprime el primer registro
print(dfe1.iloc[1])   # imprime el segundo registro
print(dfe1.iloc[-1])  # imprime el último registro


# In[71]:


dfe1.iloc[0:5]            # Primeras cinco filas
dfe1.iloc[:, 0:5]         # Primeras cinco columnas
dfe1.iloc[[0,2,1]]        # Primera, tercera y segunda filas
dfe1.iloc[:, [0,2,1]]     # Primera, tercera y segunda columnas


# In[72]:


## .iloc
dfp.iloc[[2,6,30],[5,11]]


# ### Obtener el índice y cambiar índice de la Tabla
# 
# Con `pandas` usted puede redefinir el índice ordinal original. Para esto debe encontrar una serie dentro de su DataFrame contenga valores únicos. Ejemplo:
# 
# 
# ```Python
# dfp.set_index('Pais', inplace=True)
# dfp
# ```
# 
# Es posible generar una lista de valores con los índices del Dataframe
# 
# ```Python
# dfe1 = dfe[['IDE', 'IDG', 'profesor', 'jornada', 'nota']]
# ind1 = dfe.index.to_list()
# dfe1.set_index('IDE', drop=False, inplace=True)
# ind2 = dfe.index.to_list()
# ```

# In[73]:


dfe1.head()


# In[74]:


dfe1 = dfe[['IDE', 'IDG', 'profesor']]
dfe1


# In[75]:


print(dfe1.index)
print(dfe1.index.values) ## Lista de los índices
print(dfe1.index.to_list()) ## .to_list() buscar forzar el objeto a ser una lista.


# In[76]:


ind1 = dfe.index.to_list()
ind1


# In[77]:


dfe1.set_index('profesor', drop=True, inplace = True)


# In[78]:


dfe1


# In[79]:


#dfe1.set_index("profesor",inplace=True)
list(set(dfe1.index.to_list()))
dfe1.loc["Paris"]


# In[80]:


# Celda de código para probar
#dfp.set_index('Pais', drop = True, inplace=True)
dfp


# In[81]:


dfe1 = dfe[['IDE', 'IDG', 'profesor', 'jornada', 'nota']]
ind1 = dfe.index.to_list()
dfe1.set_index('IDE', drop=False, inplace=True)
ind2 = dfe.index.to_list()


# In[82]:


# Celda de código para probar
dfe1 = dfe[['IDE', 'IDG', 'profesor', 'jornada', 'nota']]
ind1 = dfe.index.to_list()
ind1[:30] ## Los 30 primeros elementos.


# In[83]:


df_multi = dfe1.set_index(['IDE','profesor'], drop=True, inplace=False)
df_multi.index


# ### Generar una columna calculada
# 
# Crear un DataFrame a partir de un diccionario
# 
# ```Python
# dic = {'nombre':['jorge', 'Darwin', 'Miguel'], 'peso':[68.5, 78.3, 65.5], 'altura':[1.67, 1.72, 1.52]}
# dfm = pd.DataFrame(dic)
# dfm
# ```
# Usar peso y altura para calcular imc y agregar como nueva columna al Dataframe
# 
# 
# ```Python
# dfm['imc'] = dfm.peso/dfm.altura**2
# ```
# 

# In[84]:


# Celda de código para probar
dic = {'nombre':['jorge', 'Darwin', 'Miguel'], 'peso':[68.5, 78.3, 65.5], 'altura':[1.67, 1.72, 1.52]}
dfm = pd.DataFrame(dic)
dfm


# In[85]:


dfm["nueva"] = ["hola","a","todos"]
dfm


# In[86]:


dfm['imc'] = dfm.peso/dfm.altura**2
dfm


# #### _Ejercicio._
# 
# 1. Agregue una columna con los valores de 'edad'
# 2. Cambie un valor específico del DataFrame
# 

# In[87]:


dfm["edad"] = [24,45,23]
dfm


# In[88]:


dfm.iloc[1,1]= "cambio"
dfm


# In[89]:


dfm.loc[2,"edad"] = [["otro, cambio"]]
dfm


# ### Copiar y borrar información del dataframe
# - En general las funciones de *pandas* trabajan haciendo referencias de los datos. Cuando se extrae un subconjunto de los datos o se cambia el orden a las columnas, esto se hace como una nueva vista de los datos originales. Sin embargo, en algunos casos es necesario hacer una copia para no modificar la fuente original de datos. Esto se hace mediante la función __copy()__
# 
#     `df1 = dfp.copy()`
# 
# - En otros casos las funciones aplican las operaciones en datos en memoría temporal, es decir no se aplican sobre la variable que hace la operación. Por lo que se hace necesario asignar el resultado a otra variable o hacer uso de la opción __inplace=True__. En el siguiente ejemplo se muestra como realizar el borrado de filas o columnas sobre la variable:
# 
#     ```Python
#     df1.drop(columns=['Pobla', 'Superf', 'altura'], inplace=True)
#     df1.drop([0,2,4,6], inplace=True)
#     display(df1)
#     ```

# In[90]:


dfp


# In[91]:


df1 = dfp.copy()
df1


# In[92]:


df1.columns


# In[93]:


df1.drop(columns=['Pobla', 'Superf', 'altura'], inplace=True)
df1


# In[94]:


df1.drop([1,3,5,7], inplace=True)
df1


# #### _Ejercicio._
# 
# - Usar la función __zip__ para recorrer varias columnas dentro de un ciclo. Seleccione parejas de columnas y muestre la información conjunta.

# In[95]:


# celda de código para probar
ti = dfp['Eda-Me'].values
tf = dfp['E-vida'].values
for i,f in zip(ti,tf):
    print('Espectativa de vida: {} para una media de {} el indicador es {:.3f} %'.format(i,f,(100*i/f)))


# ## __3. Ordenamiento de DataFrames.__
# 
# 
# Una vez cargado un conjunto de datos en un DataFrame, `pandas` le permite realizar ordenamientos por una columna, múltiples columnas y por índice.
# 
# Este ordenamiento puede darse de forma ascendente o descendente.
# 
# ### Ordenamiento por una o varias columnas
# Para realizar ordenamiento por columna(s) usted puede utilizar la función *sort_values*. Esta función recibe argumentos de:
# 
# *   Nombre de la columna o una lista con el nombre de las columnas.
# *   ascending = verdadero o falso para cada columna
# *   inplace = verdadero para hacer el ordenamiento sobre el dataframe original.
# 
# 
# ```Python
# # ordenamiento ascendente por una columna
# dfp.sort_values(['Pais'], ascending=[True], inplace=True)
# dfp
# # ordenamiento descendente por una columna
# dfp.sort_values(['capital'], ascending=[False], inplace=True)
# dfp
# # ordenamiento dos columnas: ascendente col 1 y descendente col 2
# dfp.sort_values(['C','Pobla' ], ascending=[True, False], inplace=True)
# dfp
# # ordenamiento dos columnas: ascendente col 1 y acendente col 2
# dfp.sort_values(['C','Pobla' ], ascending=[True, True], inplace=True)
# dfp
# ```

# 
# 
# Ahora ustede puede usar la función sort_index para hacer el ordenamiento ascendente o descendente a partir del índice que se ha definido.
# 

# In[96]:


dfp.head(3)


# In[97]:


#Celda de código para probar
# ordenamiento ascendente por una columna
dfp.sort_values(['Pais'], ascending=[True], inplace=True)
dfp


# In[98]:


# ordenamiento descendente por una columna
dfp.sort_values(['capital'], ascending=[False], inplace=True)
dfp


# In[99]:


# ordenamiento dos columnas: ascendente col 1 y descendente col 2
dfp.sort_values(['capital','Pobla' ], ascending=[True, False], inplace=True)
dfp


# Ahora quisieramos generar un índice ordenando por profesor de manera descendente y guardar este índice en el dataframe. 
# 
# ```Python
# dfe1.sort_values(by=['profesor'], ascending=False, inplace=True)
# dfe1.set_index('IDE',  inplace=True)
# dfe1.reset_index(inplace=True)
# dfe1.sort_values(by=['IDE'], ascending=False, inplace=True)
# dfe1.reset_index(inplace=True)
# dfe1
# ```

# In[100]:


dfe1.reset_index(inplace=True)


# In[101]:


dfe1


# In[102]:


# Celda de código para probar
dfe1.sort_values(by=['profesor'], ascending=False, inplace=True)
dfe1


# In[103]:


dfe1.sort_values(by=['IDE'], ascending=False, inplace=True)
dfe1


# ## __4. Filtrado en DataFrames y algunos métodos de resumen.__
# 
# En pandas usted puede aplicar diferentes tipos de filtro sobre un DataFrame. Los filtros pueden ser construidos a partir de la evaluación de expresiones lógicas sobre las columnas o funciones propias de pandas.
# 
# A continuación se muestran unos ejemplos de filtros construidos con pandas.
# 
# 
# Valores máximos o mínimos sobre todo el DataFrame
# ```Python
# dfp.max() # obtiene los valores máximos de cada serie sobre todo el dataframe
# dfp.min() # obtiene los valores máximos de cada serie sobre todo el dataframe
# ```
# Valores máximos y mínimos sobre una columna
# 
# ```Python
# dfp['altura'].max() # obtiene el valor máximo de la columna seleccionada
# dfp['altura'].min() # obtiene el valor máximo de la columna seleccionada
# ```
# Valores máximos y mínimos de más de una columna
# 
# ```Python
# dfp[['altura', 'Pob-cap']].max() # obtiene el valor máximo de la columnas seleccionadas
# dfp[['altura', 'Pob-cap']].min() # obtiene el valor máximo de la columna seleccionada
# ```

# In[104]:


dfp.head(2)


# In[105]:


dfp["moneda"].unique()


# In[106]:


# máscara, una Serie de Pandas boolena.
mask = dfp["moneda"] == "Euro"
dfp[mask]


# In[107]:


# Celda de código para probar
print(dfp.max()) # obtiene los valores máximos de cada serie sobre todo el dataframe
print(dfp.min()) # obtiene los valores máximos de cada serie sobre todo el dataframe


# In[108]:


dfp["E-vida"].max()


# In[109]:


dfp[dfp["E-vida"]== dfp["E-vida"].max()]


# In[110]:


dfp[dfp["E-vida"]== dfp["E-vida"].min()]


# In[111]:


print(dfp['altura'].max()) # obtiene el valor máximo de la columna seleccionada
print(dfp['altura'].min()) # obtiene el valor máximo de la columna seleccionada


# In[112]:


print(dfp[['altura', 'Pob-cap']].max()) # obtiene el valor máximo de la columnas seleccionadas
print(dfp[['altura', 'Pob-cap']].min()) # obtiene el valor máximo de la columna seleccionada


# In[113]:


mask1 = dfp['moneda'] == "Euro"
mask1


# In[114]:


mask2 = dfp['Pobla'] <= 100
mask2


# In[115]:


((mask1)&(mask2)).sum()


# In[116]:


dfp[(mask1)&(mask2)]


# ### Filtrado por múltiples columnas con diferentes criterios
# 
# ```Python
# dfp[(dfp['Pais'].str.startswith('V')) & (dfp['altura'] > 161)]
# # Filtro donde los paises pertenecen al Contiente sea Asia, la población sea superior a 100 y el Pib PC sea superior a 3.9
# 
# dfp[(dfp['C'] == 'a') & (dfp['Pobla'] > 100) & (dfp['Pib PC'].str.replace(',','.').astype(float)> 3.9)]
# 
# # filtrado de los paises donde la edad media sea superior a 25 y menor a 60
# dfp[(dfp['Eda-Me'] > 25) & (dfp['Eda-Me'] < 60)]
# 
# # filtrado de los paises que tienen por moneda peso y la superficie es superior a 2000
# dfp[(dfp['moneda'] == 'Peso') & (dfp['Superf'] > 2000)]
# 
# #valores únicos por columna
# dfp['moneda'].unique()
# ```
# Notese que las expresiones en los filtros se debe usar paréntesis ()
# 
# 

# In[117]:


dfp[(dfp['Pais'].str.startswith('V'))]


# In[118]:


# Filtro de los paises que inicain su nombre con "V" y altura mayor a 161
dfp[(dfp['Pais'].str.startswith('V')) & (dfp['altura'] > 161)]


# In[119]:


dfp['Pib PC'].str.replace(",",".").astype(float)


# In[120]:


# Filtro donde los paises pertenecen al Contiente sea Asia, la población sea superior a 100 y el Pib PC sea superior a 3.9
dfp[(dfp['C'] == 'a') & (dfp['Pobla'] > 100) & (dfp['Pib PC'].str.replace(',','.').astype(float)> 3.9)]


# ### Filtrado con muestreo aleatorio sobre el DataFrame
# 
# ```Python
# # obtiene 25 elementos de forma aleatoria sobre el dataframe
# dfp.sample(25)
# 
# # obtiene el 60% de los elementos de forma aleatoria sobre el dataframe sin repetir ningun registro
# dfp.sample(frac=0.6, replace=False)
# ```
# Filtro por índices con valores aleatorios de forma estratificada

# In[121]:


# Celda de código para probar
# obtiene 25 elementos de forma aleatoria sobre el dataframe
dfp.sample(25)

# obtiene el 60% de los elementos de forma aleatoria sobre el dataframe sin repetir ningun registro
dfp.sample(frac=0.6, replace=False)


# ### Filtrar por valores de una columna
# 
# - Filtrar por una lista de profesores
#         
# ```Python
# dfe1 = dfe[sel_columns]
# lstp = ['Apolo', 'Eneas']
# df1 = dfe1[dfe1.profesor.isin(lstp)]
# #df1 = dfe1[~dfe1.profesor.isin(lstp)]
# df1
# ```
# 
# * Reemplazo de valores numéricos por categorías
# 
# ```Python
# 
# dicn = {3.0:'Tres', 2.0:'dos', 1.5:'uno y medio', 1.0:'uno', 
#         0.5:'medio', 0:'cero', 3.5:'tres y medio', 4:'cuatro', 
#         2.5:'dos y medio', 5:'Cinco', 4.5:'cuatro y medio'}
# dfe1.nota = dfe1.nota.map(dicn)
# 
# ```
# 
# * Filtrado de datos por lista de índices
# 
# 
# ```Python
# lst = dfe1.profesor[dfe1.profesor=='Eneas'].index[:].to_list()
# print(lst)
# dfe1[dfe1.IDE.isin(lst)]
# ```

# In[122]:


# Celda de código para probar
dfe1 = dfe[sel_columns]
lstp = ['Apolo', 'Eneas']
df1 = dfe1[dfe1.profesor.isin(lstp)]
# df1 = dfe1[~dfe1.profesor.isin(lstp)]
df1


# ### Métodos de resumen del dataframe
# 
# Existen diferentes métodos en `pandas` que operan directamente sobre el dataframe o las columnas. De esta forma se pueden obtener resultados rápidos y sencillos usando las funciones de resumen:
# 
# - **info():** Muestra información general del dataframe.
# - **describe():**  hace el resumen de una columna del dataframe dependiendo del tipo de dato de la columna.
# - **value_counts():** hace la cuenta por valores únicos de una columna.
# - **mean(), sum(), std():** existen estas funciones de resumen y más.

# In[123]:


# Celda para probar el código
dfp.info()
display(dfp.describe().T) ## .T dataframe transpuesto.
display(dfp.describe(include = ["O"]).T)
display(dfp['moneda'].value_counts())
#type(dfp)


# In[124]:


dfp['moneda'].value_counts()


# In[125]:


dfp['moneda'].value_counts(1)


# In[126]:


## Construir una tabla de frecuencias de la columna modena del dataframe dfp


# ## __5. Guardar un DataFrame en un archivo.__
# 
# Usted puede generar un nuevo archivo .csv a partir de un DataFrame. Para este caso se generará un nuevo archivo que contenga solo los paises que tienen por moneda el dólar con todas las columnas que este tiene definidas.
# 
# Usted puede especificar la codificación y el separador con el cual la función *to_csv(...)* va a construir el nuevo archivo.
# 
# ```Python
# # filtro de DataFrame por moneda
# dfp_ca = dfp[dfp['moneda']== 'Dólar']
# dfp_ca
# # escribiendo archivo
# dfp_ca.to_csv('paises_continte_americano.csv', sep=';',encoding='utf-8')
# ```
# La función *to_csv* reemplazará el archivo y todo el contenido original en caso de que usted deje el mísmo nombre de archivo. 
# 

# In[127]:


get_ipython().system('pwd')


# In[128]:


# Celda de código para probar
# filtro de DataFrame por moneda
dfp_ca = dfp[dfp['moneda']== 'Dólar']
dfp_ca
# escribiendo archivo
dfp_ca.to_csv('datas/paises_continente_americano.csv', sep=';',encoding='utf-8')


# ### Guardar un DataFrame en un archivo .xlsx
# 
# Para guardar un DataFrame en un arhivo de Excel usted debería utilizar la función *to_excel*. Esta permite crear un nuevo archivo el cual contendrá los datos del DataFrame con sus respectivas columnas. Dentro de la función se puede especificar el nombre de hoja.
# 
# Ahora se quiere guardar el archivo **.csv** ('pais.csv') en un solo archivo **.xlsx** con dos hojas separadas para los países de América y Europa.
# 
# ```Python
# dfp[(dfp['c']=='m')].to_excel("DataFramePaises.xlsx", sheet_name='america')
# dfp[(dfp['c']=='e')].to_excel("DataFramePaises.xlsx", sheet_name='europa')
# ```
# Valide el resultado. Usted se podrá dar cuenta que el archivo no contiene las dos hojas. Esto indica que la función *to_excel* no añade la otra hoja, sino que sobreescribe completamente el archivo.
# 

# In[129]:


dfp.columns


# In[130]:


# Celda de código para probar
dfp[(dfp['C']=='m')].to_excel("datas/DataFramePaises.xlsx", sheet_name='america')
dfp[(dfp['C']=='e')].to_excel("datas/DataFramePaises.xlsx", sheet_name='europa')


# En caso de que usted necesite en un solo archivo de Excel añadir más de una hoja y no perder el contenido, usted deberá utilizar la función *ExcelWriter* de pandas. Esta función recibe por argumentos la ruta con el nombre del archivo, y si lo requiere, el modo de uso del archivo.
# 
# ```Python
# # extracción de los primeros 100 registros del DataFrame del archivo base.xlsx - Religion.csv
# dfp1 = dfp.iloc[:101]
# dfp1
# dfp2 = dfp.iloc[101:]
# dfp2
# with pd.ExcelWriter('datas/PaisesTrozos.xlsx') as writer:
#     # añadiendo todo el dataframe
#     dfp.to_excel(writer, sheet_name='t1')
#     # añadiendo los primeros 100 registros.
#     df1.to_excel(writer, sheet_name='t2')
# ```
# Notese que se guarda una porción del dataframe.

# In[131]:


# Celda de código para probar
dfp1 = dfp.iloc[:101]
display(dfp1)
dfp2 = dfp.iloc[101:]
display(dfp2)
with pd.ExcelWriter('datas/PaisesTrozos.xlsx') as writer:
    # añadiendo todo el dataframe
    dfp.to_excel(writer, sheet_name='t1')
    # añadiendo los primeros 100 registros.
    dfp1.to_excel(writer, sheet_name='t2')


# ## Ejercicio en clase
# 
# Con los datos del archivo _examen.xlsx_ genere un archivo de hoja electrónica, en donde en cada hoja queda un profesor con sus respectivos alumnos.

# In[132]:


# Celda de código para probar


# ## _Trabajo de exploración._
# 
# Explorar los datasets disponibles en las librerias de seaborn y plotly. Generar un reporte con los diferentes datasets en donde se pueda apreciar el número de filas y de columnas, las columnas que tiene el dataset y el tipo de dato asociado a cada columna.

# In[133]:


# Celda de código para probar

