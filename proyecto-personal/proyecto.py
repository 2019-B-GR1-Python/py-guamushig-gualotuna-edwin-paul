# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import xlsxwriter
import matplotlib.pyplot as plt
import seaborn as sns

path_csv = './dataframe/WorldCupMatches.csv'
path_csv2 = './dataframe/WorldCups.csv'
path_guardar_pickle = './pickle/WorldCupMatches.pickle'
path_excel_informe = './graficos-excel/informe.xlsx'


df = pd.read_csv(path_csv, nrows = 852)

# df.to_pickle(path_guardar_pickle)


## Mas veces participaron
selecciones_local = df[['Year', 'Home Team Name']]
selecciones_local.columns = ['Anio', 'Seleccion']
selecciones_visita = df[['Year', 'Home Team Name']]
selecciones_visita.columns = ['Anio', 'Seleccion']
participaciones = pd.concat([selecciones_local, selecciones_visita], axis = 0)
participaciones_anio = participaciones.groupby(['Anio', 'Seleccion']).count().reset_index()
participaciones_anio = participaciones_anio['Seleccion'].value_counts().reset_index()



## GOles por partido
df["Goles totales"] = df["Home Team Goals"] + df["Away Team Goals"]
plt.figure(figsize=(13,8))
sns.boxplot(y=df["Goles totales"],
            x=df["Year"])
plt.grid(True)
plt.title("Goles marcados por anio",color='b')
plt.show()



## CAMPEONAS
campeones = df2.groupby('Winner')['Year'].count().reset_index().sort_values(by="Year",ascending=False)
campeones.columns = ['Campeon', 'Cantidad']

labels = campeones['Campeon']
labels.to_string()
fig1, ax1 = plt.subplots()
ax1.pie(campeones['Cantidad'], labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.show()




## Total de asistentes a cada mundial
total_asistentes_por_mundial = df.groupby('Year')['Attendance'].sum().reset_index()
total_asistentes_por_mundial = total_asistentes_por_mundial.astype(int)

plt.figure(figsize=(18,7))
sns.barplot(total_asistentes_por_mundial['Year'],total_asistentes_por_mundial["Attendance"])
plt.grid(True)
plt.title('Asistentes por anio', color='g', size = 25)


mundial_2014 = df.groupby('City')['Year']




# Paises que mas han particidpado
partidos_local = df["Home Team Name"].value_counts().reset_index()
partidos_local.columns = ["Pais","Partidos"]
partidos_visita = df["Away Team Name"].value_counts().reset_index()
partidos_visita.columns = ["Pais","Partidos"]
partidos_jugados = pd.concat([partidos_local,partidos_visita],axis=0)
partidos_jugados = partidos_jugados.groupby("Pais")["Partidos"].sum().reset_index().sort_values(by="Partidos",ascending=False)



# Goles marcados por anio
goles_local = df.groupby('Year')['Home Team Goals'].sum().reset_index()
goles_local.columns = ['Anio','Goles']
goles_visita = df.groupby('Year')['Away Team Goals'].sum().reset_index()
goles_visita.columns = ['Anio','Goles']
goles_anotados = pd.concat([goles_local, goles_visita],axis=0)
goles_anotados = goles_anotados.groupby('Anio')['Goles'].sum().reset_index()

total_asistentes_por_mundial = df.groupby('Year')['Attendance'].sum().reset_index()
total_asistentes_por_mundial = total_asistentes_por_mundial.astype(int)



##  Promedio asistencia

promedio_asistencia = df.groupby("Year")["Attendance"].mean().reset_index()
promedio_asistencia["Year"] = att1["Year"].astype(int)
plt.figure(figsize=(12,7))
ax = sns.pointplot(att1["Year"],att1["Attendance"],color="w")




list_data = pd.array(total_asistentes_por_mundial.values)
df = pd.DataFrame(list_data)
excel_file = './graficos-excel/informe.xlsx'
sheet_name = 'Sheet1'
writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)
workbook = writer.book
worksheet = writer.sheets[sheet_name]
chart = workbook.add_chart({'type': 'column'})
chart.add_series({
    'values':     '=Sheet1!$B$2:$B${}'.format(total_asistentes_por_mundial.size),
    'gap':        3
})

chart.set_y_axis({'major_gridlines': {'visible': False}})
chart.set_legend({'position': 'none'})
worksheet.insert_chart('D2', chart)
writer.save()