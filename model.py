import numpy as np
import pandas as pd
from sklearn.calibration import LabelEncoder
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
x = data.drop(['precio','titulo','direccion'],axis='columns')
x_cat = LabelEncoder
y = data['precio']

categories = ['ciudad','Colonia']
numerical_cols = len(data.columns)-5

# Scale the numerical features
# TODO: Compare betwwen MinMax and Standard scalers
scaler = MinMaxScaler()
numerical_x = scaler.fit_transform(x.drop(categories,axis=1))

print(x)

# ============== MODEL ================ #

# Label Encoding for categorical variables https://towardsdatascience.com/deep-embeddings-for-categorical-variables-cat2vec-b05c8ab63ac0
# https://www.kaggle.com/code/colinmorris/embedding-layers/notebook
# Embed cathegorical data -> https://arxiv.org/pdf/1604.06737v1.pdf
# TODO: Compare between only address vs ciudad and colonia vs only city
#TODO: Changing embedding size
# The rule of thumb for determining the embedding size is the cardinality size divided by 2, but no bigger than 50.

# ============= CATEGORIES =================== #
categorical_x = pd.DataFrame()

embedding_layers = []
input_layers = [layers.Input(shape=(numerical_cols,))] #Added one initial that corresponds to ALL numerical values
lblEncoders = {}

for category in categories:
    # Label Encode all categories (giving them a value of 1 to n-1)
    categorical_x = LabelEncoder().fit_transform(x[category])
    
    #Define cardinality and embeddin size for each Embedding layer
    cardinality = data[category].nunique()
    embedding_size = min(50,cardinality//2)
    
    #Creating the Embedding and Flatten layers
    input_layer = layers.Input(shape=(1,))
    embedding_layer = layers.Embedding(cardinality,embedding_size,name=category+'_embedding')(input_layer)
    embedding_layer = layers.Reshape(target_shape=(embedding_size,))(embedding_layer)

    #Adding all embedding and input layers
    embedding_layers.append(embedding_layers)
    input_layers.append(input_layer)
    
# Concatenate numerical and categorical input layers
concatenated_Input = layers.Concatenate()(input_layers)


# Using 2 hidden layers
# TODO: Compare between using 1-3 hidden layers and changing units
modelLayers = layers.Dense(64,activation='relu')(concatenated_Input)
modelLayers = layers.Dense(64,activation='relu')(modelLayers)

#Output layer
modelLayers = layers.Dense(1)(modelLayers)

#Creating the model
model = keras.Model(inputs=concatenated_Input,outputs=modelLayers)

#============= COMPILE =============== #
# TODO: Test other compilers
model.compile(optimizer='adam', loss='mean_squared_error')

# ============= TRAIN =============== #
# Split data between training and testing sets by random
x_train,x_test,y_train,y_test = train_test_split([*embedding_layers,numerical_x],y,test_size=0.2,random_state=42)

#Training
model.fit(x_train,y_train,epochs=5,batch_size=32,verbose=1)

# ============ EVALUATE ================= #
loss = model.evaluate(x_test,y_test,verbose=0)
print("Loss: {loss}")

# ============ PREDICTIONS =================== #
predictions = model.predict(x_test)

#Print 5 predictions
for i in range(5):
    print("Predicted price: {predictions[i][0]}, Actual price{y_test.iloc[i]}")