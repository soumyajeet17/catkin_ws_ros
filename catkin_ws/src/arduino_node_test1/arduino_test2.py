#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32

# Global variables to store data from Arduino nodes
data_arduino1 = 1.0
data_arduino2 = 2.0

# Callback for Arduino 1
def callback_arduino1(msg):
    global data_arduino1
    data_arduino1 = msg.data
    rospy.loginfo("Received from Arduino 1: %f", data_arduino1)

# Callback for Arduino 2
def callback_arduino2(msg):
    global data_arduino2
    data_arduino2 = msg.data
    rospy.loginfo("Received from Arduino 2: %f", data_arduino2)

def publisher():
    rospy.init_node('arduino_comm', anonymous=True)

    # Publisher for Arduino 1 and Arduino 2
    pub1 = rospy.Publisher('n1', Float32, queue_size=10)
    pub2 = rospy.Publisher('n2', Float32, queue_size=10)

    # Subscriber for Arduino 1 and Arduino 2
    rospy.Subscriber('n1', Float32, callback_arduino1)
    rospy.Subscriber('n2', Float32, callback_arduino2)

    rate = rospy.Rate(1)  # 1 Hz rate
    while not rospy.is_shutdown():
        # Publish data to both topics
        pub1.publish(data_arduino1)
        pub2.publish(data_arduino2)

        # Sleep to maintain the loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

