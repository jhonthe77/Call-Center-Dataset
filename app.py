import calendar
import streamlit as st 
import pandas as pd
import plotly.express as px

from texto import *


st.set_page_config('Proceso de Analisis',layout='wide')
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


def data_analisis():
    st.title('Proceso de Analisis de una base de agentes call center 🎧')
    df=pd.read_excel("Telecom Company Call-Center-Dataset.xlsx")
    st.write(introducion)
    st.subheader('Datos con los que trabajare')
    st.dataframe(df.head())
    st.text('Mostrare los pasos para limpiar e enriqueser los datos')

    #elimino la columna id ya que no es relevante 
    df.drop(columns='Call Id',inplace=True)
    #transformo la colonna Time y Date a fomato fecha para poder trabar con ellas 
    df['Time']=pd.to_datetime(df['Time'],format='%H:%M:%S')
    df['Date']=pd.to_datetime(df['Date'])
    #estraigo solo la hora de la colonna Time y remplazo sus valores
    df['Time']=df['Time'].dt.hour
    #remplazo los valores nulos con ceros
    df.fillna(0,inplace=True)

    #creo una lista donde extraigo los minutos y segundos y los sumos para crear una nueva columna
    minutos_segundos = [(minuto.minute*60) + minuto.second 
                        if not isinstance(minuto,int) else 0 for minuto in df['AvgTalkDuration']]

    #creo una lista donde extraigo los minutos y segundos por separado sin sumarlos
    minutos=[ round(minuto/60 ,2)if minuto > 59 else round(minuto % 60/60 ,2)
            for minuto in minutos_segundos]
    
    #creo la dos columnas y las lleno con los datos de las listas
    df['Duracion_llamada']= minutos_segundos  
    df['Duracion_llamad_minutos']= minutos

    #filtro el df y creo una copia con la Duracion_llamada que se mayor a cero para trabajar con datos de valor 
    df_=df.loc[(df['Duracion_llamada']>0)].copy()
    #creo una columna con el nombre del dia de la fecha que tengo en Date 
    df_.loc[:,'NombreDia']=df_['Date'].dt.strftime('%A')
    #creo una columna con el nombre del mes de la fecha que tengo en Date 
    df_.loc[:,'NombreMes']=df_['Date'].dt.month.apply(lambda x: calendar.month_name[x])

    #renombro las columnas con el dicionario que cree en la parte superior
    df_.rename(columns=columns_name_es,inplace=True)

    st.code(codigo)
    st.dataframe(df_.head())





data_analisis()