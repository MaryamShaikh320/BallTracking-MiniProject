import cv2
from collections import deque
from modules.physics import calculate_trajectory
from modules.tracker import get_ball_position
from modules.visualizer import draw_trajectory

points_history = []
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_ball_pos = get_ball_position(frame)
    if current_ball_pos is not None:
        points_history.append(current_ball_pos)

    if len(points_history) >= 3:
        future_arc = calculate_trajectory(points_history)
        draw_trajectory(frame, points_history, future_arc)
    
    cv2.imshow("Trajectory Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()