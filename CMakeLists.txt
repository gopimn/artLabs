cmake_minimum_required(VERSION 2.8)
project( DisplayImage )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( DisplayImage some0003.cpp )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )
