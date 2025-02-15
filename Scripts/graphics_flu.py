import pandas as pd
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objects as go


#Separacion en años

#Total
total = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_España.csv' , sep= ';')

total_2015 = total[total['Año'] == 2015]
total_2016 = total[total['Año'] == 2016]
total_2017 = total[total['Año'] == 2017]
total_2018 = total[total['Año'] == 2018]
total_2019 = total[total['Año'] == 2019]
total_2020 = total[total['Año'] == 2020]
total_2021 = total[total['Año'] == 2021]

#Andalucia
andalucia = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Andalucia.csv' , sep= ';')

andalucia_2015 = andalucia[andalucia['Año'] == 2015]
andalucia_2016 = andalucia[andalucia['Año'] == 2016]
andalucia_2017 = andalucia[andalucia['Año'] == 2017]
andalucia_2018 = andalucia[andalucia['Año'] == 2018]
andalucia_2019 = andalucia[andalucia['Año'] == 2019]

#Aragón
aragon = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Aragón.csv' , sep= ';')

aragon_2015 = aragon[aragon['Año'] == 2015]
aragon_2016 = aragon[aragon['Año'] == 2016]
aragon_2017 = aragon[aragon['Año'] == 2017]
aragon_2018 = aragon[aragon['Año'] == 2018]
aragon_2019 = aragon[aragon['Año'] == 2019]

#Asturias
asturias = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Asturias.csv' , sep= ';')

asturias_2015 = asturias[asturias['Año'] == 2015]
asturias_2016 = asturias[asturias['Año'] == 2016]
asturias_2017 = asturias[asturias['Año'] == 2017]
asturias_2018 = asturias[asturias['Año'] == 2018]
asturias_2019 = asturias[asturias['Año'] == 2019]

#Baleares
baleares = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Baleares.csv' , sep= ';')

baleares_2015 = baleares[baleares['Año'] == 2015]
baleares_2016 = baleares[baleares['Año'] == 2016]
baleares_2017 = baleares[baleares['Año'] == 2017]
baleares_2018 = baleares[baleares['Año'] == 2018]
baleares_2019 = baleares[baleares['Año'] == 2019]

#Comunidad valenciana
c_valenciana = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Valencia.csv' , sep= ';')

c_valenciana_2015 = c_valenciana[c_valenciana['Año'] == 2015]
c_valenciana_2016 = c_valenciana[c_valenciana['Año'] == 2016]
c_valenciana_2017 = c_valenciana[c_valenciana['Año'] == 2017]
c_valenciana_2018 = c_valenciana[c_valenciana['Año'] == 2018]
c_valenciana_2019 = c_valenciana[c_valenciana['Año'] == 2019]

#Canarias
canarias = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Canarias.csv' , sep= ';')

canarias_2015 = canarias[canarias['Año'] == 2015]
canarias_2016 = canarias[canarias['Año'] == 2016]
canarias_2017 = canarias[canarias['Año'] == 2017]
canarias_2018 = canarias[canarias['Año'] == 2018]
canarias_2019 = canarias[canarias['Año'] == 2019]

#Cantabria
cantabria = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Cantabria.csv' , sep= ';')

cantabria_2015 = cantabria[cantabria['Año'] == 2015]
cantabria_2016 = cantabria[cantabria['Año'] == 2016]
cantabria_2017 = cantabria[cantabria['Año'] == 2017]
cantabria_2018 = cantabria[cantabria['Año'] == 2018]
cantabria_2019 = cantabria[cantabria['Año'] == 2019]

#Cataluña
cataluña = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Cataluña.csv' , sep= ';')

cataluña_2015 = cataluña[cataluña['Año'] == 2015]
cataluña_2016 = cataluña[cataluña['Año'] == 2016]
cataluña_2017 = cataluña[cataluña['Año'] == 2017]
cataluña_2018 = cataluña[cataluña['Año'] == 2018]
cataluña_2019 = cataluña[cataluña['Año'] == 2019]

#Ceuta
ceuta = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Ceuta.csv' , sep= ';')

ceuta_2015 = ceuta[ceuta['Año'] == 2015]
ceuta_2016 = ceuta[ceuta['Año'] == 2016]
ceuta_2017 = ceuta[ceuta['Año'] == 2017]
ceuta_2018 = ceuta[ceuta['Año'] == 2018]
ceuta_2019 = ceuta[ceuta['Año'] == 2019]

#Castilla-La mancha
clm = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Castilla-La mancha.csv' , sep= ';')

clm_2015 = clm[clm['Año'] == 2015]
clm_2016 = clm[clm['Año'] == 2016]
clm_2017 = clm[clm['Año'] == 2017]
clm_2018 = clm[clm['Año'] == 2018]
clm_2019 = clm[clm['Año'] == 2019]

#Castilla y Leon
cyl = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Castilla y León.csv' , sep= ';')

cyl_2015 = cyl[cyl['Año'] == 2015]
cyl_2016 = cyl[cyl['Año'] == 2016]
cyl_2017 = cyl[cyl['Año'] == 2017]
cyl_2018 = cyl[cyl['Año'] == 2018]
cyl_2019 = cyl[cyl['Año'] == 2019]

#Extremadura
extrem = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Extremadura.csv' , sep= ';')

extrem_2015 = extrem[extrem['Año'] == 2015]
extrem_2016 = extrem[extrem['Año'] == 2016]
extrem_2017 = extrem[extrem['Año'] == 2017]
extrem_2018 = extrem[extrem['Año'] == 2018]
extrem_2019 = extrem[extrem['Año'] == 2019]

#Madrid
madrid = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Madrid.csv' , sep= ';')

madrid_2015 = madrid[madrid['Año'] == 2015]
madrid_2016 = madrid[madrid['Año'] == 2016]
madrid_2017 = madrid[madrid['Año'] == 2017]
madrid_2018 = madrid[madrid['Año'] == 2018]
madrid_2019 = madrid[madrid['Año'] == 2019]

#Melilla
melilla = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Melilla.csv' , sep= ';')

melilla_2015 = melilla[melilla['Año'] == 2015]
melilla_2016 = melilla[melilla['Año'] == 2016]
melilla_2017 = melilla[melilla['Año'] == 2017]
melilla_2018 = melilla[melilla['Año'] == 2018]
melilla_2019 = melilla[melilla['Año'] == 2019]

#Navarra
navarra = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Navarra.csv' , sep= ';')

navarra_2015 = navarra[navarra['Año'] == 2015]
navarra_2016 = navarra[navarra['Año'] == 2016]
navarra_2017 = navarra[navarra['Año'] == 2017]
navarra_2018 = navarra[navarra['Año'] == 2018]
navarra_2019 = navarra[navarra['Año'] == 2019]

#Pais Vasco
pais_vasco = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_Pais Vasco.csv' , sep= ';')

pais_vasco_2015 = pais_vasco[pais_vasco['Año'] == 2015]
pais_vasco_2016 = pais_vasco[pais_vasco['Año'] == 2016]
pais_vasco_2017 = pais_vasco[pais_vasco['Año'] == 2017]
pais_vasco_2018 = pais_vasco[pais_vasco['Año'] == 2018]
pais_vasco_2019 = pais_vasco[pais_vasco['Año'] == 2019]

#Rioja
rioja = pd.read_csv('Scripts/Datasets/Utiles/Casos gripe/tasa_semanal_gripe_La Rioja.csv' , sep= ';')

rioja_2015 = rioja[rioja['Año'] == 2015]
rioja_2016 = rioja[rioja['Año'] == 2016]
rioja_2017 = rioja[rioja['Año'] == 2017]
rioja_2018 = rioja[rioja['Año'] == 2018]
rioja_2019 = rioja[rioja['Año'] == 2019]


#Graficos por territorio

#España
total_15 = go.Scatter(x= total_2015['Semana'] , y= total_2015['Tasa gripe x 100.000 habitantes total'] , name = 'España 2015' , mode= 'lines' , marker= dict(color= '#f44336'))
total_16 = go.Scatter(x= total_2016['Semana'] , y= total_2016['Tasa gripe x 100.000 habitantes total'] , name = 'España 2016' , mode= 'lines' , marker= dict(color= '#744700'))
total_17 = go.Scatter(x= total_2017['Semana'] , y= total_2017['Tasa gripe x 100.000 habitantes total'] , name = 'España 2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
total_18 = go.Scatter(x= total_2018['Semana'] , y= total_2018['Tasa gripe x 100.000 habitantes total'] , name = 'España 2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
total_19 = go.Scatter(x= total_2019['Semana'] , y= total_2019['Tasa gripe x 100.000 habitantes total'] , name = 'España 2019' , mode= 'lines' , marker= dict(color= '#2986cc'))
total_20 = go.Scatter(x= total_2020['Semana'] , y= total_2020['Tasa gripe x 100.000 habitantes total'] , name = 'España 2020' , mode= 'lines' , marker= dict(color= '#16537e'))
total_21 = go.Scatter(x= total_2021['Semana'] , y= total_2021['Tasa gripe x 100.000 habitantes total'] , name = 'España 2021' , mode= 'lines' , marker= dict(color= '#6a329f'))

data = [total_15 , total_16 , total_17 , total_18 , total_19 , total_20 , total_21]

layout = dict(title= 'Casos de gripe en España x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

total_gripe = go.Figure(data= data , layout= layout)

#Andalucia
andalucia_15 = go.Scatter(x= andalucia_2015['Semana'] , y = andalucia_2015['Andalucia'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
andalucia_16 = go.Scatter(x= andalucia_2016['Semana'] , y = andalucia_2016['Andalucia'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
andalucia_17 = go.Scatter(x= andalucia_2017['Semana'] , y = andalucia_2017['Andalucia'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
andalucia_18 = go.Scatter(x= andalucia_2018['Semana'] , y = andalucia_2018['Andalucia'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
andalucia_19 = go.Scatter(x= andalucia_2019['Semana'] , y = andalucia_2019['Andalucia'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [andalucia_15 , andalucia_16 , andalucia_17 , andalucia_18 , andalucia_19]

layout = dict(title= 'Casos de gripe en Andalucía x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_andalucia = go.Figure(data= data , layout= layout)

#Aragon
aragon_15 = go.Scatter(x= aragon_2015['Semana'] , y= aragon_2015['Aragón'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon_16 = go.Scatter(x= aragon_2016['Semana'] , y= aragon_2016['Aragón'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
aragon_17 = go.Scatter(x= aragon_2017['Semana'] , y= aragon_2017['Aragón'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
aragon_18 = go.Scatter(x= aragon_2018['Semana'] , y= aragon_2018['Aragón'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
aragon_19 = go.Scatter(x= aragon_2019['Semana'] , y= aragon_2019['Aragón'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [aragon_15 , aragon_16 , aragon_17 , aragon_18 , aragon_19]
layout = dict(title= 'Casos de gripe en Aragón x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_aragon = go.Figure(data= data , layout= layout)

#Asturias
asturias_15 = go.Scatter(x= asturias_2015['Semana'] , y= asturias_2015['Asturias'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
asturias_16 = go.Scatter(x= asturias_2016['Semana'] , y= asturias_2016['Asturias'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
asturias_17 = go.Scatter(x= asturias_2017['Semana'] , y= asturias_2017['Asturias'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
asturias_18 = go.Scatter(x= asturias_2018['Semana'] , y= asturias_2018['Asturias'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
asturias_19 = go.Scatter(x= asturias_2019['Semana'] , y= asturias_2019['Asturias'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [asturias_15 , asturias_16 , asturias_17 , asturias_18 , asturias_19]
layout = dict(title= 'Casos de gripe en Asturias x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_asturias = go.Figure(data= data , layout= layout)

#Baleares
baleares_15 = go.Scatter(x= baleares_2015['Semana'] , y= baleares_2015['Baleares'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
baleares_16 = go.Scatter(x= baleares_2016['Semana'] , y= baleares_2016['Baleares'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
baleares_17 = go.Scatter(x= baleares_2017['Semana'] , y= baleares_2017['Baleares'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares_18 = go.Scatter(x= baleares_2018['Semana'] , y= baleares_2018['Baleares'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
baleares_19 = go.Scatter(x= baleares_2019['Semana'] , y= baleares_2019['Baleares'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [baleares_15 , baleares_16 , baleares_17 , baleares_18 , baleares_19]
layout = dict(title= 'Casos de gripe en Baleares x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_baleares = go.Figure(data= data , layout= layout)

#Comunidad Valenciana
valencia_15 = go.Scatter(x= c_valenciana_2015['Semana'] , y= c_valenciana_2015['Valencia'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
valencia_16 = go.Scatter(x= c_valenciana_2016['Semana'] , y= c_valenciana_2016['Valencia'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
valencia_17 = go.Scatter(x= c_valenciana_2017['Semana'] , y= c_valenciana_2017['Valencia'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
valencia_18 = go.Scatter(x= c_valenciana_2018['Semana'] , y= c_valenciana_2018['Valencia'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
valencia_19 = go.Scatter(x= c_valenciana_2019['Semana'] , y= c_valenciana_2019['Valencia'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [valencia_15 , valencia_16 , valencia_17 , valencia_18 , valencia_19]
layout = dict(title= 'Casos de gripe en la Comunidad Valenciana x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_valencia = go.Figure(data= data , layout= layout)

#Canarias
canarias_15 = go.Scatter(x= canarias_2015['Semana'] , y= canarias_2015['Canarias'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
canarias_16 = go.Scatter(x= canarias_2016['Semana'] , y= canarias_2016['Canarias'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
canarias_17 = go.Scatter(x= canarias_2017['Semana'] , y= canarias_2017['Canarias'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
canarias_18 = go.Scatter(x= canarias_2018['Semana'] , y= canarias_2018['Canarias'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
canarias_19 = go.Scatter(x= canarias_2019['Semana'] , y= canarias_2019['Canarias'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [canarias_15 , canarias_16 , canarias_17 , canarias_18 , canarias_19]
layout = dict(title= 'Casos de gripe en Canarias x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_canarias = go.Figure(data= data , layout= layout)

iplot(fig_canarias)

#Cantabria
cantabria_15 = go.Scatter(x= cantabria_2015['Semana'] , y= cantabria_2015['Cantabria'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
cantabria_16 = go.Scatter(x= cantabria_2016['Semana'] , y= cantabria_2016['Cantabria'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
cantabria_17 = go.Scatter(x= cantabria_2017['Semana'] , y= cantabria_2017['Cantabria'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
cantabria_18 = go.Scatter(x= cantabria_2018['Semana'] , y= cantabria_2018['Cantabria'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
cantabria_19 = go.Scatter(x= cantabria_2019['Semana'] , y= cantabria_2019['Cantabria'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [cantabria_15 , cantabria_16 , cantabria_17 , cantabria_18 , cantabria_19]
layout = dict(title= 'Casos de gripe en Cantabria x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_cantabria = go.Figure(data= data , layout= layout)

#Cataluña
cataluña_15 = go.Scatter(x= cataluña_2015['Semana'] , y= cataluña_2015['Cataluña'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
cataluña_16 = go.Scatter(x= cataluña_2016['Semana'] , y= cataluña_2016['Cataluña'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
cataluña_17 = go.Scatter(x= cataluña_2017['Semana'] , y= cataluña_2017['Cataluña'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
cataluña_18 = go.Scatter(x= cataluña_2018['Semana'] , y= cataluña_2018['Cataluña'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
cataluña_19 = go.Scatter(x= cataluña_2019['Semana'] , y= cataluña_2019['Cataluña'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [cataluña_15 , cataluña_16 , cataluña_17 , cataluña_18 , cataluña_19]
layout = dict(title= 'Casos de gripe en Cataluña x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_cataluña = go.Figure(data= data , layout= layout)

#Ceuta
ceuta_15 = go.Scatter(x= ceuta_2015['Semana'] , y= ceuta_2015['Ceuta'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
ceuta_16 = go.Scatter(x= ceuta_2016['Semana'] , y= ceuta_2016['Ceuta'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
ceuta_17 = go.Scatter(x= ceuta_2017['Semana'] , y= ceuta_2017['Ceuta'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
ceuta_18 = go.Scatter(x= ceuta_2018['Semana'] , y= ceuta_2018['Ceuta'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
ceuta_19 = go.Scatter(x= ceuta_2019['Semana'] , y= ceuta_2019['Ceuta'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [ceuta_15 , ceuta_16 , ceuta_17 , ceuta_18 , ceuta_19]
layout = dict(title= 'Casos de gripe en Ceuta x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_ceuta = go.Figure(data= data , layout= layout)

#Castilla-La mancha
clm_15 = go.Scatter(x= clm_2015['Semana'] , y= clm_2015['Castilla-La mancha'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
clm_16 = go.Scatter(x= clm_2016['Semana'] , y= clm_2016['Castilla-La mancha'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
clm_17 = go.Scatter(x= clm_2017['Semana'] , y= clm_2017['Castilla-La mancha'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
clm_18 = go.Scatter(x= clm_2018['Semana'] , y= clm_2018['Castilla-La mancha'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
clm_19 = go.Scatter(x= clm_2019['Semana'] , y= clm_2019['Castilla-La mancha'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [clm_15 , clm_16 , clm_17 , clm_18 , clm_19]
layout = dict(title= 'Casos de gripe en Castilla-La mancha x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_clm = go.Figure(data= data , layout= layout)

#Castilla y Leon
cyl_15 = go.Scatter(x= cyl_2015['Semana'] , y= cyl_2015['Castilla y León'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
cyl_16 = go.Scatter(x= cyl_2016['Semana'] , y= cyl_2016['Castilla y León'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
cyl_17 = go.Scatter(x= cyl_2017['Semana'] , y= cyl_2017['Castilla y León'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
cyl_18 = go.Scatter(x= cyl_2018['Semana'] , y= cyl_2018['Castilla y León'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
cyl_19 = go.Scatter(x= cyl_2019['Semana'] , y= cyl_2019['Castilla y León'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [cyl_15 , cyl_16 , cyl_17 , cyl_18 , cyl_19]
layout = dict(title= 'Casos de gripe en Castilla y León x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_cyl = go.Figure(data= data , layout= layout)

#Extremadura
extrem_15 = go.Scatter(x= extrem_2015['Semana'] , y= extrem_2015['Extremadura'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
extrem_16 = go.Scatter(x= extrem_2016['Semana'] , y= extrem_2016['Extremadura'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
extrem_17 = go.Scatter(x= extrem_2017['Semana'] , y= extrem_2017['Extremadura'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
extrem_18 = go.Scatter(x= extrem_2018['Semana'] , y= extrem_2018['Extremadura'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
extrem_19 = go.Scatter(x= extrem_2019['Semana'] , y= extrem_2019['Extremadura'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [extrem_15 , extrem_16 , extrem_17 , extrem_18 , extrem_19]
layout = dict(title= 'Casos de gripe en Extremadura x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_extrem = go.Figure(data= data , layout= layout)

#La Rioja
rioja_15 = go.Scatter(x= rioja_2015['Semana'] , y= rioja_2015['La Rioja'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
rioja_16 = go.Scatter(x= rioja_2016['Semana'] , y= rioja_2016['La Rioja'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
rioja_17 = go.Scatter(x= rioja_2017['Semana'] , y= rioja_2017['La Rioja'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
rioja_18 = go.Scatter(x= rioja_2018['Semana'] , y= rioja_2018['La Rioja'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
rioja_19 = go.Scatter(x= rioja_2019['Semana'] , y= rioja_2019['La Rioja'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [rioja_15 , rioja_16 , rioja_17 , rioja_18 , rioja_19]
layout = dict(title= 'Casos de gripe en La Rioja x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_rioja = go.Figure(data= data , layout= layout)

#Madrid
madrid_15 = go.Scatter(x= madrid_2015['Semana'] , y= madrid_2015['Madrid'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
madrid_16 = go.Scatter(x= madrid_2016['Semana'] , y= madrid_2016['Madrid'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
madrid_17 = go.Scatter(x= madrid_2017['Semana'] , y= madrid_2017['Madrid'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
madrid_18 = go.Scatter(x= madrid_2018['Semana'] , y= madrid_2018['Madrid'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
madrid_19 = go.Scatter(x= madrid_2019['Semana'] , y= madrid_2019['Madrid'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [madrid_15 , madrid_16 , madrid_17 , madrid_18 , madrid_19]
layout = dict(title= 'Casos de gripe en la Comunidad de Madrid x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_madrid = go.Figure(data= data , layout= layout)

#Melilla
melilla_15 = go.Scatter(x= melilla_2015['Semana'] , y= melilla_2015['Melilla'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
melilla_16 = go.Scatter(x= melilla_2016['Semana'] , y= melilla_2016['Melilla'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
melilla_17 = go.Scatter(x= melilla_2017['Semana'] , y= melilla_2017['Melilla'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
melilla_18 = go.Scatter(x= melilla_2018['Semana'] , y= melilla_2018['Melilla'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
melilla_19 = go.Scatter(x= melilla_2019['Semana'] , y= melilla_2019['Melilla'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [melilla_15 , melilla_16 , melilla_17 , melilla_18 , melilla_19]
layout = dict(title= 'Casos de gripe en Melilla x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_melilla = go.Figure(data= data , layout= layout)

#Navarra
navarra_15 = go.Scatter(x= navarra_2015['Semana'] , y= navarra_2015['Navarra'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
navarra_16 = go.Scatter(x= navarra_2016['Semana'] , y= navarra_2016['Navarra'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
navarra_17 = go.Scatter(x= navarra_2017['Semana'] , y= navarra_2017['Navarra'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
navarra_18 = go.Scatter(x= navarra_2018['Semana'] , y= navarra_2018['Navarra'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
navarra_19 = go.Scatter(x= navarra_2019['Semana'] , y= navarra_2019['Navarra'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [navarra_15 , navarra_16 , navarra_17 , navarra_18 , navarra_19]
layout = dict(title= 'Casos de gripe en la Comunidad Foral de Navarra x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_navarra = go.Figure(data= data , layout= layout)

#Pais Vasco
pais_vasco_15 = go.Scatter(x= pais_vasco_2015['Semana'] , y= pais_vasco_2015['Pais Vasco'] , name= '2015' , mode= 'lines' , marker= dict(color= '#f44336'))
pais_vasco_16 = go.Scatter(x= pais_vasco_2016['Semana'] , y= pais_vasco_2016['Pais Vasco'] , name= '2016' , mode= 'lines' , marker= dict(color= '#744700'))
pais_vasco_17 = go.Scatter(x= pais_vasco_2017['Semana'] , y= pais_vasco_2017['Pais Vasco'] , name= '2017' , mode= 'lines' , marker= dict(color= '#ce7e00'))
pais_vasco_18 = go.Scatter(x= pais_vasco_2018['Semana'] , y= pais_vasco_2018['Pais Vasco'] , name= '2018' , mode= 'lines' , marker= dict(color= '#8fce00'))
pais_vasco_19 = go.Scatter(x= pais_vasco_2019['Semana'] , y= pais_vasco_2019['Pais Vasco'] , name= '2019' , mode= 'lines' , marker= dict(color= '#2986cc'))

data = [pais_vasco_15 , pais_vasco_16 , pais_vasco_17 , pais_vasco_18 , pais_vasco_19]
layout = dict(title= 'Casos de gripe en el Pais Vasco x 100.000 habitantes' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_pais_vasco = go.Figure(data= data , layout= layout)

#Graficas por año

#2015
total_15 = go.Scatter(x= total_2015['Semana'] , y= total_2015['Tasa gripe x 100.000 habitantes total'] , name= 'Total nacional' , mode= 'lines' , marker= dict(color= '#000000'))
andalucia_15 = go.Scatter(x= andalucia_2015['Semana'] , y= andalucia_2015['Andalucia'] , name= 'Andalucia' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon_15 = go.Scatter(x= aragon_2015['Semana'] , y= aragon_2015['Aragón'] , name= 'Aragón' , mode= 'lines' , marker= dict(color= '#744700'))
asturias_15 = go.Scatter(x= asturias_2015['Semana'] , y= asturias_2015['Asturias'] , name= 'Asturias, Principado de' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares_15 = go.Scatter(x= baleares_2015['Semana'] , y= baleares_2015['Baleares'] , name= 'Baleares, Islas' , mode= 'lines' , marker= dict(color= '#8fce00'))
c_valenciana_15 = go.Scatter(x= c_valenciana_2015['Semana'] , y= c_valenciana_2015['Valencia'] , name= 'Comunidad Valenciana' , mode= 'lines' , marker= dict(color= '#2986cc'))
canarias_15 = go.Scatter(x= canarias_2015['Semana'] , y= canarias_2015['Canarias'] , name= 'Canarias, Islas' , mode= 'lines' , marker= dict(color= '#16537e'))
cantabria_15 = go.Scatter(x= cantabria_2015['Semana'] , y= cantabria_2015['Cantabria'] , name= 'Cantabria' , mode= 'lines' , marker= dict(color= '#6a329f'))
clm_15 = go.Scatter(x= clm_2015['Semana'] , y= clm_2015['Castilla-La mancha'] , name= 'Castilla-La mancha' , mode= 'lines' , marker= dict(color= '#c90076'))
cyl_15 = go.Scatter(x= cyl_2015['Semana'] , y= cyl_2015['Castilla y León'] , name= 'Castilla y León' , mode= 'lines' , marker= dict(color= '#990000'))
cataluña_15 = go.Scatter(x= cataluña_2015['Semana'] , y= cataluña_2015['Cataluña'] , name= 'Cataluña' , mode= 'lines' , marker= dict(color= '#b45f06'))
ceuta_15 = go.Scatter(x= ceuta_2015['Semana'] , y= ceuta_2015['Ceuta'] , name= 'Ceuta, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#bf9000'))
extrem_15 = go.Scatter(x= extrem_2015['Semana'] , y= extrem_2015['Extremadura'] , name= 'Extremadura' , mode= 'lines' , marker= dict(color= '#38761d'))
rioja_15 = go.Scatter(x= rioja_2015['Semana'] , y= rioja_2015['La Rioja'] , name= 'La Rioja' , mode= 'lines' , marker= dict(color= '#134f5c'))
madrid_15 = go.Scatter(x= madrid_2015['Semana'] , y= madrid_2015['Madrid'] , name= 'Madrid, Comunidad de' , mode= 'lines' , marker= dict(color= '#0b5394'))
melilla_15 = go.Scatter(x= melilla_2015['Semana'] , y= melilla_2015['Melilla'] , name= 'Melilla, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#351c75'))
navarra_15 = go.Scatter(x= navarra_2015['Semana'] , y= navarra_2015['Navarra'] , name= 'Navarra, Comunidad Foral de' , mode= 'lines' , marker= dict(color= '#741b47'))
pais_vasco_15 = go.Scatter(x= pais_vasco_2015['Semana'] , y= pais_vasco_2015['Pais Vasco'] , name= 'Pais Vasco' , mode= 'lines' , marker= dict(color= '#660000'))

data = [total_15 , andalucia_15 , aragon_15 , asturias_15 , baleares_15 , canarias_15 , cantabria_15 , clm_15 , cyl_15 , cataluña_15 , ceuta_15 , c_valenciana_15 , extrem_15 , rioja_15 , madrid_15 , melilla_15 , navarra_15 , pais_vasco_15]
layout = dict(title= 'Casos de gripe x 100.000 habitantes, año 2015' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_2015 = go.Figure(data= data , layout= layout)

#2016
total_16 = go.Scatter(x= total_2016['Semana'] , y= total_2016['Tasa gripe x 100.000 habitantes total'] , name= 'Total nacional' , mode= 'lines' , marker= dict(color= '#000000'))
andalucia_16 = go.Scatter(x= andalucia_2016['Semana'] , y= andalucia_2016['Andalucia'] , name= 'Andalucia' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon_16 = go.Scatter(x= aragon_2016['Semana'] , y= aragon_2016['Aragón'] , name= 'Aragón' , mode= 'lines' , marker= dict(color= '#744700'))
asturias_16 = go.Scatter(x= asturias_2016['Semana'] , y= asturias_2016['Asturias'] , name= 'Asturias, Principado de' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares_16 = go.Scatter(x= baleares_2016['Semana'] , y= baleares_2016['Baleares'] , name= 'Baleares, Islas' , mode= 'lines' , marker= dict(color= '#8fce00'))
c_valenciana_16 = go.Scatter(x= c_valenciana_2016['Semana'] , y= c_valenciana_2016['Valencia'] , name= 'Comunidad Valenciana' , mode= 'lines' , marker= dict(color= '#2986cc'))
canarias_16 = go.Scatter(x= canarias_2016['Semana'] , y= canarias_2016['Canarias'] , name= 'Canarias, Islas' , mode= 'lines' , marker= dict(color= '#16537e'))
cantabria_16 = go.Scatter(x= cantabria_2016['Semana'] , y= cantabria_2016['Cantabria'] , name= 'Cantabria' , mode= 'lines' , marker= dict(color= '#6a329f'))
clm_16 = go.Scatter(x= clm_2016['Semana'] , y= clm_2016['Castilla-La mancha'] , name= 'Castilla-La mancha' , mode= 'lines' , marker= dict(color= '#c90076'))
cyl_16 = go.Scatter(x= cyl_2016['Semana'] , y= cyl_2016['Castilla y León'] , name= 'Castilla y León' , mode= 'lines' , marker= dict(color= '#990000'))
cataluña_16 = go.Scatter(x= cataluña_2016['Semana'] , y= cataluña_2016['Cataluña'] , name= 'Cataluña' , mode= 'lines' , marker= dict(color= '#b45f06'))
ceuta_16 = go.Scatter(x= ceuta_2016['Semana'] , y= ceuta_2016['Ceuta'] , name= 'Ceuta, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#bf9000'))
extrem_16 = go.Scatter(x= extrem_2016['Semana'] , y= extrem_2016['Extremadura'] , name= 'Extremadura' , mode= 'lines' , marker= dict(color= '#38761d'))
rioja_16 = go.Scatter(x= rioja_2016['Semana'] , y= rioja_2016['La Rioja'] , name= 'La Rioja' , mode= 'lines' , marker= dict(color= '#134f5c'))
madrid_16 = go.Scatter(x= madrid_2016['Semana'] , y= madrid_2016['Madrid'] , name= 'Madrid, Comunidad de' , mode= 'lines' , marker= dict(color= '#0b5394'))
melilla_16 = go.Scatter(x= melilla_2016['Semana'] , y= melilla_2016['Melilla'] , name= 'Melilla, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#351c75'))
navarra_16 = go.Scatter(x= navarra_2016['Semana'] , y= navarra_2016['Navarra'] , name= 'Navarra, Comunidad Foral de' , mode= 'lines' , marker= dict(color= '#741b47'))
pais_vasco_16 = go.Scatter(x= pais_vasco_2016['Semana'] , y= pais_vasco_2016['Pais Vasco'] , name= 'Pais Vasco' , mode= 'lines' , marker= dict(color= '#660000'))

data = [total_16 , andalucia_16 , aragon_16 , asturias_16 , baleares_16 , canarias_16 , cantabria_16 , clm_16 , cyl_16 , cataluña_16 , ceuta_16 , c_valenciana_16 , extrem_16 , rioja_16 , madrid_16 , melilla_16 , navarra_16 , pais_vasco_16]
layout = dict(title= 'Casos de gripe x 100.000 habitantes, año 2016' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_2016 = go.Figure(data= data , layout= layout)

#2017
total_17 = go.Scatter(x= total_2017['Semana'] , y= total_2017['Tasa gripe x 100.000 habitantes total'] , name= 'Total nacional' , mode= 'lines' , marker= dict(color= '#000000'))
andalucia_17 = go.Scatter(x= andalucia_2017['Semana'] , y= andalucia_2017['Andalucia'] , name= 'Andalucia' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon_17 = go.Scatter(x= aragon_2017['Semana'] , y= aragon_2017['Aragón'] , name= 'Aragón' , mode= 'lines' , marker= dict(color= '#744700'))
asturias_17 = go.Scatter(x= asturias_2017['Semana'] , y= asturias_2017['Asturias'] , name= 'Asturias, Principado de' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares_17 = go.Scatter(x= baleares_2017['Semana'] , y= baleares_2017['Baleares'] , name= 'Baleares, Islas' , mode= 'lines' , marker= dict(color= '#8fce00'))
c_valenciana_17 = go.Scatter(x= c_valenciana_2017['Semana'] , y= c_valenciana_2017['Valencia'] , name= 'Comunidad Valenciana' , mode= 'lines' , marker= dict(color= '#2986cc'))
canarias_17 = go.Scatter(x= canarias_2017['Semana'] , y= canarias_2017['Canarias'] , name= 'Canarias, Islas' , mode= 'lines' , marker= dict(color= '#16537e'))
cantabria_17 = go.Scatter(x= cantabria_2017['Semana'] , y= cantabria_2017['Cantabria'] , name= 'Cantabria' , mode= 'lines' , marker= dict(color= '#6a329f'))
clm_17 = go.Scatter(x= clm_2017['Semana'] , y= clm_2017['Castilla-La mancha'] , name= 'Castilla-La mancha' , mode= 'lines' , marker= dict(color= '#c90076'))
cyl_17 = go.Scatter(x= cyl_2017['Semana'] , y= cyl_2017['Castilla y León'] , name= 'Castilla y León' , mode= 'lines' , marker= dict(color= '#990000'))
cataluña_17 = go.Scatter(x= cataluña_2017['Semana'] , y= cataluña_2017['Cataluña'] , name= 'Cataluña' , mode= 'lines' , marker= dict(color= '#b45f06'))
ceuta_17 = go.Scatter(x= ceuta_2017['Semana'] , y= ceuta_2017['Ceuta'] , name= 'Ceuta, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#bf9000'))
extrem_17 = go.Scatter(x= extrem_2017['Semana'] , y= extrem_2017['Extremadura'] , name= 'Extremadura' , mode= 'lines' , marker= dict(color= '#38761d'))
rioja_17 = go.Scatter(x= rioja_2017['Semana'] , y= rioja_2017['La Rioja'] , name= 'La Rioja' , mode= 'lines' , marker= dict(color= '#134f5c'))
madrid_17 = go.Scatter(x= madrid_2017['Semana'] , y= madrid_2017['Madrid'] , name= 'Madrid, Comunidad de' , mode= 'lines' , marker= dict(color= '#0b5394'))
melilla_17 = go.Scatter(x= melilla_2017['Semana'] , y= melilla_2017['Melilla'] , name= 'Melilla, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#351c75'))
navarra_17 = go.Scatter(x= navarra_2017['Semana'] , y= navarra_2017['Navarra'] , name= 'Navarra, Comunidad Foral de' , mode= 'lines' , marker= dict(color= '#741b47'))
pais_vasco_17 = go.Scatter(x= pais_vasco_2017['Semana'] , y= pais_vasco_2017['Pais Vasco'] , name= 'Pais Vasco' , mode= 'lines' , marker= dict(color= '#660000'))

data = [total_17 , andalucia_17 , aragon_17 , asturias_17 , baleares_17 , canarias_17 , cantabria_17 , clm_17 , cyl_17 , cataluña_17 , ceuta_17 , c_valenciana_17 , extrem_17 , rioja_17 , madrid_17 , melilla_17 , navarra_17 , pais_vasco_17]
layout = dict(title= 'Casos de gripe x 100.000 habitantes, año 2017' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_2017 = go.Figure(data= data , layout= layout)

#2018
total_18 = go.Scatter(x= total_2018['Semana'] , y= total_2018['Tasa gripe x 100.000 habitantes total'] , name= 'Total nacional' , mode= 'lines' , marker= dict(color= '#000000'))
andalucia_18 = go.Scatter(x= andalucia_2018['Semana'] , y= andalucia_2018['Andalucia'] , name= 'Andalucia' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon_18 = go.Scatter(x= aragon_2018['Semana'] , y= aragon_2018['Aragón'] , name= 'Aragón' , mode= 'lines' , marker= dict(color= '#744700'))
asturias_18 = go.Scatter(x= asturias_2018['Semana'] , y= asturias_2018['Asturias'] , name= 'Asturias, Principado de' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares_18 = go.Scatter(x= baleares_2018['Semana'] , y= baleares_2018['Baleares'] , name= 'Baleares, Islas' , mode= 'lines' , marker= dict(color= '#8fce00'))
c_valenciana_18 = go.Scatter(x= c_valenciana_2018['Semana'] , y= c_valenciana_2018['Valencia'] , name= 'Comunidad Valenciana' , mode= 'lines' , marker= dict(color= '#2986cc'))
canarias_18 = go.Scatter(x= canarias_2018['Semana'] , y= canarias_2018['Canarias'] , name= 'Canarias, Islas' , mode= 'lines' , marker= dict(color= '#16537e'))
cantabria_18 = go.Scatter(x= cantabria_2018['Semana'] , y= cantabria_2018['Cantabria'] , name= 'Cantabria' , mode= 'lines' , marker= dict(color= '#6a329f'))
clm_18 = go.Scatter(x= clm_2018['Semana'] , y= clm_2018['Castilla-La mancha'] , name= 'Castilla-La mancha' , mode= 'lines' , marker= dict(color= '#c90076'))
cyl_18 = go.Scatter(x= cyl_2018['Semana'] , y= cyl_2018['Castilla y León'] , name= 'Castilla y León' , mode= 'lines' , marker= dict(color= '#990000'))
cataluña_18 = go.Scatter(x= cataluña_2018['Semana'] , y= cataluña_2018['Cataluña'] , name= 'Cataluña' , mode= 'lines' , marker= dict(color= '#b45f06'))
ceuta_18 = go.Scatter(x= ceuta_2018['Semana'] , y= ceuta_2018['Ceuta'] , name= 'Ceuta, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#bf9000'))
extrem_18 = go.Scatter(x= extrem_2018['Semana'] , y= extrem_2018['Extremadura'] , name= 'Extremadura' , mode= 'lines' , marker= dict(color= '#38761d'))
rioja_18 = go.Scatter(x= rioja_2018['Semana'] , y= rioja_2018['La Rioja'] , name= 'La Rioja' , mode= 'lines' , marker= dict(color= '#134f5c'))
madrid_18 = go.Scatter(x= madrid_2018['Semana'] , y= madrid_2018['Madrid'] , name= 'Madrid, Comunidad de' , mode= 'lines' , marker= dict(color= '#0b5394'))
melilla_18 = go.Scatter(x= melilla_2018['Semana'] , y= melilla_2018['Melilla'] , name= 'Melilla, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#351c75'))
navarra_18 = go.Scatter(x= navarra_2018['Semana'] , y= navarra_2018['Navarra'] , name= 'Navarra, Comunidad Foral de' , mode= 'lines' , marker= dict(color= '#741b47'))
pais_vasco_18 = go.Scatter(x= pais_vasco_2018['Semana'] , y= pais_vasco_2018['Pais Vasco'] , name= 'Pais Vasco' , mode= 'lines' , marker= dict(color= '#660000'))

data = [total_18 , andalucia_18 , aragon_18 , asturias_18 , baleares_18 , canarias_18 , cantabria_18 , clm_18 , cyl_18 , cataluña_18 , ceuta_18 , c_valenciana_18 , extrem_18 , rioja_18 , madrid_18 , melilla_18 , navarra_18 , pais_vasco_18]
layout = dict(title= 'Casos de gripe x 100.000 habitantes, año 2018' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_2018 = go.Figure(data= data , layout= layout)

#2019
total_19 = go.Scatter(x= total_2019['Semana'] , y= total_2019['Tasa gripe x 100.000 habitantes total'] , name= 'Total nacional' , mode= 'lines' , marker= dict(color= '#000000'))
andalucia_19 = go.Scatter(x= andalucia_2019['Semana'] , y= andalucia_2019['Andalucia'] , name= 'Andalucia' , mode= 'lines' , marker= dict(color= '#f44336'))
aragon_19 = go.Scatter(x= aragon_2019['Semana'] , y= aragon_2019['Aragón'] , name= 'Aragón' , mode= 'lines' , marker= dict(color= '#744700'))
asturias_19 = go.Scatter(x= asturias_2019['Semana'] , y= asturias_2019['Asturias'] , name= 'Asturias, Principado de' , mode= 'lines' , marker= dict(color= '#ce7e00'))
baleares_19 = go.Scatter(x= baleares_2019['Semana'] , y= baleares_2019['Baleares'] , name= 'Baleares, Islas' , mode= 'lines' , marker= dict(color= '#8fce00'))
c_valenciana_19 = go.Scatter(x= c_valenciana_2019['Semana'] , y= c_valenciana_2019['Valencia'] , name= 'Comunidad Valenciana' , mode= 'lines' , marker= dict(color= '#2986cc'))
canarias_19 = go.Scatter(x= canarias_2019['Semana'] , y= canarias_2019['Canarias'] , name= 'Canarias, Islas' , mode= 'lines' , marker= dict(color= '#16537e'))
cantabria_19 = go.Scatter(x= cantabria_2019['Semana'] , y= cantabria_2019['Cantabria'] , name= 'Cantabria' , mode= 'lines' , marker= dict(color= '#6a329f'))
clm_19 = go.Scatter(x= clm_2019['Semana'] , y= clm_2019['Castilla-La mancha'] , name= 'Castilla-La mancha' , mode= 'lines' , marker= dict(color= '#c90076'))
cyl_19 = go.Scatter(x= cyl_2019['Semana'] , y= cyl_2019['Castilla y León'] , name= 'Castilla y León' , mode= 'lines' , marker= dict(color= '#990000'))
cataluña_19 = go.Scatter(x= cataluña_2019['Semana'] , y= cataluña_2019['Cataluña'] , name= 'Cataluña' , mode= 'lines' , marker= dict(color= '#b45f06'))
ceuta_19 = go.Scatter(x= ceuta_2019['Semana'] , y= ceuta_2019['Ceuta'] , name= 'Ceuta, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#bf9000'))
extrem_19 = go.Scatter(x= extrem_2019['Semana'] , y= extrem_2019['Extremadura'] , name= 'Extremadura' , mode= 'lines' , marker= dict(color= '#38761d'))
rioja_19 = go.Scatter(x= rioja_2019['Semana'] , y= rioja_2019['La Rioja'] , name= 'La Rioja' , mode= 'lines' , marker= dict(color= '#134f5c'))
madrid_19 = go.Scatter(x= madrid_2019['Semana'] , y= madrid_2019['Madrid'] , name= 'Madrid, Comunidad de' , mode= 'lines' , marker= dict(color= '#0b5394'))
melilla_19 = go.Scatter(x= melilla_2019['Semana'] , y= melilla_2019['Melilla'] , name= 'Melilla, Ciudad Autónoma de' , mode= 'lines' , marker= dict(color= '#351c75'))
navarra_19 = go.Scatter(x= navarra_2019['Semana'] , y= navarra_2019['Navarra'] , name= 'Navarra, Comunidad Foral de' , mode= 'lines' , marker= dict(color= '#741b47'))
pais_vasco_19 = go.Scatter(x= pais_vasco_2019['Semana'] , y= pais_vasco_2019['Pais Vasco'] , name= 'Pais Vasco' , mode= 'lines' , marker= dict(color= '#660000'))

data = [total_19 , andalucia_19 , aragon_19 , asturias_19 , baleares_19 , canarias_19 , cantabria_19 , clm_19 , cyl_19 , cataluña_19 , ceuta_19 , c_valenciana_19 , extrem_19 , rioja_19 , madrid_19 , melilla_19 , navarra_19 , pais_vasco_19]
layout = dict(title= 'Casos de gripe x 100.000 habitantes, año 2019' , xaxis=dict(title= 'Semana del año') , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_2019 = go.Figure(data= data , layout= layout)

#Gripe durante la pandemia de covid19
total_2021.loc[174 , 'Semana'] = int('54')
total_2021.loc[175 , 'Semana'] = int('55')
total_2021.loc[176 , 'Semana'] = int('56')
total_2021.loc[177 , 'Semana'] = int('57')

total_pandemia = pd.concat([total_2020, total_2021])

total_pandemia_graph = go.Scatter(x= total_pandemia['Semana'] , y= total_pandemia['Tasa gripe x 100.000 habitantes total'] , name= 'Gripe conjunto España' , mode= 'lines' , marker= dict(color= '#000000'))

data = [total_pandemia_graph]
layout = dict(title= 'Casos de gripe x 100.000 habitantes, año 2020 (53 semanas) y 2021 (54-57 semanas)' , xaxis=dict(title= 'Semana' , ticklen= 57) , yaxis= dict(title= 'Casos x 100.000 habitantes'))

fig_total_pandemia = go.Figure(data= data , layout= layout)
iplot(fig_total_pandemia)
