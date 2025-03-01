#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(data):
	# Log the received message
	rospy.loginfo("I heard: %s", data.data)
def listener():
	# Initialize the subscriber node
	rospy.init_node('listener', anonymous=True)
	# Subscribe to the 'chatter' topic with a String message type
	rospy.Subscriber('chatter', String, callback)
	# Keep the node alive and running
	rospy.spin()
if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
