import streamlit as st
from PIL import Image
import numpy as np
import io
import cv2

def create_line_drawing_image(img):
    kernel = np.array([
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        ], np.uint8)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_dilated = cv2.dilate(img_gray, kernel, iterations=1)
    img_diff = cv2.absdiff(img_dilated, img_gray)
    contour = 255 - img_diff
    return contour

st.header('Artzy', divider='rainbow')

uploaded_file = st.file_uploader("Upload your awesome art!")

col1, col2, col3 = st.columns(3)
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # Show the image filename and image.
    with col1:
        st.header("Source Image")
        st.image(bytes_data, width=200)
        
    with col2:
        st.header("Generate Sketch")
        if st.button('Generate Sketch'):
            input_image = np.array(Image.open(io.BytesIO(bytes_data))) 
            line_drawing = create_line_drawing_image(input_image)
            with col3:
                st.image(line_drawing)

