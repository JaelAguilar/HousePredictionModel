"https://stackoverflow.com/questions/15741564/how-to-remove-duplicates-from-a-csv-file"
'''from more_itertools import unique_everseen
with open('Data/dataUpdatedCorrect-6may2023.tsv, 'r') as f, open('Data/newDataUpdated.tsv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))'''
    
"https://towardsdatascience.com/data-cleaning-how-to-handle-missing-values-in-pandas-cc8570c446ec"


from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
sns.set() 
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
        
def deleteOutliers(df):
    cols = ['Baños','Estacionamientos','Terreno (m²)','Construidos (m²)','precio'] # The columns you want to search for outliers in

    # Calculate quantiles and IQR
    Q1 = df[cols].quantile(0.25) # Same as np.percentile but maps (0,1) and not (0,100)
    Q3 = df[cols].quantile(0.75)
    print("QUANTILE 3",Q3)
    IQR = Q3 - Q1

    # Return a boolean array of the rows with (any) non-outlier column values
    condition = ~((df[cols] < (Q1 - 1.5 * IQR)) | (df[cols] > (Q3 + 1.5 * IQR))).any(axis=1)
    #Caso especial para las recámaras
    df = df[condition]
    df = df[df['Recámaras']<15]

    # Filter our dataframe based on condition
    return df[condition]


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

newDF = pd.DataFrame()

newDF = deleteOutliers(df)
#newDF = deleteOutliers(newDF)
print("LONGITUD",len(newDF))
print(type(newDF))

plt.figure(0)
plt.subplot(1,16,1)
sns.boxplot(y=newDF['Terreno (m²)'], orient="h")
plt.subplot(1,16,4)
sns.boxplot(y=newDF['Construidos (m²)'], orient="h")
plt.subplot(1,16,7)
sns.boxplot(y=newDF['Recámaras'], orient="h")
plt.subplot(1,16,10)
sns.boxplot(y=newDF['Baños'], orient="h")
plt.subplot(1,16,13)
sns.boxplot(y=newDF['Estacionamientos'], orient="h")
plt.subplot(1,16,16)
sns.boxplot(y=newDF['precio'], orient="h")

plt.figure(1)
plt.subplot(2,3,1)
plt.scatter(newDF['Construidos (m²)'],newDF['precio'])
#plt.title("Precio vs Área construid a")
plt.xlabel('Construidos (m2)')
plt.ylabel('Precio')
sns.despine()

plt.subplot(232)
plt.scatter(newDF['Terreno (m²)'],newDF['precio'])
#plt.title("Precio vs Terreno")
plt.xlabel('Terreno (m2)')
plt.ylabel('Precio')
sns.despine()

plt.subplot(233)
plt.scatter(newDF['Estacionamientos'],newDF['precio'])
#plt.title("Precio vs Estacionamientos")
plt.xlabel('Estacionamientos')
plt.ylabel('Precio')
sns.despine()

plt.subplot(234)
plt.scatter(newDF['Baños'],newDF['precio'])
#plt.title("Precio vs Baños")
plt.xlabel('Baños')
plt.ylabel('Precio')
sns.despine()

plt.subplot(235)
plt.scatter(newDF['Recámaras'],newDF['precio'])
#plt.title("Precio vs Recámaras")
plt.xlabel('Recámaras')
plt.ylabel('Precio')
sns.despine()


plt.show()

newDF.to_csv('Data/newCleanData2.tsv',sep='\t',index=False)
