import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from main import detect_shapes_and_colors_from_image, detect_shapes_and_colors_from_webcam

# Create Tkinter window
app = tk.Tk()
app.title("Shape and Color Detection")
app.geometry("1000x700")  # Set window size

# Create a label for displaying the webcam feed
webcam_label = tk.Label(app)
webcam_label.pack(side=tk.TOP, padx=10, pady=10, expand=True)

# Create a frame for the buttons to help with alignment
button_frame = tk.Frame(app)
button_frame.pack(side=tk.TOP, pady=50)  # Padding to move the buttons away from the webcam feed

# Function to load an image from file and process it
def load_image_from_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_shapes_and_colors_from_image(file_path)

# Button to load an image from file (make it larger)
load_button = tk.Button(button_frame, text="Load Image", command=lambda: load_image_from_file(),
                        width=20, height=2, font=('Helvetica', 14))  # Adjust size and font
load_button.pack(side=tk.LEFT, padx=20)

def stop_webcam():
    cap.release()  # Stop the webcam
    webcam_label.configure(image='')  # Clear the image
    button_frame.pack(side=tk.TOP, pady=50)  # Show the buttons again
    back_button.pack_forget()  # Hide the back button
    
# Define the webcam and back button after all the necessary functions
def open_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam could not be opened.")
        return
    
    def update_frame():
        ret, frame = cap.read()
        if ret:
            # Process each frame with your existing function
            processed_frame = detect_shapes_and_colors_from_webcam(frame)
            
            # Convert the frame to RGB (OpenCV uses BGR by default)
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            
            # Convert the frame to a PIL image and then to a PhotoImage
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Update the label with the new image
            webcam_label.imgtk = imgtk
            webcam_label.configure(image=imgtk)
        
        # Repeat after 10ms
        if cap.isOpened():
            webcam_label.after(10, update_frame)

    # Function to stop the webcam and return to the main menu
    def stop_webcam():
        cap.release()  # Stop the webcam
        webcam_label.configure(image='')  # Clear the image
        button_frame.pack(side=tk.TOP, pady=50)  # Show the buttons again
        back_button.pack_forget()  # Hide the back button
        
    # Create the "Zurück" button (initially hidden) after the stop_webcam function is defined
    back_button = tk.Button(app, text="Zurück", command=lambda: stop_webcam(),  # Call stop_webcam directly
                            width=20, height=2, font=('Helvetica', 14))
    
    update_frame()  # Start updating the frames
    
    # Show the "Zurück" button
    back_button.pack(side=tk.BOTTOM, pady=10)

# Button to open the webcam and display the feed in the frame 
webcam_button = tk.Button(button_frame, text="Open Webcam", command=lambda: [open_webcam(), button_frame.pack_forget()],
                          width=20, height=2, font=('Helvetica', 14))  # Adjust size and font
webcam_button.pack(side=tk.RIGHT, padx=20)

# Create the "Zurück" button
back_button = tk.Button(app, text="Zurück", command=stop_webcam,  # Call stop_webcam directly
                        width=20, height=2, font=('Helvetica', 14))

# Start the Tkinter main loop
app.mainloop()
