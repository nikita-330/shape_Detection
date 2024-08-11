import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from utils.data_processing import create_model

# Prepare data
output_dir = 'dataset/shape_dataset'
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
    output_dir,
    target_size=(256, 256),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)
validation_generator = train_datagen.flow_from_directory(
    output_dir,
    target_size=(256, 256),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Create and train model
input_shape = (256, 256, 3)
num_classes = len(train_generator.class_indices)
model = create_model(input_shape, num_classes)
model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Save model
model.save('model/shape_detection_model.keras')
