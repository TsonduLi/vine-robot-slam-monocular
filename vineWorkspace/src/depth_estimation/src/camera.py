#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CameraInfo

def publish_camera_info():
    rospy.init_node('camera_info_publisher', anonymous=True)
    pub = rospy.Publisher('/camera/camera_info', CameraInfo, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        info_msg = CameraInfo()
        info_msg.header.frame_id = "camera"
        # Set default values
        info_msg.width = 320  # Adjust according to your camera's resolution
        info_msg.height = 240
        # Other fields can remain empty or with default values
        pub.publish(info_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_camera_info()
    except rospy.ROSInterruptException:
        pass

