## ROS2 Aruco package with intel realsense camera
This package integrates realsense camera with aruco packages to work with UR5 robot and also includes ur5 cell bringup package, the camera must be calibrated before use to calibrate perform following steps: https://dev.intelrealsense.com/docs/intel-realsensetm-d400-series-calibration-tools-user-guide

- clone the repo : `git clone https://github.com/SHARATHbhushan/aruco_realsense.git`

## Additional Repositories

# ros2_aruco 
- `git clone https://github.com/ipa-kut/ros2_aruco.git`

- change the params of aruco.yaml in ros2_aruco/params
```
/aruco_node:
  ros__parameters:
    aruco_dictionary_id: DICT_5X5_250
    camera_frame: camera_link
    camera_info_topic: /camera/color/camera_info
    image_topic: /camera/color/image_raw
    marker_size: 0.047
    use_sim_time: false
```

# Realsense ROS

- `git clone -b ros2 https://github.com/IntelRealSense/realsense-ros.git`

- Remove realsense2_description package

# Universal Robotics ROS2 Description

- `git clone -b ros2 https://github.com/UniversalRobots/Universal_Robots_ROS2_Description.git`

# ur5e workcell package

- `git clone https://github.com/ipa-rar/ur5e_workcell_bringup.git`

- remove install directory "world" in in Workcell_description/CMakeLists.txt

# Quick launch 

- build repository `colcon build`

- with realsense device connected launch `ros2 launch aruco_rs2 rs_aruco.launch.py`

- To visualize in rviz in another terminal launch `ros2 launch workcell_description workcell_bringup.launch.py`

- Add posearray by topic to visualize the aruco marker position
