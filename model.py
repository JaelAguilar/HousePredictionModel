#Data analysis
import numpy as np
import pandas as pd


#from sklearn.preprocessing import StandardScaler #Standarization
#from sklearn.ensemble import IsolationForest #Outlier detection

#Modeling
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.callbacks import EarlyStopping
#from keras.optimizers import Adam

data = pd.read_csv("Data/newCleanData.tsv",sep='\t')
print(data.head())
print(data.describe())
print("TIPO",type(data["Baños"]))

