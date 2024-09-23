import cv2
import numpy as np
import matplotlib.pyplot as plt

# Color recognition based on HSV values
def get_color(hue, sat, val):
    if sat < 80:  # low saturation
        return "Unclear"
    elif hue < 10 or (hue > 160 and hue < 180):
        return "Red"
    elif hue >= 15 and hue < 45:
        return "Yellow"
    elif hue >= 45 and hue < 70:
        return "Green"
    elif hue >= 70 and hue < 125:
        return "Blue"
    elif hue >= 130 and hue < 160:
        return "Violet"
    else:
        return "Unclear"

def detect_shapes_and_colors(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image could not be loaded. Check the image path.")
        return
    
    # Convert BGR to HSV for better color recognition
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Convert BGR to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply threshold to maximize edges
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        # Approximate the contour to identify the shape
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        # Find the bounding rectangle to get coordinates
        x, y, w, h = cv2.boundingRect(approx)
        
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            # Check if it is a square or rectangle
            aspectRatio = float(w) / h
            if 0.95 <= aspectRatio <= 1.05:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif len(approx) > 4:
            shape = "Circle"
        else:
            continue  # Ignore unrecognizable shapes

        # Create a mask and calculate the average color within the mask
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [cnt], -1, 255, -1)
        mean_val = cv2.mean(hsv, mask=mask)

        # Color recognition based on HSV values
        hue, sat, val = mean_val[:3]
        color = get_color(hue, sat, val)

        # Draw text and contours
        cv2.putText(image, f'{color} {shape}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
    
    # Display the result
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Path to the image
image_path = 'image_1.png'
detect_shapes_and_colors(image_path)