#!/usr/bin/env python  
import rospy
import math
import tf
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('aruco_tf_listener')
    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            t = listener.getLatestCommonTime("marker_frame", "odom", rospy.Duration(4.0))
            listener.waitForTransform("marker_frame", "odom", t, rospy.Duration(4.0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue


    rate.sleep()