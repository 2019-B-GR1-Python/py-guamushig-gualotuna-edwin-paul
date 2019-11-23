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

ab = crear_split(imagen, (5,5))

numero_iteracioes = np.random.permutation([0,1,2,3,4])
num_ite2 = np.random.permutation([5,6,7,8,9])
num_ite3 = np.random.permutation([10,11,12,13,14])
num_ite4 = np.random.permutation([15,16,17,18,19])
num_ite5 = np.random.permutation([20,21,22,23,24])

mezclar = np.concatenate(list(map(lambda i: ab[i], numero_iteracioes)))
mez2 = np.concatenate(list(map(lambda i: ab[i], num_ite2)))
mez3 = np.concatenate(list(map(lambda i: ab[i], num_ite3)))
mez4 = np.concatenate(list(map(lambda i: ab[i], num_ite4)))
mez5 = np.concatenate(list(map(lambda i: ab[i], num_ite5)))

plt.imshow(mezclar)
plt.show
plt.imshow(mez2)
plt.show
plt.imshow(mez3)
plt.show
plt.imshow(mez4)
plt.show
plt.imshow(mez5)
plt.show

numero_ite3[0]=4
numero_ite3[1]=0
mezclar = np.concatenate(list(map(lambda i: ab[i], numero_iteracioes)))



ss = np.concatenate((mezclar, mez2, mez3, mez4, mez5), axis=1)

plt.imshow(ss)
plt.imshow(imagen)



piezas_index = np.random.permutation(int(50))
mapache_random = np.concatenate(list(map(ab,piezas_index)))


plt.imshow(vv)
plt.show
