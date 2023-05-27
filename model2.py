from embedding_encoder import EmbeddingEncoder
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras import layers

#Load the dataset
df = pd.read_csv("Data/newCleanData3.tsv",sep='\t')

#Preprocess the data
x = df.drop(['precio','titulo','direccion','ciudad','Colonia'],axis='columns').astype(np.float32)
cat_x = df[['ciudad','Colonia']] #Categorical columns
x=pd.concat([x,cat_x],axis=1)
y = df['precio'].astype('float32')

#Create the embedded data
ee = EmbeddingEncoder(task="regression",verbose=1)
ee.fit(X=cat_x,y=y)
output = ee.transform(X=cat_x)
print(type( output))

#Concat original numerical data and embedded data
x = pd.concat([x,output],axis=1)

print(x.head())

#Scale the data
x = MinMaxScaler().fit_transform(x)

#Split the data into training and testing sets
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=53)

#Define the model
model = keras.Sequential([
    layers.Dense(64,activation='relu'),
    layers.Dense(64,activation='relu'),
    layers.Dense(1)
])

