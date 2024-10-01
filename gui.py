import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import threading
import numpy as np
from main import detect_shapes_and_colors  # Assuming your functions are here
from main import load_image

# Function to load an image from file and process it
def load_image_from_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = load_image(file_path)
        detect_shapes_and_colors(image)
        cv2.imshow("Image", image)
        

# Function to display the webcam feed inside the Tkinter window
def open_webcam():
    cap = cv2.VideoCapture(1)
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
            cv2.destroyAllWindows()
            cap.release()
            break
        

# Create Tkinter window
app = tk.Tk()
app.title("Shape and Color Detection")
app.geometry("800x600")  # Set window size to 1200x800 pixels

# Create a label for displaying the webcam feed
webcam_label = tk.Label(app)
webcam_label.pack(side=tk.TOP, padx=10, pady=10, expand=True)

# Create a frame for the buttons to help with alignment
button_frame = tk.Frame(app)
button_frame.pack(side=tk.TOP, pady=50)  # Padding to move the buttons away from the webcam feed

# Button to load an image from file (make it larger)
load_button = tk.Button(button_frame, text="Load Image", command=load_image_from_file, 
                        width=20, height=2, font=('Helvetica', 14))  # Adjust size and font
load_button.pack(side=tk.LEFT, padx=20)

# Button to open the webcam and display the feed in the frame (make it larger)
webcam_button = tk.Button(button_frame, text="Open Webcam", command=open_webcam, 
                        width=20, height=2, font=('Helvetica', 14))  # Adjust size and font
webcam_button.pack(side=tk.RIGHT, padx=20)

# Start the Tkinter main loop
app.mainloop()
