# Object-Pattern-Recognizer

SWENG Project Object Pattern Recognizer

## Description

Dieses Python-Projekt verwendet OpenCV, um geometrische Formen (Kreise, Quadrate, Rechtecke und Dreiecke) und deren Farben (Rot, Grün, Blau, Gelb und Violett) in Bildern zu erkennen. Es demonstriert die Verwendung von Bildverarbeitungstechniken zur Klassifizierung und Annotation von Objekten basierend auf ihren Merkmalen.

### Hauptfunktionen

- **Bild von Datei laden**: Benutzer können ein Bild von ihrem Computer laden. Das Programm erkennt und annotiert daraufhin Formen (wie Kreise, Rechtecke, Dreiecke) und deren dominante Farben (z. B. Rot, Grün, Blau) im Bild.
- **Live-Webcam-Feed**: Benutzer können auf ihre Webcam zugreifen, um Formen und Farben in Echtzeit zu erkennen. Erkannte Formen und Farben werden direkt im Webcam-Feed annotiert.
- **Protokollierung**: Alle erkannten Formen und Farben werden mit einem Zeitstempel in einer CSV-Datei protokolliert.

### Änderungen basierend auf den aktuellen Python-Dateien

- Die Funktion **`detect_shapes_and_colors_from_image`** in `shape_detection.py` analysiert Bilder, die vom Benutzer geladen wurden, und erkennt Formen und Farben.
- Die Funktion **`detect_shapes_and_colors_from_webcam`** in `shape_detection.py` wird verwendet, um die Webcam-Bilder in Echtzeit zu analysieren und Formen sowie Farben zu erkennen.
- Das Modul **`datalog.py`** verwendet die Funktion **`write_log_to_csv`**, um die erkannten Formen und Farben in der Datei `log.csv` zu protokollieren. Diese Protokolle enthalten den Zeitstempel, die erkannte Form und die Farbe.

## Prerequisites

Stellen Sie sicher, dass die folgenden Bibliotheken installiert sind:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Pillow (`Pillow`) – für die Bildverarbeitung in Tkinter
- Tkinter (wird normalerweise mit Python geliefert)
- Matplotlib – falls Diagramme benötigt werden

Sie können diese Bibliotheken mit folgendem Befehl installieren:

```bash
pip install opencv-python numpy Pillow matplotlib
```

## How to Use

### Bild von Datei laden:

1. Klicken Sie auf die Schaltfläche **"Load Image"**, um ein Bild von Ihrem Dateisystem zu öffnen.
2. Das Programm analysiert das Bild, erkennt Formen und Farben, und zeigt das verarbeitete Bild mit Annotationen an.
3. Die erkannten Formen und Farben werden in der Datei `log.csv` mit einem Zeitstempel protokolliert.

### Webcam verwenden:

1. Klicken Sie auf **"Open Webcam"**, um den Webcam-Feed zu starten.
2. Das Programm erkennt Formen und Farben in Echtzeit und zeigt sie direkt im Videostream an.
3. Drücken Sie `q`, um den Webcam-Stream zu beenden.
4. Die erkannten Formen und Farben werden ebenfalls in der Datei `log.csv` protokolliert.

## Log-Datei

Jedes Mal, wenn eine Form und eine Farbe erkannt werden, wird das Ergebnis in einer CSV-Datei (`log.csv`) mit einem Zeitstempel protokolliert. Die Protokolldatei enthält die folgenden Informationen:

- **Timestamp**: Das Datum und die Uhrzeit, zu der die Erkennung stattgefunden hat.
- **Shape**: Die erkannte Form (z. B. Kreis, Quadrat, Dreieck).
- **Color**: Die erkannte dominante Farbe (z. B. Rot, Grün, Blau).

Ein Beispiel für den Inhalt der `log.csv`-Datei:

```csv
Timestamp,Shape,Color
2024-10-21 12:45:30,Circle,Red
2024-10-21 12:45:35,Square,Blue
```

## Beispiel für erkannte Formen und Farben

- **Formen**: Kreis, Quadrat, Rechteck, Dreieck
- **Farben**: Rot, Grün, Blau, Gelb, Violett

## Entwickler

- Entwickelt von: Valerio Aemisegger, Marco Immer, Mauro Frehner
- Version: 1.0
