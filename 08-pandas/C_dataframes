#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:21 2019

@author: edwin
"""

import numpy as np 
import pandas as pd

array_pandas = np.random.randint(0,10,6).reshape(2,3)
df1 = pd.DataFrame(array_pandas)
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]
s4 = df1[3]
s5 = df1[4]

# insertar una serie
serie = pd.Series({0: 3, 1: 69})
valorsito = df1.insert(3,3,serie)
df1[5] = serie

df1[6] = s1 * s2


datos_fisicos_uno = pd.DataFrame(array_pandas, columns=['Estatura (cm)',
                                                    'Peso (kg)',
                                                    'Edad (anios)'], 
                                               index=['Edwin', 'Paul'])


df1.index = ['Edwin', 'Paul']
df1.columns = ['Data1','Data2','Data3']