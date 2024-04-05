# Enabling 3D Mapping and Localization for Multi-segment "Vine" Robot

## Overview
This project focuses on the development of 3D mapping and localization capabilities for a multi-segment "Vine" robot. Leveraging a combination of 6-axis IMU, RGB and Depth images, Time of Flight Laser Point, and real-time processing techniques, we aim to enhance the robot's understanding of its environment to facilitate better navigation and autonomy.

## Features
- **3D Mapping**: Utilizes RGB and Depth data to generate three-dimensional maps of the robot's surroundings.
- **Robot Localization**: Combines sensor data for accurate positioning and movement within the map.
- **PointCloud Assemble**: Converts sensor data into a PointCloud2 format for easy visualization and manipulation.
- **Autonomy Navigation**: Implements algorithms for autonomous movement, accounting for the robot's multi-segment flexibility and payload limitations.

## Control Strategy
The project employs an Arduino Nicla Vision for its control strategy, which includes:
- 6-axis IMU
- RGB Image capture
- On-board WiFi and Bluetooth
- Real-time streaming protocol (RTSP) streaming of QVGA video at 15fps

## Performance Optimization
Performance is enhanced through various techniques such as:
- Separate threading for CPU and CUDA
- Model size optimization for balance between speed and accuracy
- Reduction in computational complexity for faster segmentation

## Getting Started
To get started with this project, clone the repository and follow the setup instructions provided in the documentation.

```bash
git clone https://example-repository-for-vine-robot.git
cd vine-robot-3d-mapping
