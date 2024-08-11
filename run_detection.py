import tensorflow as tf
import sys
import os
from utils.shape_detection import detect_shapes
from tensorflow.keras.preprocessing.image import ImageDataGenerator

if __name__ == "__main__":
    model = tf.keras.models.load_model('model/shape_detection_model.keras')
    train_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
        'dataset/shape_dataset',
        target_size=(256, 256),
        batch_size=32,
        class_mode='categorical'
    )
    input_image_path = 'dataset/path_to_image.png'  # Adjust the path accordingly
    shape_label = detect_shapes(input_image_path, model, train_generator)
    print(f'Detected shape: {shape_label}')
