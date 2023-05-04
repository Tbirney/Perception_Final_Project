#!/bin/bash

ws_dir="$(pwd)/catkin_ws"
cd $ws_dir
catkin_make
echo "source $ws_dir/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
