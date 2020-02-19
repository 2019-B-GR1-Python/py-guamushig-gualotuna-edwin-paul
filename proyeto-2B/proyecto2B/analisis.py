#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:42:15 2020

@author: edwin
"""

import pandas as pd
import os
import xlsxwriter
import matplotlib.pyplot as plt
import seaborn as sns

path_csv = './arania_peliculas/data/datos.csv'
path_guardar_pickle = 'pickle/datos_peliculas.pickle'


df = pd.read_csv(path_csv, nrows = 852)

df