import pandas as pd
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objects as go
import os
import matplotlib.pyplot as plt

# Mortalidad enfermedades respiratorias
df1= pd.read_csv('Scripts/Datasets/Utiles/Defunciones_1980-2020/Meses_vs_causas_respiratorias.csv' , sep= ';' , encoding='latin')

lista = list(df1.columns.values)

totales = go.Scatter(x = df1["Serie mensual"] , y= df1["001-102  I-XXII.Todas las causas"] , name = 'Totales' , mode= 'lines' , marker= dict(color= '#000000'))
covid_iden = go.Scatter(x = df1["Serie mensual"] , y= df1["00A COVID-19. Virus identificado"] , name = 'Covid identificado' , mode= 'lines' , marker= dict(color= '#f44336' ))
covid_sus = go.Scatter(x = df1["Serie mensual"] , y= df1["00B COVID-19. Virus no identificado (sospechoso)"] , name = 'Covid sospechoso' , mode= 'lines' , marker= dict(color= '#f5958d'))
enfermedades_respiratorias = go.Scatter(x = df1["Serie mensual"] , y= df1["062-067  X.Enfermedades del sistema respiratorio"] , name = 'Respiratorias (sin covid)' , mode= 'lines' , marker= dict(color= '#6a329f' ))
gripe = go.Scatter(x = df1["Serie mensual"] , y= df1["062  Influenza (gripe) (incluye gripe aviar y gripe A)"] , name = 'Gripe común (influenza)' , mode= 'lines' , marker= dict(color= '#2496ec' ))
neumonia = go.Scatter(x = df1["Serie mensual"] , y= df1[lista[6]] , name = 'Neumonía' , mode= 'lines' , marker= dict(color= '#e9a336' ))
cronicas = go.Scatter(x = df1["Serie mensual"] , y= df1[lista[7]] , name = 'Enf. cronicas (excepto asma)' , mode= 'lines' , marker= dict(color= '#744700'))
asma = go.Scatter(x = df1["Serie mensual"] , y= df1["065  Asma"] , name = 'Asma' , mode= 'lines' , marker= dict(color= '#bf9000'))
insuf = go.Scatter(x = df1["Serie mensual"] , y= df1["066  Insuficiencia respiratoria"] , name = 'Insuficiencia respiratoria' , mode= 'lines' , marker= dict(color= '#9fc5e8'))
otras = go.Scatter(x = df1["Serie mensual"] , y= df1["067  Otras enfermedades del sistema respiratorio"] , name = 'Otras enfermedades respiratorias' , mode= 'lines' , marker= dict(color= '#cfdee3'))

defunciones = [totales , covid_iden , covid_sus , enfermedades_respiratorias , gripe , neumonia , cronicas , asma , insuf , otras]

layout = dict(title = "Defunciones relacionadas con causas respiratorias 1980-2020" , xaxis= dict(title= 'Serie mensual' , ticklen= 123) , yaxis = dict(title= 'Nº personas fallecidas' , ticklen= 123))

respiratorias = go.Figure(data= defunciones , layout=layout)



#Mortalidad todos los grupos
df2 = pd.read_csv("Scripts/Datasets/Utiles/Defunciones_1980-2020/Grupos_de_causas_mortales_1980_2020.csv" , sep= ';')


totales = go.Scatter(x = df2["Serie mensual"] , y= df2["001-102  I-XXII.Todas las causas"] , name = 'Totales' , mode= 'lines' , marker= dict(color= '#000000'))
I = go.Scatter(x = df2["Serie mensual"] , y= df2["001-008  I.Enfermedades infecciosas y parasitarias"] , name = 'Infecciosas y parásitas (incluye covid19)' , mode= 'lines' , marker= dict(color= '#fb1239'))
II = go.Scatter(x = df2["Serie mensual"] , y= df2["009-041  II.Tumores"] , name = 'Tumores' , mode= 'lines' , marker= dict(color= '#aa40ff'))
III = go.Scatter(x = df2["Serie mensual"] , y= df2["042-043  III.Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad"] , name = 'Hematopoyéticas y autoinmunidad' , mode= 'lines' , marker= dict(color= '#6b6929'))
IV = go.Scatter(x = df2["Serie mensual"] , y= df2["044-045  IV.Enfermedades endocrinas, nutricionales y metabólicas"] , name = 'Trastornos endocrinos y metabólicos' , mode= 'lines' , marker= dict(color= '#eeac60'))
V = go.Scatter(x = df2["Serie mensual"] , y= df2["046-049  V.Trastornos mentales y del comportamiento"] , name = 'Trastornos mentales' , mode= 'lines' , marker= dict(color= '#f0851b'))
VI_VIII = go.Scatter(x = df2["Serie mensual"] , y= df2["050-052  VI-VIII.Enfermedades del sistema nervioso y de los órganos de los sentidos"] , name = 'Sistema nervioso' , mode= 'lines' , marker= dict(color= '#99cccc'))
IX = go.Scatter(x = df2["Serie mensual"] , y= df2["053-061 IX.Enfermedades del sistema circulatorio"] , name = 'Sistema circulatorio' , mode= 'lines' , marker= dict(color= '#ffa97e'))
X = go.Scatter(x = df2["Serie mensual"] , y= df2["062-067  X.Enfermedades del sistema respiratorio"] , name = 'Sistema respiratorio' , mode= 'lines' , marker= dict(color= '#aaaacc'))
XI = go.Scatter(x = df2["Serie mensual"] , y= df2["068-072  XI.Enfermedades del sistema digestivo"] , name = 'Sistema digestivo' , mode= 'lines' , marker= dict(color= '#8b8f2b'))
XII = go.Scatter(x = df2["Serie mensual"] , y= df2["073  XII.Enfermedades de la piel y del tejido subcutáneo"] , name = 'Cutaneas' , mode= 'lines' , marker= dict(color= '#b00b69'))
XIII = go.Scatter(x = df2["Serie mensual"] , y= df2["074-076  XIII.Enfermedades del sistema osteomuscular y del tejido conjuntivo"] , name = 'Sistema osteomuscular (locomotor)' , mode= 'lines' , marker= dict(color= '#420a55'))
XIV = go.Scatter(x = df2["Serie mensual"] , y= df2["077-080  XIV.Enfermedades del sistema genitourinario"] , name = 'Sistema genitourinario' , mode= 'lines' , marker= dict(color= '#aa99ff'))
XV = go.Scatter(x = df2["Serie mensual"] , y= df2["081  XV.Embarazo, parto y puerperio"] , name = 'Embarazo y parto' , mode= 'lines' , marker= dict(color= '#99a4aa'))
XVI = go.Scatter(x = df2["Serie mensual"] , y= df2["082  XVI.Afecciones originadas en el periodo perinatal"] , name = 'Período perinatal' , mode= 'lines' , marker= dict(color= '#a0604a'))
XVII = go.Scatter(x = df2["Serie mensual"] , y= df2["083-085  XVII.Malformaciones congénitas, deformidades y anomalías cromosómicas"] , name = 'Malformaciones y anomalías cromosómicas' , mode= 'lines' , marker= dict(color= '#eab9ac'))
XVIII = go.Scatter(x = df2["Serie mensual"] , y= df2["086-089  XVIII.Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte"] , name = 'Otras enfermedades anormales' , mode= 'lines' , marker= dict(color= '#007474'))
XX = go.Scatter(x = df2["Serie mensual"] , y= df2["090-102  XX.Causas externas de mortalidad"] , name = 'Causas externas' , mode= 'lines' , marker= dict(color= '#1a0dab'))

defunciones = [totales , I, II, III, IV , VI_VIII , IX , X , XI , XII , XIII , XIV , XV , XVI , XVII , XVIII , XX]

layout = dict(title = "Defunciones por grupos principales de causas 1980-2020" , xaxis= dict(title= 'Serie mensual' , ticklen= 123) , yaxis = dict(title= 'Nº personas fallecidas' , ticklen= 123))

fallecimientos = go.Figure(data= defunciones , layout=layout)

