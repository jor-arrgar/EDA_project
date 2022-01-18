import pandas as pd
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objects as go
import os
import matplotlib.pyplot as plt

#Camas por 1000 hab
df1 = pd.read_csv('Scripts/Datasets/Utiles/Indicadores_hospitalarios/camas_x_1000_hab.csv' , sep= ';', encoding='latin')
lista_columnas = list(df1.columns.values)

andalucia = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[1]] , name = 'Andalucia' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[2]] , name = 'Aragón' , mode= 'lines' , marker= dict(color= '#744700'))
asturias = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[3]] , name = 'Asturias' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[4]] , name = 'Baleares, Islas' , mode= 'lines' , marker= dict(color= '#8fce00'))
canarias = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[5]] , name = 'Canarias, Islas' , mode= 'lines' , marker= dict(color= '#2986cc'))
cantabria = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[6]] , name = 'Cantabria' , mode= 'lines' , marker= dict(color= '#16537e'))
clm = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[7]] , name = 'Castilla-La mancha' , mode= 'lines' , marker= dict(color= '#6a329f'))
cyl = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[8]] , name = 'Castilla y León' , mode= 'lines' , marker= dict(color= '#c90076'))
cataluña = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[9]] , name = 'Cataluña' , mode= 'lines' , marker= dict(color= '#990000'))
ceuta = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[10]] , name = 'Ceuta' , mode= 'lines' , marker= dict(color= '#b45f06'))
valencia = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[11]] , name = 'Com. Valenciana' , mode= 'lines' , marker= dict(color= '#bf9000'))
españa = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[12]] , name = 'España (total)' , mode= 'lines' , marker= dict(color= '#000000'))
extrem = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[13]] , name = 'Extremadura' , mode= 'lines' , marker= dict(color= '#38761d'))
galicia = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[14]] , name = 'Galicia' , mode= 'lines' , marker= dict(color= '#134f5c'))
rioja = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[15]] , name = 'La Rioja' , mode= 'lines' , marker= dict(color= '#0b5394'))
madrid = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[16]] , name = 'Madrid' , mode= 'lines' , marker= dict(color= '#351c75'))
melilla = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[17]] , name = 'Melilla' , mode= 'lines' , marker= dict(color= '#741b47'))
murcia = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[18]] , name = 'Murcia' , mode= 'lines' , marker= dict(color= '#e06666'))
navarra = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[19]] , name = 'Navarra' , mode= 'lines' , marker= dict(color= '#f6b26b'))
pv = go.Scatter(x= df1[lista_columnas[0]] , y= df1[lista_columnas[20]] , name = 'Pais Vasco' , mode= 'lines' , marker= dict(color= '#93c47d'))

data = [españa , andalucia , aragon , asturias , baleares , canarias , cantabria , clm , cyl , cataluña , ceuta , valencia , extrem , galicia , rioja , madrid , melilla , murcia , navarra , pv]
layout = dict(title= 'Camas hospitalarias x 1.000 habitantes' , xaxis= dict(title= 'Año') , yaxis= dict(title= 'Camas x 1000 hab'))

camas = go.Figure(data= data , layout=layout)

#Gasto sanitario
df2 = pd.read_csv('Scripts/Datasets/Utiles/Indicadores_hospitalarios/gasto_publico_sanitario_españa.csv' , sep= ';')
df2 = df2.sort_values('a?o' , ascending= True)
df2 = df2.reset_index()

gasto = go.Bar(x= df2['a?o'] , y= df2["valores_2_dec"] , name= 'Gasto sanitario' , marker= dict(color='#50c976'))
data = [gasto]
layout = go.Layout(barmode= 'group')

gasto_sanitario = go.Figure(data= data , layout= layout)



#Porcentaje gasto atencion primaria
df3 = pd.read_csv('Scripts/Datasets/Utiles/Indicadores_hospitalarios/%_gasto_publico_atencion_primaria.csv' , sep= ';')
lista_columnas = list(df3.columns.values)

andalucia = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[1]] , name = 'Andalucia' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[2]] , name = 'Aragón' , mode= 'lines' , marker= dict(color= '#744700'))
asturias = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[3]] , name = 'Asturias' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[4]] , name = 'Baleares, Islas' , mode= 'lines' , marker= dict(color= '#8fce00'))
canarias = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[5]] , name = 'Canarias, Islas' , mode= 'lines' , marker= dict(color= '#2986cc'))
cantabria = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[6]] , name = 'Cantabria' , mode= 'lines' , marker= dict(color= '#16537e'))
clm = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[7]] , name = 'Castilla-La mancha' , mode= 'lines' , marker= dict(color= '#6a329f'))
cyl = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[8]] , name = 'Castilla y León' , mode= 'lines' , marker= dict(color= '#c90076'))
cataluña = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[9]] , name = 'Cataluña' , mode= 'lines' , marker= dict(color= '#990000'))
ceuta = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[10]] , name = 'Ceuta' , mode= 'lines' , marker= dict(color= '#b45f06'))
valencia = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[11]] , name = 'Com. Valenciana' , mode= 'lines' , marker= dict(color= '#bf9000'))
españa = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[12]] , name = 'España (total)' , mode= 'lines' , marker= dict(color= '#000000'))
extrem = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[13]] , name = 'Extremadura' , mode= 'lines' , marker= dict(color= '#38761d'))
galicia = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[14]] , name = 'Galicia' , mode= 'lines' , marker= dict(color= '#134f5c'))
rioja = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[15]] , name = 'La Rioja' , mode= 'lines' , marker= dict(color= '#0b5394'))
madrid = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[16]] , name = 'Madrid' , mode= 'lines' , marker= dict(color= '#351c75'))
melilla = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[17]] , name = 'Melilla' , mode= 'lines' , marker= dict(color= '#741b47'))
murcia = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[18]] , name = 'Murcia' , mode= 'lines' , marker= dict(color= '#e06666'))
navarra = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[19]] , name = 'Navarra' , mode= 'lines' , marker= dict(color= '#f6b26b'))
pv = go.Scatter(x= df3[lista_columnas[0]] , y= df3[lista_columnas[20]] , name = 'Pais Vasco' , mode= 'lines' , marker= dict(color= '#93c47d'))

data = [españa , andalucia , aragon , asturias , baleares , canarias , cantabria , clm , cyl , cataluña , ceuta , valencia , extrem , galicia , rioja , madrid , melilla , murcia , navarra , pv]
layout = dict(title= 'Porcentaje de gasto en atención primaria por CCAA' , xaxis= dict(title= 'Año') , yaxis= dict(title= '%'))

porcentaje_atencion_primaria = go.Figure(data= data , layout= layout)
