# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(lista_numeros)
serie_b = pd.Series(tupla_numeros)
serie_C = pd.Series(np_numeros)
serie_d = pd.Series([
        True,
        12.12,
        (),
        [],
        None, 
        10,
        {'Edwin', 22}
        ])

serie_d[5]

lista_ciudades = ["quito", "cuenca", "loja", "esmeraldas"]

serie_ciudad = pd.Series(lista_ciudades, index=[
        "q",
        "c",
        "l",
        "e"])

serie_ciudad["e"]
serie_ciudad[3]


valores_ciudad = {
        "quito": 1200, 
        "cuenca": 13000, 
        "loja": 3489, 
        "esmeraldas": 6969
        }

serie_valor_ciudad = pd.Series(valores_ciudad)
serie_valor_ciudad[0]
serie_valor_ciudad["loja"]

ciudad_menor_50000 = serie_valor_ciudad > 5000




serie_valor_ciudad = serie_valor_ciudad * 1.1
serie_valor_ciudad["quito"] = serie_valor_ciudad - 0.5
print("lima" in serie_valor_ciudad)
print("loja" in serie_valor_ciudad)


ciudades_uno = pd.Series({
        "montanita": 300,
        "guayaquil": 10000,
        "quito": 2000})

ciudades_dos = pd.Series({
"loja": 300,
"guayaquil": 10000})

ciudades_uno["loja"] = 0

ciudad_add = ciudades_uno.add(ciudades_dos)

ciudades_concatenadas = pd.concat([
ciudades_uno,
ciudades_dos
])

ciu_concatenadas_v = pd.concat([
ciudades_uno,
ciudades_dos
], verify_integrity = True)

ciu_append = ciudades_uno.append(
ciudades_dos,
verify_integrity = True)

ciudades_uno.max()

pd.Series.max(ciudades_uno)
pd.Series.max()

pd.Series.min(ciudades_uno)
pd.Series.min()


# estadistica
ciudades_uno.mean()
ciudades_uno.median()

np.average(ciudades_uno)


ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values(
	ascending =  False).head(2)
ciudades_uno.sort_values().tail(2)
