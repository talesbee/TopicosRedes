import csv
import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  
from sklearn.preprocessing import LabelEncoder


def executaIA(entrada, tamanhoTeste):

    df = pd.read_csv(entrada)

    data = df

    data.columns = data.columns.astype(str)

    #[0,1,2,3]
    feature = df.iloc[:,0:2]
    label = df.iloc[:,3]

    scaler = MinMaxScaler((-1,1))

    x = scaler.fit_transform(feature) 

    y = label

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = tamanhoTeste, random_state = 7)

    model = XGBClassifier()

    le = LabelEncoder()
    y_train = le.fit_transform(y_train)

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    print('Acerto de: ',accuracy_score(y_test, y_pred)*100)
