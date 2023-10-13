import pandas as pd
import plotly.express as px
import streamlit as st


def visualizacion_analisis():
    df_ = pd.read_csv('Callcenter.csv')
    df_['Fecha'] = pd.to_datetime(df_['Fecha'])
    fecha_min = df_['Fecha'].min()
    fecha_max = df_['Fecha'].max()

    st.subheader(
        'Hecho Por Jhon Kerly Mosquera 🕵️‍♂️ Este panel se estara atualizando')
    st.sidebar.header('Filtar Los Datos 🔎')
    st.title('Analisis con visualizaciónes 📈')

    st.subheader("Selecciona un rango de fechas:")
    col00, col11 = st.columns(2)
    with col00:
        fecha_init = st.date_input(
            "Fecha Inicial", fecha_min, min_value=fecha_min, max_value=fecha_max)

    with col11:
        # Widget para la fecha final con valor máximo
        fecha_end = st.date_input(
            "Fecha Final", fecha_max, min_value=fecha_min, max_value=fecha_max)

    Tema = st.sidebar.multiselect(
        label='Filtre Por Tema 🔎',
        options=df_['Tema'].unique(),
        default=df_['Tema'].unique()[:])

    Agente = st.sidebar.multiselect(
        label='Filtre Por Agente 🔎',
        options=df_['Agente'].unique(),
        default=df_['Agente'].unique()[:4])

    NombreDia = st.sidebar.multiselect(
        label='Filtre Por Dia 🔎',
        options=df_['NombreDia'].unique(),
        default=df_['NombreDia'].unique()[:])

    Resuelto = st.sidebar.multiselect(
        label='Filtre Por Resuelto 🔎',
        options=df_['Resuelto'].unique(),
        default=df_['Resuelto'].unique()[0]
    )

    df_ = df_.query(
        'Tema==@Tema & Agente==@Agente & NombreDia==@NombreDia & Resuelto==@Resuelto & Fecha >= @fecha_init and Fecha <= @fecha_end')

    col1, col2 = st.columns(2)
    theme = 'streamlit'
    with col1:
        df_agente = df_.groupby(
            'Agente')['Calificación de satisfacción'].mean().reset_index()
        fig = px.bar(df_agente, x='Agente', y='Calificación de satisfacción', color='Agente',
                     title='Promedio de la Calificacion de cada Agente')
        st.plotly_chart(fig, use_container_width=True, theme=theme)

    with col2:
        df_agente = df_.groupby(
            'Agente')['Calificación de satisfacción'].mean().reset_index()
        fig = px.pie(df_agente, names='Agente', values='Calificación de satisfacción', color='Agente', hole=0.7,
                     title='Promedio de la Calificacion de cada Agente')
        st.plotly_chart(fig, use_container_width=True, theme=theme)

    df_agente = df_.groupby(['Agente', 'Tema'])[
        'Calificación de satisfacción'].mean().reset_index()

    col5, col6 = st.columns(2)

    with col5:
        fig = px.bar(df_agente, x='Agente', y='Calificación de satisfacción', color='Tema', barmode='group',
                     title='Promedio de la Calificacion de cada Tema por Agente')
        st.plotly_chart(fig, use_container_width=True, theme=theme)

    with col6:
        fig = px.line(df_agente,
                      x='Agente',
                      y='Calificación de satisfacción',
                      color='Tema',
                      title='Evolución de Calificaciones de Satisfacción por Agente Y Tema',
                      labels={'Calificación de satisfacción': 'Calificación'},
                      markers=True)

        st.plotly_chart(fig, use_container_width=True, theme=theme)

    col3, col4 = st.columns(2)

    with col4:
        fig = px.bar(df_agente,
                     x='Tema',
                     y='Calificación de satisfacción',
                     color='Agente',
                     barmode='group',
                     title='Calificaciones de Satisfacción por Agente y Tema',
                     labels={'Calificación de satisfacción': 'Calificación'})
        st.plotly_chart(fig, use_container_width=True, theme=theme)

    with col3:
        fig = px.line(df_agente,
                      x='Tema',
                      y='Calificación de satisfacción',
                      color='Agente',
                      title='Evolución de Calificaciones de Satisfacción por Tema y Agente',
                      labels={'Calificación de satisfacción': 'Calificación'},
                      markers=True)

        st.plotly_chart(fig, use_container_width=True, theme=theme)

    df_agente = df_.groupby(['Agente', 'Tema', 'Resuelto']).size(
    ).reset_index(name='Resuelto_count')

    col5, col6 = st.columns(2)

    with col5:
        fig = px.bar(df_agente,
                     x='Tema',
                     y='Resuelto_count',
                     color='Agente',
                     barmode='group',
                     title='Resulucion de Tema por Agente',
                     labels={'Resuelto_count': 'Resuelto(Y/N)'},
                     text='Resuelto')
        st.plotly_chart(fig, use_container_width=True, theme=theme)

    with col6:

        fig = px.line(df_agente,
                      x='Tema',
                      y='Resuelto_count',
                      color='Agente',
                      title='Evolución de Resuluciones Tema y Agente',
                      labels={'Resuelto_count': 'Resuelto(Y/N)'},
                      markers=True,
                      text='Resuelto')

        st.plotly_chart(fig, use_container_width=True, theme=theme)

    col7, col8 = st.columns(2)

    with col8:

        colores_agentes = {'Becky': 'blue', 'Dan': 'green', 'Diane': 'red', 'Greg': 'purple',
                           'Jim': 'orange', 'Joe': 'cyan', 'Martha': 'magenta', 'Stewart': 'yellow'}
        fig = px.line_polar(df_agente,
                            theta='Tema',
                            r='Resuelto_count',
                            color='Agente',  # Utiliza la columna 'Agente' para asignar colores
                            color_discrete_map=colores_agentes,  # Asigna colores basados en el diccionario
                            title='Fortaleza para dar Soluciones de los Tema por Agente',
                            labels={'Resuelto_count': 'Resuelto(Y/N)'},
                            markers=True,
                            line_close=True)
        fig.update_traces(fill='toself')
        fig.update_layout(
            polar=dict(
                bgcolor='#83C9FF',  # Cambia el color del fondo
                radialaxis=dict(
                    visible=True,
                    gridcolor='black',  # Cambia el color de la cuadrícula radial
                ),
            ),
        )
        fig.update_layout(
            legend=dict(
                orientation='v',  # Cambia la orientación a horizontal
                yanchor='auto',  # Ancla la leyenda en la parte superior
                y=1.1 # Ajusta la posición vertical de la leyenda
            )
        )

        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col7:
        st.subheader('Fortaleza para dar Soluciones de los Tema por Agente')
        st.dataframe(df_agente.head(), width=500)






    df_agente = df_.groupby(['Agente', 'Tema', 'Resuelto'])[
        'Velocidad de respuesta en segundos'].mean().reset_index()
    
    col12, col13= st.columns(2)

    with col12:
        fig = px.bar(df_agente, x='Tema', y='Velocidad de respuesta en segundos',
                    color='Agente', barmode='group'
                    ,title='Promedio de Velocidad de respuesta en segundos por Tema y por Agente')
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col13:
        fig = px.line(df_agente, x='Tema',
                    y='Velocidad de respuesta en segundos', color='Agente', markers=True
                     ,title='Promedio de Velocidad de respuesta en segundos por Tema y por Agente')
        st.plotly_chart(fig, theme=None, use_container_width=True)


    col14, col15= st.columns(2)
    with col15:
        fig = px.bar(df_agente, x='Agente',
                    y='Velocidad de respuesta en segundos', color='Tema', barmode='group'
                     ,title='Promedio de Velocidad de respuesta en segundos por Agente y por Tema')
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col14:
        fig = px.line(df_agente, x='Agente',
                    y='Velocidad de respuesta en segundos', color='Tema', markers=True
                     ,title='Promedio de Velocidad de respuesta en segundos por Agente y por Tema')
        st.plotly_chart(fig, theme=None, use_container_width=True)



    col9, col10 = st.columns(2)
    with col9:

        colores_agentes = {'Becky': 'blue', 'Dan': 'green', 'Diane': 'red', 'Greg': 'purple',
                           'Jim': 'orange', 'Joe': 'cyan', 'Martha': 'magenta', 'Stewart': 'yellow'}
        fig = px.line_polar(df_agente,
                            theta='Tema',
                            r='Velocidad de respuesta en segundos',
                            color='Agente',  # Utiliza la columna 'Agente' para asignar colores
                            color_discrete_map=colores_agentes,  # Asigna colores basados en el diccionario
                            title='Fortaleza de respuesta en segundos por Agente y por Tema',
                            labels={
                                'Velocidad de respuesta en segundos': 'Promedio de Velocidad de respuesta en segundos'},
                            markers=True,
                            line_close=True)
        fig.update_traces(fill='toself')
        fig.update_layout(
            polar=dict(
                bgcolor='#83C9FF',  # Cambia el color del fondo
                radialaxis=dict(
                    visible=True,
                    gridcolor='black',  # Cambia el color de la cuadrícula radial
                ),
            ),
        )

        fig.update_layout(
            legend=dict(
                orientation='v',  # Cambia la orientación a horizontal
                yanchor='auto',  # Ancla la leyenda en la parte superior
                y=1.1 # Ajusta la posición vertical de la leyenda
            )
        )
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col10:
        st.subheader('Fortaleza de respuesta en segundos por Agente y por Tema')
        st.dataframe(df_agente.head(), use_container_width=True)
    df_agente = df_.groupby(['Agente', 'Tema', 'Resuelto'])[
        'Velocidad de respuesta en segundos'].mean().reset_index()
    





    df_agente=df_.groupby(['Agente','Tema','Resuelto'])['Duración de la llamada'].mean().reset_index()

    
    col20, col21= st.columns(2)

    with col20:
        fig = px.bar(df_agente, x='Tema', y='Duración de la llamada',
                    color='Agente', barmode='group'
                    ,title='Promedio de Duración de la llamada por Tema y por Agente')
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col21:
        fig = px.line(df_agente, x='Tema',
                    y='Duración de la llamada', color='Agente', markers=True
                     ,title='Promedio de Duración de la llamada por Tema y por Agente')
        st.plotly_chart(fig, theme=None, use_container_width=True)


    col22, col23= st.columns(2)
    with col23:
        fig = px.bar(df_agente, x='Agente',
                    y='Duración de la llamada', color='Tema', barmode='group'
                     ,title='Promedio de Duración de la llamada por Agente y por Tema')
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col22:
        fig = px.line(df_agente, x='Agente',
                    y='Duración de la llamada', color='Tema', markers=True
                     ,title='Promedio de Duración de la llamada por Agente y por Tema')
        st.plotly_chart(fig, theme=None, use_container_width=True)



    col24, col25 = st.columns(2)
    with col24:

        colores_agentes = {'Becky': 'blue', 'Dan': 'green', 'Diane': 'red', 'Greg': 'purple',
                           'Jim': 'orange', 'Joe': 'cyan', 'Martha': 'magenta', 'Stewart': 'yellow'}
        fig = px.line_polar(df_agente,
                            theta='Tema',
                            r='Duración de la llamada',
                            color='Agente',  # Utiliza la columna 'Agente' para asignar colores
                            color_discrete_map=colores_agentes,  # Asigna colores basados en el diccionario
                            title='Fortaleza de respuesta en Duración de la llamada por Agente y por Tema',
                            labels={
                                'Duración de la llamada': 'Promedio de Duración de la llamada'},
                            markers=True,
                            line_close=True)
        fig.update_traces(fill='toself')
        fig.update_layout(
            polar=dict(
                bgcolor='#83C9FF',  # Cambia el color del fondo
                radialaxis=dict(
                    visible=True,
                    gridcolor='black',  # Cambia el color de la cuadrícula radial
                ),
            ),
        )

        fig.update_layout(
            legend=dict(
                orientation='v',  # Cambia la orientación a horizontal
                yanchor='auto',  # Ancla la leyenda en la parte superior
                y=1.1 # Ajusta la posición vertical de la leyenda
            )
        )
        st.plotly_chart(fig, theme=None, use_container_width=True)

    with col25:
        st.subheader('Fortaleza de respuesta en Duración de la llamada por Agente y por Tema')
        st.dataframe(df_agente.head(), use_container_width=True)
