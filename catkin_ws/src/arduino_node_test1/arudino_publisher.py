#!/usr/bin/env python2.7
import rospy
# the following line depends upon the
# type of message you are trying to publish
from std_msgs.msg import Int32

nodeName='msgpublisher'
topicName='information'

rospy.init_node(nodeName, anonymous=True)
publisher1=rospy.Publisher(topicName, Int32, queue_size=5)
ratePublisher=rospy.Rate(1)
intMessage=1

while not rospy.is_shutdown():
	rospy.loginfo(intMessage)
	publisher1.publish(intMessage)
	intMessage=intMessage+1
	ratePublisher.sleep()
