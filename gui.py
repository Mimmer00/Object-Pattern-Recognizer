import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from main import detect_shapes_and_colors  # Assuming your functions are here

def load_image_from_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_shapes_and_colors(file_path)

def open_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam could not be opened.")
        return

    cv2.namedWindow("Webcam")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process each frame with your existing function
        processed_frame = detect_shapes_and_colors(frame)  # Modify this function to return the image
        cv2.imshow("Webcam", processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit the live video
            break

    cap.release()
    cv2.destroyAllWindows()

app = tk.Tk()
app.title("Shape and Color Detection")

load_button = tk.Button(app, text="Load Image", command=load_image_from_file)
load_button.pack(side=tk.LEFT, padx=20, pady=20)

webcam_button = tk.Button(app, text="Open Webcam", command=open_webcam)
webcam_button.pack(side=tk.RIGHT, padx=20, pady=20)

app.mainloop()
