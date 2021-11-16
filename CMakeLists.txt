cmake_minimum_required(VERSION 3.0.2)
project(ros_lab_dino)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   DinoFacts.srv
 )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  LIBRARIES ros_lab_dino
  CATKIN_DEPENDS rospy std_msgs message_runtime
  DEPENDS system_lib
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

