import streamlit as st
import functions as f

main_menu = st.sidebar.selectbox('Menu principal' , ('Introducción' , '¿Qué es la covid19?' , 'La pandemia en datos' , 'Otros datos' , 'Conclusiones'))

if main_menu == 'Introducción':
    f.introduccion()


elif main_menu == '¿Qué es la covid19?':
    f.covid19()

elif main_menu == 'La pandemia en datos':
    f.datos_covid19()

elif main_menu == 'Otros datos':
    f.otros_datos()

elif main_menu == 'Conclusiones':
    f.conclusiones()





