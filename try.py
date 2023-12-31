import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

def load_and_test_model(model_path):
    # Load the model
    model = load_model(model_path)

    # Print the model summary
    model.summary()

# Replace this with the path to your model file
MODEL_PATH = 'model\model_sequential.keras'

load_and_test_model(MODEL_PATH)


