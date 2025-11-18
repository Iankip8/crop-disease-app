import tensorflow as tf

def load_model():
    model = tf.keras.models.load_model("model/model.keras")
    return model
