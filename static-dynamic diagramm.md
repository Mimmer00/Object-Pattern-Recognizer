sequenceDiagram
    participant User as 👤 User
    participant GUI as GUI
    participant ShapeDetection as Shape Detection
    participant DataLog as Data Logger
    participant CSV as log.csv
    participant Webcam as Webcam

    alt Load Image from File
        User->>GUI: Select Image
        GUI->>ShapeDetection: detect_shapes_and_colors_from_image()
        ShapeDetection->>ShapeDetection: load_image(image_path)
        ShapeDetection->>ShapeDetection: convert_to_hsv_and_gray(image)
        ShapeDetection->>ShapeDetection: find_contours(gray_image)
        alt Shape and Color Detected
            ShapeDetection->>DataLog: write_log_to_csv(shape, color)
            DataLog->>CSV: Append shape and color with timestamp
        else No Shape Detected
            ShapeDetection-->>GUI: No shapes found
        end
    else Load Image from Webcam
        User->>GUI: Start Webcam
        GUI->>Webcam: Open feed
        loop Every Frame
            Webcam->>ShapeDetection: detect_shapes_and_colors_from_webcam()
            ShapeDetection->>ShapeDetection: convert_to_hsv_and_gray(frame)
            ShapeDetection->>ShapeDetection: find_contours(gray_frame)
            alt Shape and Color Detected
                ShapeDetection->>DataLog: write_log_to_csv(shape, color)
                DataLog->>CSV: Append shape and color with timestamp
            else No Shape Detected
                ShapeDetection-->>GUI: No shapes found
            end
        end
        User->>GUI: Stop Webcam
        GUI->>Webcam: Close feed
    end
    GUI->>User: Display detected shapes and colors
