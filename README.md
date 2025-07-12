# Enhancing Traffic Flow and Energy Efficiency in Autonomous Vehicle Fleets through Swarm Intelligence

An intelligent and adaptive traffic management system that leverages real-time object detection (YOLOv8) and swarm intelligence to optimize lane allocation and improve urban traffic flow.

---

## Project Overview

Modern cities face increasing traffic congestion, long travel times, and inefficient energy usage due to outdated static traffic control systems. This project presents a dynamic and decentralized solution using:

- YOLOv8 for real-time vehicle detection and lane occupancy monitoring.
- Swarm Intelligence algorithms (e.g., Ant Colony Optimization, Particle Swarm Optimization) for decentralized coordination among autonomous vehicles.
- Reinforcement Learning principles for adaptive lane reallocation.

Result: Smoother traffic flow, reduced vehicle idle time, and improved lane utilization in a simulated urban environment.

---

## Key Features

- Real-time vehicle detection and classification using YOLOv8.
- Swarm-based coordination of autonomous vehicles (AVs).
- Adaptive lane switching and speed optimization.
- Decentralized decision-making (no centralized traffic controller).
- Real-time response to traffic congestion.
- Visualizations: Lane occupancy, traffic intensity, and load distribution.
- Simulated using SUMO (Simulation of Urban Mobility).

---

## Technologies Used

| Component         | Description                                      |
|------------------|--------------------------------------------------|
| YOLOv8           | For real-time object detection of vehicles       |
| Python           | Core development language                        |
| OpenCV           | Video processing & frame analysis                |
| SUMO             | Traffic simulation environment                   |
| Swarm Algorithms | ACO, PSO for cooperative decentralized control   |
| Matplotlib       | Graphical plots and data visualization           |
| NumPy/Pandas     | Data handling and manipulation                   |

---


## Core Concepts
- YOLOv8 is used for object detection on video frames to identify number, type, and position of vehicles.
- Swarm intelligence allows each autonomous vehicle to act as a decentralized agent that:
    - Shares information with nearby AVs,
    - Makes rerouting decisions,
    - Balances lane loads dynamically.
- No central controller is required — decisions emerge from local interactions.

## Contributors
- Shushma Sree G
- Karthi D

