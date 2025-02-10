import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os
import json
import pathlib
import threading
import sys
from robot.api.deco import keyword

MODEL_PATH = 'Dentrite.h5'
METADATA_PATH = 'Dentrite_metadata.json'
DATASET_PATH = r"C:\Users\Kira10\Pictures\Saved Pictures\photos"
PREDICTION_PATH = 'REPORT.txt'

@keyword("Predict")
def Predict():

    print(MODEL_PATH)
    print(METADATA_PATH)
    print(DATASET_PATH)
    print(PREDICTION_PATH)

    model = load_model(MODEL_PATH)

    with open(METADATA_PATH, 'r') as f:
        metadata = json.load(f)
    image_size = tuple(map(int, metadata['image_size']))
    class_names = metadata['class_names']

    test_dir = pathlib.Path(DATASET_PATH)
    images_path = list(test_dir.glob('*.jpg')) + list(test_dir.glob('*.png'))
    print(f"Found images: {images_path}")


    report_file_path = PREDICTION_PATH

    with open(report_file_path, 'w') as report_file:
        report_file.write("Prediction Report\n")
        report_file.write("=================\n\n")

        for img_path in images_path:

            # Load and preprocess the image
            img = tf.keras.preprocessing.image.load_img(img_path, target_size=image_size)
            img_arr = tf.keras.preprocessing.image.img_to_array(img)
            img_arr = tf.expand_dims(img_arr, 0)  # Add batch dimension (for model input)

            predictions = model.predict(img_arr)
            predicted_class_index = np.argmax(predictions)
            predicted_class = class_names[predicted_class_index]
            predicted_accuracy = predictions[0][predicted_class_index]  # Probability of the predicted class

            result_line = f"Image: {os.path.basename(img_path)} -> Predicted Class: {predicted_class}, Confidence: {predicted_accuracy:.2f}\n"
            report_file.write(result_line)

