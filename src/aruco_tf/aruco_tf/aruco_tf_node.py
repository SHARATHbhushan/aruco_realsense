#! /usr/bin/env python3

import rclpy
import sys

from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from scipy.spatial.transform import Rotation as R
from tf2_ros.transform_broadcaster import TransformBroadcaster
from geometry_msgs.msg import PoseArray, Pose

class DynamicBroadcaster(Node):

    def __init__(self):
        super().__init__('dynamic_broadcaster')
        self.name_ = "aruco_poses"
        self.get_logger().info("Broadcasting pose of : {}".format(self.name_))
        self.tfb_ = TransformBroadcaster(self)
        self.sub_pose = self.create_subscription(PoseArray, "/aruco_poses", self.handle_pose, 10)

    def handle_pose(self, msg):
        tfs = TransformStamped()
        tfs.header.stamp = self.get_clock().now().to_msg()
        tfs.header.frame_id="camera_link"
        tfs._child_frame_id = self.name_
        tfs.transform.translation.x = msg.poses.x
        tfs.transform.translation.y = msg.pose_array.poses.pose.position.y
        tfs.transform.translation.z = msg.pose_array.poses.pose.position.z  

        #r = R.from_euler('xyz',[0,0,msg.theta])

        tfs.transform.rotation.x = msg.pose.orientation.x
        tfs.transform.rotation.y = msg.pose.orientation.x
        tfs.transform.rotation.z = msg.pose.orientation.x
        tfs.transform.rotation.w = msg.pose.orientation.w

        self.tfb_.sendTransform(tfs)    

def main():
    rclpy.init()
    node = DynamicBroadcaster()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()