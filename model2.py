from embedding_encoder import EmbeddingEncoder
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("Data/newCleanData3.tsv",sep='\t')
x = df.drop(['precio','titulo','direccion','ciudad','Colonia'],axis='columns').astype(np.float32)
cat_x = df[['ciudad','Colonia']]
x=pd.concat([x,cat_x],axis=1)
y = df['precio'].astype('float32')

