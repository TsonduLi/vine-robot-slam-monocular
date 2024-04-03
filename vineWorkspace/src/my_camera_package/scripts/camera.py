#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CameraInfo
from camera_info_manager import CameraInfoManager

def camera_info_publisher():
    rospy.init_node('camera_info_publisher')
    
    # Initialize camera_info_manager with the camera name and calibration URL
    camera_info_url = 'file:///home/yimeng/vineWorkspace/src/depthimage_to_laserscan/config/ost.yaml'
    camera_name = 'my_camera'
    cim = CameraInfoManager(cname=camera_name, url=camera_info_url)
    cim.loadCameraInfo()  # Load the calibration data
    
    # Start the camera_info_manager
    if not cim.isCalibrated():
        rospy.logwarn("Camera is not calibrated")
    cim.setCameraName(camera_name)
    info_pub = rospy.Publisher('/camera/camera_info', CameraInfo, queue_size=10)
    
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        # Get the CameraInfo from camera_info_manager
        camera_info_msg = cim.getCameraInfo()
        info_pub.publish(camera_info_msg)
        rate.sleep()

if __name__ == '__main__':
    camera_info_publisher()


