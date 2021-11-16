# ROS-FirstLab-DinoRandomaizer 
***

Install
=====================
1. cd <your_ros_workspace>/src
2. git clone https://github.com/LordCabbage/ROS-FirstLab-DinoRandomaizer

"/usr/bin/env: python: No such file or directory" problem solution 
=====================
run this commands:
1. whereis python3
2. sudo ln -s /usr/bin/python3 /usr/bin/python

Build
=====================
1. cd <your_ros_workspace>
2. catkin_make

Run
=====================
0. roscore
1. Open other terminal
2. cd <your_ros_workspace>
3. source devel/setup.bash
4. rosrun ros_lab_dino DinoSubscriber.py
5. Open other terminal
6. cd <your_ros_workspace>
7. source devel/setup.bash
8. rosrun ros_lab_dino DinoPublisher.py + 'any word'

Rosservice
=====================
0. roscore
1. Open other terminal
2. cd <your_ros_workspace>
3. source devel/setup.bash
4. rosrun ros_lab_dino DinoSubscriber.py
5. Open other terminal
6. cd <your_ros_workspace>
7. source devel/setup.bash
8. rosservice call /dino_facts "a: 'any word'" 

Examples Using rosrun
=====================
1. Initial subscriber with server
   1. cd <your_ros_workspace>
   2. source devel/setup.bash
2. rosrun ros_lab_dino DinoSubscriber.py
   1. output from subscriber console = "Ready to give you true facts"
3. Initial publisher with client
   1. cd <your_ros_workspace>
   2. source devel/setup.bash
4. rosrun ros_lab_dino DinoPublisher.py ros
   1. output from subscriber console = "Returning real name of ros"
   2. output from publisher console = "Requesting facts about Rosrex"
   3. output from publisher console = "Fact about Rosrex is ready"
   4. output from subscriber console = "Rosrex belonged to the  Theropoda family and lived in the Cretaceous" 

Examples Using rosservice
=====================
1. Initial
   1. cd <your_ros_workspace>
   2. source devel/setup.bash
2. rosrun ros_lab_dino DinoSubscriber.py
   1. output from subscriber console = "Ready to give you true facts"
3. Initial service
   1. cd <your_ros_workspace>
   2. source devel/setup.bash
4. rosservice call /dino_facts "a: 'ros'" 
   1. output from subscriber console = "Returning real name of ros"
   2. output from service console = "b: "Rosdraco"
