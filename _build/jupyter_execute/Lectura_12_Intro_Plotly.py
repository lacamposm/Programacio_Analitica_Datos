#!/usr/bin/env python
# coding: utf-8

# # Introducción a la librería `Plotly`
# 
# **Tema:**
# 
#  * Introducción a la librería: [`Plotly`](https://plotly.com/python/).

# Plotly es en realidad una libreria de `JavaScript`. Es rápido y fácil de implementar gráficas simples. El módulo [`plotly.express`](https://plotly.com/python/plotly-express/) permite producir gráficos profesionales facilmente. Lo más importante, obtienes gráficos interactivos. Además, es el módulo más simple para crear rápidamente gráficos básicos y comunes. También es posible hacer gráficos más personalizados y avanzados con [`plotly.graph_objects`.](https://plotly.com/python-api-reference/generated/plotly.graph_objects.html)
# 
# Finalmente como `Plotly` es extremadamente personalizable, por lo tanto, la documentación debe ser nuestro recurso principal en caso de dudas.

# Una figura de Plotly tiene tres componentes principales.
# 
# 1. `layout`: Es un diccionario de atributos que controlan el aspecto y el estilo del plot. Hay un `layout` por plot.
# 
# 2. `data`. Es una lista de diccionarios que configura el tipo de gráfico (`type`) y los datos que se monstrarán. La combinación de `data` más `type` es una `trace`. Puede tener varios `trace` por plot. 
# 
# 3. `frames` También hay un elemento de marcos que no usaremos veremos en este curso.
# 
# Pruebe el siguiente codigo:
# 
# ```Python
# import plotly.express as px
# import plotly.graph_objects as go
# 
# fig = go.Figure() ## Creamos una Figure
# fig.show()        ## Mostramos la figura.
# ```

# In[1]:


import pandas as pd
import numpy as np
##
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


fig = go.Figure()
fig.show()


# Podemos construir una figura a manera de diccionario.

# In[3]:


ventas_mensuales = dict(data = [{'type': 'bar', 'x': ['Jan', 'Feb', 'March'], 'y': [450, 475, 400]}],
                        layout = {'title':{"text":"Ventas de enero-marzo de 2022",
                                           "font":{"color":"rgb(2,255,6)"}}})
##
fig = go.Figure(ventas_mensuales)
fig.show()


# ## _Gráfica univariadas en Plotly._
# 
# 
# No vamos a crear figuras desde un diccionario, en su lugar, aprovecharemos los potentes módulos de accesos directos de Plotly. 
# 
# 1. `plotly express` permite crear gráficos rápidos y sencillos especificando un DataFrame y usando sus nombres de columna como argumentos. Recordemos que las gráficas univariadas incluyen: barplots, histogramas, box-plots y density plots.

# ### ***Barplots***
# 
# Considere el siguiente ejemplo:
# 
# ```python
# import pandas as pd
# weekly_temps = pd.DataFrame({'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
#                              'temp': [28, 27, 25, 31, 32, 35, 36]})
# fig = px.bar(data_frame=weekly_temps, x='day', y='temp')
# fig.show()
# ```
# 
# 
# 5. Gráficos de barras con plotly.express
# Reconstruyamos la trama de la última lección usando plotly express. Cuando se usa plotly express, es una convención importar como px. Aquí está el DataFrame utilizado. Creamos un objeto de figura usando la barra de puntos px. Los argumentos principales son el marco de datos que contiene los datos y qué columnas de ese marco de datos se asignan al eje x y al eje y. Finalmente mostramos la trama.
# 
# 6. Histogramas
# Si bien un histograma puede parecer un gráfico de barras, tiene algunas diferencias clave. Cada columna, llamada contenedor, representa un rango de valores que las muestras podrían tener para una variable en particular. La altura de cada barra suele ser el recuento de cuántas muestras cayeron dentro de ese rango, aunque son posibles otras agregaciones. Puede elegir los contenedores usted mismo o hacer que Plotly elija los contenedores por usted.

# In[4]:


weekly_temps = pd.DataFrame({'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                             'temp': [28, 27, 25, 31, 32, 35, 36]})
fig = px.bar(data_frame=weekly_temps, x='day', y='temp')
fig.show()


# En el plot anterior tenemos un barplot, puede ir a la [documentación](https://plotly.com/python-api-reference/generated/plotly.express.bar) para mayor ampliación.

# ### [***Histogramas.***](https://plotly.github.io/plotly.py-docs/generated/plotly.express.histogram.html)

# La tabla de datos `penguins.csv` contiene información y medidas sobre tres clases de pinguinos. Se hará uso seguido de esta tabla para los ejemplos y ejercicios. Importela con las siguientes líneas de código.
# 
# ```python
# penguins = pd.read_csv("datas/data_plotly/penguins.csv", index_col=0)
# penguins.reset_index(drop=True,inplace=True)
# ```

# In[5]:


## Celda de código para probar.
penguins = pd.read_csv("datas/data_plotly/penguins.csv", index_col=0)
penguins.reset_index(drop=True,inplace=True)


# Realizar un histograma con `plotly.express` es bastante simple.
# 
# ```python
# fig = px.histogram(data_frame = penguins, x = 'Body Mass (g)', nbins = 10)
# fig.show()
# ```

# In[6]:


## Celda de código para probar.
fig = px.histogram(data_frame = penguins, x = 'Body Mass (g)', nbins = 10)
fig.show()


# ### [***Box-plot.***](https://plotly.github.io/plotly.py-docs/generated/plotly.express.box.html)

# In[7]:


## Celda de código para probar
fig = px.box(data_frame=penguins, x="Flipper Length (mm)")
fig.show()


# #### _Ejercicio 1:_
# 
# Construya un DataFrame llamado `notas` que tenga 2 columnas, una con nombres de 5 estudiantes y la otra con sus respectivas notas definitivas de la asignatura. Seguido realice un barplot de los nombres contra su respectiva calificación.
# 
# ### _Respuesta:_

# In[8]:


notas = pd.DataFrame({"estudiante":["Luisa","Camila","Felix","Carlos","Alejandra"],
                      "calificación":[4.3,5,3.7,3.0,4.1]}) 
##
fig = px.bar(data_frame = notas, x = "estudiante",y = "calificación")
fig.show()


# ##### _Ejercicio 2:_
# 
# Ha sido contratado por una empresa de la bolsa de valores de New York que está interesada en mejorar sus capacidades de visualización de datos.
# 
# Debe generar un plot para la distribución de los ingresos de las principales empresas en los Estados Unidos. Están particularmente interesados ​​en qué tipo de ingresos lo colocan en el 'soporte superior' de las empresas.
# 
# También se desea saber si hay valores atípicos y que se muestren en el plot. Vamos a considerar el DataFrame `revenues`.
# 
# 1. Importe y explore un poco el DataFrameExamine 
# 
# 2. Crear un box-plot.
# 
# 3. Establezca `hover_data` para mostrar el nombre de la empresa correspondiente.
# 
# Para importar la tabla siga este código:
# ```python
# revenues = pd.read_csv("datas/data_plotly/revenue_data.csv")
# display(revenues.head())
# ```

# In[9]:


## Celda de código para probar.
revenues = pd.read_csv("datas/data_plotly/revenue_data.csv")
display(revenues.head())
##
fig = px.box(data_frame=revenues, y="Revenue", hover_data=["Company"])
fig.show()


# #### _Ejercicio 3._
# 
# Continuando con el ejercicio anterior, se quiere entender un poco más la distribución de los datos. ¿Hay muchas empresas con menores ingresos o mayores ingresos? ¿Tiene algo de forma de campana o está sesgado hacia ingresos más altos o más bajos?.
# 
# Cree un histograma con el DataFrame del ejecicio anterior para buscar responder la pregunta.

# In[10]:


fig = px.histogram(data_frame = revenues, x = "Revenue", nbins = 5)
fig.show()


# El equipo de inversión puede ver claramente cómo los datos están sesgados hacia menores ingresos. La mayoría de las empresas caen en el primer bin.

# ## _Personalización del `color`_
# 
# 
# La personalización en plotly se puede lograr de varias formas.
# 
# 1. Cuando se crea el plot si hay un argumento interesante disponible (`color`). 
# 
# 2. `update_layout` Toma un diccionario como argumento, especificando los elementos de diseño que se actualizarán. Por ejemplo, actualizar el texto del título. La forma en que realice la personalización depende de cómo cree el plot y de lo que se desea informar.
# 
# 

# ### _`color`_
# 
# Personalizar el color de los plot es un método poderoso que puede ayudar a cumplir con fines estéticos y estilísticos. Además de transmitir información con fines analíticos. 
# 
# En `plotly.express` muchos plots tienen un argumento de color. Ojo, no el color en sí. A cada categoría de una columna se le asigna automáticamente un color. Se crea una escala de colores si especifica una columna numérica. 
# 
# Considere el siguiente código:
# 
# ```Python
# notas["ciudad"] = ["Armenia","Cali","Bogotá","Cali","Bogotá"]
# fig = px.bar(data_frame = notas, x='estudiante', y='calificación',
#              title='Calificación estudiantes con ciudad.',color='ciudad')
# fig.show()
# ```
# 
# 

# In[11]:


notas["ciudad"] = ["Armenia","Cali","Bogotá","Cali","Bogotá"]
fig = px.bar(data_frame = notas, x='estudiante', y='calificación',
             title='Calificación estudiantes con ciudad.',color='ciudad')
fig.show()


# Al plot anterior agregamos `color` y cada ciudad es de un color diferente. Los colores se eligen automaticamente.

# ### _Colores específicos en plotly.express._
# 
# Supongamos que no deseamos los colores predeterminados en las barras anteriores. El argumento, `color_discrete_map` es un diccionario que mapea valores categóricos a colores. Así, podemos pasar para las distintas ciudades nuestros colores pensonalizados.
# 

# Finalmente, es posible que se desee tener una escala de colores basada en una columna numérica. El argumento `color_continuous_scale` nos permite hacer esto con escalas de color integradas o construidas.
# 
# Considere el siguiente código:
# 
# ```Python
# notas["temp_ciudad"] = np.array([24.5,28.0,28.0,17,17])
# ##
# fig = px.bar(data_frame = notas, x='estudiante', y='calificación', 
#              color='temp_ciudad', color_continuous_scale= ["yellow","orange","red"])
# fig.show()
# ```

# In[12]:


## Celda código para probar.
notas["temp_ciudad"] = np.array([24.5,28.0,28.0,17,17])
##
fig = px.bar(data_frame = notas, x='estudiante', y='calificación', 
             color='temp_ciudad', color_continuous_scale= ["yellow","orange","red"])
fig.show()


# #### ***Ejercicio 4.***
# 
# La Bolsa de Valores de New York lo contrató nuevamente para la construcción de un box-plot de los ingresos de la empresa.
# 
# Se desea comparar las diferentes industrias usando unos colores específicos para cada una.
# 
# Realice un box-plot con la solicitud realizada, busque colores adecuados según la industria.
# 
# Importe la nueva tabla con el siguiente código:
# 
# ```Python
# revenues2 = pd.read_csv("datas/data_plotly/revenue_data2.csv")
# revenues2["Revenue"] = [float(x) if x != "Unknown"  else np.nan for x in revenues2["Revenue"]]
# ```
# 
# **Hint:** Haga uso del parámetro `color_discrete_map`

# In[13]:


revenues2 = pd.read_csv("datas/data_plotly/revenue_data2.csv")
revenues2["Revenue"] = [float(x) if x != "Unknown"  else np.nan for x in revenues2["Revenue"]]


# In[14]:


cate_color_map = {"Tech": 'green','Oil': "black", 'Pharmaceuticals': 'skyblue',
                  "Professional Services" : "red"}
##
fig = px.box(data_frame = revenues2, y = "Revenue", color_discrete_map = cate_color_map,
             color='Industry')
fig.show()


# #### _Ejercicio 5._
# 
# La firma de la bolsa de valores de New York pensó que un histograma brinda una gran perspectiva sobre cómo se distribuyen los ingresos de las firmas que están analizando.
# 
# Debe construir un histograma incluyendo según las industrias. Use los mismos colores del plot anterior.

# In[15]:


## Celda de código para probar.
fig = px.histogram(data_frame = revenues2, x = "Revenue", nbins = 5, color_discrete_map = cate_color_map,
                   color='Industry')
fig.show()


# Muchas de las empresas `Unknwown` se encuentran en el extremo inferior, y `Professional Services`no está realmente presente más allá del bin de 200k. Los dos contenedores más altos están compuestos solo por `tech`.

# ## ***Visualizaciones bivariadas.***
# 
# 
# Los gráficos bivariados muestran y permiten la comparación de dos variables o dos atributos de una muestra. Tenemos tres tipos de plot para estas relaciones.
# 
# ### ***Scatter plot***
# 
# Con `plotly.express` crearemos un scatter plot de la masa corporal y la longitud de las aletas del dataset `penguins`. 
# 
# Considere el siguiente código:
# 
# ```python
# fig = px.scatter(data_frame = penguins, x = "Body Mass (g)", y = "Flipper Length (mm)")
# fig.show()
# ```
# 
# 

# In[16]:


## Celda de código para probar.
fig = px.scatter(data_frame = penguins, x = "Body Mass (g)", y = "Flipper Length (mm)")
fig.show()


# Consulte la [documentación](https://plotly.com/python-api-reference/generated/plotly.express.scatter) para obtener más información.
# 
# 

# ### _Lineplots en plotly.express._
# 
# Un lineplot es una visualización típica para trazar alguna variable a lo largo del tiempo. 
# 
# 
# Podemos crear un gráfico de líneas del precio mensual de las acciones de Microsoft durante los últimos 5 años utilizando `plotly.express`. Considere el siguiente código:
# 
# ```Python
# life_gdp = px.data.gapminder()
# df = life_gdp.query("country=='Canada'")
# fig = px.line(df, x="year", y="lifeExp", title='Esperanza de vida en Life expectancy in Canada')
# fig.show()
# ```

# In[17]:


## Celda de código para probar.
life_gdp = px.data.gapminder()
df = life_gdp.query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Esperanza de vida en Life expectancy in Canada')
fig.show()


# ### _Scatter y lines plots con `graph_objects`_
# 
# Considere los siguientes 2 ejemplos:
# 
# ```Python
# ## Ejemplo 1.
# fig = go.Figure(go.Scatter(x = penguins['Body Mass (g)'],y = penguins['Flipper Length (mm)'], mode = 'markers'))
# fig = go.Figure(go.Scatter(x = msft_stock['Date'], y = msft_stock['Opening Stock Price'],mode = 'lines'))
# ## Ejemplo 2.
# df = px.data.gapminder().query("country=='Canada'")
# fig = go.Figure(go.Scatter(x = df["year"], y = df["lifeExp"],mode = 'lines'))
# fig.show()
# ```
# 
# Tenga en cuenta que `graph_objects` requiere subconjuntos de columnas DataFrame reales en lugar de solo nombres de columnas.

# In[18]:


## Celda de código para probar.
fig = go.Figure(go.Scatter(x = penguins['Body Mass (g)'],y = penguins['Flipper Length (mm)'], 
                           mode = 'markers'))
fig.show()


# In[19]:


df = px.data.gapminder().query("country=='Canada'")
fig = go.Figure(go.Scatter(x = df["year"], y = df["lifeExp"],mode = 'lines'))
fig.show()


# #### _Ejercicio 5._
# 
# Haga uso del DataFrame `penguins`.
# 
# 1. Cree el siguiente diccionario:
# 
# ```Python
# color_map = {'Adelie': 'rgb(235, 52, 52)' , 'Gentoo': 'rgb(235, 149, 52)', 'Chinstrap': 'rgb(67, 52, 235)'}
# ```
# 
# Este un diccionario para asignar colores particulares a las clases de pinguinos.
# 
# 2. Cree un scatterplot con `px`  visualizando las características de `Culmen Length (mm)` y `Culmen Depth (mm)` por especie en el mismo plot.
# 
# 3. Establezca el parámetro adecuado para hacer uso de la personalización de colores.

# #### _Ejercicio 5._
# 
# Como analista de datos, un grupo de científicos investigadores de la Antártida lo contrató para ayudarlos a explorar e informar sobre su trabajo.
# 
# El grupo se pregunta si puede ayudarlos a trazar sus datos en relación con las estadísticas sobre los atributos corporales de los pingüinos. También sospechan que existe algún patrón relacionado con las especies, pero no están seguros de cómo trazar este elemento adicional.
# 
# Debe crear un scatterplot con colores personalizados por especie y enfrentar las varibles `Culmen Length (mm)` en el eje $x$ y `Culmen Depth (mm)` en el eje $y$.

# In[20]:


## Celda de código para probar.
color_map = {'Adelie': 'rgb(235,52,52)', "Gentoo": 'rgb(235,149,52)','Chinstrap': 'rgb(67,52,235)'}
##
fig = px.scatter(data_frame = penguins, title="Penguin Culmen Statistics", x = 'Culmen Length (mm)',
                 y='Culmen Depth (mm)', color='Species', color_discrete_map = color_map,)
fig.show()


# In[21]:


## Celda de código para probar.
color_map = {'Adelie': 'rgb(235, 52, 52)' , 'Gentoo': 'rgb(235, 149, 52)', 'Chinstrap': 'rgb(67, 52, 235)'}
fig = px.scatter(data_frame = penguins, title = "Penguin Culmen Statistics", x="Culmen Length (mm)",
                 y="Culmen Depth (mm)", color = "Species", color_discrete_map = color_map,
                 )
fig.show()


# Parece que hay una relación entre estas dos variables, y con el mapa de colores de especies agregado, hay agrupaciones claras en los datos. Esta será una gran herramienta para los científicos. ¡Veamos si podemos agregar más valor a su trabajo usando otras parcelas!

# ### `graph_objects` vs `plotly.express`
# 
# 
# Entonces, ¿cuándo usas cada libreria? En gran parte se trata de personalización. Ambos tienen mucho que ofrecer, aunque `graph_objects` hace menos automáticamente y tiene más opciones de personalización, 
# 
# ### ***plot de correlación***
# 
# Recuerde de su curso de estadística la correlación de Person, es decir, la relación lineal entre dos variables numéricas. Pruebe el siguiente código:
# 
# ```python
# penguin_corr = penguins.corr(method='pearson')
# fig = go.Figure(go.Heatmap(
#         z=penguin_corr.values.tolist(),
#         x=penguin_corr.columns,
#         y=penguin_corr.columns,
#         colorscale='rdylgn'))
# fig.show()
# ```
# 
# 

# In[22]:


## Celda de código para probar.
penguin_corr = penguins.corr(method='pearson')
fig = go.Figure(go.Heatmap(
        z=penguin_corr.values.tolist(),
        x=penguin_corr.columns,
        y=penguin_corr.columns,
        colorscale='rdylgn',
        zmin=-1, zmax=1))
fig.show()


# ¡Trabajo fantástico! A los científicos les resultará muy interesante ver qué atributos se correlacionan positiva y negativamente entre sí. Esta fue una visualización más creativa y compleja, pero muy común y útil para el trabajo de ciencia de datos. ¡Aprovechemos sus habilidades de trazado aprendiendo una personalización más avanzada!

# ## _Personalización de información flotante y leyendas_
# 
# La información flotante es lo que aparece cuando el mouse pasa sobre un punto de datos en una visualización de Plotly. De forma predeterminada, el estilo flotante es el 'más cercano' (`hovermode=closest` )visto en los gráficos hasta el momento. 
# 
# Usando `plotly.express` el argumento `hover_name` se utiliza tomando una columna específica que aparecerá en negrita en la parte superior del cuadro flotante. `hover_data` es una lista de nombres de columnas o un diccionario para incluir/excluir columnas. 
# 
# Considere el siguiente código:
# 
# ```Python
# ## Pruebe primero uno y luego el otro compare.
# fig = px.scatter(data_frame = revenues2, x = "Revenue",y="employees", hover_data = ['age'],
#                  hover_name = "Industry")
# fig.show()
# ##
# fig = px.scatter(data_frame = revenues2, x = "Revenue",y="employees", hover_data = 
#                  {"age":True,"Revenue":False}
#                  )
# fig.show()
# ```
# 
# Note que `age` no estará en la visualización en sí, pero veremos `age` en el desplazamiento.

# In[23]:


revenues2["employees"] = [float(x.replace(",","")) for x in revenues2["employees"]]
fig = px.scatter(data_frame = revenues2, x = "Revenue",y="employees", hover_data = ['age'],
                 hover_name = "Industry")
fig.show()


# In[24]:


## Celda de código para probar
fig = px.scatter(data_frame = revenues2, x = "Revenue",y="employees", hover_data = 
                 {"age":True,"Revenue":False}
                 )
fig.show()


# ### _Estilo de la información flotante._
# 
# La información flotante se puede personalizar mediante el elemento de diseño `hoverlabel`, que es un diccionario que especifica muchas propiedades estilísticas siendo este un elemento del `layout`.
# 
# 

# ## `legend`
# 
# 
# Otra personalización es una leyenda (legend). Una leyenda es un cuadro de información que proporciona una clave para los elementos dentro del plot. Con Plotly, aparecerá automáticamente una leyenda al especificar argumentos que crean elementos que lo requieren. 
# 
# Puede activar y diseñar la leyenda usamos `update_layout()`. El argumento `showlegend = True` mostrará una leyenda con estilo y posición predeterminados (arriba, justo fuera del gráfico). 
# 
# El argumento `legend` es un diccionario que especifica el estilo y la posición de la leyenda. Los argumentos x e y son 0-1 flotantes que establecen el porcentaje en estos ejes para colocar la leyenda. Hay muchos otros elementos estilísticos como bgcolor (color de fondo), ancho de borde, título y fuente.
# 
# Considere el siguiente ejemplo:
# 
# ```python
# fig = px.scatter(data_frame = revenues2, x = "Revenue",y = "employees", color = "Industry")
# fig.update_layout({'showlegend': True, 'legend': {'title': 'Todas las compañias', 'x': 0.5, 
#                                                   'y': 0.8,'bgcolor': 'rgb(246,228,129)'}})
# fig.show()
# ```
# 
# 

# In[25]:


## Celda de código para probar.
fig = px.scatter(data_frame = revenues2, x = "Revenue",y = "employees", color = "Industry")
fig.update_layout({'showlegend': True, 'legend': {'title': 'Todas las compañias', 'x': 0.5, 
                                                  'y': 0.8,'bgcolor': 'rgb(246,228,129)'}})
fig.show()


# #### _Ejemplo 1._
# 
# Vamos a considerar el dataset `gapminder`, se desea comprender la relación (si existe) entre el `gdpPercap` y la esperanza de vida (`lifeExp`). Vamos a crear una leyenda clara para una mejor compresión de la información.
# 
# Crearemos un scatter plot y una leyenda mediante el siguiente código:
# 
# ```Python
# life_gdp = px.data.gapminder()
# fig = px.scatter(data_frame = life_gdp, x = "lifeExp", y = "gdpPercap", color = 'continent')
# my_legend = {'x': 0.2, 'y': 0.95, 'bgcolor': 'rgb(60, 240, 201)', 'borderwidth': 5}
# fig.update_layout({'showlegend': True, 'legend': my_legend})
# fig.show()
# ```

# In[26]:


## Celda de código para probar.
fig = px.scatter(data_frame = life_gdp, x = "lifeExp", y = "gdpPercap", color = 'continent')
my_legend = {'x': 0.2, 'y': 0.95, 'bgcolor': 'rgb(60, 240, 201)', 'borderwidth': 5}
fig.update_layout({'showlegend': True, 'legend': my_legend})
fig.show()


# #### _Ejercicio 6._
# 
# Mejore el plot del ejemplo anterior incluyendo más información en el cursor y darle estilo.
# 
# Agregue las columnas de `continent`, `lifeExp`, `gdpPercap`, además establezca `country` para que aparezca en la parte superior de la información flotante.

# In[27]:


## Celda de código para probar.
fig = px.scatter(data_frame = life_gdp, x = "lifeExp", y = "gdpPercap", color='continent',
                 hover_data=["continent", "lifeExp", "gdpPercap"],
                 hover_name='country')
fig.show()


# ## _Agregar anotaciones._
# 
# 
# 
# Las anotaciones son cuadros adicionales de texto y datos que se agregan a un plot. Siempre están presentes. Estos tienen dos propósitos principales:
# 
# 1. Es posible que desee llamar la atención o agregar notas sobre un punto de datos en particular. 
# 
# 2. Puede que desee agregar un cuadro de texto con variables y texto, como un cuadro de texto en Microsoft Word.
# 
# En Plotly puedes agregar anotaciones de varias maneras.
#   
#   a.) Existe el método `add_annotation()` para agregar una sola anotación. 
# 
#   b.) También puede usar el método `update_layout()` junto con el argumento `annotations`. Esta es una lista de objetos de anotación, por lo que este método es útil para agregar múltiples anotaciones. Acá, vamos a trabajar con `update_layout()`.
# 
# 

# ### ***Anotación importantes***
# 
# Hay algunos argumentos clave de un objeto de anotación, un diccionario, que vale la pena mencionar. 
# 
# 1. El argumento booleano `showarrow` determina si se agrega una flecha para apuntar a un punto de datos en particular. Sin esto, solo tienes un cuadro de texto. La flecha también se puede diseñar. 
# 
# 2. El argumento de `text` es el texto real que se mostrará. Al ser un `string` de `Python`, también puede insertar variables aquí. 
# 
# 3. Los argumentos `x` e `y` son coordenadas que posicionan la anotación. Estos pueden estar vinculados a un punto de datos o absolutamente en el gráfico, como un cuadro de texto en Microsoft Word. 
# 
# !Tenga cuidado de colocar anotaciones absolutamente como si sus datos cambiaran, pueden superponerse. Veremos cómo especificar el posicionamiento en ambos sentidos!

# ### ***Anotaciones de posicionamiento.***
# 
# De forma predeterminada, los argumentos `x` e `y` estarán en las unidades del gráfico. También puede posicionar de forma absoluta configurando los argumentos `xref` e `yref` en `paper`papel. Luego, los argumentos `x` e `y` están entre 0 y 1 y representan el porcentaje a lo largo de ese eje para colocar la anotación. No está vinculado a un punto x-y en particular. Por ejemplo, establecer `x` e `y` en el punto 0.5 con este método estaría justo en el centro del plot.

# Considere el siguiente código:
# 
# ```python
# temp = life_gdp.groupby("country", as_index = False)[["lifeExp","gdpPercap"]].mean()
# temp1 = life_gdp[["continent", "country"]].drop_duplicates()
# data_plot = temp.merge(temp1, on = "country", how = "left")
# ##
# fig = px.scatter(data_frame = data_plot, x = "lifeExp", y = "gdpPercap", color='continent',
#                  hover_data=["continent", "lifeExp", "gdpPercap"],
#                  hover_name='country', title = "Promedios: Esperanza de vida vs.Ingreso Percapita.")
# ##
# higt_annotation = {'x': 68.9, 'y': 66000, 'showarrow': True, 'arrowhead': 4,
#                     'font': {'color': 'black'}, 'text': "Altisima calidad vida!"}
# ##
# low_annotation = {'x': 36.7, 'y': 1672, 'showarrow': True, 'arrowhead': 4,
#                     'font': {'color': 'green'}, 'text': "Menor esperanza de vida!"}
# fig.update_layout({'annotations': [higt_annotation, low_annotation]})
# fig.show()
# ```

# In[28]:


## Celda de código para probar.
temp = life_gdp.groupby("country", as_index = False)[["lifeExp","gdpPercap"]].mean()
temp1 = life_gdp[["continent", "country"]].drop_duplicates()
data_plot = temp.merge(temp1, on = "country", how = "left")
##
fig = px.scatter(data_frame = data_plot, x = "lifeExp", y = "gdpPercap", color='continent',
                 hover_data=["continent", "lifeExp", "gdpPercap"],
                 hover_name='country', title = "Promedios: Esperanza de vida vs.Ingreso Percapita.")
##
higt_annotation = {'x': 68.9, 'y': 66000, 'showarrow': True, 'arrowhead': 4,
                    'font': {'color': 'black'}, 'text': "Altisima calidad de vida!"}
##
low_annotation = {'x': 36.7, 'y': 1672, 'showarrow': True, 'arrowhead': 4,
                    'font': {'color': 'green'}, 'text': "Menor esperanza de vida!"}
fig.update_layout({'annotations': [higt_annotation, low_annotation]})
fig.show()


# El siguiente código adiciona un mensaje positivo:
# 
# ```python
# today = "Viernes!!!"
# ## Mensaje 
# message_annotation = {'x': 0.5, 'y': 0.95, 'xref': 'paper', 'yref': 'paper',
#                       'text': f'Por fin... {today} :)',
#                       'font': {'size': 20, 'color': 'white'},
#                       'bgcolor': 'rgb(237, 64, 200)',
#                       'showarrow': False}
# fig.update_layout({'annotations': [message_annotation]})
# fig.show()
# ```

# In[29]:


today = "Viernes!!!"
## Mensaje 
message_annotation = {'x': 0.5, 'y': 0.95, 'xref': 'paper', 'yref': 'paper',
                      'text': f'Por fin... {today} :)',
                      'font': {'size': 20, 'color': 'white', 'family':'italic'},
                      'bgcolor': 'rgb(237, 64, 200)',
                      'showarrow': False}
fig.update_layout({'annotations': [message_annotation]})
fig.show()


# ## ***Edición de los ejes del plot.*** 
# 
# Vamos a considerar el DataFrame `penguins`, sobre él, vamos a encontrar el promedio del tamaño de sus aletas por especie.
# 
# ```Python
# penguin_flippers = penguins.groupby(by = "Species", as_index = False)['Flipper Length (mm)'].mean()
# 
# ```
# 
# 

# In[30]:


## Celda de código para probar.
penguin_flippers = penguins.groupby(by = "Species", as_index = False)['Flipper Length (mm)'].mean()


# Supongamos que deseamos presentar la información del plot: 
# 
# ```python
# fig = px.bar(penguin_flippers, x = 'Species', y = 'Flipper Length (mm)')
# fig.show()
# ```
# 
# en español.
# 
# 

# In[31]:


## Celda de código para probar.
fig = px.bar(penguin_flippers, x = 'Species', y = 'Flipper Length (mm)')
fig.show()


# 
# ### _Edición de los títulos de los ejes_
# 
# Este método abreviado utiliza `update_xaxes()` y `update_yaxes()`. El argumento `title_text` establece lo que queremos que aparezca en cada eje. 
# 
# 
# ```Python
# fig.update_xaxes(title_text = "Especies")
# fig.update_yaxes(title_text = "Longitud promedio aleta")
# ```

# In[32]:


## Celda de código para probar.
fig.update_xaxes(title_text = "Especies")
fig.update_yaxes(title_text = "Longitud promedio aleta")


# Podríamos también usar el método general `update_layout()` y pasar un diccionario apropiado que mapee qué elementos de diseño actualizar. 
# 
# ```python
# fig.update_layout({'xaxis': {'title': {'text': 'Especies'}},
#                    'yaxis': {'title':{'text': "Longitud promedio aleta"}}
#                    }
#                   )
# ```

# In[33]:


## Celda de código para probar.
fig.update_layout({'xaxis': {'title': {'text': 'Especies'}},
                   'yaxis': {'title':{'text': "Longitud promedio aleta"}}
                   }
                  )


# 
# ####  _Edición de rangos de ejes._
# 
# A veces, es posible que desee obligar a usar un rango específico para los ejes, en lugar de un rango automático. 
# 
# Con el siguiente código:
# 
# ```Python
# fig.update_layout({'yaxis':{'range' : 
#                             [150, penguin_flippers["Flipper Length (mm)"].max() + 30]
#                             }
#                    }
#                   )
# ```

# In[34]:


## Celda de código para probar.
fig.update_layout({'yaxis':{'range' : 
                            [150, penguin_flippers["Flipper Length (mm)"].max() + 30]
                            }
                   }
                  )


# Ahora se observa de manera más detallada la diferencia entre las distintas categorías.

# ## _Subplots._
# 
# Los subplots son como miniplots colocados en un arreglo de cuadrícula. Son útiles para mostrar diferentes tipos de gráficos para los mismos datos, o el mismo tipo de plot con diferente data.
# 
# 
# El arreglo se realiza pensando como un arreglo rectangular, puede tener 4 plots dispuestos en una cuadrícula de 2x2 , debe tener cuidado, con cada adición que hace los plots serán mas pequeños.
# 
# Recordemos que las `traces` son conformadas por un set de datos más el `type` de gráfico. Es posible construir plots con varias `traces`, para esto de debe usar `fig.add_trace(X)` donde es un `graph_objects`.
# 
# ### `graph_objects (go) vs plotly.express (px)`
# 
# 
# Cuando se hace uso de `add_trace()`, podemos usar plots de `px`, pero es más complejo y no es la mejor práctica, luego, usaremos plots de `go` cada vez que usemos `add_trace()`. Siempre tenga en mente consultar la documentación de ser necesario.
# 
# ### _Creando un subplot de 1x2_
# 
# Considere el siguiente ejemplo:
# 
# ```Python
# from plotly.subplots import make_subplots
# fig = make_subplots(rows=2, cols=1)
# fig.add_trace(go.Histogram(x = revenues['Revenue'], nbinsx = 5), row=1, col=1)
# fig.add_trace(go.Box(x = revenues['Revenue'],  hovertext = revenues['Company']), row = 2, col = 1)
# fig.show()
# ```
# 

# In[35]:


## Celda de código para probar.
from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=1)
fig.add_trace(go.Histogram(x = revenues['Revenue'], nbinsx = 5), row=1, col=1)
fig.add_trace(go.Box(x = revenues['Revenue'],  hovertext = revenues['Company']), row = 2, col = 1)
fig.show()


# Se construyó un histograma la variable `Revenue` y así mismo un box-plot.
# 
# 

# ### _Personalización de los subplots._
# 
# Note en el plot anterior no hay título general y en las leyendas se tiene 'trace 1' y 'trace 2', es deseable cambiar alguno o ambos de estos aspectos.
# 
# #### _Títulos de los subplots._
# 
# Considere el siguiente código:
# 
# ```Python
# from plotly.subplots import make_subplots
# fig = make_subplots(rows=2, cols=1, subplot_titles=['Histogram of company revenues', 'Box plot of company revenues'])
# fig.add_trace(go.Histogram(x = revenues['Revenue'], nbinsx = 5), row=1, col=1)
# fig.add_trace(go.Box(x = revenues['Revenue'],  hovertext = revenues['Company']), row = 2, col = 1)
# fig.update_layout({'title': {'text':'Plots of company revenues', 'x': 0.5, 'y': 0.9}})
# fig.show()
# ```

# In[36]:


from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=1, 
                    subplot_titles=['Histograma ingresos empresa','Box-plot ingresos empresa'])
##
fig.add_trace(go.Histogram(x=revenues['Revenue'],nbinsx = 5),row=1,col=1)
fig.add_trace(go.Box(x = revenues['Revenue'],  hovertext=revenues['Company']), row=2, col=1)
fig.update_layout({'title': {'text':'Plots de ingresos de la empresa.', 'x': 0.1, 'y': 0.95,}})
fig.show()


# Agregamos un título pricipal así como para los subplots.

# ### _Leyendas de los plots._
# 
# Podemos arreglar fácilmente los nombres de las leyendas, basta con agregar el parámetro `name` cuando se crean las `traces`.
# 
# ```Python
# ```

# In[37]:


## Celda de código para probar.


# ### _Subplots apilados._
# 
# Considere el sigueinte ejemplo:
# 
# ```Python
# fig = make_subplots(rows=3, cols=1)
# row_num = 1
# for species in penguins['Species'].unique():
#     df = penguins[penguins['Species'] == species]
#     fig.add_trace(go.Scatter(x = df['Culmen Length (mm)'], y = df['Culmen Depth (mm)'], name = species, 
#                              mode = 'markers'), row = row_num, col = 1)
#     row_num +=1
# fig.show()
# ```
# 
# Le parece que todo funciona bien con los ejes?

# In[38]:


## Celda de código par probar.
fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
row_num = 1
for species in penguins['Species'].unique():
    df = penguins[penguins['Species'] == species]
    fig.add_trace(go.Scatter(x = df['Culmen Length (mm)'], y = df['Culmen Depth (mm)'], name = species, 
                             mode = 'markers'), row = row_num, col = 1)
    row_num +=1
fig.show()


# Para solucionar el problema de los ejes dispares, agregue el parámetro `shared_xaxes=True`,con ello se puede ver claramente la diferecnia por especie.

# #### _Ejercicio 8._
# 
# Haciendo uso del DataFrame `renueves2`, se desea comprender la distribución de cada industria sin tener que desplazarse para ver. Para ello, debe crear un histograma de los ingresos de la empresa (`Revenue`) por industria como un subplot apilado y con el eje $x$ compartido para permitir una comparación significativa de las industrias.
# 
# Puede seguir estos si lo desea:
# 
# 1. Crear una la cuadrícula de subplots con 3 filas y 1 columna que compartan el eje $x$.
# 2. Via un ciclo `for` recorra las industrias deseadas, agregando en cada paso un histograma con el nombre de la industria.

# In[39]:


## Celda de código para probar.
fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
row_num = 1
for industry in ['Tech', 'Retail', 'Professional Services']:
    df = revenues2[revenues2.Industry == industry]
    fig.add_trace(go.Histogram(x=df['Revenue'], name=industry),row=row_num, col=1)
    row_num +=1
fig.show()


# ## _Superposición de varios plots_
# 
# Superponer plots, a diferencia de los subplots, sucede cuando superponemos varios plots, todas dentro del mismo plot. No tenemos cada plot en una ubicación de la cuadrícula separada (o parcela separada).
# 
# Para crear esto, usamos `add_trace()`, no lo vamos a usar, pero existe gran variedad de funciones como `add_bar()`, `add_area()`, `add_box()`, etc. La domentación será su ayuda.
# 
# La superposición de gráficos es útil por una variedad de razones, tales como: Acceder a más opciones de personalización. Por ejemplo, podríamos usar `add_trace()` para agregar y dar formato a gráficos de líneas múltiples, en lugar de simplemente establecer el argumento de color como antes. Al mostrar tipos de gráficos complementarios sin desorden, los diferentes tipos de gráficos también pueden dirigir la atención en comparación con todos los datos que usan el mismo tipo de gráfico. Además, la superposición mantienen las visualizaciones ajustadas para comparaciones cercanas en comparación con subplots divididas o subplots separados.
# 
# Considere el ejemplo:
# 
# ```Python
# data_filter = life_gdp.loc[(life_gdp["country"]== "Australia")]
# fig = go.Figure()
# fig.add_trace(go.Bar(x = data_filter['year'], y = data_filter["lifeExp"], name="Cantidad de Población"))
# fig.add_trace(go.Scatter(x = data_filter['year'], y = data_filter["lifeExp"],
#                          name = "Población linea temporal", mode = "lines+markers"))
# fig.show()
# ```

# In[40]:


## Celda de código para probar.
data_filter = life_gdp.loc[(life_gdp["country"]== "Australia")]
fig = go.Figure()
fig.add_trace(go.Bar(x = data_filter['year'], y = data_filter["lifeExp"], name="Cantidad de Población"))
fig.add_trace(go.Scatter(x = data_filter['year'], y = data_filter["lifeExp"],
                         name = "Población linea temporal", mode = "lines+markers"))
fig.show()


# ## _Botones de tiempo._
# 
# Los botones de tiempo se pueden agregar a los plots de líneas para filtrar o acercar un segmento de tiempo específico. Puede ver botones de tiempo comunes en la mayoría de los sitios web de acciones. 
# 
# Los botones de tiempo en Plotly son un diccionario que especifica:
# 
# 
# * `label`: Es el texto que aparecerá en el botón.
# * `count`: Es el conteo de cuántos pasos se deben tomar al hacer clic en el botón.
# * `step`: Es el período de fecha como se debe mover, quizá año, mes o día y más.
# * `stepmode`:  Este es el más compleho. Puede ser `'todate'` o `'backwards'`.  `'todate'` significa desde el comienzo del período de tiempo completo más cercano indicado en el paso (después de ir hacia atrás por conteo). `'backwards'` es simplemente retroceder por conteo. 
# 
# 
# Para ilustar lo anterior considere la siguiente data:
# 
# ```Python
# ## Primero importamos el DataFrame.
# rain = pd.read_csv("datas/data_plotly/rain.csv",)
# rain["Date"] = pd.to_datetime(rain["Date"])
# rain = rain.sort_values(by = ["Date"]).reset_index(drop = True)
# ```
# 
# Este contiene la información de las lluvias (mm), de la ciudad de Sydney en Australia desde 01-01-2020 hasta 10-12-2020. Vamos a considerar solo las fechas hasta el 20 de octubre.
# 
# ```Python
# temp = rain.head(284)
# date_buttons = [{'count': 6, 'step': "month", 'stepmode': "todate", 'label': "6M_HOY"},
#                 {'count': 14, 'step': "day", 'stepmode': "todate", 'label': "2SEM_HOY"}]
# ##
# fig = px.line(data_frame=temp, x='Date',y='Rainfall', title="LLuvia (mm) en Sydney")
# fig.update_layout({'xaxis': {'rangeselector': {'buttons': date_buttons}}})
# fig.show()
# ```

# In[41]:


## Celda de código para probar.
rain = pd.read_csv("datas/data_plotly/rain.csv",)
rain["Date"] = pd.to_datetime(rain["Date"])
rain = rain.sort_values(by = ["Date"]).reset_index(drop = True)


# In[42]:


## Celda de código para probar.
temp = rain.head(274)
date_buttons = [{'count': 6, 'step': "month", 'stepmode': "todate", 'label': "6M_HOY"},
                {'count': 14, 'step': "day", 'stepmode': "todate", 'label': "2SEM_HOY"}]
##
fig = px.line(data_frame=temp, x='Date',y='Rainfall', title="LLuvia (mm) en Sydney")
fig.update_layout({'xaxis': {'rangeselector': {'buttons': date_buttons}}})
fig.show()


# 
# En el ejemplo anterior se tomó se tomó un botón de 6 meses (es decir, `count` es igual a 6 y `step` es igual a un mes). 
# 
# Para el `stepmode` `backward` se ampliará el plot para comerzar el 20 de abril, ya que es solo 6 meses hacia atrás. En cambio, para el `stemode` `todate` se amplia el plot para comenzar el  01 de mayo, el comienzo del mes más cercano una vez que se toma el zoom, es decir, después del 20 de abril.
# 
# 

# #### _Ejercicio 9._
# 
# Debe realizar un plot line con la capacidad de filtar los datos de las últimas 4 semanas (`4SEM_HOY`), las últimas 48 horas (`48HR`) y el año hasta la fecha (`Y_HOY`).
# Considere solo las fechas hasta el 31 de octubre.
# 
# Puede seguir los siguientes pasos si desea:
# 
# 1. Cree la lista de botones especificados con los nombres indicados anteriormente.
# 2. Cree un line plot básico usando el DataFrame `rain`, usando apropiadamente las columnas `Date`  y `Rainfall`
# 3. Actualice la figura usando `update_layout()` para construir botones usando la lista que acaba de crear.

# In[43]:


date_buttons = [{'count': 28, 'label': "4SEM_HOY", 'step': "day", 'stepmode': "todate"},
                {'count': 48, 'label': "48HR", 'step': "hour", 'stepmode': "todate"},
                {'count': 1, 'label': "Y_HOY", 'step': "year", 'stepmode': "todate"}]
##
tempo = rain.head(285)
fig = px.line(data_frame=tempo, x='Date', y='Rainfall', title="Rainfall (mm)")
fig.update_layout({'xaxis': {'rangeselector': {'buttons': date_buttons}}}
                  )
fig.show()


# ### _Botones personalizados._
# 
# Los botones personalizados en Plotly son elementos pequeños pero poderosos que pueden actualizar los datos o los elementos de diseño utilizados en el gráfico. Todo se debe hacer con `update_layout()`.
# 
# Los botones personalizados se facilitan a través del elemento de diseño `updatemenus`. Esta es una lista de diccionarios para cada conjunto de botones.
# 
# * `type`:  Establece si son `buttons` o `dropdown`
# 
# * `direction`: La dirección establece si queremos botones al lado o uno encima del otro. 
# 
# * `x/y`: Posicionar elementos. 
# 
# * `showactive`: `True/False`  Permite indicar si el botón activo aparece cuando se presiona. Activo aquí significa seleccionado actualmente. 
# 
# * `buttons`: Es una lista de objetos de bonotes.

# Consideremos el siguiente plot:
# 
# ```python
# fig = px.bar(data_frame = revenues2, x = 'Industry', y = 'Revenue', color = 'Industry')
# fig.show()
# ```

# In[44]:


## Celda de código para probar.
fig = px.bar(data_frame = revenues2, x = 'Industry', y = 'Revenue', color = 'Industry')
fig.show()


# Vamos a crear los botones para cambiar el tipo de gráfico. 
# 
# ```python
# my_buttons = [
# {'label': "Bar plot", ## Texto del botón.
#  'method': "update",  ## El método está configurado para actualizar, lo que permite que el botón 
#                       ## modifique datos o elementos de diseño.
#  'args': [{"type": "bar"}]}, ## diccionario de lo que se actualizará.
# ##
# {'label': "scatterplot",
#  'method': "update",
#  'args': [{"type": "scatter", 'mode': 'markers'}]},
#            ]
# ```
# 

# In[45]:


## Celda de código para probar.
my_buttons = [
{'label': "Bar plot", ## Texto del botón.
 'method': "update",  ## El método está configurado para actualizar, lo que permite que el botón 
                      ## modifique datos o elementos de diseño.
 'args': [{"type": "bar"}]}, ## diccionario de lo que se actualizará.
##
{'label': "box-plot",
 'method': "update",
 'args': [{"type": "box", 'mode': 'markers'}]},
           ]


# #### _El argumento de `arg`_
# 
# El argumento `args` es una de las partes más confusas de Plotly. Es una lista de varios diccionarios.
# 
# 1. El primer diccionario establece los argumentos y valores para enviar al elemento `data`de datos del elemento de la  seguimiento de la figura. 
# 2. El segundo diccionario contiene los argumentos para enviar al `layout` de la figura.

# ### _Interactividad de los botones._
# 
# Llamamos a `update_layout()` y establecemos el argumento `updatemenus`. El `type` es `buttons`.  Establecemos `direction` en `down`, ya que deseamos que nuestros botones estén uno encima del otro. También configuramos `x/y` para colocarlos a la derecha de la gráfica aproximadamente a la mitad. Tengamos el botón activo como nuestro bar plot y hagamos que aparezca activo (`showactive`:`True`), de lo contrario, puede ser confuso por qué el botón no está activo.
# 
# Finalmente, agregamos la lista de botones que hicimos anteriormente y mostramos el plot.
# 
# ```Python
# fig.update_layout({
#     'updatemenus': [{'type': "buttons",'direction': 'down','x': 1.3, 'y': 0.5,
#                      'showactive': True,'active': 0,'buttons': my_buttons}]  })
# fig.show()
# ```

# In[46]:


fig.update_layout({
    'updatemenus': [{'type': "buttons",'direction': 'down','x': 1.3, 'y': 0.5,
                     'showactive': True,'active': 0,'buttons': my_buttons}]  })
fig.show()


# ## _`dropdown`: Menús desplegables._
# 
# Un menú desplegable es una forma de proporcionar entrada de usuario para seleccionar entre diferentes opciones, al igual que los botones. Puede crear tantas opciones como desee en Plotly para actualizar datos o elementos de diseño. 
# 
# Los menús desplegables se crean de manera muy similar a los botones. 
# 
# Primero consideremos el DataFrame de trabajo:
# 
# ```Python
# data_dropdown = penguins.groupby(by = ["Sex","Species"], as_index=False).size()
# data_dropdown
# list_names = ['Adelie Penguin (Pygoscelis adeliae)', 'Chinstrap penguin (Pygoscelis antarctica)',
#               'Gentoo penguin (Pygoscelis papua)']
# ```
# 
# 

# In[47]:


## Celda de código para probar.
data_dropdown = penguins.groupby(by = ["Sex","Species"], as_index=False).size()
data_dropdown
list_names = ['Adelie Penguin (Pygoscelis adeliae)', 'Chinstrap penguin (Pygoscelis antarctica)',
              'Gentoo penguin (Pygoscelis papua)']


# Ahora construimos las tres figuras:
# 
# ```Python
# fig = go.Figure()
# for specie in list_names:    
#     df = data_dropdown[data_dropdown["Species"] == specie]
#     fig.add_trace(go.Bar(x = df["Sex"], y = df["size"], name = specie))
# ```
# 

# In[48]:


fig = go.Figure()
for specie in list_names:
    df = data_dropdown[data_dropdown["Species"] == specie]
    fig.add_trace(go.Bar(x = df["Sex"], y = df["size"], name = specie))


# 
# Se hace uso de `args`, a uno elemnto de esta lista se pasa un diccionario con key `visible` y una lista de booleanos para prender o apagar el plot generado.
# 
# ```Python
# dropdown_buttons = [{'label': 'ALL', 'method': 'update', ## Agregamos título y método
#                      'args': [{'visible': [True, True, True]}, ## Apagados y predidos.
#                               {'title': 'Todas las especies'}]}, ## Título del plot.
# ##
#                     {'label': 'Adelie', 'method': 'update', ## Agregamos título y método
#                      'args': [{'visible': [True, False, False]}, ## Apagados y predidos.
#                               {'title': 'Esp.1'}]},              ## Título del plot.
# ##
#                     {'label': 'Chinstrap', 'method': 'update', ## Agregamos título y método
#                      'args': [{'visible': [False, True, False]}, ## Apagados y predidos.
#                               {'title': 'Esp2.'}]},              ## Título del plot.
# ## 
#                     {'label': "Gentoo", 'method': "update", ## Agregamos título y método
#                      'args': [{"visible": [False, False, True]}, ## Apagados y predidos.
#                               {'title': 'Esp3.'}]},              ## Título del plot.
#                     ]
# ```

# In[49]:


## Celda de código para probar.
dropdown_buttons = [{'label': 'ALL', 'method': 'update', ## Agregamos título y método
                     'args': [{'visible': [True, True, True]}, ## Apagados y predidos.
                              {'title': 'Todas las especies'}]}, ## Título del plot.
##
                    {'label': 'Adelie', 'method': 'update', ## Agregamos título y método
                     'args': [{'visible': [True, False, False]}, ## Apagados y predidos.
                              {'title': 'Esp.1'}]},              ## Título del plot.
##
                    {'label': 'Chinstrap', 'method': 'update', ## Agregamos título y método
                     'args': [{'visible': [False, True, False]}, ## Apagados y predidos.
                              {'title': 'Esp2.'}]},              ## Título del plot.
## 
                    {'label': "Gentoo", 'method': "update", ## Agregamos título y método
                     'args': [{"visible": [False, False, True]}, ## Apagados y predidos.
                              {'title': 'Esp3.'}]},              ## Título del plot.
                    ]


# Finalmente, adicionamos las actualizaciones al igual que el caso de los botones:
# 
# ```python
# fig.update_layout({'updatemenus':
#                    [{'type': "dropdown",
#                      'x': 1.3,'y': 0.5,
#                      'showactive': True,
#                      'active': 0,
#                      'buttons': dropdown_buttons}]})
# fig.show()
# ```

# In[50]:


## Celda de código para probar.
fig.update_layout({'updatemenus':
                   [{'type': "dropdown",
                     'x': 1.3,'y': 0.5,
                     'showactive': True,
                     'active': 0,
                     'buttons': dropdown_buttons}]})
fig.show()

