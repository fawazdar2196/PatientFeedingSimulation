Patient Feeding Simulation using Reinforcement Learning
Overview

This repository contains a reinforcement learning–based simulation study for assistive robotic tasks using the Assistive Gym environment. The project focuses on evaluating how different RL algorithms perform on human-care interaction tasks such as feeding, drinking, bathing, and scratching.

The work began with a model-based approach using PyDreamer and was later extended to a comparative evaluation against Recurrent PPO and DreamerV3 to understand performance differences across tasks.

Assistive Tasks Studied

The following Assistive Gym tasks were evaluated:

Feeding

Drinking

Bed Bathing

Itch Scratching

Dressing

Arm Manipulation

Each task measures:

Task success rate

Interaction force

Cumulative reward

Algorithms Compared

The project compares three reinforcement learning approaches:

PyDreamer (model-based RL, initial baseline)

Recurrent PPO (model-free RL with memory)

DreamerV3 (advanced model-based RL)

Although the project initially used PyDreamer, later experiments showed that PPO-based approaches were more stable and effective for contact-sensitive assistive tasks such as feeding.

Key Results (Summary)
Task	Best Performing Method	Notes
Feeding	DreamerV3 / PPO	High success, low force
Drinking	DreamerV3	Highest reward
Itch Scratching	DreamerV3	Best overall balance
Bed Bathing	DreamerV3	Significant improvement over PPO
Dressing	All struggled	Task complexity
Arm Manipulation	All struggled	High force, low success

Example (Feeding task):

PPO: 90% success, low interaction force

DreamerV3: 100% success, lowest force

PyDreamer: Lower stability
