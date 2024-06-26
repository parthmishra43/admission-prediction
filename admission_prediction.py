import numpy as np
import pandas as pd

df= pd.read_csv("/content/Admission_Predict_Ver1.1.csv")

df.drop(columns=['Serial No.'],inplace=True)
df.head()

X= df.iloc[:,0:-1]
y= df.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1)

from sklearn.preprocessing import MinMaxScaler
scaler= MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_scaled

import tensorflow
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(7,activation='relu',input_dim=7))
model.add(Dense(7,activation='relu'))
model.add(Dense(1,activation='linear'))
model.summary()

model.compile(optimizer='Adam',loss='mean_squared_error',metrics=['mean_squared_error'])

history = model.fit(X_train,y_train,epochs=100)

y_pred= model.predict(X_test)
from sklearn.metrics import r2_score
r2_score(y_test,y_pred)

