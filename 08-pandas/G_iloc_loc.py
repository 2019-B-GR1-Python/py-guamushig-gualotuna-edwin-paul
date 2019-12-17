#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:05:22 2019

@author: edwin
"""

import pandas as pd

path_guardado = './data/artwork_data_complete.pickle'
df = pd.read_pickle(path_guardado)

df2 = df.set_index('id')

# obtiene la fila del indice 1035
primero = df.loc[0]
segundo = df.iloc[0]


"""
Crear un dataframe:
                 nota 1   disciplina
    pepito       7           5
    juanita      8           9
    maria        9           2
"""

datos = [['pepito', 7, 5], ['juanita', 8, 9], ['maria', 9, 2]]
columnas = ['nombre', 'nota1', 'disciplina']
df3 = pd.DataFrame(datos, columns=columnas)

data = [
        {'nombre': 'pepito', 'nota1': 7, 'disciplia': 5},
        {'nombre': 'juanita', 'nota1': 8, 'disciplia': 9},
        {'nombre': 'maria', 'nota1': 9, 'disciplia': 2}
        ]

df4 = pd.DataFrame(data)

df4.loc[0]
df4.iloc[0]


## obtener columnas
df4 = df4.set_index('nombre')
df4.loc['pepito', 'disciplia']
df4.loc['pepito', ['disciplia', 'nota1']]


## 
df4.loc[['pepito', 'juanita'], 'nota1']
df4.loc[[True, False, True]]
condicion_nota = (df4['nota1'] > 7) & (df4['disciplia'] > 7)
mayores_siete = df4.loc[condicion_nota]



## Estudiantes meenores a 7 en discilplna sube a 7
nota_menor_7 = df4['disciplia'] > 7
df4.loc[nota_menor_7] = 7

## Solo a pepito se le pondra 10 en todo
df4.loc['pepito',:] = 10

## Disciplina se les baje a 7
df4.loc[:, 'disciplia'] = 6


df4['promedio'] = (df4['nota1'] + df4['disciplia'])/2