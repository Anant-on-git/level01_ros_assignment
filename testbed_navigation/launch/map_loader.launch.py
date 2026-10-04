#!/usr/bin/env python3
"""Load and publish the testbed occupancy-grid map."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import LifecycleNode, Node


def generate_launch_description():
    """Start the map server and automatically move it to the active state."""
    package_share = get_package_share_directory('testbed_bringup')
    map_yaml = os.path.join(package_share, 'maps', 'testbed_world.yaml')

    map_server = LifecycleNode(
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{
            'yaml_filename': map_yaml,
            'use_sim_time': True,
        }],
    )

    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='map_server_lifecycle_manager',
        output='screen',
        parameters=[{
            'autostart': True,
            'node_names': ['map_server'],
            'use_sim_time': True,
        }],
    )

    return LaunchDescription([map_server, lifecycle_manager])
