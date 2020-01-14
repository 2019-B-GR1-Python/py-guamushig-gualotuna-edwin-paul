#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:18:10 2020

@author: edwin
"""

import numpy as np 
import pandas as pd
import math

path_guardado_complete = './data/artwork_data_complete.pickle'
df = pd.read_pickle(path_guardado_complete)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado = seccion_df.groupby('artist')
type(df_agrupado)

for acquisitionYear, registros in df_agrupado:
    print(registros)
    
# contar valores de una columna
a = seccion_df['units'].value_counts()
# verificar si la columna esta vacia
a.empty


def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if(a.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            """
            promedio = np.nanmean(series)
            series_valores_llenos = series.fillna(promedio)
            return series_valores_llenos
        
            """
            suma = 0
            numero_valores = 1
            for valor_serie in series:
                if(isinstance(valor_serie, str)):     
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
                else:
                    pass
            promedio = suma / numero_valores
            # buscar los na y agregar el valor de 'promedio'
            series_valores_llenos = series.fillna(promedio) 
            return series_valores_llenos
        elif(tipo == 'value_counts'):
            for valor_serie in series:
                if(isinstance(valor_serie, str)):
                    valor = valor_serie
                else: 
                    pass
            series_valores_llenos = series.fillna(valor)
            return series_valores_llenos
 
                    
            

def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        # copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
        # copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
        copia.loc[:,'units'] = llenar_valores_vacios(serie_h, 'value_counts')
        copia.loc[:,'inscription'] = llenar_valores_vacios(serie_h, 'value_counts')
        lista_df.append(copia)
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores

valores_llenos = transformar_df(seccion_df)

        
        
        
        
        
        
        
        
        
        
        