import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


data = pd.read_csv("Data/newCleanData2.tsv",sep='\t')
print(data.head())
print(data.describe())
print("TIPO",type(data["Baños"]))

# Split data between features and prices
x = data.drop('precio',axis='columns').values
y = data['precio'].values

# Split data between training and testing sets by random
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Scale the features
# TODO: Compare betwwen MinMax and Standard scalers
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)
