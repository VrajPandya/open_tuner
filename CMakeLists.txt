cmake_minimum_required(VERSION 3.5)
project(open_tuner)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(open_tuner)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ..)

set(SOURCE_FILES
    open_tuner/open_tuner.cpp
    open_tuner/open_tuner_gui.cpp
    )

set (open_tuner_INCLUDE_DIR
    "/usr/include/python3.5/"
    "open_tuner"
    )

include_directories(${open_tuner_INCLUDE_DIR})

add_executable(open_tuner ${SOURCE_FILES})