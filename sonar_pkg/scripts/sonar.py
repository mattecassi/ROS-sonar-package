import numpy as np
import matplotlib.pyplot as plt
import time
import rospy
from sonar_real.msg import object_pose

class ContinuousScatterPlot:
    def __init__(self, limits=(5, 5)):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-limits[0], limits[0])  # Set X-axis limits
        self.ax.set_ylim(-limits[1], limits[1])  # Set Y-axis limits 
        self.scatter = self.ax.scatter([], [])
        plt.ion()  # Turn on interactive mode
        self._data = [] # to add in the future

        
    def update_plot(self, new_x, new_y):
        self.scatter.set_offsets(np.column_stack((new_x, new_y)))
        self.fig.canvas.draw()  # Redraw the plot
    
    def run(self):
        while True:
            # Generate new data
            new_x = np.random.randn(10)   # Generate new X-axis values
            new_y = np.random.randn(10)  # Generate new Y-axis values
            
            # Update the plot
            self.update_plot(new_x, new_y)
            
            plt.pause(0.1)  # Pause for a short time (in seconds) before updating the plot

def callback(object_pose):
    rospy.loginfo(f"new data: {object_pose}")
    scatter_plot.update_plot(object_pose.x,object_pose.z)

if __name__ == "__main__":
    print("RUNNING SONAR")
    topic_name = "sonar_poses"
    rospy.init_node('sonar_node')

    sub = rospy.Subscriber(topic_name, object_pose,callback)
    # Create an instance of ContinuousScatterPlot and run it
    scatter_plot = ContinuousScatterPlot()
    #scatter_plot.run()
    rospy.spin()
