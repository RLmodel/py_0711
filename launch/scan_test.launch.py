import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription


def generate_launch_description():
    
    
    turtlesim_node = Node(              
        package='turtlesim',
        executable='turtlesim_node',
        output='log',
    )
    
    rplidar_ros2_pkg = get_package_share_directory('rplidar_ros')
    rplidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(rplidar_ros2_pkg, 'launch', "rplidar_a2m8_launch.py"))
    )
    
    scan_node = Node(
        package='py_0711',
        executable='emergency',
        name='serial',
        output='log',
        emulate_tty=True
    )
    
    return LaunchDescription([
        turtlesim_node,
        rplidar_launch,
        scan_node,
        
    ])