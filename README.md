
# Object Pattern Recognizer

SWENG Project Object Pattern Recognizer

## Description

This Python project uses OpenCV to detect geometric shapes (circles, squares, rectangles, and triangles) and their colors (red, green, blue, yellow, and violet) in images. It demonstrates the use of image processing techniques to classify and annotate objects based on their features.

### Main Features

- **Load Image from File**: Users can load an image from their computer. The program detects and annotates shapes (such as circles, rectangles, and triangles) and their dominant colors (e.g., red, green, blue) in the image.
- **Live Webcam Feed**: Users can access their webcam to detect shapes and colors in real time. Detected shapes and colors are annotated directly in the webcam feed.
- **Logging**: All detected shapes and colors are logged with a timestamp in a CSV file, which can be also downloaded with the "Download Log" button.

### Updates Based on Current Python Files

- The function **`detect_shapes_and_colors_from_image`** in `shape_detection.py` analyzes images loaded by the user and detects shapes and colors.
- The function **`detect_shapes_and_colors_from_webcam`** in `shape_detection.py` is used to analyze webcam images in real time to detect shapes and colors.
- The **`datalog.py`** module uses the **`write_log_to_csv`** function to log detected shapes and colors in the `log.csv` file. These logs include the timestamp, recognized shape, and color.

## Prerequisites

Ensure that the following libraries are installed:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Pillow (`Pillow`) – for image processing in Tkinter
- Tkinter (typically included with Python)
- Matplotlib – if charts are needed

You can install these libraries with the following command:

```bash
pip install opencv-python numpy Pillow matplotlib
```

## How to Use

### Load Image from File:

1. Click the **"Load Image"** button to open an image from your file system.
2. The program analyzes the image, detects shapes and colors, and displays the processed image with annotations.
3. The detected shapes and colors are logged in the `log.csv` file with a timestamp.

### Use Webcam:

1. Click **"Open Webcam"** to start the webcam feed.
2. The program detects shapes and colors in real time and displays them directly in the video stream.
3. Press `q` to stop the webcam stream.
4. The detected shapes and colors are also logged in the `log.csv` file.

## Log File

Each time a shape and color are detected, the result is recorded in a CSV file (`log.csv`) with a timestamp. The log file contains the following information:

- **Timestamp**: The date and time when the recognition occurred.
- **Shape**: The recognized shape (e.g., circle, square, triangle).
- **Color**: The recognized dominant color (e.g., red, green, blue).

An example of the contents of the `log.csv` file:

```csv
Timestamp,Shape,Color
2024-10-21 12:45:30,Circle,Red
2024-10-21 12:45:35,Square,Blue
```
The Log file can be downloaded as a CSV file with the "Download Log" button.

## Examples of Recognized Shapes and Colors

- **Shapes**: Circle, Square, Rectangle, Triangle
- **Colors**: Red, Green, Blue, Yellow, Violet

## Developers

- Developed by: Valerio Aemisegger, Marco Immer, Mauro Frehner
- Version: 1.0
