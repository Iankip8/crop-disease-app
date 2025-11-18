import os
import tensorflow as tf
import gdown  # pip install gdown

MODEL_PATH = "model/model.keras"
MODEL_URL = "https://drive.google.com/file/d/1q242ho4J0doDKNDT9gdezbU8Zyoe2lTZ/view?usp=drive_link"  # e.g., from Google Drive or Hugging Face

def load_model():
    # Download model if not present
    if not os.path.exists(MODEL_PATH):
        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        print("Downloading model...")
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
    # Load the model
    model = tf.keras.models.load_model(MODEL_PATH)
    return model
