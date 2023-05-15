"https://stackoverflow.com/questions/15741564/how-to-remove-duplicates-from-a-csv-file"
'''from more_itertools import unique_everseen
with open('Data/dataUpdatedCorrect-6may2023.tsv, 'r') as f, open('Data/newDataUpdated.tsv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))'''
    
"https://towardsdatascience.com/data-cleaning-how-to-handle-missing-values-in-pandas-cc8570c446ec"


import pandas as pd
import numpy as np

df = pd.read_csv('Data/newDataUpdated.tsv', sep='\t')

def NaNtoMean(*attributeList):
    global df
    for attribute in attributeList:
        df[attribute] = df[attribute].astype('float64')
        df[attribute].fillna(round(df[attribute].mean(),1),inplace=True)
    
def NaNtoFalse(*attributeList):
    global df
    for attribute in attributeList:
        df[attribute].fillna(False,inplace=True)
        
def deleteColumns(*attributeList):
    global df
    for attribute in attributeList:
        df = df.drop(attribute, axis=1)

#Special cases -> Superficie construida (m²), Amueblado, Habitaciones (en total)
df['Construidos (m²)'] = np.where(df['Construidos (m²)'].isna(),df['Superficie construida (m²)'],df['Construidos (m²)'])

df['Recámaras'] = np.where(df['Habitaciones (en total)'].isna()==False,df['Habitaciones (en total)'],df['Recámaras'])

for old, new in [('Yes',True),('Sí',True),('No',False)]:
    df['Amueblado'] = np.where(df['Amueblado']==old,new,df['Amueblado'])
    
df.precio=df['precio'].replace('[\$,]', '', regex=True).astype(float)
print(df['precio'])

NaNtoMean('Baños','Estacionamientos','Recámaras','Terreno (m²)','Construidos (m²)')

NaNtoFalse('Armarios empotrados','Roof Garden','Totalmente cercado','Estacionamiento techado','Alberca','Jardín','Internet de banda ancha disponible','Estacionamiento para Visitas','Estacionamiento vigilado','Calefacción','Balcón','Acceso a TV de paga','Patio','Garaje','Jacuzzi','Estudio','Piso de loseta','Sistema de alarma','Cancha de tenis','Cocina Equipada','Cuarto de servicio','Gimnasio','Estacionamiento abierto','Área de juegos infantiles','Aire acondicionado','Terraza','Área de entretenimiento al aire libre','Intercomunicador','Chimenea','Alberca','Piso de duela','Amueblado')


deleteColumns('Nivel','Mantenimiento','Disponible desde','Construido (Año)','Condiciones de Precio','Superficie construida (m²)','Habitaciones (en total)')

df.to_csv('Data/newCleanData.tsv',sep='\t',index=False)
