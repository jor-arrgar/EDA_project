import pandas as pd
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objects as go
import os
import matplotlib.pyplot as plt

#Casos covid por ccaa
covid_semanal_ccaa = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/covid_semanal_ccaa.csv' , sep= ';')

lista_ccaa = list(covid_semanal_ccaa.columns.values)
lista_ccaa = lista_ccaa[1:]
print(lista_ccaa)

casos_totales = [] #Casos en España (suma de todas las ccaa)
for pos , semana in enumerate(list(covid_semanal_ccaa['Semana'])):
    casos = 0
    for ccaa in lista_ccaa:
        casos += covid_semanal_ccaa.iloc[pos].loc[ccaa]
    casos_totales.append(casos)
covid_semanal_ccaa['España'] = casos_totales

lista_ccaa = list(covid_semanal_ccaa.columns.values)
lista_ccaa = lista_ccaa[1:]
    #Generacion de grafica
andalucia = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[0]] , name= lista_ccaa[0] , mode= 'lines' , marker= dict(color= '#f44336'))
aragon = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[1]] , name= lista_ccaa[1] , mode= 'lines' , marker= dict(color= '#744700'))
asturias = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[2]] , name= lista_ccaa[2] , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[3]] , name= ('Baleares, Islas') , mode= 'lines' , marker= dict(color= '#8fce00'))
canarias = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[4]] , name= ('Canarias, Islas') , mode= 'lines' , marker= dict(color= '#2986cc'))
cantabria = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[5]] , name= lista_ccaa[5] , mode= 'lines' , marker= dict(color= '#16537e'))
cataluña = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[6]] , name= lista_ccaa[6] , mode= 'lines' , marker= dict(color= '#6a329f'))
clm = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[7]] , name= lista_ccaa[7] , mode= 'lines' , marker= dict(color= '#c90076'))
cyl = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[8]] , name= lista_ccaa[8] , mode= 'lines' , marker= dict(color= '#990000'))
ceuta = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[9]] , name= lista_ccaa[9] , mode= 'lines' , marker= dict(color= '#b45f06'))
c_valenciana = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[10]] , name= lista_ccaa[10] , mode= 'lines' , marker= dict(color= '#bf9000'))
extrem = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[11]] , name= lista_ccaa[11] , mode= 'lines' , marker= dict(color= '#38761d'))
galicia = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[12]] , name= lista_ccaa[12] , mode= 'lines' , marker= dict(color= '#134f5c'))
rioja = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[13]] , name= lista_ccaa[13] , mode= 'lines' , marker= dict(color= '#0b5394'))
madrid = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[14]] , name= lista_ccaa[14] , mode= 'lines' , marker= dict(color= '#351c75'))
melilla = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[15]] , name= lista_ccaa[15] , mode= 'lines' , marker= dict(color= '#741b47'))
murcia = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[16]] , name= lista_ccaa[16] , mode= 'lines' , marker= dict(color= '#e06666'))
navarra = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[17]] , name= lista_ccaa[17] , mode= 'lines' , marker= dict(color= '#93c47d'))
pv = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[18]] , name= lista_ccaa[18] , mode= 'lines' , marker= dict(color= '#6fa8dc'))
españa = go.Scatter(x= covid_semanal_ccaa['Semana'] , y= covid_semanal_ccaa[lista_ccaa[19]] , name= lista_ccaa[19] , mode= 'lines' , marker= dict(color= '#000000'))

data = [españa , andalucia , aragon , asturias , baleares , canarias , cantabria , cataluña , clm , cyl , ceuta , c_valenciana , extrem , galicia , rioja , madrid , melilla , murcia , navarra , pv]
layout = dict(title= 'Casos semanales de covid19 por CCAA' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de casos'))

fig_covid_semanal_ccaa = go.Figure(data= data , layout=layout)

#Casos covid por provincia
covid_semanal_prov = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/covid_semanal_provincias.csv' , sep= ';')

lista_provincias = list(covid_semanal_prov.columns.values)
lista_provincias = lista_provincias[1:]

casos_totales_prov = [] #Casos en España (suma de todas las provincias)
for pos , semana in enumerate(list(covid_semanal_prov['Semana'])):
    casos = 0
    for provincia in lista_provincias:
        casos += covid_semanal_prov.iloc[pos].loc[provincia]
    casos_totales_prov.append(casos)
covid_semanal_prov['España'] = casos_totales_prov
casos_totales == casos_totales_prov

lista_provincias = list(covid_semanal_prov.columns.values)

    #Generacion de grafica
alava = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[1]] , name= lista_provincias[1] , mode= 'lines' , marker= dict(color= '#f44336'))
albacete = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[2]] , name= lista_provincias[2] , mode= 'lines' , marker= dict(color= '#744700'))
alicante = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[3]] , name= lista_provincias[3] , mode= 'lines' , marker= dict(color= '#ce7e00'))
almeria = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[4]] , name= lista_provincias[4] , mode= 'lines' , marker= dict(color= '#8fce00'))
asturias = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[5]] , name= lista_provincias[5] , mode= 'lines' , marker= dict(color= '#2986cc'))
avila = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[6]] , name= lista_provincias[6] , mode= 'lines' , marker= dict(color= '#16537e'))
badajoz = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[7]] , name= lista_provincias[7] , mode= 'lines' , marker= dict(color= '#6a329f'))
barcelona = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[8]] , name= lista_provincias[8] , mode= 'lines' , marker= dict(color= '#ea9999'))
burgos = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[9]] , name= lista_provincias[9] , mode= 'lines' , marker= dict(color= '#f9cb9c'))
caceres = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[10]] , name= lista_provincias[10] , mode= 'lines' , marker= dict(color= '#ffe599'))
cadiz = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[11]] , name= lista_provincias[11] , mode= 'lines' , marker= dict(color= '#b6d7a8'))
cantabria = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[12]] , name= lista_provincias[12] , mode= 'lines' , marker= dict(color= '#a2c4c9'))
castellon = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[13]] , name= lista_provincias[13] , mode= 'lines' , marker= dict(color= '#9fc5e8'))
ceuta = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[14]] , name= lista_provincias[14] , mode= 'lines' , marker= dict(color= '#b4a7d6'))
ciudad_real = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[15]] , name= lista_provincias[15] , mode= 'lines' , marker= dict(color= '#d5a6bd'))
cordoba = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[16]] , name= lista_provincias[16] , mode= 'lines' , marker= dict(color= '#cc0000'))
cuenca = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[17]] , name= lista_provincias[17] , mode= 'lines' , marker= dict(color= '#e69138'))
gerona = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[18]] , name= lista_provincias[18] , mode= 'lines' , marker= dict(color= '#f1c232'))
granada = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[19]] , name= lista_provincias[19] , mode= 'lines' , marker= dict(color= '#6aa84f'))
guadalajara = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[20]] , name= lista_provincias[20] , mode= 'lines' , marker= dict(color= '#45818e'))
guipuzcoa = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[21]] , name= lista_provincias[21] , mode= 'lines' , marker= dict(color= '#3d85c6'))
huelva = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[22]] , name= lista_provincias[22] , mode= 'lines' , marker= dict(color= '#674ea7'))
huesca = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[23]] , name= lista_provincias[23] , mode= 'lines' , marker= dict(color= '#a64d79'))
jaen = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[24]] , name= lista_provincias[25] , mode= 'lines' , marker= dict(color= '#990000'))
coruña = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[25]] , name= lista_provincias[25] , mode= 'lines' , marker= dict(color= '#b45f06'))
rioja = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[26]] , name= lista_provincias[26] , mode= 'lines' , marker= dict(color= '#bf9000'))
las_palmas = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[27]] , name= lista_provincias[27] , mode= 'lines' , marker= dict(color= '#38761d'))
leon = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[28]] , name= lista_provincias[28] , mode= 'lines' , marker= dict(color= '#134f5c'))
lerida = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[29]] , name= lista_provincias[29] , mode= 'lines' , marker= dict(color= '#0b5394'))
lugo = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[30]] , name= lista_provincias[30] , mode= 'lines' , marker= dict(color= '#351c75'))
madrid = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[31]] , name= lista_provincias[31] , mode= 'lines' , marker= dict(color= '#741b47'))
malaga = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[32]] , name= lista_provincias[32] , mode= 'lines' , marker= dict(color= '#e06666'))
melilla = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[33]] , name= lista_provincias[33] , mode= 'lines' , marker= dict(color= '#f6b26b'))
murcia = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[34]] , name= lista_provincias[34] , mode= 'lines' , marker= dict(color= '#ffd966'))
navarra = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[35]] , name= lista_provincias[35] , mode= 'lines' , marker= dict(color= '#93c47d'))
orense = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[36]] , name= lista_provincias[36] , mode= 'lines' , marker= dict(color= '#76a5af'))
palencia = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[37]] , name= lista_provincias[37] , mode= 'lines' , marker= dict(color= '#6fa8dc'))
pontevedra = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[38]] , name= lista_provincias[38] , mode= 'lines' , marker= dict(color= '#8e7cc3'))
salamanca = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[39]] , name= lista_provincias[39] , mode= 'lines' , marker= dict(color= '#c27ba0'))
tenerife = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[40]] , name= lista_provincias[40] , mode= 'lines' , marker= dict(color= '#990000'))
segovia = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[41]] , name= lista_provincias[41] , mode= 'lines' , marker= dict(color= '#b45f06'))
sevilla = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[42]] , name= lista_provincias[42] , mode= 'lines' , marker= dict(color= '#bf9000'))
soria = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[43]] , name= lista_provincias[43] , mode= 'lines' , marker= dict(color= '#38761d'))
tarragona = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[44]] , name= lista_provincias[44] , mode= 'lines' , marker= dict(color= '#134f5c'))
teruel = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[45]] , name= lista_provincias[45] , mode= 'lines' , marker= dict(color= '#0b5394'))
toledo = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[46]] , name= lista_provincias[46] , mode= 'lines' , marker= dict(color= '#351c75'))
valencia = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[47]] , name= lista_provincias[47] , mode= 'lines' , marker= dict(color= '#741b47'))
valladolid = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[48]] , name= lista_provincias[48] , mode= 'lines' , marker= dict(color= '#444444'))
vizcaya = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[49]] , name= lista_provincias[49] , mode= 'lines' , marker= dict(color= '#999999'))
zamora = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[50]] , name= lista_provincias[50] , mode= 'lines' , marker= dict(color= '#05e75c'))
zaragoza = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[51]] , name= lista_provincias[51] , mode= 'lines' , marker= dict(color= '#ccff00'))
españa = go.Scatter(x= covid_semanal_prov['Semana'] , y= covid_semanal_prov[lista_provincias[52]] , name= lista_provincias[52] , mode= 'lines' , marker= dict(color= '#000000'))

data = [españa , alava , albacete , alicante , almeria , asturias , avila , badajoz , barcelona , burgos , caceres , cadiz , cantabria , castellon , ceuta , ciudad_real , cordoba , cuenca , gerona , granada , guadalajara , guipuzcoa , huelva , huesca , jaen , coruña , rioja , las_palmas , leon , lerida , lugo , madrid , malaga , melilla , murcia , navarra , orense , palencia , pontevedra , salamanca , tenerife , segovia , sevilla , soria , tarragona , teruel , toledo , valencia , valladolid , vizcaya , zamora , zaragoza]
layout = dict(title= 'Casos semanales de covid19 por provincia' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de casos'))

fig_covid_semanal_prov = go.Figure(data= data , layout= layout)

#Graficas de ingresos y defunciones

df_alava = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/alava_provincias_completo.csv' , sep= ';')
df_albacete = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/albacete_provincias_completo.csv' , sep= ';')
df_alicante = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/alicante_provincias_completo.csv' , sep= ';')
df_almeria = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/almeria_provincias_completo.csv' , sep= ';')
df_asturias = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/asturias_provincias_completo.csv' , sep= ';')
df_avila = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/avila_provincias_completo.csv' , sep= ';')
df_badajoz = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/badajoz_provincias_completo.csv' , sep= ';')
df_baleares = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/barcelona_provincias_completo.csv' , sep= ';')
df_barcelona =pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/barcelona_provincias_completo.csv' , sep= ';') 
df_burgos = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/burgos_provincias_completo.csv' , sep= ';')
df_caceres = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/caceres_provincias_completo.csv' , sep= ';')
df_cadiz = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/cadiz_provincias_completo.csv' , sep= ';')
df_cantabria =pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/cantabria_provincias_completo.csv' , sep= ';') 
df_castellon =pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/castellon_provincias_completo.csv' , sep= ';') 
df_ceuta = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/ceuta_provincias_completo.csv' , sep= ';')
df_ciudad_real = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/ciudad_real_provincias_completo.csv' , sep= ';')
df_cordoba = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/cordoba_provincias_completo.csv' , sep= ';')
df_cuenca = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/cuenca_provincias_completo.csv' , sep= ';')
df_gerona = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/gerona_provincias_completo.csv' , sep= ';')
df_granada = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/granada_provincias_completo.csv' , sep= ';')
df_guadalajara = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/guadalajara_provincias_completo.csv' , sep= ';')
df_guipuzcoa = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/guipuzcoa_provincias_completo.csv' , sep= ';')
df_huelva = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/huelva_provincias_completo.csv' , sep= ';')
df_huesca = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/huesca_provincias_completo.csv' , sep= ';')
df_jaen = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/jaen_provincias_completo.csv' , sep= ';')
df_coruña = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/coruña_provincias_completo.csv' , sep= ';')
df_rioja = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/rioja_provincias_completo.csv' , sep= ';')
df_las_palmas = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/palmas_provincias_completo.csv' , sep= ';')
df_leon = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/leon_provincias_completo.csv' , sep= ';')
df_lerida = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/lerida_provincias_completo.csv' , sep= ';')
df_lugo = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/lugo_provincias_completo.csv' , sep= ';')
df_madrid = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/madrid_provincias_completo.csv' , sep= ';')
df_malaga = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/malaga_provincias_completo.csv' , sep= ';')
df_melilla = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/melilla_provincias_completo.csv' , sep= ';')
df_murcia = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/murcia_provincias_completo.csv' , sep= ';')
df_navarra = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/navarra_provincias_completo.csv' , sep= ';')
df_orense = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/orense_provincias_completo.csv' , sep= ';')
df_palencia = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/palencia_provincias_completo.csv' , sep= ';')
df_pontevedra = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/pontevedra_provincias_completo.csv' , sep= ';')
df_salamanca = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/salamanca_provincias_completo.csv' , sep= ';')
df_tenerife = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/tenerife_provincias_completo.csv' , sep= ';')
df_segovia = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/segovia_provincias_completo.csv' , sep= ';')
df_sevilla = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/sevilla_provincias_completo.csv' , sep= ';')
df_soria = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/soria_provincias_completo.csv' , sep= ';')
df_tarragona = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/tarragona_provincias_completo.csv' , sep= ';')
df_teruel = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/teruel_provincias_completo.csv' , sep= ';')
df_toledo = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/toledo_provincias_completo.csv' , sep= ';')
df_valencia = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/valencia_provincias_completo.csv' , sep= ';')
df_valladolid = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/valladoli_provincias_completo.csv' , sep= ';')
df_vizcaya = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/vizcaya_provincias_completo.csv' , sep= ';')
df_zamora = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/zamora_provincias_completo.csv' , sep= ';')
df_zaragoza = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/provincias_completo/zaragoza_provincias_completo.csv' , sep= ';')

# Alava
casos = go.Scatter(x= df_alava['Semana'] , y= df_alava['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_alava['Semana'] , y= df_alava['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_alava['Semana'] , y= df_alava['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_alava['Semana'] , y= df_alava['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Alava' , xaxis= dict(title= 'Semana'))

fig_alava = go.Figure(data= data , layout= layout)
iplot(fig_alava)

#Albacete
casos = go.Scatter(x= df_albacete['Semana'] , y= df_albacete['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_albacete['Semana'] , y= df_albacete['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_albacete['Semana'] , y= df_albacete['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_albacete['Semana'] , y= df_albacete['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Albacete' , xaxis= dict(title= 'Semana'))

fig_albacete = go.Figure(data= data , layout= layout)
iplot(fig_albacete)

#Alicante
casos = go.Scatter(x= df_alicante['Semana'] , y= df_alicante['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_alicante['Semana'] , y= df_alicante['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_alicante['Semana'] , y= df_alicante['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_alicante['Semana'] , y= df_alicante['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Alicante' , xaxis= dict(title= 'Semana'))

fig_alicante = go.Figure(data= data , layout= layout)
iplot(fig_alicante)

#Almeria
casos = go.Scatter(x= df_almeria['Semana'] , y= df_almeria['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_almeria['Semana'] , y= df_almeria['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_almeria['Semana'] , y= df_almeria['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_almeria['Semana'] , y= df_almeria['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Almeria' , xaxis= dict(title= 'Semana'))

fig_almeria = go.Figure(data= data , layout= layout)
iplot(fig_almeria)

#Asturias
casos = go.Scatter(x= df_asturias['Semana'] , y= df_asturias['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_asturias['Semana'] , y= df_asturias['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_asturias['Semana'] , y= df_asturias['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_asturias['Semana'] , y= df_asturias['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Asturias' , xaxis= dict(title= 'Semana'))

fig_asturias = go.Figure(data= data , layout= layout)
iplot(fig_asturias)

#Avila
casos = go.Scatter(x= df_avila['Semana'] , y= df_avila['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_avila['Semana'] , y= df_avila['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_avila['Semana'] , y= df_avila['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_avila['Semana'] , y= df_avila['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Ávila' , xaxis= dict(title= 'Semana'))

fig_avila = go.Figure(data= data , layout= layout)
iplot(fig_avila)

#Badajoz
casos = go.Scatter(x= df_badajoz['Semana'] , y= df_badajoz['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_badajoz['Semana'] , y= df_badajoz['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_badajoz['Semana'] , y= df_badajoz['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_badajoz['Semana'] , y= df_badajoz['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Badajoz' , xaxis= dict(title= 'Semana'))

fig_badajoz = go.Figure(data= data , layout= layout)
iplot(fig_badajoz)

#Baleares
casos = go.Scatter(x= df_baleares['Semana'] , y= df_baleares['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_baleares['Semana'] , y= df_baleares['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_baleares['Semana'] , y= df_baleares['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_baleares['Semana'] , y= df_baleares['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Baleares, Islas' , xaxis= dict(title= 'Semana'))

fig_baleares = go.Figure(data= data , layout= layout)
iplot(fig_baleares)

#Barcelona
casos = go.Scatter(x= df_barcelona['Semana'] , y= df_barcelona['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_barcelona['Semana'] , y= df_barcelona['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_barcelona['Semana'] , y= df_barcelona['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_barcelona['Semana'] , y= df_barcelona['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Barcelona' , xaxis= dict(title= 'Semana'))

fig_barcelona = go.Figure(data= data , layout= layout)
iplot(fig_barcelona)

#Burgos
casos = go.Scatter(x= df_burgos['Semana'] , y= df_burgos['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_burgos['Semana'] , y= df_burgos['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_burgos['Semana'] , y= df_burgos['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_burgos['Semana'] , y= df_burgos['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Burgos' , xaxis= dict(title= 'Semana'))

fig_burgos = go.Figure(data= data , layout= layout)
iplot(fig_burgos)

#Caceres
casos = go.Scatter(x= df_caceres['Semana'] , y= df_caceres['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_caceres['Semana'] , y= df_caceres['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_caceres['Semana'] , y= df_caceres['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_caceres['Semana'] , y= df_caceres['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Cáceres' , xaxis= dict(title= 'Semana'))

fig_caceres = go.Figure(data= data , layout= layout)
iplot(fig_caceres)

#Cadiz
casos = go.Scatter(x= df_cadiz['Semana'] , y= df_cadiz['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_cadiz['Semana'] , y= df_cadiz['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_cadiz['Semana'] , y= df_cadiz['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_cadiz['Semana'] , y= df_cadiz['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Cádiz' , xaxis= dict(title= 'Semana'))

fig_cadiz = go.Figure(data= data , layout= layout)
iplot(fig_cadiz)

#Cantabria
casos = go.Scatter(x= df_cantabria['Semana'] , y= df_cantabria['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_cantabria['Semana'] , y= df_cantabria['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_cantabria['Semana'] , y= df_cantabria['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_cantabria['Semana'] , y= df_cantabria['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Cantabria' , xaxis= dict(title= 'Semana'))

fig_cantabria = go.Figure(data= data , layout= layout)
iplot(fig_cantabria)

#Castellon
casos = go.Scatter(x= df_castellon['Semana'] , y= df_castellon['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_castellon['Semana'] , y= df_castellon['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_castellon['Semana'] , y= df_castellon['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_castellon['Semana'] , y= df_castellon['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Castellón' , xaxis= dict(title= 'Semana'))

fig_castellon = go.Figure(data= data , layout= layout)
iplot(fig_castellon)

#Ceuta
casos = go.Scatter(x= df_ceuta['Semana'] , y= df_ceuta['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_ceuta['Semana'] , y= df_ceuta['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_ceuta['Semana'] , y= df_ceuta['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_ceuta['Semana'] , y= df_ceuta['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Ceuta' , xaxis= dict(title= 'Semana'))

fig_ceuta = go.Figure(data= data , layout= layout)
iplot(fig_ceuta)

#Ciudad Real
casos = go.Scatter(x= df_ciudad_real['Semana'] , y= df_ciudad_real['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_ciudad_real['Semana'] , y= df_ciudad_real['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_ciudad_real['Semana'] , y= df_ciudad_real['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_ciudad_real['Semana'] , y= df_ciudad_real['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Ciudad Real' , xaxis= dict(title= 'Semana'))

fig_ciudad_real = go.Figure(data= data , layout= layout)
iplot(fig_ciudad_real)

#Cordoba
casos = go.Scatter(x= df_cordoba['Semana'] , y= df_cordoba['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_cordoba['Semana'] , y= df_cordoba['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_cordoba['Semana'] , y= df_cordoba['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_cordoba['Semana'] , y= df_cordoba['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Córdoba' , xaxis= dict(title= 'Semana'))

fig_cordoba = go.Figure(data= data , layout= layout)
iplot(fig_cordoba)

#La Coruña
casos = go.Scatter(x= df_coruña['Semana'] , y= df_coruña['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_coruña['Semana'] , y= df_coruña['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_coruña['Semana'] , y= df_coruña['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_coruña['Semana'] , y= df_coruña['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'La Coruña' , xaxis= dict(title= 'Semana'))

fig_coruña = go.Figure(data= data , layout= layout)
iplot(fig_coruña)

#Cuenca
casos = go.Scatter(x= df_cuenca['Semana'] , y= df_cuenca['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_cuenca['Semana'] , y= df_cuenca['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_cuenca['Semana'] , y= df_cuenca['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_cuenca['Semana'] , y= df_cuenca['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Cuenca' , xaxis= dict(title= 'Semana'))

fig_cuenca = go.Figure(data= data , layout= layout)
iplot(fig_cuenca)

#Gerona
casos = go.Scatter(x= df_gerona['Semana'] , y= df_gerona['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_gerona['Semana'] , y= df_gerona['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_gerona['Semana'] , y= df_gerona['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_gerona['Semana'] , y= df_gerona['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Gerona' , xaxis= dict(title= 'Semana'))

fig_gerona = go.Figure(data= data , layout= layout)
iplot(fig_gerona)

#Granada
casos = go.Scatter(x= df_granada['Semana'] , y= df_granada['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_granada['Semana'] , y= df_granada['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_granada['Semana'] , y= df_granada['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_granada['Semana'] , y= df_granada['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Granada' , xaxis= dict(title= 'Semana'))

fig_granada = go.Figure(data= data , layout= layout)
iplot(fig_granada)

#Guadalajara
casos = go.Scatter(x= df_guadalajara['Semana'] , y= df_guadalajara['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_guadalajara['Semana'] , y= df_guadalajara['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_guadalajara['Semana'] , y= df_guadalajara['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_guadalajara['Semana'] , y= df_guadalajara['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Guadalajara' , xaxis= dict(title= 'Semana'))

fig_guadalajara = go.Figure(data= data , layout= layout)
iplot(fig_guadalajara)

#Guipuzcoa
casos = go.Scatter(x= df_guipuzcoa['Semana'] , y= df_guipuzcoa['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_guipuzcoa['Semana'] , y= df_guipuzcoa['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_guipuzcoa['Semana'] , y= df_guipuzcoa['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_guipuzcoa['Semana'] , y= df_guipuzcoa['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Guipúzcoa' , xaxis= dict(title= 'Semana'))

fig_guipuzcoa = go.Figure(data= data , layout= layout)
iplot(fig_guipuzcoa)

#Huelva
casos = go.Scatter(x= df_huelva['Semana'] , y= df_huelva['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_huelva['Semana'] , y= df_huelva['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_huelva['Semana'] , y= df_huelva['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_huelva['Semana'] , y= df_huelva['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Huelva' , xaxis= dict(title= 'Semana'))

fig_huelva = go.Figure(data= data , layout= layout)
iplot(fig_huelva)

#Huesca
casos = go.Scatter(x= df_huesca['Semana'] , y= df_huesca['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_huesca['Semana'] , y= df_huesca['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_huesca['Semana'] , y= df_huesca['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_huesca['Semana'] , y= df_huesca['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Huesca' , xaxis= dict(title= 'Semana'))

fig_huesca = go.Figure(data= data , layout= layout)
iplot(fig_huesca)

#Jaen
casos = go.Scatter(x= df_jaen['Semana'] , y= df_jaen['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_jaen['Semana'] , y= df_jaen['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_jaen['Semana'] , y= df_jaen['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_jaen['Semana'] , y= df_jaen['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Jaen' , xaxis= dict(title= 'Semana'))

fig_jaen = go.Figure(data= data , layout= layout)
iplot(fig_jaen)

#Leon
casos = go.Scatter(x= df_leon['Semana'] , y= df_leon['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_leon['Semana'] , y= df_leon['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_leon['Semana'] , y= df_leon['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_leon['Semana'] , y= df_leon['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'León' , xaxis= dict(title= 'Semana'))

fig_leon = go.Figure(data= data , layout= layout)
iplot(fig_leon)

#Lerida
casos = go.Scatter(x= df_lerida['Semana'] , y= df_lerida['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_lerida['Semana'] , y= df_lerida['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_lerida['Semana'] , y= df_lerida['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_lerida['Semana'] , y= df_lerida['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Lérida' , xaxis= dict(title= 'Semana'))

fig_lerida = go.Figure(data= data , layout= layout)
iplot(fig_lerida)

#Lugo
casos = go.Scatter(x= df_lugo['Semana'] , y= df_lugo['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_lugo['Semana'] , y= df_lugo['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_lugo['Semana'] , y= df_lugo['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_lugo['Semana'] , y= df_lugo['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Lugo' , xaxis= dict(title= 'Semana'))

fig_lugo = go.Figure(data= data , layout= layout)
iplot(fig_lugo)

#Madrid
casos = go.Scatter(x= df_madrid['Semana'] , y= df_madrid['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_madrid['Semana'] , y= df_madrid['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_madrid['Semana'] , y= df_madrid['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_madrid['Semana'] , y= df_madrid['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Madrid' , xaxis= dict(title= 'Semana'))

fig_madrid = go.Figure(data= data , layout= layout)
iplot(fig_madrid)

#Malaga
casos = go.Scatter(x= df_malaga['Semana'] , y= df_malaga['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_malaga['Semana'] , y= df_malaga['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_malaga['Semana'] , y= df_malaga['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_malaga['Semana'] , y= df_malaga['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Málaga' , xaxis= dict(title= 'Semana'))

fig_malaga = go.Figure(data= data , layout= layout)
iplot(fig_malaga)

#Melilla
casos = go.Scatter(x= df_melilla['Semana'] , y= df_melilla['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_melilla['Semana'] , y= df_melilla['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_melilla['Semana'] , y= df_melilla['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_melilla['Semana'] , y= df_melilla['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Melilla' , xaxis= dict(title= 'Semana'))

fig_melilla = go.Figure(data= data , layout= layout)
iplot(fig_melilla)

#Murcia
casos = go.Scatter(x= df_murcia['Semana'] , y= df_murcia['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_murcia['Semana'] , y= df_murcia['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_murcia['Semana'] , y= df_murcia['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_murcia['Semana'] , y= df_murcia['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Murcia' , xaxis= dict(title= 'Semana'))

fig_murcia = go.Figure(data= data , layout= layout)
iplot(fig_murcia)

#Navarra
casos = go.Scatter(x= df_navarra['Semana'] , y= df_navarra['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_navarra['Semana'] , y= df_navarra['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_navarra['Semana'] , y= df_navarra['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_navarra['Semana'] , y= df_navarra['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Navarra' , xaxis= dict(title= 'Semana'))

fig_navarra = go.Figure(data= data , layout= layout)
iplot(fig_navarra)

#Orense
casos = go.Scatter(x= df_orense['Semana'] , y= df_orense['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_orense['Semana'] , y= df_orense['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_orense['Semana'] , y= df_orense['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_orense['Semana'] , y= df_orense['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Orense' , xaxis= dict(title= 'Semana'))

fig_orense = go.Figure(data= data , layout= layout)
iplot(fig_orense)

#Palencia
casos = go.Scatter(x= df_palencia['Semana'] , y= df_palencia['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_palencia['Semana'] , y= df_palencia['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_palencia['Semana'] , y= df_palencia['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_palencia['Semana'] , y= df_palencia['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Palencia' , xaxis= dict(title= 'Semana'))

fig_palencia = go.Figure(data= data , layout= layout)
iplot(fig_palencia)

#Las Palmas
casos = go.Scatter(x= df_las_palmas['Semana'] , y= df_las_palmas['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_las_palmas['Semana'] , y= df_las_palmas['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_las_palmas['Semana'] , y= df_las_palmas['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_las_palmas['Semana'] , y= df_las_palmas['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Las Palmas de Gran Canaria' , xaxis= dict(title= 'Semana'))

fig_las_palmas = go.Figure(data= data , layout= layout)
iplot(fig_las_palmas)

#Pontevedra
casos = go.Scatter(x= df_pontevedra['Semana'] , y= df_pontevedra['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_pontevedra['Semana'] , y= df_pontevedra['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_pontevedra['Semana'] , y= df_pontevedra['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_pontevedra['Semana'] , y= df_pontevedra['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Pontevedra' , xaxis= dict(title= 'Semana'))

fig_pontevedra = go.Figure(data= data , layout= layout)
iplot(fig_pontevedra)

#La Rioja
casos = go.Scatter(x= df_rioja['Semana'] , y= df_rioja['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_rioja['Semana'] , y= df_rioja['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_rioja['Semana'] , y= df_rioja['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_rioja['Semana'] , y= df_rioja['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'La Rioja' , xaxis= dict(title= 'Semana'))

fig_rioja = go.Figure(data= data , layout= layout)
iplot(fig_rioja)

#Salamanca
casos = go.Scatter(x= df_salamanca['Semana'] , y= df_salamanca['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_salamanca['Semana'] , y= df_salamanca['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_salamanca['Semana'] , y= df_salamanca['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_salamanca['Semana'] , y= df_salamanca['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Salamanca' , xaxis= dict(title= 'Semana'))

fig_salamanca = go.Figure(data= data , layout= layout)
iplot(fig_salamanca)

#Segovia
casos = go.Scatter(x= df_segovia['Semana'] , y= df_segovia['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_segovia['Semana'] , y= df_segovia['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_segovia['Semana'] , y= df_segovia['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_segovia['Semana'] , y= df_segovia['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Segovia' , xaxis= dict(title= 'Semana'))

fig_segovia = go.Figure(data= data , layout= layout)
iplot(fig_segovia)

#Sevilla
casos = go.Scatter(x= df_sevilla['Semana'] , y= df_sevilla['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_sevilla['Semana'] , y= df_sevilla['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_sevilla['Semana'] , y= df_sevilla['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_sevilla['Semana'] , y= df_sevilla['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Sevilla' , xaxis= dict(title= 'Semana'))

fig_sevilla = go.Figure(data= data , layout= layout)
iplot(fig_sevilla)

#Soria
casos = go.Scatter(x= df_soria['Semana'] , y= df_soria['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_soria['Semana'] , y= df_soria['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_soria['Semana'] , y= df_soria['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_soria['Semana'] , y= df_soria['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Soria' , xaxis= dict(title= 'Semana'))

fig_soria = go.Figure(data= data , layout= layout)
iplot(fig_soria)

#Tarragona
casos = go.Scatter(x= df_tarragona['Semana'] , y= df_tarragona['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_tarragona['Semana'] , y= df_tarragona['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_tarragona['Semana'] , y= df_tarragona['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_tarragona['Semana'] , y= df_tarragona['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Tarragona' , xaxis= dict(title= 'Semana'))

fig_tarragona = go.Figure(data= data , layout= layout)
iplot(fig_tarragona)

#Tenerife
casos = go.Scatter(x= df_tenerife['Semana'] , y= df_tenerife['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_tenerife['Semana'] , y= df_tenerife['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_tenerife['Semana'] , y= df_tenerife['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_tenerife['Semana'] , y= df_tenerife['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Santa Cruz de Tenerife' , xaxis= dict(title= 'Semana'))

fig_tenerife = go.Figure(data= data , layout= layout)
iplot(fig_tenerife)

#Teruel
casos = go.Scatter(x= df_teruel['Semana'] , y= df_teruel['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_teruel['Semana'] , y= df_teruel['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_teruel['Semana'] , y= df_teruel['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_teruel['Semana'] , y= df_teruel['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Teruel' , xaxis= dict(title= 'Semana'))

fig_teruel = go.Figure(data= data , layout= layout)
iplot(fig_teruel)

#Toledo
casos = go.Scatter(x= df_toledo['Semana'] , y= df_toledo['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_toledo['Semana'] , y= df_toledo['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_toledo['Semana'] , y= df_toledo['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_toledo['Semana'] , y= df_toledo['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Toledo' , xaxis= dict(title= 'Semana'))

fig_toledo = go.Figure(data= data , layout= layout)
iplot(fig_toledo)

#Valencia
casos = go.Scatter(x= df_valencia['Semana'] , y= df_valencia['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_valencia['Semana'] , y= df_valencia['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_valencia['Semana'] , y= df_valencia['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_valencia['Semana'] , y= df_valencia['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Valencia' , xaxis= dict(title= 'Semana'))

fig_valencia = go.Figure(data= data , layout= layout)
iplot(fig_valencia)

#Valladolid
casos = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Vizcaya' , xaxis= dict(title= 'Semana'))

fig_vizcaya = go.Figure(data= data , layout= layout)
iplot(fig_vizcaya)

#Vizcaya
casos = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_vizcaya['Semana'] , y= df_vizcaya['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Vizcaya' , xaxis= dict(title= 'Semana'))

fig_vizcaya = go.Figure(data= data , layout= layout)
iplot(fig_vizcaya)

#Valladolid
casos = go.Scatter(x= df_valladolid['Semana'] , y= df_valladolid['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_valladolid['Semana'] , y= df_valladolid['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_valladolid['Semana'] , y= df_valladolid['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_valladolid['Semana'] , y= df_valladolid['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Valladolid' , xaxis= dict(title= 'Semana'))

fig_valladolid = go.Figure(data= data , layout= layout)
iplot(fig_valladolid)

#Zamora
casos = go.Scatter(x= df_zamora['Semana'] , y= df_zamora['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_zamora['Semana'] , y= df_zamora['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_zamora['Semana'] , y= df_zamora['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_zamora['Semana'] , y= df_zamora['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Zamora' , xaxis= dict(title= 'Semana'))

fig_zamora = go.Figure(data= data , layout= layout)
iplot(fig_zamora)

#Zaragoza
casos = go.Scatter(x= df_zaragoza['Semana'] , y= df_zaragoza['Casos'] , name= 'Casos covid19' , mode= 'lines' , marker= dict(color= '#000000'))
hospitalizaciones = go.Scatter(x= df_zaragoza['Semana'] , y= df_zaragoza['Hospitalizaciones'] , name= 'Hospitalizaciones' , mode= 'lines' , marker= dict(color= '#8fce00'))
uci = go.Scatter(x= df_zaragoza['Semana'] , y= df_zaragoza['Ingresos UCI'] , name= 'Ingresos UCI' , mode= 'lines' , marker= dict(color= '#16537e'))
fallecimientos = go.Scatter(x= df_zaragoza['Semana'] , y= df_zaragoza['Fallecimientos'] , name= 'Fallecimientos' , mode= 'lines' , marker= dict(color= '#f44336'))

data = [casos , hospitalizaciones , uci , fallecimientos]
layout = dict(title= 'Zaragoza' , xaxis= dict(title= 'Semana'))

fig_zaragoza = go.Figure(data= data , layout= layout)
iplot(fig_zaragoza)

# Graficas de camas en hospitales
camas_totales_ccaa = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/asistencia_hospitalaria/total_camas_semana_ccaa.csv' , sep= ';')
camas_covid_ccaa = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/asistencia_hospitalaria/camas_covid_semana_ccaa.csv' , sep= ';')
camas_no_covid_ccaa = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/asistencia_hospitalaria/camas_no_covid_semana_ccaa.csv' , sep= ';')

lista_ccaa = list(camas_totales_ccaa.columns.values)

#Andalucia
camas_libres = camas_totales_ccaa[lista_ccaa[1]] - (camas_covid_ccaa[lista_ccaa[1]] + camas_no_covid_ccaa[lista_ccaa[1]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[1]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[1]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Andalucia' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_andalucia = go.Figure(data= data , layout= layout)

#Aragon
camas_libres = camas_totales_ccaa[lista_ccaa[2]] - (camas_covid_ccaa[lista_ccaa[2]] + camas_no_covid_ccaa[lista_ccaa[2]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[2]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[2]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Aragón' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_aragon = go.Figure(data= data , layout= layout)

#Asturias
camas_libres = camas_totales_ccaa[lista_ccaa[3]] - (camas_covid_ccaa[lista_ccaa[3]] + camas_no_covid_ccaa[lista_ccaa[3]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[3]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[3]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Asturias' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_asturias = go.Figure(data= data , layout= layout)

#Baleares
camas_libres = camas_totales_ccaa[lista_ccaa[12]] - (camas_covid_ccaa[lista_ccaa[12]] + camas_no_covid_ccaa[lista_ccaa[12]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[12]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[12]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Baleares, Islas' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_baleares = go.Figure(data= data , layout= layout)

#Canarias
camas_libres = camas_totales_ccaa[lista_ccaa[13]] - (camas_covid_ccaa[lista_ccaa[13]] + camas_no_covid_ccaa[lista_ccaa[13]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[13]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[13]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Canarias, Islas' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_canarias = go.Figure(data= data , layout= layout)
iplot(fig_camas_canarias)

#Cantabria
camas_libres = camas_totales_ccaa[lista_ccaa[4]] - (camas_covid_ccaa[lista_ccaa[4]] + camas_no_covid_ccaa[lista_ccaa[4]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[4]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[4]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Cantabria' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_cantabria = go.Figure(data= data , layout= layout)
iplot(fig_camas_cantabria)

#Castilla-La mancha
camas_libres = camas_totales_ccaa[lista_ccaa[5]] - (camas_covid_ccaa[lista_ccaa[5]] + camas_no_covid_ccaa[lista_ccaa[5]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[5]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[5]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Castilla-La mancha' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_clm = go.Figure(data= data , layout= layout)

#Castilla y León
camas_libres = camas_totales_ccaa[lista_ccaa[6]] - (camas_covid_ccaa[lista_ccaa[6]] + camas_no_covid_ccaa[lista_ccaa[6]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[6]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[6]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Castilla y León' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_cyl = go.Figure(data= data , layout= layout)

#Cataluña
camas_libres = camas_totales_ccaa[lista_ccaa[7]] - (camas_covid_ccaa[lista_ccaa[7]] + camas_no_covid_ccaa[lista_ccaa[7]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[7]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[7]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Cataluña' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_cataluña = go.Figure(data= data , layout= layout)

#Ceuta
camas_libres = camas_totales_ccaa[lista_ccaa[8]] - (camas_covid_ccaa[lista_ccaa[8]] + camas_no_covid_ccaa[lista_ccaa[8]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[8]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[8]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Ceuta' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_ceuta = go.Figure(data= data , layout= layout)

#Comunidad Valenciana
camas_libres = camas_totales_ccaa[lista_ccaa[9]] - (camas_covid_ccaa[lista_ccaa[9]] + camas_no_covid_ccaa[lista_ccaa[9]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[9]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[9]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Comunidad Valenciana' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_valencia = go.Figure(data= data , layout= layout)

#Extremadura
camas_libres = camas_totales_ccaa[lista_ccaa[10]] - (camas_covid_ccaa[lista_ccaa[10]] + camas_no_covid_ccaa[lista_ccaa[10]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[10]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[10]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Extremadura' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_extrem = go.Figure(data= data , layout= layout)

#Galicia
camas_libres = camas_totales_ccaa[lista_ccaa[11]] - (camas_covid_ccaa[lista_ccaa[11]] + camas_no_covid_ccaa[lista_ccaa[11]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[11]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[11]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Galicia' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_galicia = go.Figure(data= data , layout= layout)

#La Rioja
camas_libres = camas_totales_ccaa[lista_ccaa[14]] - (camas_covid_ccaa[lista_ccaa[14]] + camas_no_covid_ccaa[lista_ccaa[14]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[14]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[14]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'La Rioja' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_rioja = go.Figure(data= data , layout= layout)

#Madrid
camas_libres = camas_totales_ccaa[lista_ccaa[15]] - (camas_covid_ccaa[lista_ccaa[15]] + camas_no_covid_ccaa[lista_ccaa[15]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[15]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[15]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Madrid' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_madrid = go.Figure(data= data , layout= layout)

#Melilla
camas_libres = camas_totales_ccaa[lista_ccaa[16]] - (camas_covid_ccaa[lista_ccaa[16]] + camas_no_covid_ccaa[lista_ccaa[16]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[16]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[16]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Melilla' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_melilla = go.Figure(data= data , layout= layout)

#Murcia
camas_libres = camas_totales_ccaa[lista_ccaa[17]] - (camas_covid_ccaa[lista_ccaa[17]] + camas_no_covid_ccaa[lista_ccaa[17]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[17]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[17]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Murcia' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_murcia = go.Figure(data= data , layout= layout)

#Navarra
camas_libres = camas_totales_ccaa[lista_ccaa[18]] - (camas_covid_ccaa[lista_ccaa[18]] + camas_no_covid_ccaa[lista_ccaa[18]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[18]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[18]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Navarra' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_navarra = go.Figure(data= data , layout= layout)

#Pais Vasco
camas_libres = camas_totales_ccaa[lista_ccaa[19]] - (camas_covid_ccaa[lista_ccaa[19]] + camas_no_covid_ccaa[lista_ccaa[19]])
camas_libres_barra = go.Bar(x= camas_totales_ccaa['Semana'] , y= camas_libres , name= 'Camas libres' , marker= dict(color='#000000'))
camas_covid = go.Bar(x = camas_covid_ccaa['Semana'] , y= camas_covid_ccaa[lista_ccaa[19]] , name= 'Camas ocupadas por pacientes covid19' , marker= dict(color= '#f44336'))
camas_no_covid = go.Bar(x= camas_no_covid_ccaa['Semana'] , y= camas_no_covid_ccaa[lista_ccaa[19]] , name= 'Camas ocupadas por pacientes no covid19' , marker= dict(color= '#2986cc'))

data= [camas_covid , camas_no_covid , camas_libres_barra]
layout = go.Layout(barmode='stack' , title= 'Pais Vasco' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Nº de camas'))

fig_camas_pv = go.Figure(data= data , layout= layout)



