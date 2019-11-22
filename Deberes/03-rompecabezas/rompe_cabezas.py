#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 01:45:24 2019

@author: edwin
"""

import os
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import random 

# leer imagen
imagen=mpimg.imread('titan.jpg')
mostrar_imagen = plt.imshow(imagen)

#ver pixeles de imagen
imagen.shape

"""
hacer random :v

piezas = np.random.permutation(10)
imagen_prueba = np.concatenate(list(map(lambda x: dividir_imagen[x], piezas)))
plt.imshow(imagen_prueba)
"""


# dividir eje de las x
parte = np.split(imagen,10,axis=1)
plt.imshow(parte[2])
parte[2].shape
parte2 = np.split(parte[3],5,axis=0)
plt.imshow(parte2[4])


# funcion para dividir imagen
def crear_split(arreglo_imagen, tamanio):
    x, y = tamanio
    return np.split(np.concatenate(np.split(arreglo_imagen, y, axis=1)), x*y)

ab = crear_split(imagen, (5,10))
plt.imshow(ab[49])


# funcion intercambiar posiciones arreglo 
