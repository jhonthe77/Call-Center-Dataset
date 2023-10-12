import pandas as pd
import plotly.express as px
import streamlit as st



def visualizacion_analisis():
    st.title('Analisis con visualizaciónes')
    col1, col2=st.columns(2)
    theme='streamlit'
    with col1:
        df_=pd.read_csv('Callcenter.csv')
        df_agente=df_.groupby('Agente')['Calificación de satisfacción'].mean().reset_index()
        fig=px.bar(df_agente,x='Agente',y='Calificación de satisfacción',color='Agente',
                title='Promedio de la Calificacion de cada Agente')
        st.plotly_chart(fig,use_container_width=True,theme=theme)

    with col2:
        df_=pd.read_csv('Callcenter.csv')
        df_agente=df_.groupby('Agente')['Calificación de satisfacción'].mean().reset_index()
        fig=px.pie(df_agente,names='Agente',values='Calificación de satisfacción',color='Agente',
                title='Promedio de la Calificacion de cada Agente')
        st.plotly_chart(fig,use_container_width=True,theme=theme)
