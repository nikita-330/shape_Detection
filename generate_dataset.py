import sys
import os
import cv2
import numpy as np
from tqdm import tqdm
from utils.shape_generation import generate_random_shape

def generate_dataset(output_dir, num_images=500, image_size=256):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in tqdm(range(num_images)):
        image = generate_random_shape(image_size)
        cv2.imwrite(os.path.join(output_dir, f'image_{i:04d}.png'), image)

if __name__ == "__main__":
    output_dir = 'dataset/shape_dataset'
    generate_dataset(output_dir)
