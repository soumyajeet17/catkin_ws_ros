#include <ros.h>
#include <std_msgs/Float32.h>
// ROS Node Handle
ros::NodeHandle nh;
// Data variables
float my_data = 1.0; // Arduino 1's own data
float received_data = 0.0; // Data from Arduino 2

// Callback function for the subscriber
void dataCallback(const std_msgs::Float32 &msg)
{
  received_data = msg.data; // Update received data
  my_data = my_data + 0.1*(msg.data-my_data);
}

// Publisher and Subscriber
std_msgs::Float32 msg;
ros::Publisher pub("n1", &msg);
ros::Subscriber<std_msgs::Float32> sub("n2", &dataCallback);
void setup() {
nh.initNode();
nh.advertise(pub); // Advertise the publisher
nh.subscribe(sub); // Subscribe to the topic
}
void loop() {
msg.data = my_data; // Update message with local data
pub.publish(&msg);
nh.spinOnce();
delay(1000);
}
