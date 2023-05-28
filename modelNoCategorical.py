from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow import keras
from keras import layers
from keras.utils import plot_model

# Load the dataset
df = pd.read_csv('Data/newCleanData3.tsv',sep='\t')  # Replace 'house_data.csv' with your dataset file

# Preprocess the data
X = df.drop(['precio','titulo','direccion','Colonia','ciudad'], axis=1)
y = df['precio']

scaler = MinMaxScaler()
X= scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Determine the embedding size for the categorical feature

# Define the model
model = keras.Sequential([
    layers.Dense(128, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X_train, y_train, epochs=500, batch_size=32, verbose=1)
plot_model(model, to_file='model.png', show_shapes=True)

# Evaluate the model
loss = model.evaluate(X_test, y_test, verbose=0)
print(f'Test loss: {loss}')

# Make predictions
predictions = model.predict(X_test)

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
