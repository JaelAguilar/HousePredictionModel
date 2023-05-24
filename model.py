import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras import layers
from keras.layers import Embedding,Flatten,Dense
from keras.optimizers import Adam


data = pd.read_csv("Data/newCleanData3.tsv",sep='\t')
print(data.head())
print(data.describe())
print("TIPO",type(data["Baños"]))

# Split data between features and prices
x = data.drop(['precio','titulo','direccion','ciudad','Colonia'],axis='columns').values
y = data['precio'].values

# Split data between training and testing sets by random
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Scale the features
# TODO: Compare betwwen MinMax and Standard scalers
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

print(x_test)

# ============== MODEL ================ #

# Label Encoding for categorical variables https://towardsdatascience.com/deep-embeddings-for-categorical-variables-cat2vec-b05c8ab63ac0
# https://www.kaggle.com/code/colinmorris/embedding-layers/notebook
# Embed cathegorical data -> https://arxiv.org/pdf/1604.06737v1.pdf
# TODO: Compare between only address vs ciudad and colonia vs only city
#TODO: Changing embedding size
# The rule of thumb for determining the embedding size is the cardinality size divided by 2, but no bigger than 50.
cardinality = data['ciudad'].nunique()
embedding_size_city = min(50,cardinality//2)
city_input = keras.Input(shape=(1,),name="cities")

#Creates an Embedding layer 
city_embedded = Embedding(cardinality,embedding_size_city,input_length=1, name='city_embedding')(city_input)

# Code to use when adding more categorical data
# concatenated = keras.layers.Concatenate()([city_embedded,suburb_embedded])

# Using 2 hidden layers
# TODO: Compare between using 1-3 hidden layers and changing units
modelLayers = Flatten()(city_embedded)
modelLayers = Dense(64,activation='relu')(modelLayers)
modelLayers = Dense(64,activation='relu')(modelLayers)
modelLayers = Dense(1)(modelLayers)

#============= COMPILE =============== #
# TODO: Test other compilers
model.compile(optimizer=Adam, loss='mean_squared_error')

# ============= TRAIN =============== #

model.fit(x_train,y_train,epochs=5,batch_size=32,verbose=1)

# ============ EVALUATE ================= #
loss = model.evaluate(x_test,y_test,verbose=0)

# ============ PREDICTIONS =================== #
predictions = model.predict(x_test)

#Print 5 predictions
for i in range(5):
    print("Predicted price: {predictions[i][0]}, Actual price{y_test.iloc[i]}")