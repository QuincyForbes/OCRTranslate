import logging
from PIL import Image
import cv2
import numpy as np
import google.cloud.vision as vision
from google.auth import load_credentials_from_file
import io
import math
import os
import re
import openai
import yaml

# Configure logging
logging.basicConfig(level=logging.INFO)

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

openai.api_key = config["OpenAPIKey"]

credentials, project = load_credentials_from_file("cred.json")
client = vision.ImageAnnotatorClient(credentials=credentials)

# Other functions omitted for brevity

def execute(image_path, prompt):
    try:
        img = Image.open(image_path)  # Load the image file
        logging.info(f"Image {image_path} loaded successfully.")
        img = np.array(img)

        chunks = []
        detected_texts = []

        # Set your chunk size (this is a square so x and y are the same)
        chunk_size = 3069

        # Calculate the number of chunks needed in the x and y directions
        num_x_chunks = img.shape[1] // chunk_size + (1 if img.shape[1] % chunk_size else 0)
        num_y_chunks = img.shape[0] // chunk_size + (1 if img.shape[0] % chunk_size else 0)

        for i in range(num_y_chunks):
            row_chunks = []
            for j in range(num_x_chunks):
                y_start = i * chunk_size
                y_end = (i + 1) * chunk_size

                x_start = j * chunk_size
                x_end = (j + 1) * chunk_size

                # This line extracts the chunk from the image
                chunk = img[y_start:y_end, x_start:x_end]
                processed_chunk, texts = process_chunk(preprocess_image(chunk))
                row_chunks.append(processed_chunk)
                detected_texts.extend(texts)
            chunks.append(row_chunks)

        # Reassembling the chunks
        reassembled_image = cv2.vconcat([cv2.hconcat(h_chunks) for h_chunks in chunks])

        processed_text = process_text(detected_texts)
        ai_complete = generate_text(prompt, processed_text)

        filename = os.path.basename(image_path)  # Get the base filename
        filename_without_extension = os.path.splitext(filename)[
            0
        ]  # Get the filename without extension
        proc_filename = f"proc_{filename_without_extension}.png"  # Processed chunk filename

        cv2.imwrite(os.path.join("outputs", proc_filename), reassembled_image)
        logging.info(f"Processed image saved as {os.path.join('outputs', proc_filename)}.")

        return proc_filename, ai_complete

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None, None
