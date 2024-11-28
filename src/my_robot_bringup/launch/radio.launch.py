from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    robot_names = []
    num_of_robot = 5
    for i in range (1, num_of_robot+1):
        robot = "robot_" + str(i)
        robot_names.append(robot)
    
    robot_news_station_nodes = []

    for robot in robot_names:
        robot_news_station_nodes.append(Node(
            package = "my_py_pkg",
            executable = "robot_news_station",
            name = "robot_news_station" + robot.lower(),
            parameters = [{"Robot_name":robot}]
        ))

    smartphone = Node(
        package = "my_cpp_pkg",
        executable = "smartphone",
        name = "smartphone"
    )

    for node in robot_news_station_nodes:
        ld.add_action(node)
    ld.add_action(smartphone)
    return ld