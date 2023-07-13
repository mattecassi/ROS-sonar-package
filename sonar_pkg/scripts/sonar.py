import numpy as np
import cv2
import time
import rospy
from sonar_pkg.msg import object_pose

class ContinuousScatterPlot:
    def __init__(self, limits=(5, 5)):
        self.limits = limits
        self.window_size = (100, 100)  # Set the size of the plot window
        self.canvas = np.ones((self.window_size[0], self.window_size[1], 3), dtype=np.uint8) * 255
        self.multi = self.window_size[0] / limits[0] 
    def update_plot(self, new_x, new_y):
        # Scale the new data to fit within the plot window
        scaled_x =  int(self.window_size[0]/2 + self.multi *new_x) # ((new_x / self.limits[0]) + 0.5) * (self.window_size[0] - 1)
        scaled_y =  int(self.window_size[1]/2 + self.multi *new_y) # new_y# ((new_y / self.limits[1]) + 0.5) * (self.window_size[1] - 1)y
        # Clear the canvas
        self.canvas.fill(255)
        print(scaled_x, scaled_y)
        # Draw the scatter plot
        #for x, y in zip(scaled_x, scaled_y):
        cv2.circle(self.canvas, (int(scaled_x), int(scaled_y)), 2, (0, 0, 0), -1)

        # Show the plot
        cv2.imshow("Continuous Scatter Plot", self.canvas)
        cv2.waitKey(1)  # Wait for a short time before updating the plot


def callback(object_pose):
    rospy.loginfo(f"new data: {object_pose}")
    scatter_plot.update_plot(object_pose.x, object_pose.z)


if __name__ == "__main__":
    print("RUNNING SONAR")
    topic_name = "sonar_poses"
    rospy.init_node('sonar_node')
    print(rospy.get_param_names())
    topic_name = topic_name if "/sonar_node/topic_name" not in rospy.get_param_names() \
        else rospy.get_param("/sonar_node/topic_name")
    print(topic_name)
    sub = rospy.Subscriber(topic_name, object_pose, callback)

    # Create an instance of ContinuousScatterPlot and run it
    scatter_plot = ContinuousScatterPlot()
    rospy.spin()
