# Enabling 3D Mapping and Localization for Multi-segment Vine Robot

## Overview
This project is dedicated to developing 3D mapping and localization capabilities for a multi-segment "Vine" robot. By integrating a combination of 6-axis IMU, RGB and Depth images, Time of Flight Laser Point, and real-time processing techniques, we enhance the robot's environmental understanding to facilitate improved navigation and autonomy.
## Demonstration Video
Click the image below to watch the demonstration video:
[![Vine Robot Demonstration](https://drive.google.com/uc?id=1orD6T02gCoKNCI5ZiVkwGCjW6SpTG-4V =250x250)](https://drive.google.com/file/d/1HP5o8t7EaylewrrqVIK36IUchOBx5_r5/view?usp=sharing)


## Features
- **Depth Estimation**: Depth estimation is achieved through Deep Learning-based semantic segmentation and models, specifically using [DINOv2](https://github.com/isl-org/ZoeDepth) and [MiDas](https://github.com/isl-org/MiDaS). Post-estimation, the RGB-D results are calibrated to enhance accuracy and reliability using the [ZoeDepth](https://github.com/isl-org/ZoeDepth) calibration tool.
- **Robot Localization**: Combines sensor data for accurate positioning and movement within the map, enhanced by Deep Learning-based semantic segmentation and depth estimation models.
- **3D Mapping**: Utilizes RGB, RGB-D and Odometry data to generate three-dimensional maps of the robot's surroundings.
- **PointCloud Assembly**: Converts sensor data into a PointCloud2 format for easy visualization and manipulation.

## Data Collection

Our system leverages the [Arduino Nicla Vision](https://docs.arduino.cc/hardware/nicla-vision/) as a versatile sensor suite which supports On-board WiFi and Bluetooth capabilities for comprehensive data collection, integrated with the [OpenMV](https://openmv.io/) platform. It employs MicroPython APIs to facilitate the synchronized transmission of multi-modal data, ensuring robust data synchronization through advanced multithreading techniques. The setup efficiently streams a rich dataset, including:

- 6-axis IMU readings, for detailed motion and orientation data.
- QVGA video at 10fps, providing visual feedback from the environment.
- Time of Flight (ToF) Laser Point measurements, for precise distance mapping


## Performance Optimization
Performance is enhanced through various techniques such as:
- Separate threading for CPU and CUDA
- Model size optimization for balance between speed and accuracy
- Reduction in computational complexity for faster segmentation

## ROS Packages
This project integrates multiple ROS packages to achieve its objectives:
- For **Robot Localization**, we use the `robot_localization` package, which is a versatile package providing state estimation for navigating robots. More details can be found in the [official documentation](https://docs.ros.org/en/melodic/api/robot_localization/html/index.html).
- **3D Mapping** is accomplished using the `RTAB-Map` (Real-Time Appearance-Based Mapping), a graph-based SLAM approach leveraging both visual and depth information. You can find more about RTAB-Map at [Introlab's RTAB-Map page](https://introlab.github.io/rtabmap/).
- **Camera Calibration** is performed with the `camera_calibration` package, providing a user-friendly interface and tools for calibrating camera sensors. More information is available on the [camera_calibration wiki](https://wiki.ros.org/camera_calibration).
- The `laser_assembler` package is utilized to combine LaserScan/PointCloud data into a coherent point cloud, suitable for mapping and further processing. Details on this package can be found at the [laser_assembler wiki page](https://wiki.ros.org/laser_assembler).
