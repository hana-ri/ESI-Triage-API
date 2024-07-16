import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from flask import request
import joblib
import pandas as pd
import numpy as np
from keras.models import load_model

label_encoder = joblib.load('./Triage Model/LabelEncoder.pkl')
robustScaler = joblib.load('C:/Users/USER/Documents/Kuliah/My Final Destination/Dokumen Teknik/Joblib_RobustScaler.pkl')
model = load_model('./Triage Model/Model.h5')

def index():
    return {'status': 'OK',}

def predict():
    data = request.get_json()

    predict = loadModel(data)
    return {"result": predict[0]}

def loadModel(data):
    numerical_columns = ['age', 'triage_vital_hr', 'triage_vital_sbp', 'triage_vital_dbp', 'triage_vital_rr', 'triage_vital_o2', 'triage_vital_temp']

    custome_input = pd.DataFrame(data)

    # print(custome_input[['triage_vital_temp']].to_string())
    custome_input[numerical_columns] = robustScaler.transform(custome_input[numerical_columns])
    # print(custome_input[['triage_vital_temp']].to_string())

    y_pred = model.predict(custome_input, batch_size=1024)
    y_pred = np.argmax(y_pred, axis=1)

    response = label_encoder.inverse_transform(y_pred)
    print(response)
    return response
