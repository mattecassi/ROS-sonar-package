FROM ros:noetic
# use bash
SHELL ["/bin/bash", "-c"]
# Create workspace with catkin
RUN mkdir -p /catkin_ws/src
WORKDIR /catkin_ws/src
RUN source /opt/ros/noetic/setup.bash; catkin_init_workspace
COPY sonar_pkg /catkin_ws/src/sonar_pkg
WORKDIR /catkin_ws
CMD ["/bin/bash"]
