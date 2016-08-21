cmake_minimum_required(VERSION 2.8.3)
project(rgbd_pipes)

find_package(catkin REQUIRED COMPONENTS
  ecto
)

find_package(ecto REQUIRED)

catkin_python_setup()
catkin_package(
)
