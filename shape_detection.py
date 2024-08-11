import cv2
import numpy as np
import tensorflow as tf

def detect_shapes(image_path, model, train_generator):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} could not be loaded. Check the file path.")
    image_resized = cv2.resize(image, (256, 256)) / 255.0
    image_resized = np.expand_dims(image_resized, axis=0)
    predictions = model.predict(image_resized)
    class_index = np.argmax(predictions)
    class_label = list(train_generator.class_indices.keys())[class_index]
    return class_label
