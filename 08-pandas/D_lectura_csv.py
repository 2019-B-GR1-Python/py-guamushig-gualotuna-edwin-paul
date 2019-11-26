#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:37 2019

@author: edwin
"""

import pandas as pd
import os


# El pandas permite leer JSON, CSV, HTML, XML....
# Archivos binarios

path = './data/artwork_data.csv'

columnas = ['id', 'artist', 'title', 'medium', 'year', 
            'acquisitionYear', 'height', 'width', 'units']

df = pd.read_csv(path, nrows = 10)

df2 = pd.read_csv(path, nrows=10, usecols=columnas)

df3 = pd.read_csv(path, nrows=10, usecols=columnas, index_col = 'id')

df4 = pd.read_csv(path)

path_guardado = './data/artwork_data.pickle'
path_guardado_complete = './data/artwork_data_complete.pickle'

df3.to_pickle(path_guardado)
df4.to_pickle(path_guardado_complete)
df5 = pd.read_pickle(path_guardado)
