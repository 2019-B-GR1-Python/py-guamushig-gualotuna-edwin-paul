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


def leer_imagen():
    # leer imagen
    imagen=mpimg.imread('titan.jpg')
    mostrar_imagen = plt.imshow(imagen)
    plt.show

def mostrar_pixeles():
    #ver pixeles de imagen
    return imagen.shape



"""
hacer random :v

piezas = np.random.permutation(10)
imagen_prueba = np.concatenate(list(map(lambda x: dividir_imagen[x], piezas)))
plt.imshow(imagen_prueba)

# dividir eje de las x
parte = np.split(imagen,10,axis=1)
plt.imshow(parte[2])
parte[2].shape
parte2 = np.split(parte[3],5,axis=0)
plt.imshow(parte2[4])
"""

def dividir_imagen(arreglo_imagen, tamanio):
    x, y = tamanio
    return np.split(np.concatenate(np.split(arreglo_imagen, y, axis=1)), x*y)



def unir_imagen():
    ab = dividir_imagen(imagen, (5,5))
    num_ite1 = np.random.permutation([0,1,2,3,4])
    num_ite2 = np.random.permutation([5,6,7,8,9])
    num_ite3 = np.random.permutation([10,11,12,13,14])
    num_ite4 = np.random.permutation([15,16,17,18,19])
    num_ite5 = np.random.permutation([20,21,22,23,24])
    
    mix1 = np.concatenate(list(map(lambda i: ab[i], num_ite1)))
    mix2 = np.concatenate(list(map(lambda i: ab[i], num_ite2)))
    mix3 = np.concatenate(list(map(lambda i: ab[i], num_ite3)))
    mix4 = np.concatenate(list(map(lambda i: ab[i], num_ite4)))
    mix5 = np.concatenate(list(map(lambda i: ab[i], num_ite5)))
    
def mostrar_rompe():
    ss = np.concatenate((mix1, mix2, mix3, mix4, mix5), axis=1)
    plt.imshow(ss)
    return ss



def listar_posiciones_por_columna(columna):
    if columna == 0:
        return print(num_ite1)
    elif columna == 1:
        return num_ite2
    elif columna == 2:
        return num_ite3
    elif columna == 3:
        return num_ite4
    elif columna == 4:
        return num_ite5
    

def mover_piezas(posicion_inicial, posicion_final, valor1, valor2):
    
    if (valor1>=0 and valor2<=4):  
        num_ite1[int(posicion_inicial)] = int(valor1)
        num_ite1[int(posicion_final)] = int(valor2)
        mix1 =  np.concatenate(list(map(lambda i: ab[i], num_ite1)))
    elif (valor1>=5 and valor2<=9):    
        num_ite2[posicion_inicial] = valor1
        num_ite2[posicion_final] = valor2
        mix2 =  np.concatenate(list(map(lambda i: ab[i], num_ite2)))
    elif (valor1>=10 and valor2<=14):    
        num_ite3[posicion_inicial] = valor1
        num_ite3[posicion_final] = valor2
        mix3 =  np.concatenate(list(map(lambda i: ab[i], num_ite3)))
    elif (valor1>=15 and valor2<=19):
        num_ite4[posicion_inicial] = valor1
        num_ite4[posicion_final] = valor2
        mix4 =  np.concatenate(list(map(lambda i: ab[i], num_ite4)))
    elif (valor1>=20 and valor2<=24):
        num_ite5[posicion_inicial] = valor1
        num_ite5[posicion_final] = valor2
        mix5 =  np.concatenate(list(map(lambda i: ab[i], num_ite5)))
    
    # ss = np.concatenate((mix1, mix2, mix3, mix4, mix5), axis=1)
    # plt.imshow(ss)

def graficar():
    mix1 = np.concatenate(list(map(lambda i: ab[i], num_ite1)))
    mix2 = np.concatenate(list(map(lambda i: ab[i], num_ite2)))
    mix3 = np.concatenate(list(map(lambda i: ab[i], num_ite3)))
    mix4 = np.concatenate(list(map(lambda i: ab[i], num_ite4)))
    mix5 = np.concatenate(list(map(lambda i: ab[i], num_ite5)))
    
    ss = np.concatenate((mix1, mix2, mix3, mix4, mix5), axis=1)
    plt.imshow(ss)
    plt.show




def menu():
    opcion = None
    while (opcion != 0):
        print("********************************")
        print("Rompecabezas POLICRUSH")
        print("Escoge una opcion del menu:")
        print("1) Mostart original\n2) Mostrar rompecabezas\n3) Ver posiciones\n4) Mover\n0) Salir")
        print("*********************************")
        opcion = int(input("Seleccione una opcion: "))
        print("*************************************")
        if (opcion == 1):
            leer_imagen()
            break
        elif (opcion == 2):
            unir_imagen()
            mostrar_rompe()
            break
        elif (opcion == 3):
            columna = input('COlumna que desa mover: ')
            tamanio = listar_posiciones_por_columna(int(columna))
            print(tamanio)
            break
        elif(opcion == 4):
            posicion_ini = input('Posicion inicial: ')
            posicion_fin = input('Posicion final: ')
            valor_uno = input('Valor 1 : ')
            valor_dos = input('valor2 ')
            mover_piezas(int(posicion_ini), int(posicion_fin), int(valor_uno), int(valor_dos))
            graficar()
            break
            
        elif (opcion == 0):
            print("Adios")
        else:
            print("Errooor")
            opcion = 0


menu()



