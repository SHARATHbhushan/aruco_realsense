
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    #Included_launch = launch_ros.actions.IncludeLaunchDescription(package='realsense2_camera', launch='rs_launch.py') 
    params_aruco_node = os.path.join(
        get_package_share_directory('ros2_aruco'),
        'params',
        'aruco_node.yaml'
        )

    return LaunchDescription([
        
        Node(
            package="ros2_aruco",
            executable="aruco_node",
            output="screen",
            parameters = [params_aruco_node],
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('realsense2_camera'),
                    'launch',
                    'rs_launch.py'
                ])
            ])),
    ])
