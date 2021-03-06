#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:22:39 2019

@author: edwin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:37 2019

@author: edwin
"""

import pandas as pd
import os
import numpy as np
import sqlite3
import mysql


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



##############

path_guardado = './data/artwork_data.pickle'
df5 = pd.read_pickle(path_guardado)


path = './data/artwork_data.csv'
path_archivo_guardado = 'mi_datafame_completo.xls'
df4 = pd.read_csv(path)

df = df4.iloc[4990:50019,:].copy()

df.to_excel(path_archivo_guardado, index = False)

# queremos mostrar ciertas columnas
columnas = ['artist', 'title', 'year']
df.to_excel(path_archivo_guardado, columns = columnas ,index = False)


# multiples hojas
path_multiple = 'mi_datafame_completo_multiple.xls'

writer = pd.ExcelWriter(path_multiple, engine = 'xlsxwriter')

#definimos nuestras hojas
df.to_excel(writer,  sheet_name = 'Primera')
df.to_excel(writer,  sheet_name = 'Segunda', index = False)
df.to_excel(writer,  sheet_name = 'Tercera', columns = columnas)
writer.save()



# nuero de artistas
num_artistas = df['artist'].value_counts()


# colotes
path_colores = 'mi_datafame_completo_colores.xls'
writer = pd.ExcelWriter(path_colores, engine = 'xlsxwriter')
num_artistas.to_excel(writer, sheet_name = 'Artistas')

hoja_de_artistas = writer.sheets['Artistas']

rango_de_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

#crear el formato que le queremos dar
formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_type": "percentile",
        "max_value": "99"
        }

hoja_de_artistas.conditional_format(rango_de_celdas, formato_artistas)
writer.save()





import xlsxwriter

excel_grafico = xlsxwriter.Workbook('excel_graficas.xlsx')
worksheet = excel_grafico.add_worksheet()

data = num_artistas.values
worksheet.write_column('A1', data)

chart = excel_grafico.add_chart({'type': 'line'})

chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

worksheet.insert_chart('C1', chart)

excel_grafico.close()












######## Exportar a base de datos



with sqlite3.connect('bbd_artist.bd') as conexion: 
    df4.to_sql('py_artistas', conexion)
    
    
## Exportar a mysql
    
import mysql.connector
with mysql.connect('mysql://edwin:123456@localhost:32771/test') as conexion:
    df4.to_sql('tabla_mysql', conexion)
    
    
    
    
### JSON #######

df2.to_json('artista.json', orient='table')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    