import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from main import detect_shapes_and_colors_from_image, detect_shapes_and_colors_from_webcam

app = tk.Tk()
app.title("Shape and Color Detection")
app.geometry("1000x700")

webcam_label = tk.Label(app)
webcam_label.pack(side=tk.TOP, padx=10, pady=10, expand=True)

button_frame = tk.Frame(app)
button_frame.pack(side=tk.TOP, pady=50)  # Padding to move the buttons away from the webcam feed

def load_image_from_file():
    """
    Open a file dialog to allow the user to select an image file from the file system. 
    Once selected, the function processes the image by detecting shapes and colors.
    
    Args:
        None
    
    Returns:
        None
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_shapes_and_colors_from_image(file_path)

load_button = tk.Button(button_frame, text="Load Image", command=lambda: load_image_from_file(),
                        width=20, height=2, font=('Helvetica', 14))  # Adjust size and font
load_button.pack(side=tk.LEFT, padx=20)

def stop_webcam():
    """
    Stop the webcam feed and release the camera resources. This function also clears 
    the webcam feed display and redisplays the main buttons.

    Args:
        None
    
    Returns:
        None
    """
    cap.release()  
    webcam_label.configure(image='')
    button_frame.pack(side=tk.TOP, pady=50) 
    back_button.pack_forget()  

def open_webcam():
    """
    Open the webcam feed and display it in the Tkinter window. Each frame from the webcam 
    is processed in real-time to detect shapes and colors.

    Args:
        None

    Returns:
        None
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam could not be opened.")
        return
    
    def update_frame():
        """
        Capture and process the current frame from the webcam feed. This function runs 
        recursively every 10 milliseconds to continuously update the webcam feed.

        Args:
            None
        
        Returns:
            None
        """
        ret, frame = cap.read()
        if ret:
           
            processed_frame = detect_shapes_and_colors_from_webcam(frame)
            
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            webcam_label.imgtk = imgtk
            webcam_label.configure(image=imgtk)

        if cap.isOpened():
            webcam_label.after(10, update_frame)

    def stop_webcam():
        """
        Stop the webcam feed, release the camera resources, clear the webcam feed display, 
        and return to the main menu by redisplaying the buttons.

        Args:
            None
        
        Returns:
            None
        """
        cap.release() 
        webcam_label.configure(image='') 
        button_frame.pack(side=tk.TOP, pady=50) 
        back_button.pack_forget()  

    back_button = tk.Button(app, text="Zurück", command=lambda: stop_webcam(),
                            width=20, height=2, font=('Helvetica', 14))
    
    update_frame() 
    
    back_button.pack(side=tk.BOTTOM, pady=10)

webcam_button = tk.Button(button_frame, text="Open Webcam", command=lambda: [open_webcam(), button_frame.pack_forget()],
                          width=20, height=2, font=('Helvetica', 14)) 
webcam_button.pack(side=tk.RIGHT, padx=20)

back_button = tk.Button(app, text="Zurück", command=stop_webcam, 
                        width=20, height=2, font=('Helvetica', 14))

app.mainloop()