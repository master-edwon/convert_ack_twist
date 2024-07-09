import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch.substitutions import FindExecutable


def generate_launch_description():
    package_name = 'convert_ack_twist'

    convert_node = Node(package=package_name,
                            executable='convert_msg',
                            name='convert_msg',
                            output='screen',
                            # arguments=['--ros-args', '--log-level', 'debug']
        )

    ack_pub_node = Node(package=package_name,
                          executable='ack_publisher',
                          name='ackermann_publisher',
                          output='screen',
                          # arguments=['--ros-args', '--log-level', 'debug']
        )
    #ros2 topic pub /ackermann_cmd ackermann_msgs/msg/AckermannDriveStamped "{drive: {speed: 1.0, steering_angle: 0.5}}"
    reference_cmd_exec = ExecuteProcess(
        cmd=[FindExecutable(name='ros2'), 'topic', 'pub', '/ackermann_cmd',
             'ackermann_msgs/msg/AckermannDriveStamped', '{drive: {speed: 1.0, steering_angle: 0.5}}'],
        shell=True
        )


    return LaunchDescription([
        #ack_pub_node,
        reference_cmd_exec,
        convert_node,
    ])