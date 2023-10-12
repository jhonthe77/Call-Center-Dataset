introducion='''
El proceso exploratorio de datos (EDA) es como desentrañar los secretos del universo de los datos. Comienza con la recolección y limpieza de datos, donde se despojan de cualquier confusión o desorden. Luego, a través del análisis, estos datos revelan sus verdades ocultas, sus conexiones y estructuras. Es como descifrar un código cósmico. La visualización es la manifestación de estas verdades, permitiendo ver la belleza y complejidad de lo que antes estaba oculto. Finalmente, este conocimiento brinda poder: poder para tomar decisiones informadas y diseñar estrategias que transformen el mundo. El EDA es la clave para desvelar la sabiduría enterrada en los datos y, en última instancia, para crear un impacto significativo.
'''
codigo ='''
#lectura del archivo
df=pd.read_excel("Telecom Company Call-Center-Dataset.xlsx")

#dicionario para renombara las columnas del df
columns_name_es={
    'Agent': 'Agente',
    'Date': 'Fecha',
    'Time': 'Hora',
    'Topic': 'Tema',
    'Answered (Y/N)': 'Respondido (S/N)',
    'Resolved': 'Resuelto',
    'Speed of answer in seconds': 'Velocidad de respuesta en segundos',
    'AvgTalkDuration': 'Duración promedio de la llamada',
    'Satisfaction rating': 'Calificación de satisfacción',
    'Duracion_llamada': 'Duración de la llamada',
    'Duracion_llamad_minutos': 'Duración de la llamada en minutos'
}

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
#muestro los datos
df_.head()
'''

columns_name_es={
    'Agent': 'Agente',
    'Date': 'Fecha',
    'Time': 'Hora',
    'Topic': 'Tema',
    'Answered (Y/N)': 'Respondido (S/N)',
    'Resolved': 'Resuelto',
    'Speed of answer in seconds': 'Velocidad de respuesta en segundos',
    'AvgTalkDuration': 'Duración promedio de la llamada',
    'Satisfaction rating': 'Calificación de satisfacción',
    'Duracion_llamada': 'Duración de la llamada',
    'Duracion_llamad_minutos': 'Duración de la llamada en minutos'
}


explicacion_info='''
Te explico un poco qué es esta información. Primero, debes saber que un DataFrame no es más que una tabla de Excel en Python. Partiendo de que sabes qué es un DataFrame, ahora te explico lo que estás observando.

Lo primero es el tipo de archivo con el que estás trabajando. Luego, está el número de registros que contiene el DataFrame, que en este caso va de 0 a 4999. A continuación, verás información sobre las columnas que contiene. En la parte izquierda están los nombres, en el centro están los datos que no están nulos y al final está el tipo de dato que tienen.

Después, te muestra los tipos de datos presentes en el DataFrame y, por último, te indica cuánta memoria RAM estás utilizando.
'''

explicacion_info2='''
Como podemos apreciar, tenemos un nuevo DataFrame con más datos y con las columnas con la misma cantidad de datos y su tipo de dato acorde. Este DataFrame está filtrado donde omití 946 filas que tenían valores nulos. No apliqué ninguna técnica para trabajar con ellos ya que no afentan la calidad de los datos, por ejemplo, una de varias es rellenarlos con el promedio. Pero se puede apreciar que no afectan la calidad de los datos y por eso opté por rellenarlos con ceros. Llegué a esta conclusión mostrando las descripciones estadísticas básicas del DataFrame, como son el promedio, la distribución estándar, el valor máximo, el valor mínimo y los cuartiles de las columnas que son el 25%, 50% y el 75%. Es así como están distribuidos los datos en el DataFrame.

Para concluir, vemos que el DataFrame está enriquecido con nuevos datos creados a partir de los datos existentes. Luego, pasaré a las visualizaciones analizando variables importantes del DataFrame de marea, tanto individual como agrupadas. Finalmente, mostraré al final las estadísticas básicas del DataFrame para que tengan una idea de lo que les mencioné anteriormente.
'''