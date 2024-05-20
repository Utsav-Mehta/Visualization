import streamlit as st
from PIL import Image
import os

# Set the directory where your images are stored
image_directory = "Pictures"

# List all image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Sort the images if needed, here we assume they are named in order
image_files.sort()

# Limit to 17 images
image_files = image_files[:17]

# Display each image with a caption
st.title("🌾 Agri Sense EDA")

for i, image_file in enumerate(image_files):
    image_path = os.path.join(image_directory, image_file)
    image = Image.open(image_path)
    st.image(image, caption=f"Image {i+1}", use_column_width=True)