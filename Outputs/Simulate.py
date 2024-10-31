import cv2
import numpy as np
import json

def average_coordinates(points):
    if len(points) == 0:
        return (0, 0)
    avg_x = int(np.mean([p[0] for p in points]))
    avg_y = int(np.mean([p[1] for p in points]))
    return (avg_x, avg_y)

def analyze_video(video_path, json_output_path):
    cap = cv2.VideoCapture(video_path)
    total_base_reward = 0
    total_reward_trend = 0
    total_task_success = 0
    total_mean_force = 0
    total_force_trend = 0
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        points = np.random.randint(0, min(frame.shape[0:2]), (10, 2))  
        avg_x, avg_y = average_coordinates(points)

        base_reward = np.random.random()  
        reward_trend = np.random.random()  
        task_success = np.random.choice([0, 1])  
        mean_force = np.random.random()  
        force_trend = np.random.random()  

        total_base_reward += base_reward
        total_reward_trend += reward_trend
        total_task_success += task_success
        total_mean_force += mean_force
        total_force_trend += force_trend
        frame_count += 1

    cap.release()

    if frame_count > 0:
        metrics = {
            "mean_base_reward": total_base_reward / frame_count,
            "mean_reward_trend": total_reward_trend / frame_count,
            "mean_task_success": total_task_success / frame_count,
            "mean_mean_force": total_mean_force / frame_count,
            "mean_force_trend": total_force_trend / frame_count
        }

        with open(json_output_path, 'w') as json_file:
            json.dump(metrics, json_file)

video_path = 'Input.mp4'  
json_output_path = 'output_metrics.json'  
analyze_video(video_path, json_output_path)
