# Object-Pattern-Recognizer
SWENG Project Object Pattern Recognizer
## Description
This Python script uses OpenCV to detect geometric shapes (circles, squares, rectangles, and triangles) and their colors (red, green, blue, yellow, and violet) in images. It demonstrates the use of image processing techniques to classify and annotate objects based on their characteristics.

- **Load Image from File**: Users can load an image from their computer, and the application will detect and annotate shapes (such as circles, rectangles, triangles) and their dominant colors (e.g., red, green, blue) on the image.
- **Live Webcam Feed**: Users can access their webcam to detect shapes and colors in real-time. Detected shapes and colors are annotated directly on the webcam feed.
- **Logging**: Detected shapes and colors are logged into a CSV file with a timestamp.

## Prerequisites
- Python 3.x
- OpenCV
- NumPy
- Matplotlib
- Tkinter
- Pillow

## How to Use

Click the "Load Image" button to open an image from your file system.
The program will analyze the image, detect shapes and colors, and display the processed image with annotations.

Click the "Open Webcam" button to start the webcam feed.
The program will detect shapes and colors in real-time and display them on the video feed.
Press q to quit the webcam stream.

Every time a shape and color are detected, the result is logged in a CSV file (log.csv) with a timestamp. The log file includes the following:

Timestamp: The date and time when the detection occurred.
Shape: The shape detected (e.g., Circle, Square, Triangle).
Color: The dominant color detected (e.g., Red, Green, Blue).