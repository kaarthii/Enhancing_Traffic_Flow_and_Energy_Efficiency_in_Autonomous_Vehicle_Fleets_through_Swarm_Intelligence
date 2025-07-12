import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('models/best.pt')

# Thresholds
heavy_threshold = 10

# ACO pheromones
pheromone_left = 1.0
pheromone_right = 1.0
evaporation = 0.1
reward = 2.0

def update_pheromones(left, right):
    global pheromone_left, pheromone_right
    if left < right:
        pheromone_left += reward / (left + 1)
        pheromone_right *= (1 - evaporation)
    else:
        pheromone_right += reward / (right + 1)
        pheromone_left *= (1 - evaporation)

def suggest_lane():
    total = pheromone_left + pheromone_right
    prob_left = pheromone_left / total
    return "Left Lane" if prob_left > 0.5 else "Right Lane"

# Video capture
cap = cv2.VideoCapture('Vehicle_Detection_Image_Dataset/video4.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('aco_output.avi', fourcc, 20.0, 
                      (int(cap.get(3)), int(cap.get(4))))

# Fonts
font = cv2.FONT_HERSHEY_SIMPLEX
font_color = (255, 255, 255)
bg_color = (0, 0, 255)
alert_color = (0, 255, 255)
scale = 1

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, imgsz=640, conf=0.4)
    frame_drawn = results[0].plot()

    boxes = results[0].boxes.xyxy
    left_count = 0
    right_count = 0

    for box in boxes:
        x_center = (box[0] + box[2]) / 2
        if x_center < frame.shape[1] // 2:
            left_count += 1
        else:
            right_count += 1

    update_pheromones(left_count, right_count)
    suggestion = suggest_lane()

    # Annotations
    cv2.rectangle(frame_drawn, (10, 20), (450, 90), bg_color, -1)
    cv2.putText(frame_drawn, f"Left Lane: {left_count}", (20, 50), font, scale, font_color, 2)
    cv2.putText(frame_drawn, f"Intensity: {'Heavy' if left_count > heavy_threshold else 'Smooth'}", 
                (20, 85), font, scale, font_color, 2)

    cv2.rectangle(frame_drawn, (820, 20), (1260, 90), bg_color, -1)
    cv2.putText(frame_drawn, f"Right Lane: {right_count}", (830, 50), font, scale, font_color, 2)
    cv2.putText(frame_drawn, f"Intensity: {'Heavy' if right_count > heavy_threshold else 'Smooth'}", 
                (830, 85), font, scale, font_color, 2)

    cv2.putText(frame_drawn, f"ACO Suggestion: Use {suggestion}", 
                (300, 150), font, scale + 0.3, alert_color, 3)

    cv2.imshow("Swarm Traffic", frame_drawn)
    out.write(frame_drawn)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
