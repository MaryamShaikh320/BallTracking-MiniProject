import cv2
import numpy as np

def draw_trajectory(frame, past_points, future_points):
    for point in past_points:
        cv2.circle(frame, point, 3, (255, 0, 0), -1)
    
    if len(future_points) > 1:
        pts = np.array(future_points, dtype=np.int32).reshape(-1, 1, 2)

        cv2.polylines(frame, [pts], isClosed=false, color=(0, 0, 255), thickness=2)