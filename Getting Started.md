### Getting Started Guide

Welcome to the **Object Pattern Recognizer** project! This guide will help you set up the environment, understand the main components, and begin detecting shapes and colors in images or real-time webcam feeds.

---

### Project Overview

This project uses **Python** and **OpenCV** to recognize and log geometrical shapes (e.g., circles, squares) and colors (e.g., red, green) in images and webcam feeds. Detected shapes and colors are stored with a timestamp in a CSV file for easy tracking.

---

### Prerequisites

Ensure you have the following software and libraries:

1. **Python 3.x**
2. **Required Libraries**:
   - `opencv-python` (for image processing)
   - `numpy` (for numerical operations)
   - `Pillow` (for image display in Tkinter)
   - `Tkinter` (for GUI, usually included with Python)
   - `matplotlib` (for displaying processed images)

To install the required packages, run:
```bash
pip install opencv-python numpy Pillow matplotlib
```

### Project Structure

Here's a breakdown of the main files:

1. **datalog.py**: Manages logging of recognized shapes and colors with timestamps to `log.csv`.
2. **shape_detection.py**: Contains the main shape and color detection functions for images and webcam frames.
3. **gui.py**: Builds the user interface for loading images or accessing the webcam feed.
4. **README.md**: Provides an overview of the project and instructions.
5. **log.csv**: Stores all detected shapes and colors with timestamps (created automatically).

---

### Running the Project

#### 1. Launch the GUI

To start the application, run `gui.py`:
```bash
python gui.py
```

#### 2. Using the Application

**A. Load an Image from File**
- Click the **"Load Image"** button in the GUI.
- Select an image file from your computer.
- The application will detect shapes and colors, annotate the image, and display the results.
- Each detected shape and color is logged to `log.csv` with a timestamp.

**B. Use the Webcam for Real-Time Detection**
- Click **"Open Webcam"** to start the live feed.
- Detected shapes and colors will appear as overlays on the video stream.
- Press **q** to exit the webcam feed.
- Detected shapes and colors are logged in real-time to `log.csv`.

---

### CSV Log File

Every detection is stored in `log.csv` in the following format:

```
Timestamp,Shape,Color
2024-10-21 12:45:30,Circle,Red
2024-10-21 12:45:35,Square,Blue
```

This file is useful for tracking detections over time, and it includes:
- **Timestamp**: Date and time of detection.
- **Shape**: Recognized shape (e.g., Circle, Square, etc.).
- **Color**: Dominant detected color.

---

### Developer Information

- **Developed by**: Valerio Aemisegger, Marco Immer, Mauro Frehner
- **Version**: 1.0
