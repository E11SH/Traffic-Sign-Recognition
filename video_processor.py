import cv2
import numpy as np


def process_video(video_path, output_path, model, label_map):
    
    # Processes an entire video file, applies sign detection, and saves the output.
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    
    out = cv2.VideoWriter(output_path, fourcc, 20.0,
                          (int(cap.get(3)), int(cap.get(4))))

    # Add a check to ensure the VideoWriter was created successfully
    if not out.isOpened():
        print("Error: Could not open video writer. Check if the 'avc1' codec is supported.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = detect_signs(frame, model, label_map)
        out.write(processed_frame)

    print(f"Video processing complete. Output saved to {output_path}")
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def detect_signs(frame, model, label_map, input_size=(32, 32), conf_thresh=0.4):
 
    #Detects and classifies traffic signs in a single video frame.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red mask
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 20 and h > 20 and w < frame.shape[1] and h < frame.shape[0]:
            roi = frame[y:y + h, x:x + w]
            
            roi_resized = cv2.resize(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB), input_size) / 255.0
            roi_resized = np.expand_dims(roi_resized, axis=0)

            preds = model.predict(roi_resized, verbose=0)
            class_id = int(np.argmax(preds))
            confidence = float(np.max(preds))
            
            print(f"  -> Detected ROI with confidence: {confidence:.2f} for Class ID: {class_id}")
            if confidence > conf_thresh and class_id in label_map:
                print(f"    ===> SUCCESS! Drawing box for Class ID: {class_id} with confidence {confidence:.2f}")
                label_text = f"{label_map[class_id]} ({confidence * 100:.1f}%)"
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 255, 0), 2)
    return frame