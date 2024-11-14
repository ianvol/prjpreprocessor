import cv2
import os
import numpy as np

def preprocess_image(image, target_size=(256, 256)):
    image = cv2.resize(image, target_size)
    if len(image.shape) == 2 or image.shape[2] == 1: # Check if grayscale
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    image = image / 255.0
    return image

def process_images_in_folder(input_folder, output_folder):
    extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff']
    for filename in os.listdir(input_folder):
        _, ext = os.path.splitext(filename)
        if ext.lower() not in extensions: # If not image, skip
            continue

        file_path = os.path.join(input_folder, filename)
        image = cv2.imread(file_path) # Read from disk
        processed_image = preprocess_image(image, target_size=(256, 256)) # Runpreprocessing
        processed_image_uint8 = (processed_image * 255).astype(np.uint8) # Convert back to 8bit unsigned int format

        output_path = os.path.join(output_folder, filename)
        with open(output_path, 'wb') as f:
            cv2.imwrite(f, processed_image_uint8) # Use context manager for proper resource management
        print("Done")

input_folder = input("Input folder path: ")
output_folder = input("Output folder path: ")

process_images_in_folder(input_folder, output_folder)