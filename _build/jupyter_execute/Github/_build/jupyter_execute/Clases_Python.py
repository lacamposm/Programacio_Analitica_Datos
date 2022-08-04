#!/usr/bin/env python
# coding: utf-8

# # Clases en `Python` (En construcción)
# 
# ---

# In[1]:


get_ipython().system('python --version')


# In[2]:


class Coche:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False
    def arracar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "se ha arrancado")
    def parar(self):
        self.arrancado = False
        print("El", self.marca, self.modelo, "se ha parado") 

laguna = Coche("Renault","laguna")


# In[3]:


laguna.arracar()
print(laguna.arrancado)
##
laguna.parar()
print(laguna.arrancado)


# In[4]:


laguna.marca


# In[5]:


tesla = Coche("Tesla","Model 3")
print(tesla.marca,tesla.modelo)


# In[6]:


class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,4.5)
x.r, x.i


# In[7]:


class Humano:
    def __init__(self, edad):
        self.r = edad
        print("soy un nuevo objeto")

    def hablar(self, mensaje):
        print(mensaje)


# In[8]:


pedro = Humano(32)
pedro.r
pedro.hablar("Veo amigo")


# In[9]:


print(pedro)


# In[10]:


help(Coche)


# In[11]:


laguna.arrancado


# In[12]:


laguna.marca = "dlgkldflk"


# In[13]:


print(laguna.marca)


# In[14]:


Coche(marca="Rejkh")

