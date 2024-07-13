import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from flask import request, jsonify
import json
import joblib
import pandas as pd
import tensorflow as tf
import numpy as np

label_encoder = joblib.load('./Triage Model/assets/label_encoder_ESI.pkl')
robustScaler = joblib.load('./Triage Model/assets/robust_scaler.pkl')
model = tf.keras.models.load_model('./Triage Model/assets/model_ESI.h5')

def index():
    return {'status': 'OK',}

def predict():
    data = request.get_json()

    predict = loadModel(data)
    return {"result": predict[0]}

def loadModel(data):
    numerical_columns = ['age', 'triage_vital_hr', 'triage_vital_sbp', 'triage_vital_dbp', 'triage_vital_rr', 'triage_vital_o2', 'triage_vital_temp']

    custome_input = pd.DataFrame(data)
    # print(custome_input.to_string())
    custome_input[numerical_columns] = robustScaler.transform(custome_input[numerical_columns])
    y_pred = model.predict(custome_input)
    y_pred = np.argmax(y_pred, axis=1)

    response = label_encoder.inverse_transform(y_pred)
    # print(response)
    return response
    # return 'loadOk'
