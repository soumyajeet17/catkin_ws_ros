#!/usr/bin/env python2.7
import rospy
# the following line depends upon the
# type of message you are trying to publish
from std_msgs.msg import Int32
nodeName='msgsubscriber'
topicName='info_back'

def callbackFunction(messege):
	print("we received %d"%messege.data)
rospy.init_node(nodeName)
rospy.Subscriber(topicName, Int32, callbackFunction)
rospy.spin()
