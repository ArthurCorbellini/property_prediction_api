
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler  # noqa
import joblib


def predict(data):
    df = pd.DataFrame([data])

    ct = joblib.load("neural_model/imports/column_transformer.pkl")
    X = ct.transform(df)

    model = load_model("neural_model/imports/neural_model_v1.h5")
    prediction_data = model.predict(X)

    return prediction_data
