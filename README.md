# Patient Feeding Simulation using Reinforcement Learning

## Overview
This repository contains a reinforcement learning–based simulation study for assistive robotic tasks using the Assistive Gym environment. The project focuses on evaluating how different RL algorithms perform on human-care interaction tasks such as feeding, drinking, bathing, and scratching.

The work initially started with a model-based approach using PyDreamer and was later extended to a comparative evaluation against Recurrent PPO and DreamerV3 to analyse performance, stability, and safety across assistive tasks.

---

## Assistive Tasks Studied
The following Assistive Gym tasks were evaluated:

- Feeding  
- Drinking  
- Bed Bathing  
- Itch Scratching  
- Dressing  
- Arm Manipulation  

Each task was evaluated using:
- Task success rate  
- Mean interaction force  
- Mean cumulative reward  

---

## Algorithms Compared
The following reinforcement learning approaches were implemented and compared:

- PyDreamer (model-based RL – initial baseline)
- Recurrent PPO (model-free RL with memory)
- DreamerV3 (advanced model-based RL)

While the project initially relied on PyDreamer, later experiments showed that PPO-based approaches were more stable and effective for contact-sensitive assistive tasks such as feeding.

---

## Key Results Summary

| Task | Strongest Performer | Notes |
|----|----|----|
| Feeding | DreamerV3 / PPO | High success, low force |
| Drinking | DreamerV3 | Highest reward |
| Itch Scratching | DreamerV3 | Best balance |
| Bed Bathing | DreamerV3 | Large improvement over PPO |
| Dressing | All struggled | High task complexity |
| Arm Manipulation | All struggled | High force, low success |

Detailed numerical results are available in `results.csv`.

---

## Repository Structure

```
PatientFeedingSimulation/
│
├── Step1.py               # Environment setup and task execution
├── analyze_video.py       # Video-based analysis of simulation output
├── Result.py              # Metrics aggregation and evaluation
├── results.csv            # Quantitative comparison of algorithms
├── simulation_data.csv    # Logged simulation data
├── Outputs/               # Visual outputs and plots
├── New.mp4                # Simulation demo video
└── pydreamer/             # Initial model-based RL implementation
```

---

## Visual Evidence
This repository includes:
- Simulation demo video (`New.mp4`)
- Output plots in the `Outputs/` directory
- CSV-based evaluation metrics

These artefacts demonstrate working simulations and algorithmic evaluation rather than conceptual code only.

---

## Technical Scope
- Language: Python  
- Frameworks: Assistive Gym, Reinforcement Learning (PPO, Dreamer variants)  
- Focus: Algorithm development, experimentation, and evaluation  
- Deployment: Not applicable (research simulation environment)

---

## Author
Fawaz Ahmed Dar  
GitHub: https://github.com/fawazdar2196
