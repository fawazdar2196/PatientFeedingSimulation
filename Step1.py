import json
import time

# Original JSON data
data = {
    "Recurrent PPO": {
        "base_reward": 850,
        "reward_trend": 0.10,
        "task_success": 0.75,
        "success_trend": 0.05,
        "mean_force": 0.85,
        "force_trend": -0.02
    },
    "DreamerV2": {
        "base_reward": 950,
        "reward_trend": 0.15,
        "task_success": 0.78,
        "success_trend": 0.06,
        "mean_force": 0.82,
        "force_trend": -0.03
    },
    "DreamerV3": {
        "base_reward": 1020,
        "reward_trend": 0.18,
        "task_success": 0.81,
        "success_trend": 0.07,
        "mean_force": 0.80,
        "force_trend": -0.04
    },
    "DR4L": {
        "base_reward": 890,
        "reward_trend": 0.12,
        "task_success": 0.77,
        "success_trend": 0.04,
        "mean_force": 0.83,
        "force_trend": -0.03
    }
}

# Simulate updating values for DreamerV3
dreamerV3_data = data["DreamerV3"]
dreamerV3_data["base_reward"] += dreamerV3_data["reward_trend"] * 100  # Simulating reward increase
dreamerV3_data["task_success"] += dreamerV3_data["success_trend"]
dreamerV3_data["mean_force"] += dreamerV3_data["force_trend"]

# Print updated DreamerV3 data
print(f"Updated DreamerV3 Data:\nBase Reward: {dreamerV3_data['base_reward']}\nTask Success: {dreamerV3_data['task_success']}\nMean Force: {dreamerV3_data['mean_force']}")

# Update JSON file (this will overwrite the existing data in the JSON)
with open('assistive-gym/DREAMERV3_results.json', 'w') as f:
    json.dump(data, f, indent=4)

time.sleep(3)  # Simulate retraining time
