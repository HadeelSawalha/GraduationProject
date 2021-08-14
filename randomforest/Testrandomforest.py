import classifier as classifier
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
#connect database
import mysql.connector

db = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='pnumeniafinal'
)

def determineType(whiteBloodCells,Neutrophils,Lymphocytes,crp):

    data_set = pd.read_csv('randomforest/dataset500.csv')

    x = data_set.iloc[:,1:5].values
    y = data_set.iloc[:,5].values
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    st_x = StandardScaler()
    x_train = st_x.fit_transform(x)
    loaded_classifier = joblib.load("randomforest/Finalrandom_forest500.joblib")
    list=[whiteBloodCells,Neutrophils,Lymphocytes,crp]
    x_test = st_x.transform([list])
    y_pred=loaded_classifier.predict(x_test)
    result=y_pred[0]
    res=str(result)
    return res
