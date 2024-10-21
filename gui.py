import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from main import detect_shapes_and_colors_from_image, detect_shapes_and_colors_from_webcam

app = tk.Tk()
app.title("Shape and Color Detection")
app.attributes("-fullscreen", True)  

splash_frame = tk.Frame(app)
splash_frame.pack(fill="both", expand=True)

splash_text = tk.Label(splash_frame, text="Welcome to Shape and Color Detection", font=('Helvetica', 24))
splash_text.pack(pady=50)

splash_image = Image.open("image_0.png")
splash_image = splash_image.resize((500, 400))  
splash_image = ImageTk.PhotoImage(splash_image)

splash_label = tk.Label(splash_frame, image=splash_image)
splash_label.image = splash_image  
splash_label.pack(pady=20)

webcam_label = tk.Label(app)
webcam_label.pack(side=tk.TOP, padx=10, pady=10, expand=True)

button_frame = tk.Frame(app)
button_frame.pack(side=tk.TOP, pady=50)  

def load_image_from_file():
    """
    Opens a file dialog for selecting an image file, then processes it 
    by calling the detect_shapes_and_colors_from_image function from the main module.
    """
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_shapes_and_colors_from_image(file_path)
        
load_button = tk.Button(button_frame, text="Load Image", command=lambda: load_image_from_file(),
                        width=20, height=2, font=('Helvetica', 14))
load_button.pack(side=tk.LEFT, padx=20)

def stop_webcam():
    """
    Stops the webcam feed by releasing the camera and clearing the webcam_label. 
    Also hides the "Zurück" button and re-displays the main buttons.
    """
    cap.release()
    webcam_label.configure(image='')
    button_frame.pack(side=tk.TOP, pady=50)
    back_button.pack_forget()

def open_webcam():
    """
    Opens the webcam and displays the feed in the GUI. Each frame is processed using the
    detect_shapes_and_colors_from_webcam function. The "Zurück" button is shown, allowing the user to stop the feed.
    """
    splash_frame.pack_forget()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam could not be opened.")
        return
    
    def update_frame():
        """
        Captures frames from the webcam, processes them, converts the frame to RGB,
        and updates the Tkinter Label with the processed frame.
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
        Stops the webcam, clears the display, and re-displays the main buttons.
        """
        cap.release() 
        webcam_label.configure(image='')
        splash_frame.pack(fill="both", expand=True) 
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

exit_button = tk.Button(app, text="Exit", command=app.quit, 
                        width=20, height=2, font=('Helvetica', 14))
exit_button.pack(side=tk.BOTTOM, padx=40, pady=10)  

app.mainloop()
