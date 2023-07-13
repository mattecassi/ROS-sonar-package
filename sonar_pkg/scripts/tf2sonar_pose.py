#!/usr/bin/python3
import rospy
from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage
from sonar_pkg.msg import object_pose
"""
This script has been created for a demo. 
You can easily forget about its existance.
"""
def tf2pose(msg):
    data = msg.transforms[0]
    if data.child_frame_id == "tag1":
        pose = object_pose()
        pose.x = data.transform.translation.x
        pose.y = data.transform.translation.y
        pose.z = data.transform.translation.z
        
        pose.oid = 0
        pub.publish(pose)

if __name__ == "__main__":
    rospy.init_node("converter_node")
    print(rospy.get_param_names())
    topic_name = "sonar_poses"
    topic_name = topic_name if "/tf2pose/topic_name" \
        not in rospy.get_param_names() \
        else rospy.get_param("/tf2pose/topic_name") 
    print(topic_name)
    
    pub = rospy.Publisher(topic_name, object_pose, queue_size=1)
    sub = rospy.Subscriber("/tf", TFMessage, callback=tf2pose)
    rospy.spin()
