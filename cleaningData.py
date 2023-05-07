"https://stackoverflow.com/questions/15741564/how-to-remove-duplicates-from-a-csv-file"
'''from more_itertools import unique_everseen
with open('Data/dataUpdated.tsv', 'r') as f, open('Data/newDataUpdated.tsv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))'''
    
"https://towardsdatascience.com/data-cleaning-how-to-handle-missing-values-in-pandas-cc8570c446ec"


import pandas as pd
import numpy as np

df = pd.read_csv('Data/data.tsv', sep='\t')
#df.head(10)
print(df.isnull().sum())

# Baños
missing_values=['True','contado','Negociable']
df['Baños']=df['Baños'].replace(missing_values,np.NaN)

df['Baños'] = df['Baños'].astype("float64")
df['Baños'].fillna(round(df['Baños'].mean(),1),inplace=True)


# Armarios empotrados
missing_values = ['True']
df['Armarios empotrados']=df['Armarios empotrados'].replace(missing_values,np.NaN)

df['Armarios empotrados'] = df['Armarios empotrados'].astype("float64")
df['Armarios empotrados'].fillna(round(df['Armarios empotrados'].mean(),1),inplace=True)

print(df['Roof Garden'].unique())


#print(df.isnull().sum())