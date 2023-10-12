import pandas as pd
import plotly.express as px
import streamlit as st




def visualizacion_analisis():
    df_=pd.read_csv('Callcenter.csv')
    st.sidebar.header('Filtar Los Datos 🔎')
    Tema=st.sidebar.multiselect(
    label='Filtre Por Tema 🔎',
    options=df_['Tema'].unique(),
    default=df_['Tema'].unique()[:4])

    Agente=st.sidebar.multiselect(
    label='Filtre Por Agente 🔎',
    options=df_['Agente'].unique(),
    default=df_['Agente'].unique()[:4])

    NombreDia=st.sidebar.multiselect(
    label='Filtre Por NombreDia 🔎',
    options=df_['NombreDia'].unique(),
    default=df_['NombreDia'].unique()[:2])

    NombreMes=st.sidebar.multiselect(
    label='Filtre Por NombreMes 🔎',
    options=df_['NombreMes'].unique(),
    default=df_['NombreMes'].unique()[:2])

    df_= df_.query('Tema==@Tema & Agente==@Agente & NombreDia==@NombreDia & NombreMes==@NombreMes')


    st.title('Analisis con visualizaciónes 📈')
    col1, col2=st.columns(2)
    theme='streamlit'
    with col1:
        df_agente=df_.groupby('Agente')['Calificación de satisfacción'].mean().reset_index()
        fig=px.bar(df_agente,x='Agente',y='Calificación de satisfacción',color='Agente',
                title='Promedio de la Calificacion de cada Agente')
        st.plotly_chart(fig,use_container_width=True,theme=theme)

    with col2:
        df_agente=df_.groupby('Agente')['Calificación de satisfacción'].mean().reset_index()
        fig=px.pie(df_agente,names='Agente',values='Calificación de satisfacción',color='Agente',
                title='Promedio de la Calificacion de cada Agente')
        st.plotly_chart(fig,use_container_width=True,theme=theme)


    
   


    
    df_agente=df_.groupby(['Agente','Tema'])['Calificación de satisfacción'].mean().reset_index()

    col5, col6=st.columns(2)

    with col5:
        fig=px.bar(df_agente,x='Agente',y='Calificación de satisfacción',color='Tema',barmode='group',
                title='Promedio de la Calificacion de cada Tema por Agente')
        st.plotly_chart(fig,use_container_width=True,theme=theme)

    with col6:
        fig = px.line(df_agente, 
                x='Agente', 
                y='Calificación de satisfacción', 
                color='Tema',
                title='Evolución de Calificaciones de Satisfacción por Agente Y Tema',
                labels={'Calificación de satisfacción': 'Calificación'},
                markers=True)

        st.plotly_chart(fig,use_container_width=True,theme=theme)


    col3, col4=st.columns(2)

    with col4:
        fig = px.bar(df_agente, 
                x='Tema', 
                y='Calificación de satisfacción', 
                color='Agente',
                barmode='group',
                title='Calificaciones de Satisfacción por Agente y Tema',
                labels={'Calificación de satisfacción': 'Calificación'})
        st.plotly_chart(fig,use_container_width=True,theme=theme)

    with col3:
        fig = px.line(df_agente, 
                x='Tema', 
                y='Calificación de satisfacción', 
                color='Agente',
                title='Evolución de Calificaciones de Satisfacción por Tema y Agente',
                labels={'Calificación de satisfacción': 'Calificación'},
                markers=True)

        st.plotly_chart(fig,use_container_width=True,theme=theme)
        



