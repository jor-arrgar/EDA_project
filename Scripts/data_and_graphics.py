import streamlit as st

#Conexión a los diferentes notebooks en los que se han generado las gráficas
import conclusiones as c
import graphics_covid as gc
import graphics_flu as gf
import graphics_mortality_80_20 as gd_80_20
import graphics_sanitary_indicators as gsi

def lines_raw():
    election_menu = st.sidebar.selectbox('Datos' , ('Contagios' , 'Ingresos hospitalarios y defunciones' ,'Nº de camas por comunidad autónoma'))
    
    if election_menu == 'Contagios':
        territorio = st.selectbox('Escala territorial' , ('Comunidades Autónomas' , 'Provincias'))
        
        if territorio == 'Comunidades Autónomas':
            st.plotly_chart(gc.fig_covid_semanal_ccaa)
        elif territorio == 'Provincias':
            st.plotly_chart(gc.fig_covid_semanal_prov)
    
    elif election_menu == 'Ingresos hospitalarios y defunciones':
        #Menu selector de territorio. Cuando se indica una CCAA, surge el menu de selección de provincias
            españa = st.checkbox('ESPAÑA')
            andalucia = st.checkbox('ANDALUCIA')
            if andalucia:
                almeria = st.checkbox('Almeria')
                cadiz = st.checkbox('Cádiz')
                cordoba = st.checkbox('Córdoba')
                granada = st.checkbox('Granada')
                huelva = st.checkbox('Huelva')
                jaen = st.checkbox('Jaén')
                malaga = st.checkbox('Málaga')
                sevilla = st.checkbox('Sevilla')
            aragon = st.checkbox('ARAGÓN')
            if aragon:
                huesca = st.checkbox('Huesca')
                teruel = st.checkbox('Teruel')
                zaragoza = st.checkbox('Zaragoza')
            asturias = st.checkbox('ASTURIAS')
            baleares = st.checkbox('BALEARES, ISLAS')
            c_valenciana = st.checkbox('COMUNIDAD VALENCIANA')
            if c_valenciana:
                alicante = st.checkbox('Alicante')
                castellon = st.checkbox('Castellón')
                valencia = st.checkbox('Valencia')
            canarias = st.checkbox('CANARIAS, ISLAS')
            if canarias:
                las_palmas = st.checkbox('Las Palmas de Gran Canaria')
                tenerife = st.checkbox('Santa Cruz de Tenerife')
            cantabria = st.checkbox('CANTABRIA')
            cataluña = st.checkbox('CATALUÑA')
            if cataluña:
                barcelona = st.checkbox('Barcelona')
                gerona = st.checkbox('Gerona')
                lerida = st.checkbox('Lérida')
                tarragona = st.checkbox('Tarragona')
            clm = st.checkbox('CASTILLA-LA MANCHA')
            if clm:
                albacete = st.checkbox('Albacete')
                cuenca = st.checkbox('Cuenca')
                ciudad_real = st.checkbox('Ciudad Real')
                guadalajara = st.checkbox('Guadalajara')
                toledo = st.checkbox('Toledo')
            cyl = st.checkbox('CASTILLA Y LEÓN')
            if cyl:
                avila = st.checkbox('Avila')
                burgos = st.checkbox('Burgos')
                leon = st.checkbox('León')
                salamanca = st.checkbox('Salamanca')
                segovia = st.checkbox('Segovia')
                soria = st.checkbox('Soria')
                palencia = st.checkbox('Palencia')
                valladolid = st.checkbox('Valladolid')
                zamora = st.checkbox('Zamora')
            ceuta = st.checkbox('CEUTA')
            extrem = st.checkbox('EXTREMADURA')
            if extrem:
                badajoz = st.checkbox('Badajoz')
                caceres = st.checkbox('Cáceres')
            galicia = st.checkbox('GALICIA')
            if galicia:
                coruña = st.checkbox('La Coruña')
                lugo = st.checkbox('Lugo')
                orense = st.checkbox('Orense')
                pontevedra = st.checkbox('Pontevedra')
            rioja = st.checkbox('LA RIOJA')
            madrid = st.checkbox('MADRID')
            melilla = st.checkbox('MELILLA')
            murcia = st.checkbox('MURCIA')
            navarra = st.checkbox('NAVARRA')
            pv = st.checkbox('PAIS VASCO')
            if pv:
                alava = st.checkbox('Álava')
                guipuzcoa = st.checkbox('Guipúzcoa')
                vizcaya = st.checkbox('Vizcaya')

            #Generacion de las gráficas. Las provincias se ordenan de forma alfabetica

            try:
                if alava:
                    st.plotly_chart(gc.fig_alava)
            except:
                pass
            try:
                if albacete:
                    st.plotly_chart(gc.fig_albacete)
            except:
                pass
            try:
                if alicante:
                    st.plotly_chart(gc.fig_alicante)
            except:
                pass
            try:
                if almeria:
                    st.plotly_chart(gc.fig_almeria)
            except:
                pass
            try:
                if asturias:
                    st.plotly_chart(gc.fig_asturias)
            except:
                pass
            try:
                if avila:
                    st.plotly_chart(gc.fig_avila)
            except:
                pass
            try:            
                if badajoz:
                    st.plotly_chart(gc.fig_badajoz)
            except:
                pass
            try:            
                if baleares:
                    st.plotly_chart(gc.fig_baleares)
            except:
                pass
            try:
                if barcelona:
                    st.plotly_chart(gc.fig_barcelona)
            except:
                pass
            try:
                if burgos:
                    st.plotly_chart(gc.fig_burgos)
            except:
                pass
            try:
                if caceres:
                    st.plotly_chart(gc.fig_caceres)
            except:
                pass
            try:                
                if cadiz:
                    st.plotly_chart(gc.fig_cadiz)
            except:
                pass
            try:
                if cantabria:
                    st.plotly_chart(gc.fig_cantabria)
            except:
                pass
            try:
                if castellon:
                    st.plotly_chart(gc.fig_castellon)
            except:
                pass
            try:            
                if ceuta:
                    st.plotly_chart(gc.fig_ceuta)
            except:
                pass
            try:
                if ciudad_real:
                    st.plotly_chart(gc.fig_ciudad_real)
            except:
                pass
            try:
                if cordoba:
                    st.plotly_chart(gc.fig_cordoba)
            except:
                pass
            try:
                if cuenca:
                    st.plotly_chart(gc.fig_cuenca)
            except:
                pass
            try:
                if gerona:
                    st.plotly_chart(gc.fig_gerona)
            except:
                pass
            try:
                if granada:
                    st.plotly_chart(gc.fig_granada)
            except:
                pass
            try:
                if guadalajara:
                    st.plotly_chart(gc.fig_guadalajara)
            except:
                pass
            try:
                if guipuzcoa:
                    st.plotly_chart(gc.fig_guipuzcoa)
            except:
                pass
            try:
                if huelva:
                    st.plotly_chart(gc.fig_huelva)
            except:
                pass
            try:
                if huesca:
                    st.plotly_chart(gc.fig_huesca)
            except:
                pass
            try:
                if jaen:
                    st.plotly_chart(gc.fig_jaen)
            except:
                pass
            try:
                if coruña:
                    st.plotly_chart(gc.fig_coruña)
            except:
                pass
            try:                
                if rioja:
                    st.plotly_chart(gc.fig_rioja)
            except:
                pass
            try:
                if las_palmas:
                    st.plotly_chart(gc.fig_las_palmas)
            except:
                pass
            try:
                if leon:
                    st.plotly_chart(gc.fig_leon)
            except:
                pass
            try:
                if lerida:
                    st.plotly_chart(gc.fig_lerida)
            except:
                pass
            try:
                if lugo:
                    st.plotly_chart(gc.fig_lugo)
            except:
                pass
            try:
                if madrid:
                    st.plotly_chart(gc.fig_madrid)
            except:
                pass
            try:
                if malaga:
                    st.plotly_chart(gc.fig_malaga)
            except:
                pass
            try:                
                if melilla:
                    st.plotly_chart(gc.fig_melilla)
            except:
                pass
            try:
                if murcia:
                    st.plotly_chart(gc.fig_murcia)
            except:
                pass
            try:                
                if navarra:
                    st.plotly_chart(gc.fig_navarra)
            except:
                pass
            try:
                if orense:
                    st.plotly_chart(gc.fig_orense)
            except:
                pass
            try:
                if palencia:
                    st.plotly_chart(gc.fig_palencia)
            except:
                pass
            try:
                if pontevedra:
                    st.plotly_chart(gc.fig_pontevedra)
            except:
                pass
            try:
                if salamanca:
                    st.plotly_chart(gc.fig_salamanca)
            except:
                pass
            try:
                if tenerife:
                    st.plotly_chart(gc.fig_tenerife)
            except:
                pass
            try:
                if segovia:
                    st.plotly_chart(gc.fig_segovia)
            except:
                pass
            try:
                if sevilla:
                    st.plotly_chart(gc.fig_sevilla)
            except:
                pass
            try:
                if soria:
                    st.plotly_chart(gc.fig_soria)
            except:
                pass
            try:
                if tarragona:
                    st.plotly_chart(gc.fig_tarragona)
            except:
                pass
            try:
                if teruel:
                    st.plotly_chart(gc.fig_teruel)
            except:
                pass
            try:
                if toledo:
                    st.plotly_chart(gc.fig_toledo)
            except:
                pass
            try:
                if valencia:
                    st.plotly_chart(gc.fig_valencia)
            except:
                pass
            try:            
                if valladolid:
                    st.plotly_chart(gc.fig_valladolid)
            except:
                pass
            try:
                if vizcaya:
                    st.plotly_chart(gc.fig_vizcaya)
            except:
                pass
            try:
                if zamora:
                    st.plotly_chart(gc.fig_zamora)
            except:
                pass
            try:
                if zaragoza:
                    st.plotly_chart(gc.fig_zaragoza)
            except:
                pass
    
    elif election_menu == 'Nº de camas por comunidad autónoma':

        #Menu de seleccion de ccaa
        andalucia = st.checkbox('Andalucia')
        aragon = st.checkbox('Aragón')
        asturias = st.checkbox('Asturias')
        baleares = st.checkbox('Baleares, Islas')
        c_valenciana = st.checkbox('Comunidad Valenciana')
        canarias = st.checkbox('Canarias, Islas')
        cantabria = st.checkbox('Cantabria')
        cataluña = st.checkbox('Cataluña')
        clm = st.checkbox('Castilla-La mancha')
        cyl = st.checkbox('Castilla y León')
        ceuta = st.checkbox('Ceuta')
        extrem = st.checkbox('Extremadura')
        galicia = st.checkbox('Galicia')
        rioja = st.checkbox('La Rioja')
        madrid = st.checkbox('Madrid')
        melilla = st.checkbox('Melilla')
        murcia = st.checkbox('Murcia')
        navarra = st.checkbox('Navarra')
        pv = st.checkbox('Pais Vasco')

        #Generación de gráficas
        if andalucia:
            st.plotly_chart(gc.fig_camas_andalucia)
        if aragon:
            st.plotly_chart(gc.fig_camas_aragon)
        if asturias:
            st.plotly_chart(gc.fig_camas_asturias)
        if baleares:
            st.plotly_chart(gc.fig_camas_baleares)
        if c_valenciana:
            st.plotly_chart(gc.fig_camas_valencia)
        if canarias:
            st.plotly_chart(gc.fig_camas_canarias)
        if cantabria:
            st.plotly_chart(gc.fig_camas_cantabria)
        if cataluña:
            st.plotly_chart(gc.fig_camas_cataluña)
        if clm:
            st.plotly_chart(gc.fig_camas_clm)
        if cyl:
            st.plotly_chart(gc.fig_camas_cyl)
        if ceuta:
            st.plotly_chart(gc.fig_camas_ceuta)
        if extrem:
            st.plotly_chart(gc.fig_camas_extrem)
        if galicia:
            st.plotly_chart(gc.fig_camas_galicia)
        if rioja:
            st.plotly_chart(gc.fig_camas_rioja)
        if madrid:
            st.plotly_chart(gc.fig_camas_madrid)
        if melilla:
            st.plotly_chart(gc.fig_camas_melilla)
        if murcia:
            st.plotly_chart(gc.fig_camas_murcia)
        if navarra:
            st.plotly_chart(gc.fig_camas_navarra)
        if pv:
            st.plotly_chart(gc.fig_camas_pv)


def other_data():
    data_menu = st.sidebar.selectbox('Datos' , ('Mortalidad en España' , 'Mortalidad enfermedades respiratorias' , 'Incidencia de gripe' , 'Sistema sanitario'))

    if data_menu == 'Mortalidad en España':
        st.header('Mortalidad en España entre 1980 y 2020')
        st.plotly_chart(gd_80_20.fallecimientos)
        
    
    elif data_menu == 'Mortalidad enfermedades respiratorias':
        st.header('Mortalidad por enfermedades respiratorias en España entre 1980 y 2020')
        st.plotly_chart(gd_80_20.respiratorias)
        

    elif data_menu == 'Incidencia de gripe':
        st.header('Incidencia de gripe entre 2015 y 2021')
        flu_menu = st.selectbox('Visualización' , ('Graficas por territorio' , 'Graficas por año'))
        
        if flu_menu == 'Graficas por territorio':
            st.write('Graficas por territorio')
            #Checkboxes de seleccion de territorio
            españa = st.checkbox('España')
            andalucia = st.checkbox('Andalucia')
            aragon = st.checkbox('Aragón')
            asturias = st.checkbox('Asturias')
            baleares = st.checkbox('Baleares, Islas')
            c_valenciana = st.checkbox('Comunidad Valenciana')
            canarias = st.checkbox('Canarias, Islas')
            cantabria = st.checkbox('Cantabria')
            cataluña = st.checkbox('Cataluña')
            ceuta = st.checkbox('Ceuta')
            clm = st.checkbox('Castilla-La mancha')
            cyl = st.checkbox('Castilla y León')
            extrem = st.checkbox('Extremadura')
            rioja = st.checkbox('La Rioja')
            madrid = st.checkbox('Madrid')
            melilla = st.checkbox('Melilla')
            navarra = st.checkbox('Navarra, Com. Foral')
            pv = st.checkbox('Pais Vasco')
            #Generacion de graficas de los territorios indicados
            if españa:
                st.plotly_chart(gf.total_gripe)
            if andalucia:
                st.plotly_chart(gf.fig_andalucia)
            if aragon:
                st.plotly_chart(gf.fig_aragon)
            if asturias:
                st.plotly_chart(gf.fig_asturias)
            if baleares:
                st.plotly_chart(gf.fig_baleares)
            if c_valenciana:
                st.plotly_chart(gf.fig_valencia)
            if canarias:
                st.plotly_chart(gf.fig_canarias)
            if cantabria:
                st.plotly_chart(gf.fig_cantabria)
            if cataluña:
                st.plotly_chart(gf.fig_cataluña)
            if clm:
                st.plotly_chart(gf.fig_clm)
            if cyl:
                st.plotly_chart(gf.fig_cyl)
            if ceuta:
                st.plotly_chart(gf.fig_ceuta)
            if extrem:
                st.plotly_chart(gf.fig_extrem)
            if rioja:
                st.plotly_chart(gf.fig_rioja)
            if madrid:
                st.plotly_chart(gf.fig_madrid)
            if melilla:
                st.plotly_chart(gf.fig_melilla)
            if navarra:
                st.plotly_chart(gf.fig_navarra)
            if pv:
                st.plotly_chart(gf.fig_pais_vasco)
            

        else:
            st.write('Graficas por año')
            #Checkboxes de seleccion de año
            año_15 = st.checkbox('Año 2015')
            año_16 = st.checkbox('Año 2016')
            año_17 = st.checkbox('Año 2017')
            año_18 = st.checkbox('Año 2018')
            año_19 = st.checkbox('Año 2019')
            año_20_21 = st.checkbox('Año 2020-2021')

            #Generacion de graficas de los años seleccionados
            if año_15:
                st.plotly_chart(gf.fig_2015)
            if año_16:
                st.plotly_chart(gf.fig_2016)
            if año_17:
                st.plotly_chart(gf.fig_2017)
            if año_18:
                st.plotly_chart(gf.fig_2018)
            if año_19:
                st.plotly_chart(gf.fig_2019)
            if año_20_21:
                st.plotly_chart(gf.fig_total_pandemia)

    
    elif data_menu == 'Sistema sanitario':
        st.header('Sistema sanitario')
        system_menu = st.selectbox('Grafica' , ('Camas hospitalarias x 1000 habitantes' , 'Gasto público en el sistema sanitario' , 'Porcentaje de gasto antención primaria'))
        
        if system_menu == 'Camas hospitalarias x 1000 habitantes':
            st.plotly_chart(gsi.camas)

        elif system_menu == 'Gasto público en el sistema sanitario':
            st.pyplot(gsi.gasto_sanitario)

        else:
            st.plotly_chart(gsi.porcentaje_atencion_primaria)


def conclusiones():

    st.plotly_chart(c.covid_vs_influenza)
    st.write(c.conclusiones)