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

# Baños
df['Baños'] = df['Baños'].astype("float64")
df['Baños'].fillna(round(df['Baños'].mean(),1),inplace=True)

# Armarios empotrados
df['Armarios empotrados'].fillna(False,inplace=True)

print(df['Roof Garden'].unique())


#print(df.isnull().sum())