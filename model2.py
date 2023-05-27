from embedding_encoder import EmbeddingEncoder
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras import layers
from keras.utils import plot_model

#Load the dataset
df = pd.read_csv("Data/newCleanData3.tsv",sep='\t')

#Preprocess the data
x = df.drop(['precio','titulo','direccion','ciudad','Colonia'],axis='columns').astype(np.float32)
cat_x = df[['ciudad','Colonia']] #Categorical columns
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

# Compile the model
model.compile(optimizer='adam', loss='mse')

#Train the model
history = model.fit(x_train, y_train, epochs=200, batch_size=32, verbose=1)
plot_model(model, to_file='model.png', show_shapes=True)

# Evaluate the model
loss = model.evaluate(x_test, y_test, verbose=0)
print(f'Test loss: {loss}')

# Make predictions
predictions = model.predict(x_test)

# Print the first few predictions
for i in range(5):
    print(f'Predicted price: {predictions[i][0]}, Actual price: {y_test.iloc[i]}')
    
#Show data
plt.figure(0)
plt.plot(history.history['loss'])
plt.plot()
plt.yscale('log')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')

plt.figure(1)
plt.scatter(y_test, predictions)
x = np.linspace(0,int(y_test.values.max()))
y = x
plt.plot(x, y, color='red', label="y = y'")
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted Prices')
plt.show()


