#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:17:46 2019

@author: edwin
"""

import pandas as pd


path_guardado = './data/artwork_data_complete.pickle'
df = pd.read_pickle(path_guardado)


# Obtener nombre de los artistas
serie_de_artistas = df['artist']
artistas = pd.unique(serie_de_artistas)
artistas.size

## Filtrar artistas
blake = df['artist'] == 'Blake, William'
blake.value_counts()

## saber cuantas obras tene cada artista
df['artist'].value_counts()

# obtner obras de blake
df_blake = df[blake]


