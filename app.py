import streamlit as st
import calendar
import streamlit as st
import pandas as pd
import plotly.express as px
from texto import *
from io import StringIO, BytesIO
from visualizacion_analisis import *

st.set_page_config('Proceso de Analisis', layout='wide')





def data_analisis():
    st.subheader('Hecho Por Jhon Kerly Mosquera 🕵️‍♂️')

    st.title('Proceso de Analisis de una base de agentes call center 🎧')
    df = pd.read_excel("Telecom Company Call-Center-Dataset.xlsx")
    st.write(introducion)

    buffer = StringIO()
    buffer2 = StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()

# Mostrar el reproductor de audio
    st.subheader('Escuchar La lectura del texto')
    st.audio("audios/20231011_213345.mp3", format='audio/mp3')

    st.subheader('Esta es la Informacion que me entrega el df')
    with st.expander('Ver la infromación que arroja el DataFrme 📋', expanded=True):
        col, col1, = st.columns(2)
        with col:
            st.text(info)
        with col1:
            st.subheader('Explicacion de la informacion')
            st.write(explicacion_info, unsafe_allow_html=True)
            st.audio('audios/20231011_223221.mp3', format='audio/mp3')

    st.subheader('Datos con los que trabajare')
    st.dataframe(df.head(), use_container_width=True)
    st.subheader('Mostrare los pasos para limpiar y enriqueser los datos 👇')

    # elimino la columna id ya que no es relevante
    df.drop(columns='Call Id', inplace=True)
    # transformo la colonna Time y Date a fomato fecha para poder trabar con ellas
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
    df['Date'] = pd.to_datetime(df['Date'])
    # estraigo solo la hora de la colonna Time y remplazo sus valores
    df['Time'] = df['Time'].dt.hour
    # remplazo los valores nulos con ceros
    df.fillna(0, inplace=True)

    # creo una lista donde extraigo los minutos y segundos y los sumos para crear una nueva columna
    minutos_segundos = [(minuto.minute*60) + minuto.second
                        if not isinstance(minuto, int) else 0 for minuto in df['AvgTalkDuration']]

    # creo una lista donde extraigo los minutos y segundos por separado sin sumarlos
    minutos = [round(minuto/60, 2)if minuto > 59 else round(minuto % 60/60, 2)
               for minuto in minutos_segundos]

    # creo la dos columnas y las lleno con los datos de las listas
    df['Duracion_llamada'] = minutos_segundos
    df['Duracion_llamad_minutos'] = minutos

    # filtro el df y creo una copia con la Duracion_llamada que se mayor a cero para trabajar con datos de valor
    df_ = df.loc[(df['Duracion_llamada'] > 0)].copy()
    # creo una columna con el nombre del dia de la fecha que tengo en Date
    df_.loc[:, 'NombreDia'] = df_['Date'].dt.strftime('%A')
    # creo una columna con el nombre del mes de la fecha que tengo en Date
    df_.loc[:, 'NombreMes'] = df_['Date'].dt.month.apply(
        lambda x: calendar.month_name[x])

    # renombro las columnas con el dicionario que cree en la parte superior
    df_.rename(columns=columns_name_es, inplace=True)
    df_['Fecha'] = pd.to_datetime(df_['Fecha']).dt.date


   


    with st.expander(f'Ver El Codigo Para Depurar y Enriqueser los Datos📋',expanded=True):
        st.code(codigo)
    st.dataframe(df_.head(), use_container_width=True)

    df_['Fecha'] = pd.to_datetime(df_['Fecha'])
    df_.info(buf=buffer2)
    info2 = buffer2.getvalue()

    st.subheader('Esta es la Informacion que me entrega el df')
    with st.expander('Ver la infromación que arroja el DataFrme 📋', expanded=True):
        col2, col3, = st.columns(2)
        with col2:
            st.text(info2)
        with col3:
            st.subheader('Explicacion de la informacion')
            st.write(explicacion_info2, unsafe_allow_html=True)
            st.audio('audios/20231011_231621.mp3', format='audio/mp3')

    st.subheader('Esta es la estadistica basica que me entrega el df')
    st.dataframe(df_.describe(), use_container_width=True)

    col4, col5 = st.columns(2)
    df_au = pd.read_csv("Callcenter.csv")

    def convert_df(df_au):
        return df_au.to_csv(index=False).encode('utf-8')

    csv = convert_df(df_au)

    with col4:
        st.download_button(
            "Presiona para descargar el CSV",
            csv,
            "Callcenter.csv",
            "text/csv",
            key='download-csv',
            use_container_width=True

        )

    # Leer el archivo XLSX
    xlsx_file_path = "Callcenter.xlsx"  # Cambia a la ruta correcta de tu archivo XLSX
    df = pd.read_excel(xlsx_file_path)

    # Función para convertir DataFrame a XLSX
    def convert_df_to_xlsx(df):
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        buffer.seek(0)
        return buffer

    # Convierte el DataFrame a XLSX y obtén el contenido
    xlsx_content = convert_df_to_xlsx(df)

    with col5:
        # Agrega un botón para descargar el archivo XLSX
        st.download_button(
            label="Presiona para descargar el Excel",
            data=xlsx_content,
            file_name="Callcenter.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key='download-xlsx',
            use_container_width=True
        )


    st.title("Video de apertura del Archivo ")

    # Ruta del archivo de video en formato WebM
    video_path = open("video/20231012 101004 Edit1-1.webm",'rb' ) # Cambia a la ruta correcta de tu video WebM
    video_file=video_path.read()
    # Agregar el video a la aplicación
    st.video(video_file)







# Llama a la función para mostrar los elementos en la barra lateral




pages = {
    "Data analisis 📋 ": data_analisis,
    "Analisis con visualizacion 📊 ": visualizacion_analisis,
    
}
st.sidebar.image('servicio-premium.ico', width=80)
# Sidebar para la selección de página

url_redireccion = "https://costumer-jb7mpmynfrbpw7ayujy3y3.streamlit.app/"  # Reemplaza con tu URL

# Inserta un enlace en el sidebar que redirige a la URL especificada
st.sidebar.markdown(f"[Ir a Panel De Análisis Empresarial]({url_redireccion})")
page_selection = st.sidebar.radio("Selecciona una página 📃", tuple(pages.keys()))




# Llama a la función correspondiente a la página seleccionada
pages[page_selection]()





# Llama a la función principal para ejecutar la app


