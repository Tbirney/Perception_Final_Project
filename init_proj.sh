#!/bin/bash

ws_dir="$(pwd)/catkin_ws"
cd $ws_dir
catkin_make
grep -qxF "source $ws_dir/devel/setup.bash" ~/.bashrc || echo "source $ws_dir/devel/setup.bash" >> ~/.bashrc
grep -qxF "export TURTLEBOT3_MODEL=burger" ~/.bashrc || echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
source ~/.bashrc
