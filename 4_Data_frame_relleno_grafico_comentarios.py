# -*- coding: utf-8 -*-

import os
os.chdir(r'C:\Program BI\Python Basico 2.0\Clase 3')

import pandas as pd
# Leer la serie de precios de activos
df = pd.read_excel('serie.xlsx')
# llenar los nan con 0's
df_0 = df.fillna(0)
# llenar con el valor anterior encontrado
df_2 = df.fillna(method='ffill')
df_2.drop(0,inplace=True)

# llenar con el valor despues encontrado
df_3 = df.fillna(method='backfill')

# llenar con el valor despues encontrado
#df_2 = df.fillna(method='Interp')

df_4 = df.interpolate(method='linear')

df_nan =  df.dropna(how = 'all')

# interpolando sola una columna
df_3 = df
df_3[['USDCOP Curncy']] =\
 df[['USDCOP Curncy']].interpolate(method='linear')

# Interpolando en forma horizontal
df_4 = df.interpolate(method='linear')
df_5 = df_4.drop(columns=["date"])

df_6 = df_5.interpolate(method='linear',axis=1)
                 
df_5.interpolate(method='linear',axis=1,inplace=True)



df_5 = df
df_5.index = df["date"]
df_5 = df.drop(columns=["date"])

df_5.interpolate(method='linear',axis=1,inplace=True)

df_4.dtypes

df_4 = df.interpolate(method='linear')
df_na = df_4.isna()

# para verificar si alguna columna posee algun nan
df_4.isna().any()
df_4.isna().all()


df.isna().any()
df.index = df['date']
df.drop(columns=['date'], inplace=True)
df.isna().any(axis=1)

# para ver todas las librerias instaladas en python:
# pip list

# para instalar una nueva librería:
# pip install nombre_libreria
# ejemplo:
# pip install pandas

# Lectura  de las ventas
# Ver gráficos
import pandas as pd
import matplotlib.pyplot as plt

ventas = pd.read_excel('Ventas_comercial.xlsx')
plt.hist('Cantidad',data = ventas)
plt.title('Mi primer histograma')
plt.savefig('mi_primer_historgrama.jpeg')

plt.plot('Fecha','Cantidad','bo',\
         label='Cantidad',data = ventas)
plt.title('Mi primer plot')
plt.savefig('mi_primer_plot.jpeg')


plt.plot('Fecha','Cantidad','r+',\
         label='Cantidad',data = ventas)

# las libreria matplotlib le agrega funcionalidades a la libreria pandas
ventas.plot('Fecha','Cantidad')
ventas.plot('Fecha','Cantidad',title = 'cantidad vendida')
ventas.hist('Cantidad')
plt.savefig('grafico.jpeg')

ventas.boxplot('Cantidad')
df= ventas.describe()



