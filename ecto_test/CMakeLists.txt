cmake_minimum_required(VERSION 2.8.3)
project(ecto_test)

find_package(catkin REQUIRED COMPONENTS
  ecto
)

find_package(ecto REQUIRED)
## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

catkin_python_setup()

catkin_package()

ectomodule(tutorial DESTINATION ${PROJECT_NAME} INSTALL
  src/tutorial.cpp
  src/hello.cpp
  src/add.cpp
  src/increment.cpp
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
