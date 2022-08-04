#!/usr/bin/env python
# coding: utf-8

# # Introducción a los notebooks y al lenguaje Markdown
# 
#  **Temas:**
#  - Introducción a los notebooks
#  - Introducción al lenguaje de Markdown

# ## ¿Qué es Markdown?
# 
# 
# Markdown es un lenguaje de marcado ligero que puede usar para agregar elementos de formato a documentos de texto sin formato. Creado por John Gruber en 2004, Markdown es ahora uno de los lenguajes de marcado más populares del mundo.
# 
# Usar Markdown es diferente a usar un editor WYSIWYG . En una aplicación como Microsoft Word, hace clic en botones para dar formato a palabras y frases, y los cambios son visibles inmediatamente. Markdown no es así. Cuando crea un archivo con formato de Markdown, agrega la sintaxis de Markdown al texto para indicar qué palabras y frases deben verse diferentes.
# 
# Por ejemplo, para denotar un encabezado, agregue un hashtag (por ejemplo, # Encabezado). O para poner una frase en negrilla, agregue dos asteriscos antes y después (p. ej., **Este texto en negrilla**). Puede llevar un tiempo acostumbrarse a ver la sintaxis de Markdown en su texto.
# 
# Puede agregar elementos de formato Markdown a un archivo de texto sin formato utilizando una aplicación de edición de texto. O puede usar una de las muchas aplicaciones de Markdown para los sistemas operativos macOS, Windows, Linux, iOS y Android. También hay varias aplicaciones basadas en web diseñadas específicamente para escribir en Markdown.
# 
# Según la aplicación que utilice, es posible que no pueda obtener una vista previa del documento formateado en tiempo real. Pero eso está bien. Según Gruber , la sintaxis de Markdown está diseñada para ser legible y discreta, por lo que el texto de los archivos de Markdown se puede leer incluso si no se procesa.
# 
# El objetivo principal del diseño de la sintaxis de formato de Markdown es hacer que sea lo más legible posible. La idea es que un documento con formato de Markdown se pueda publicar tal cual, como texto sin formato, sin que parezca que ha sido marcado con etiquetas o instrucciones de formato.
# 
# 

# ## ¿Por qué usar Markdown?
# 
# 
# ¿Por qué escribir con Markdown cuando puede presionar botones en una interfaz para formatear su texto? Resulta que hay un par de razones diferentes por las que las personas usan Markdown en lugar de otros editores.
# 
# Markdown se puede utilizar para todo. La gente lo usa para crear sitios web , documentos , notas , libros , presentaciones , mensajes de correo electrónico y documentación técnica .
# 
# Markdown es portátil. Los archivos que contienen texto con formato Markdown se pueden abrir con prácticamente cualquier aplicación. Si decide que no le gusta la aplicación Markdown que está usando actualmente, puede importar sus archivos Markdown a otra aplicación Markdown. Eso está en marcado contraste con las aplicaciones de procesamiento de textos como Microsoft Word que bloquean su contenido en un formato de archivo propietario.
# 
# Markdown es independiente de la plataforma. Puede crear texto con formato Markdown en cualquier dispositivo que ejecute cualquier sistema operativo.
# 
# Markdown es una prueba de futuro. Incluso si la aplicación que está utilizando deja de funcionar en algún momento en el futuro, aún podrá leer su texto con formato Markdown utilizando una aplicación de edición de texto. Esta es una consideración importante cuando se trata de libros, tesis universitarias y otros documentos importantes que deben conservarse indefinidamente.
# 
# El descuento está en todas partes. Los sitios web como Reddit y GitHub son compatibles con Markdown, y muchas aplicaciones de escritorio y basadas en la web lo admiten.

# ## Desarrollo de la sesión
# 
# A continuación se muestran diferentes ejemplos del uso del lenguaje de __markdown__ para los notebooks de `Python`. El ejercicio consiste en ingresar a cada celda en modo de edición (haciendo doble-clic) y revise cómo se escribe, cómo se ve y luego practique desarrollando sus propios ejemplos.

# ## 1. Encabezados en celdas de texto:
# Para crear un encabezado, agregue hashtag (#) adelante de una palabra o frase. El número de signos numéricos que utilice debe corresponder al nivel del encabezado. Por ejemplo, para crear un título de nivel tres  utilice tres signos numéricos (p. ej., ### Subtítulo).
# 
# ***Ejemplos:***
# 
# ```html
# ## TÍTULO DE PRIMER NIVEL
# Con código html
# <h1>TÍTULO DE PRIMER NIVEL</h1> 
# 
# ## Título segundo nivel
# Con código html 
# <h2>Título segundo nivel</h2> 
# 
# ### Título tercer nivel
# Con código html 
# <h3>Título tercer nivel</h3>
# 
# ### Título cuarto nivel
# Con código html 
# <h4>Título cuarto nivel</h4>
# 
# Logramos llegar hasta el nivel 6.
# 
# ### Título de sexto nivel
# Con código html
# <h6>Título de sexto nivel<h6/>
# ```

# ### 2. Realce de texto
# 
# Con respecto al resaltado del texto...
# 
# * Poner texto en negrilla: __texto en negrita__ texto normal o **texto en negrilla**
# * Poner texto en cursiva: *texto cursiva* texto normal o _texto en cursiva_
# * ¿Cómo logra texto en cursiva y negrilla?
# *  Texto tachado ~~tachado~~
# * Intercalar texto mono-espacio y fin de linea:
# ```html
# <br>`texto mono`<br> texto normal
# * Tamaño de la letra:  <font size = 5> El parametro `size` determina el tamaño </font>
# *   Color en el texto cuando sea necesario <font color=yellow>color Amarillo</font> o texto color <font color=green>color verde</font>
# 
# ```

# In[1]:


def suma(x,y):
  sum = x+y
  return sum

suma(4,5)


# ### 3. Listas 
# 
# 
# ### Listas desordenadas:
# 
# * puedo iniciar guión o con asterisco: Definimos algo
# * Otro item de la lista principal: Definimos otra cosa.
# - item 1 de la lista
# - item 2 de la lista
# 
# ### Listas desordenadas:
# 
# Ahora revisemos listas numeradas
# 
# 6. Primer elemento de la lista
# 2. Algo más que decir
# 3. Segundo elemento de la lista
#    1. sub lista - elemento 1
#    2. sub lista - elemento 2
# 4. Podemos dejar el mismo número
# 5. inserto nuevo elemento
# 45. La lista sigue numerando automáticamente...

# ### 4. Sangría del párrafo
# También tenemos la posibilidad de sangrar el texto cuando sea necesario
# ```html
# > este es un ejemplo
# >> se puede aún más
# >>> tantas veces cómo sea necesario!
# ```

# ## 5. Documentar código
# 
# Cuándo se necesita usar bloques de código con realce de sintaxis dentro de una celda de texto, por ejemplo para explicar un proceso algorítmico:
# 
# ```python
# def suma(x,y):
#   sum = x+y
#   return sum
# 
# suma(4,5)
# ```
# 
# 
# ```python
# # código de python
# if x > 2:
#     s = "string"
# ```
# 
# 
# 
# ```javascript
# # This is formatted as code
# def f1(xx):
#     s = 'string'
# ```
# 
# 
# 
# 
# ```python
# # Tiene formato de código
# def function(a, b):
#     print('algo')
#     if a > b:
#         print('otra cosa')
# ```
# 
# 
# 
# ```Javascript
# // comentario javascript
# if(x=1; x<10; x++){
#   console.log("Hola mundo")  
# }
# ```
# Este es otro bloque de código, por ejemplo para otra tarea:
# 
# ```Python
# # comentario python
# def minimun(A):
#     A.sort()
#     print('ordena arreglo')
#     return a[0]
# ```
# 
# ```Json
# {
#   "firstName": "John",
#   "lastName": "Smith",
#   "age": 25
# }
# ```
# ***
# 
# 

# ## 6. Uso de caracteres especiales Unicode
# Carácteres Unicode ejemplos: &#9728; &#9730; &#9742; &#9775; &#9731; &#129349; &#128525;
# 
# 
# Uso de código decimal y hexadecimal: &#960; &#x3c0; &#405; &#x195; &#x2602; &#x1f31e;
# 
# Para un listado completo de todos los caracteres buscar en: [unicode-table.com/es/](https://unicode-table.com/es/)
# 
# Para lograr escaparnos de los caracteres que son de uso del lenguaje usamos: `\`
# <br></br>
# _**Algunos ejemplos...**_
# 
# 
# * Contra barra y espacio: \\ \
# * Asterisco y barra baja: \*  \_
# * Paréntesis: \{\} \[\] \(\)
# * Sostenido: \#
# * Otros: \+ \- \. \! \: \
# 
# Para finalizar una línea de separación 
# 
# ```
# ***
# ```
# 
# También se puede hacer con guíones:
# 
# ```
# ---
# ```

# ### 7. Use latex para las ecuaciones:
# 
# A continuación ejemplos de codificación en latex para mostrar ecuaciones con calidad. 
# - $\sum \int \frac{\sqrt{x}}{a^2}$
# 
# - $\sum_{i=1}^n \alpha_i + \frac{num}{1- e^{2\pi n}}$
# 
# - $\sin^2 x + \cos^2 x = 1$
# 
# 
# - $S = \mathrm{k_B}\ln\Omega$
# 
# 
# - $$\left[\begin{matrix}   a & b & c \\   d & e & f \\   g & h & i \end{matrix}\right]$$
# 
# 
# - $$\mathbf{K}=\int_V \mathbf{B}^\intercal \mathbf{D B}\mathrm{d}x \mathrm{d}y \mathrm{d}z$$
# 
# 
# - $$\sum_{k=1}^N \sqrt{k_i^2+1}$$
# 
# 
# - $$\left({1+\displaystyle\frac{1}{n}}\right)^n$$
# 
# - $$y(x_{i}) = 4 + x_{i}^{2}$$
#  
# Existe gran cantidad de documentación de __latex__ en la red:
# - En este sitio puede iniciar a practicar con algunas fórmulas [latex formulas](http://minisconlatex.blogspot.com/2010/11/ecuaciones.html)
# - Un manual en línea para escribir ecuaciones de latex: [manual de latex](https://manualdelatex.com/tutoriales/ecuaciones)
# 
# También puede practicar en un editor en línea [Editor de ecuaciones](https://www.codecogs.com/latex/eqneditor.php?lang=es-es)
# 
# ***

# ### 8. Editar tablas 
# Siguiendo algunas convenciones simples, como se muestra en el siguiente ejemplo, puede generar tablas interesantes
# 
# Operación | Siginificado | Resultado
# |:--- | :---: | ---:
# 5032 + 7624 + 365  | sumar valores | 13021
# 18213 - 9567.5  | restar valores | 8645.5
# 13.3 * 8.52  | multiplicación |  113.316
# 35698.7 / 798.23 | división |  44.72232314
# 23 / 8 | División | 2.875
# 23 // 8 | División entera | 2
# 23 % 8 | Módulo de la división | 7
# 13\*\*2 | Potenciación | 169
# 
# | h1 | h2 |
# | :---: | :---: |
# | hola | mundo |
# 
#  columna 1 | columna 2 | columna 3
#  :--- | ---: | :---:
#  1 | 2| $x_i$

# ### 9. Tarea de buscar y practicar
# - Inserte una imagen
# - Agregue código html embebido 
# - Utilice hiper-vínculos
# - Pruebe markdown en otros sitios, por ejemplo: [Dillinger](https://dillinger.io/)
# 
# 
# - Revisar:
# 
# 1. [markdown](https://markdown-it.github.io/)
# 2. [colab getting started](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)

# ## _Créditos_
# 
# [Markdown guide.](https://www.markdownguide.org/getting-started/)
