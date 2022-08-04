#!/usr/bin/env python
# coding: utf-8

# # Más sobre la libreria `pandas`
# 
# La información vienen comunmente en formatos excel, csv, txt, o quizá esté en alguna url. Aunque estos pueden estar en otro formato (JSON, API'S) nos centraremos en los tres primeros.

# In[1]:


ls -l


# In[2]:


## Librerías requeridas
import numpy as np
import pandas as pd

## pd.set_option('display.max_columns', None) ## Número de columnas máximo a mostrar. 
                                              ## None se reemplaza por el # máximo de columnas.


# In[3]:


## Función .head() muestra los 5 primeros elementos
df_csv = pd.read_csv('datas/downloaded_medals.csv', sep = ",")
df_csv.head()


# In[4]:


df_csv = df_csv.drop(columns=['Unnamed: 0']) ## Borrar columna
df_csv.head()


# In[5]:


## Función .tail() muestra los 5 últimos elementos
df_csv = pd.read_csv('datas/downloaded_medals.csv', index_col=0)
df_csv.tail()


# ## _Archivos excel._

# In[6]:


# Archivos Excel
df_Excel= pd.ExcelFile('datas/downloaded_medals.xls')
df_Excel.sheet_names


# In[7]:


df_Excel = df_Excel.parse("Sheet1")
df_Excel.head()


# # Archivos JSON.

# In[8]:


df_json = pd.read_json("datas/downloaded_medals.json")
df_json.head()


# #### Ejercicio 1
# 
# Importar el archivo `'Winter Olympic Medals.xlsx'` y definir en cada caso un dataframe para cada hoja. Además en cada caso, mostrar su cabeza y su cola.
# 
# **Respuesta:**

# In[9]:


#celda de código para probar.
df_Excel_1 = pd.ExcelFile('datas/Winter Olympic Medals.xlsx')
df_Excel_1.sheet_names


# In[10]:


df_excel = pd.read_excel('datas/Winter Olympic Medals.xlsx', sheet_name=['Data', 'Ranks', 'Sources'])
df_aux = df_excel["Data"]
df_aux.head()


# ## _Desde una URL._
# 

# In[11]:


## Dependerá de donde y como estén los datos.
df_url = pd.read_excel('https://query.data.world/s/zilmgkqzxjhjrfn2pllc4dhikcvrzt')
df_url.head()


# In[12]:


url = "http://winterolympicsmedals.com/medals.csv"
df_url_1 = pd.read_csv(url)
df_url_1.head()


# ## _Información del `dataframe`_
# 

# In[13]:


# Copiamos un dataframe
df = df_url.copy()
df.head()


# In[14]:


## Nombres columnas
df.columns


# In[15]:


## Tipos de datos en el dataframe
df.dtypes


# In[16]:


df.info()


# In[17]:


df.describe().T # df.describe.transpose()


# In[18]:


df = df.rename(columns={"Year":"Año", "Sport":"Deporte", "Country":"País", "Event":"Evento","Gender":"Género","Medal":"Medalla",
                        "Age of Athlete":"Edad_Atleta","Name of Athlete or Team":"Nombre_atleta_o_Equipo"})
df.head()


# ### _Sub dataframes._
# 

# In[19]:


## Serie de pandas
df['Edad_Atleta']


# In[20]:


df['Evento']


# In[21]:


df['Género'].unique()


# In[22]:


subset = df[['Año', 'Deporte', 'Evento']]
subset


# In[23]:


df["Deporte"].value_counts()


# In[24]:


df["Deporte"].value_counts(1,dropna=False)


# In[25]:


df['Género'].value_counts(1,dropna=False)*100


# In[26]:


df.info()


# In[27]:


numeric = ["Edad_Atleta"]
other_features = [x for x in df.columns if x not in numeric] ## list comprehension
other_features


# In[28]:


df_categoric = df[other_features]
df_categoric.head()


# ## `.loc` y `.iloc`
# 
# 
# Si deseamos seleccionar un subdataframe, con registros y columnas particulares podemos hacerlos con estos 2 métodos. `.loc` es la localización en texto (elas columnas) y `.iloc()` será vía indexación numérica.

# In[29]:


df.head()


# In[30]:


df.loc[4] ## Registro 4 de la tabla.


# In[31]:


type(df.loc[4])


# In[32]:


df.loc[:8] ## 8 Primeros registros del dataframe


# In[33]:


df.iloc[10:20] # Registros desde el 11 y hasta el 20


# In[34]:


pares = [i for i in range(len(df['Año'])) if i%2==0]
df.loc[pares]


# In[35]:


impares = [i for i in range(len(df['Año'])) if i%2==1]
df.iloc[impares]


# In[36]:


pd.DataFrame(df.loc[:,"Deporte"])


# In[37]:


df.loc[:,["Deporte","Evento"]]


# In[38]:


for i,j in enumerate(df.columns):
  print((i,j))


# In[39]:


df.iloc[pares,[0,1,7]]


# ## _Máscaras._
# 
# Supongamos que deseamos obtener los regístros que cumplen cierta condición. Por ejemplo, todos aquellos donde el género sea mujer, las personas menores de 30 años, aquellos que ganaron plata, o quizá mujeres que ganaron plata y son menores de 30 años.
# 
# Para hacer esto necesitamos una serie de `pandas` de tipo booleano, que determina que registros cumplen la condición deseada.

# In[40]:


df.head()


# In[41]:


mask = (df['Año'] > 1950)
mask


# In[42]:


## Tenemos todos los registros de quienes ganaron medalla después del Año 1948
df[mask]


# In[43]:


mask_1 = (df['Edad_Atleta'] <= 20)


# In[44]:


menores_de_20 = df[mask_1]
menores_de_20


# In[45]:


menores_de_20.describe().T


# In[46]:


menores_de_20.reset_index()


# In[47]:


menores_de_20.reset_index(drop=True,)


# In[48]:


## Podemos juntar ambas condiciones
menores_ano_cincuenta = df[mask&mask_1]
menores_ano_cincuenta = menores_ano_cincuenta.reset_index(drop=True)
menores_ano_cincuenta.head()


# In[49]:


menores_ano_cincuenta["Medalla"].value_counts()


# In[50]:


df[mask & mask_1]["Medalla"].value_counts()


# In[51]:


mask_2 = df['País'] == "China"
df[mask & mask_1 & mask_2]#["Género"].value_counts()*100


# In[52]:


df[mask & mask_1 & mask_2]["Género"].value_counts()


# In[53]:


df[mask & mask_1 & mask_2]["Género"].value_counts(1)*100


# In[54]:


df[mask|mask_1|mask_2]["Género"].value_counts()


# 
# ## _NaN_
# 
# Suele ocurrir que en nuestro `dataframe` se tengan valores perdidos. Estos deben ser tratados por métodos de imputación que mas adelante discutiremos. Por ahora veremos como eliminarlos o modificarlos.

# In[55]:


df.info()


# In[56]:


df_drop = df.dropna()
df_drop.head()


# In[57]:


df_drop.shape


# In[58]:


df['Edad_Atleta'].isna()


# In[59]:


df[df['Edad_Atleta'].isna()]


# In[60]:


## Podemos obtener la negación de la máscara
df[~(df['Edad_Atleta'].isna())]


# In[61]:


df.info()


# In[62]:


## Todo regístro None o NaN es reemplazado por 0
df.fillna("Alerta!!!")


# In[63]:


df["Edad_Atleta"].fillna(0)


# In[64]:


df["Edad_Atleta_imputado"] = df["Edad_Atleta"].fillna(df["Edad_Atleta"].mean())
df.head(10)


# In[65]:


df['Edad_Atleta'].value_counts(dropna = False)


# In[66]:


df.describe().T


# In[67]:


df_drop.shape


# ## `pandas.crosstab`
# 
# La función `pandas.crosstab` devuelve la tabla de contingencia resultante de cruzar dos o más columnas de un dataframe. Por defecto ell resultado evalúa las frecuencias (absolutas o relativas) de cada combinación de valores, es posible especificar una función de agregación.

# In[68]:


pd.crosstab(df['Género'],df['Medalla'])


# In[69]:


## Podemos obtener la suma por filas y columnas (subtotales) y renombrar esta
pd.crosstab(df['Género'],df['Medalla'], margins=True, margins_name="Total",)


# In[70]:


## Podemos mostrar las frecuencias "normalizadas" (es decir una parte de la unidad). Se puede obtener respecto 
## al total o con respecto a los subtotales de filas o columnas. Asignamos al parámetro normalize el valor True,
## la normalización se realiza con respecto al total de muestras
pd.crosstab(df['Género'],df['Medalla'], normalize=True)


# Del total de las medallas entregadas: 
# 
# 1.   19.8% fueron de bronce y entregas a hombres.
# 2.   12.2% fueron de plata y entregadas a mujeres.
# 
# En cada casilla podemos extraer información similar.
# 

# In[71]:


pd.crosstab(df['Género'],df['Medalla'], normalize=True, margins=True, margins_name= "Total %")


# In[72]:


pd.crosstab(df['Género'],df['País'])


# In[73]:


pais_genero = pd.DataFrame(pd.crosstab(df['Género'],df['País']).unstack()).rename({0:"Conteo"},axis=1)
pais_genero.head(30)


# In[74]:


pais_genero.index


# In[75]:


pais_genero.loc["Belgium"]


# ## _Conclusiones._
# 
# Revisamos el método de importación de archivos en distintios formatos. Además, se vieron varios métodos de consulta de los `dataframe`. Se revisó `pandas.croostab` es una tabla de contingencía generada apartir del `dataframe.`
