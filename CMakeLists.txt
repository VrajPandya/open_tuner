cmake_minimum_required(VERSION 3.5)
project(open_tuner)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(open_tuner)

set(SOURCE_FILES
    open_tuner/open_tuner.cpp
    open_tuner/open_tuner-gui.cpp
    )

include_directories(include /usr/include/python3.5)

add_executable(open_tuner ${SOURCE_FILES})