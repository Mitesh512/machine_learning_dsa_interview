import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from scipy import stats

# -------------------------------------------------------
# Data Preprocessing
# -------------------------------------------------------

# 1. Handling Nans
def handle_missing_values(df, num_strategy = "mean", cat_strategy = "mode"):
    df = df.copy()
    for col in df.columns:
        if df[col].dtype == "O":
            if cat_strategy == "mode":
                df[col] = df[col].fillna(df[col].mode()[0])
            elif cat_strategy == "constant":
                df[col] = df[col].fillnam("missing")
        else:
            if num_strategy == "mean":
                df[col]= df[col].fillna(df[col].mean())
            
            elif num_strategy == "median":
                df[col] = df[col].fillnma(df[col].median())
    return df


# transform: to reduce skewness and stabilize variance
def transform_features(df, columns, method= "log"):
    df = df.copy()
    for col in columns:
        if method == "log":
            df[col] = np.log1p(df[col])
        elif method == "boxcox":
            if (df[col] > 0).all:
                df[col], _ = stats.boxcox(df[col])
    return df


# Outlier Handling
def handle_outliers(df, columns):
    df = df.copy()
    for col  in columns:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr , q3 + 1.5 * iqr
        df[col] = np.clip(df[col], lower, upper)
    return df

# Scaling
def scale_features(df, cols):
    df = df.copy()
    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])
    return df, scaler

# Encoding:
def encode_categorical(df, columns):
    df = df.copy()
    encoders = {}
    for col in columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype("O"))
        encoders[col] = le
    return df, encoders
 
 
 # Text to features
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_text(df):
    tfidf = TfidfVectorizer(max_features=5000, stop_words="english")
    X_text = tfidf.fit_transform(df['comments_text'].fillna(""))
    y = df['label']
    df = df.drop(columns = ['comments_text','label'])
    x_full = np.hstack([X_text, np.array(df)])
    
    return tfidf, x_full, y
            