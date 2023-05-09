"https://stackoverflow.com/questions/15741564/how-to-remove-duplicates-from-a-csv-file"
'''from more_itertools import unique_everseen
with open('Data/dataUpdatedCorrect-6may2023.tsv, 'r') as f, open('Data/newDataUpdated.tsv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))'''
    
"https://towardsdatascience.com/data-cleaning-how-to-handle-missing-values-in-pandas-cc8570c446ec"


import pandas as pd
import numpy as np

df = pd.read_csv('Data/newDataUpdated.tsv', sep='\t')
#df.head(10)
print(df.isnull().sum())


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

NaNtoMean('Baños','Estacionamientos','Construidos (m²)','Habitaciones (en total)','Recámaras','Terreno (m²)')

NaNtoFalse('Armarios empotrados','Roof Garden','Totalmente cercado','Estacionamiento techado','Alberca','Jardín','Internet de banda ancha disponible','Estacionamiento para Visitas','Estacionamiento vigilado','Calefacción','Balcón','Acceso a TV de paga','Patio','Garaje','Jacuzzi','Estudio','Piso de loseta','Sistema de alarma','Cancha de tenis','Cocina Equipada','Cuarto de servicio','Gimnasio','Estacionamiento abierto','Área de juegos infantiles','Aire acondicionado','Terraza','Área de entretenimiento al aire libre','Intercomunicador','Chimenea','Alberca','Piso de duela')

deleteColumns('Nivel','Mantenimiento','Disponible desde','Construido (Año)','Condiciones de Precio')

# Special cases -> Amueblado, Superficie construida (m²)
print('\n',df['Amueblado'].value_counts(dropna=False))

print(df.isnull().sum())