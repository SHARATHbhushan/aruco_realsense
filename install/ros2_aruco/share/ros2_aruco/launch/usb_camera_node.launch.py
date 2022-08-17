import os

from launch import LaunchDescription
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ns = "/camera"

    params_aruco_node = os.path.join(
        get_package_share_directory('ros2_aruco'),
        'params',
        'aruco_node.yaml'
        )

    params_camera = os.path.join(
        get_package_share_directory('ros2_aruco'),
        'params',
        'camera_params.yaml'
        )

    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            output="screen",
            namespace=ns,
            parameters=[params_camera],
        ),
        Node(
            package='usb_cam',
            executable='show_image.py',
            output="screen",
            namespace=ns,
        ),
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            arguments=["1","0","0","0","0","0","world","default_cam"],
            output="screen"
        ),
        Node(
            package="ros2_aruco",
            executable="aruco_node",
            output="screen",
            parameters = [params_aruco_node],
        ),
    ])
