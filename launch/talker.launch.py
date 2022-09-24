from launch import launch_description
from launch_ros.actions import Node

def generate_launch_description():
    return launchdescription(
        Node(
            package='demo_nodes_cpp',
            executable='talker'

        )
    )
