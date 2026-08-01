import numpy as np

def calculate_trajectory(points, future_steps=15):
    if len(points) < 3:
        return []
    
    x_coords = np.array([p[0] for p in points])
    y_coords = np.array([p[1] for p in points])
    
    try:
        curve_coefficients = np.polyfit(x_coords, y_coords, 2)
        poly_func = np.poly1d(curve_coefficients)

        x_direction = x_coords[-1] - x_coords[0]
        step_size = 10 if x_direction >= 0 else -10

        last_x = x_coords[-1]
        future_x = [last_x + (i * step_size) for i in range (1, future_steps + 1)]

        future_points = []
        for x in future_x:
            y = int(poly_func(x))
            future_points.append(int(x), int(y))
        
        return future_points
    
    except (np.RankWarning, TypeError):
        return []