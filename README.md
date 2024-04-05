# Enabling 3D Mapping and Localization for Multi-segment "Vine" Robot

## Overview
This project is dedicated to developing 3D mapping and localization capabilities for a multi-segment "Vine" robot. By integrating a combination of 6-axis IMU, RGB and Depth images, Time of Flight Laser Point, and real-time processing techniques, we enhance the robot's environmental understanding to facilitate improved navigation and autonomy.

## Features
- **Depth Estimation**: Implemented using Deep Learning-based semantic segmentation ([DINOv2](https://github.com/isl-org/ZoeDepth)) and depth estimation models ([MiDas](https://github.com/isl-org/MiDaS)).
- **Data Collection and Transmission**: Utilizes MicroPython APIs on the [OpenMV](https://openmv.io/) platform for concurrent transmission of IMU, sensor images, and laser data via MQTT, ensuring data synchronization with multithreading techniques.
- **3D Mapping**: Utilizes RGB and Depth data to generate three-dimensional maps of the robot's surroundings.
- **Robot Localization**: Combines sensor data for accurate positioning and movement within the map, enhanced by Deep Learning-based semantic segmentation and depth estimation models, achieving a localization error below 10% without Lidar.
- **PointCloud Assembly**: Converts sensor data into a PointCloud2 format for easy visualization and manipulation.


## Control Strategy
The project employs an Arduino Nicla Vision for its control strategy, which includes:
- 6-axis IMU
- RGB Image capture
- On-board WiFi and Bluetooth
- Real-time streaming protocol (RTSP) streaming of QVGA video at 10fps

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
- The `laser_assembler` package is utilized to combine laser scan data into a coherent point cloud, suitable for mapping and further processing. Details on this package can be found at the [laser_assembler wiki page](https://wiki.ros.org/laser_assembler).
