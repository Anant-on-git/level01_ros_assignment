#!/usr/bin/env python3
"""Bring up the testbed simulation, map server, and AMCL localization."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    """Launch all components needed to localize the testbed robot."""
    bringup_share = get_package_share_directory('testbed_bringup')
    navigation_share = get_package_share_directory('testbed_navigation')

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                bringup_share,
                'launch',
                'testbed_full_bringup.launch.py',
            )
        )
    )

    map_loader = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                navigation_share,
                'launch',
                'map_loader.launch.py',
            )
        )
    )

    amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        name='amcl',
        output='screen',
        parameters=[os.path.join(
            navigation_share,
            'config',
            'amcl_params.yaml',
        )],
    )

    # Wait for the map loader to configure and activate map_server first.
    configure_amcl = TimerAction(
        period=6.0,
        actions=[ExecuteProcess(
            cmd=['ros2', 'lifecycle', 'set', '/amcl', 'configure'],
            output='screen',
        )],
    )

    activate_amcl = TimerAction(
        period=8.0,
        actions=[ExecuteProcess(
            cmd=['ros2', 'lifecycle', 'set', '/amcl', 'activate'],
            output='screen',
        )],
    )

    return LaunchDescription([
        simulation,
        map_loader,
        amcl,
        configure_amcl,
        activate_amcl,
    ])
