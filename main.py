import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    """
    Load an image from a specified path.
    
    Args:
        image_path (str): The path to the image file.
    
    Returns:
        image: The loaded image in BGR format or None if loading fails.
    """
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image could not be loaded. Check the image path.")
    return image

def convert_to_hsv_and_gray(image):
    """
    Convert an image from BGR to HSV and Grayscale.
    
    Args:
        image: The image in BGR format.
    
    Returns:
        tuple: A tuple containing the HSV and Grayscale images.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return hsv, gray

def find_contours(gray_image):
    """
    Find contours in a grayscale image after applying binary inversion thresholding.
    
    Args:
        gray_image: The image in grayscale format.
    
    Returns:
        contours: A list of contours found in the image.
    """
    _, thresh = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def get_shape(contour):
    """
    Determine the shape of an object based on its contour.
    
    Args:
        contour: A contour of the object.
    
    Returns:
        str: The name of the shape or None if the shape is unrecognizable.
    """
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        aspectRatio = cv2.boundingRect(approx)[2] / cv2.boundingRect(approx)[3]
        return "Square" if 0.95 <= aspectRatio <= 1.05 else "Rectangle"
    elif len(approx) > 4:
        return "Circle"
    return None

def get_color(hsv_image, mask):
    """
    Determine the main color of an area in an image specified by a mask.
    
    Args:
        hsv_image: The image in HSV format.
        mask: A binary mask where the color is to be determined.
    
    Returns:
        str: The name of the dominant color.
    """
    mean_val = cv2.mean(hsv_image, mask=mask)
    hue, sat, _ = mean_val[:3]
    if sat < 40:
        return "Unclear"
    elif hue < 10 or (hue > 150 and hue < 190):
        return "Red"
    elif hue >= 15 and hue < 45:
        return "Yellow"
    elif hue >= 45 and hue < 70:
        return "Green"
    elif hue >= 70 and hue < 125:
        return "Blue"
    elif hue >= 130 and hue < 160:
        return "Violet"
    return "Unclear"

def detect_shapes_and_colors(image_path):
    """
    Load an image, detect shapes and their colors, and display the result with annotations.
    
    Args:
        image_path (str): The path to the image file.
    """
    image = load_image(image_path)
    if image is None:
        return

    hsv, gray = convert_to_hsv_and_gray(image)
    contours = find_contours(gray)

    for cnt in contours:
        shape = get_shape(cnt)
        if shape:
            mask = np.zeros_like(gray)
            cv2.drawContours(mask, [cnt], -1, 255, -1)
            color = get_color(hsv, mask)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.putText(image, f'{color} {shape}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
            cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
    
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
    
#image_path = 'image_1.png'
#detect_shapes_and_colors(image_path)
