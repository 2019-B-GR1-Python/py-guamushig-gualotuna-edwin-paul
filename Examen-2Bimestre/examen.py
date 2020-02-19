# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

# Examen

# 1)  Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros

data = {
        'Nombre': ['Edwin', 'Paul', 'Ronal', 'Renato', 'Javier', 'Nicol', 'Ivan','Henry', 'Ignacio', 'Lily'],
        'Apellido': ['Guamushi', 'Gualotunia', 'Alvarado', 'SAnhez', 'Lara', 'Piedra', 'Vargas','Torres', 'Garcia', 'Solano'],
        'Edad': ['22', '23', '24', '26', '27', '28', '29','30', '31', '32'],
        'Algo': ['12', 'zc', '123', 'asd', 'df', 'we', 'we','30', '31', '32'],
        'Universidad': ['EPN', 'EPN', 'CEC', 'UCE', 'PUCE', 'UPS', 'UTC','UTPL', 'UNACH', 'ESPOL'],
        'Ciudad': ['Qu', 'Gu', 'Lo', 'La', 'Ma', 'Mont', 'Riob','SanGa', 'Esme', 'Sang']
        }

df = pd.DataFrame(data, columns=['Nombre', 'Apellido','Edad', 'Algo', 'Universidad', 'Ciudad'])

cinco_registros = df[:4]
cinco_ultimos_registros = df[5:]


#2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico

arreglo_numpy = np.random.random(24).reshape(6,4)
fecha = pd.date_range('2020-2-10', '2020-2-19')
fecha_serie = pd.Series(fecha.format())
df2 = pd.DataFrame(arreglo_numpy, columns=['a','b','c','d'])
df2['fecha'] = fecha_serie
df2 = df2.set_index('fecha')

# 4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.

print(df[['Nombre', 'Apellido']])

df.values


# 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe

df2_estadistica = df2.describe()

# 6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos

dfaux = df.pivot(index='Nombre', columns='Apellido', values='Edad').reset_index()

# 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente

print(df.sort_values(by=['Nombre'], ascending=[True]))

print(df.sort_values(by=['Apellido'], ascending=[False]))


# 8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

arreglo_numpy_entero = np.random.randint(0,10,60).reshape(10,6)
df8 = pd.DataFrame(arreglo_numpy_entero, columns=['a','b','c','d', 'e', 'f'])

df_mayores = df8[df8 > 7]


# 9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

arreglo_mix = np.random.randint(0,10,60).reshape(10,6)
df9 = pd.DataFrame(arreglo_numpy_entero, columns=['a','b','c','d', 'e', 'f'])
valores_nan = float('NaN')
df9['Valores Nan'] = valores_nan

df9 = df9.fillna(0)
# Pra dataframe anterior
df_mayores = df_mayores.fillna(0)


# 10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

# Mediana
print(df8.mean())

# Promedio
print(df8.describe())


# 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe
arreglo_d_uno = np.random.randint(0,10,60).reshape(10,6)
df101 = pd.DataFrame(arreglo_d_uno, columns=['a','b','c','d', 'e', 'f'])
arreglo_d_dos = np.random.randint(0,10,60).reshape(10,6)
df102 = pd.DataFrame(arreglo_d_dos, columns=['a','b','c','d', 'e', 'f'])

df101 = pd.merge(df101.reset_index(), df102.reset_index())


# 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.
# 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna

df8_frecuencia1 = df8['a'].value_counts()
df8_frecuencia2 = df8['b'].value_counts()
df8_frecuencia3 = df8['c'].value_counts()
df8_frecuencia4 = df8['d'].value_counts()
df8_frecuencia5 = df8['e'].value_counts()

# 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C





