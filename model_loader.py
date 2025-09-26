import os
import pandas as pd
from tensorflow.keras.models import load_model

MODEL_PATH = os.path.join('C:/Users/mhesh/Desktop/traffic-sign-recognition/traffic_sign_cnn.h5') 
META_PATH = os.path.join('C:/Users/mhesh/Downloads/data_set/Meta.csv')

# Load Model
model = load_model(MODEL_PATH)
print("✅ Model loaded successfully from disk.")

# Load Label Map
meta_df = pd.read_csv(META_PATH)
meta_df.columns = meta_df.columns.str.strip()

label_col = 'SignName'

label_map = dict(zip(meta_df['ClassId'].astype(int), meta_df[label_col]))

print("✅ Label map created successfully.")