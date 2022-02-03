'''
import pandas as pd
#import plotly
from plotly.offline import init_notebook_mode, iplot, plot
init_notebook_mode(connected=True)
import plotly.graph_objects as go
import os
import matplotlib.pyplot as plt

#Incidencia de covid
covid_semanal_ccaa = pd.read_csv('Scripts/Datasets/Utiles/CNE_covid/covid_semanal_ccaa.csv' , sep= ';')

    #Casos covid en el conjunto de España
lista_ccaa = list(covid_semanal_ccaa.columns.values)
lista_ccaa = lista_ccaa[1:]

casos_totales = []
semanas = list(covid_semanal_ccaa['Semana'])
for pos , semana in enumerate(semanas):
    casos = 0
    for ccaa in lista_ccaa:
        casos += covid_semanal_ccaa.iloc[pos].loc[ccaa]
    casos_totales.append(casos)

    #Calculo de la incidencia en 100.000.
incidencia = []

for semana in casos_totales:
    valor = round((semana * 100000) / 47332614 , 3)
    incidencia.append(valor)

#Incidencia de gripe
total_gripe = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_España.csv' , sep= ';')

total_gripe_2015 = total_gripe[total_gripe['Año'] == 2015]
total_gripe_2016 = total_gripe[total_gripe['Año'] == 2016]
total_gripe_2017 = total_gripe[total_gripe['Año'] == 2017]
total_gripe_2018 = total_gripe[total_gripe['Año'] == 2018]
total_gripe_2019 = total_gripe[total_gripe['Año'] == 2019]
total_gripe_2020 = total_gripe[total_gripe['Año'] == 2020]
total_gripe_2021 = total_gripe[total_gripe['Año'] == 2021]

#Grafica
covid = go.Scatter(x= semanas , y= incidencia , name= 'Covid19' , mode= 'lines' , marker= dict(color='#000000'))

gripe_16 = go.Scatter(x= total_gripe_2016['Semana'] , y= total_gripe_2016['Tasa gripe x 100.000 habitantes total'] , name= 'Gripe 2015' , marker= dict(color= '#f44336'))
gripe_17 = go.Scatter(x= total_gripe_2017['Semana'] , y= total_gripe_2017['Tasa gripe x 100.000 habitantes total'] , name= 'Gripe 2015' , marker= dict(color= '#8fce00'))
gripe_18 = go.Scatter(x= total_gripe_2018['Semana'] , y= total_gripe_2018['Tasa gripe x 100.000 habitantes total'] , name= 'Gripe 2015' , marker= dict(color= '#2986cc'))
gripe_19 = go.Scatter(x= total_gripe_2019['Semana'] , y= total_gripe_2019['Tasa gripe x 100.000 habitantes total'] , name= 'Gripe 2015' , marker= dict(color= '#6a329f'))
gripe_20 = go.Scatter(x= total_gripe_2020['Semana'] , y= total_gripe_2020['Tasa gripe x 100.000 habitantes total'] , name= 'Gripe 2015' , marker= dict(color= '#744700'))
gripe_21 = go.Scatter(x= total_gripe_2020['Semana'] , y= total_gripe_2020['Tasa gripe x 100.000 habitantes total'] , name= 'Gripe 2015' , marker= dict(color= '#38761d'))

data= [covid , gripe_16 , gripe_17 , gripe_18 , gripe_19 , gripe_20 , gripe_21]
layout = dict(title= 'Covid19 vs Influenza. Incidencia por 100.000 habitantes' , xaxis= dict(title= 'Semana') , yaxis= dict(title= 'Casos por 100.000 habitantes'))

covid_vs_influenza = go.Figure(data= data , layout= layout)
'''


#Conclusiones

conclusiones = '''La covid19, enfermedad causada por el coronavirus SARS-CoV-2 ha supuesto un importante reto sanitario en todo el mundo. En España provocó un importante aumento de la mortalidad, especialmente durante el año 2020. \n
Los sistemas de salud de las diferentes comunidades autónomas no han sufrido un exceso de carga, al menos no en el periodo comprendido entre agosto de 2020 y diciembre de 2021, que es del que se disponen datos. \n
La primera ola fue la más peligrosa y la que mayor proporción de positivos necesitó de ingreso hospitalario; en las olas posteriores, aunque con una incidencia más elevada, las nuevas cepas, el desarrollo de vacunas frente a SARS-CoV-2 y de medicamentos y tratamientos frente a la enfermedad ha disminiudo enormente la presión sobre los sistemas de salud. \n
Las medidas adoptadas contra el virus desde las esferas gubernamentales parecen haber tenido un efecto positivo, pero para poder demostrarlo sería necesario una comparativa frente a un territorio de características demográficas similares a España y que hubiese adoptado un enfoque contrario al que se aplicó aquí.'''