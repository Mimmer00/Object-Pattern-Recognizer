import cv2
import numpy as np
import matplotlib.pyplot as plt

# Farberkennung basierend auf HSV-Werten
def get_color(hue, sat, val):
    if sat < 80:  # geringe Sättigung
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
    # Bild laden
    image = cv2.imread(image_path)
    if image is None:
        print("Fehler: Bild konnte nicht geladen werden. Überprüfe den Pfad zum Bild.")
        return
    
    # Konvertiere BGR zu HSV für bessere Farberkennung
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Farbkonvertierung von BGR zu Graustufen
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Schwellenwertanwendung, um die Kanten zu maximieren
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Konturen finden
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        # Approximiere die Kontur, um die Form zu erkennen
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        # Finde das umschließende Rechteck, um die Koordinaten zu erhalten
        x, y, w, h = cv2.boundingRect(approx)
        
        if len(approx) == 3:
            shape = "Triangle"
        elif len(approx) == 4:
            # Überprüfen ob es ein Quadrat oder Rechteck ist
            aspectRatio = float(w) / h
            if 0.95 <= aspectRatio <= 1.05:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif len(approx) > 4:
            shape = "Circle"
        else:
            continue  # Nicht erkennbare Formen werden ignoriert

        # Maske erstellen und die durchschnittliche Farbe innerhalb der Maske berechnen
        mask = np.zeros_like(gray)
        cv2.drawContours(mask, [cnt], -1, 255, -1)
        mean_val = cv2.mean(hsv, mask=mask)

        # Farberkennung basierend auf HSV-Werten
        hue, sat, val = mean_val[:3]
        color = get_color(hue, sat, val)

        # Text und Konturen zeichnen
        cv2.putText(image, f'{color} {shape}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        cv2.drawContours(image, [cnt], -1, (0, 255, 0), 2)
    
    # Das Ergebnis anzeigen
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Pfad zum Bild
image_path = 'image_1.png'
detect_shapes_and_colors(image_path)