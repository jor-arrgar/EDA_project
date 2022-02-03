import streamlit as st
import data_and_graphics as dg

def introduccion():
    st.title('LA PANDEMIA DE COVID19')
    st.write('Proyecto de exploración y análisis de datos realizado por Jorge Arranz como parte del curso en Data Science de la academia The Bridge. \nEn este proyecto se analizan los datos relacionados con la pandemia de covid19 en España. Esta pandemia comenzó en enero de 2020 en China y ha afectado a todo el planeta desde estonces. \n')
    st.image('.\images\Covid-19.jpg')
    st.write('La finalidad de este trabajo es demostrar que la covid19 ha sido una enfermedad pandémica y que las medidas adoptadas para frenar o paliar sus efectos sobre la población han surtido el efecto deseado reduciendo tanto la incidencia como la mortalidad. \n\nEl análisis ha sido realizado en Python 3.7, "latin" como lenguaje de codificación y se ha usado la interfaz de Streamlit para una mejor visualización de los diferentes datos. Las gráficas han sido generadas con Plotly y los datos han sido extraídos de fuentes oficiales del Gobierno de España (INE , Instituto Carlo III y Ministerio de Sanidad). Salvo con los datos de incidencia de gripe, los valores realcionados con el covid han sido extraídos como valores totales y posteriormente se han transformado en valores de incidencia (x100.000 habitantes). \n\nProyecto finalizado el 16 de enero de 2022 con datos hasta el 26 de diciembre de 2021.')

def covid19():
    st.title('¿QUÉ ES LA COVID19?')
    st.image('.\images\entubado.jfif')
    st.write('''La covid19 es una enfermedad que afecta al sistema respiratorio, tanto a nivel de vias respiratorias superiores como inferiores. Está causada por el coronavirus SARS-CoV-2 en sus diferentes variantes. \nEste virus se cree que surgio a finales del año 2019, siendo enero de 2020 los primeros casos que llamaron la atención a las autoridades chinas. Se cree que el virus surgió en Wuhan (China), concretamente en su mercado de especies animales, por una persona que ingerió un murciélago infectado con un coronavirus que presento las características adecuadas para pasar al ser humano y transmitirse entre personas con una gran virulencia y rapidez. \n\nEn enero China empezó a avisar al mundo y en febrero el virus se empezó a expandir por todo el globo, pero no fue hasta marzo que los paises europeos empezaron a tomar medidas para evitar su propagación, siendo en su mayoria confinamientos generales a toda la población que no ocupase un puesto de trabajo en sectores esenciales. Tras la primera ola, las medidas de contención se limitaron pero no desaparecieron, y se han mantenido en el tiempo hasta 2022, como la obligatoriedad de mascarilla en interiores y las limitaciones de aforo en espacios cerrados y eventos masivos. \n\nEl desarrollo de las vacunas frente a SARS-CoV-2 y de medicamentos para tratar la enfermedad, así como la aparación de de nuevas variantes que aunque más transmisivas son menos agresivas contra el hospedador, hacen pensar que durante este año 2022 se pasará a convivir con el virus de la misma forma que se convive con la gripe u otros virus endémicos que afectan a grandes grupos de población.''')
    st.image('.\images\murcielago.jfif')
def datos_covid19():
    st.title('LA PANDEMIA EN DATOS')
    st.write('Es importante destacar que las series temporales de los datos del covid19 están ordenados en semanas, pero que incluyen dos años diferentes en los que no se dividen las semanas: \nEl año 2020 corresponde con el rango de semanas 2 a 53 y el año 2021 desde la semana 54 hasta la 104.')
    dg.lines_raw()

def otros_datos():
    st.title('OTROS DATOS')
    dg.other_data()

def conclusiones():
    st.title('CONCLUSIONES')
    dg.conclusiones()