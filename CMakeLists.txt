cmake_minimum_required(VERSION 3.5)
project(open_tuner)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(open_tuner)

set (OPEN_TUNER_ROOT ${PROJECT_SOURCE_DIR})

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/open_tuner/open_tuner.h.in"
  "${PROJECT_BINARY_DIR}/include/open_tuner.h"
  )

configure_file (
  "${PROJECT_SOURCE_DIR}/open_tuner/open_tuner_gui.h.in"
  "${PROJECT_BINARY_DIR}/include/open_tuner_gui.h"
  )

#set(OUTPUT_NAME "ot")

#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ..)

#set(EXECUTABLE_OUTPUT_PATH "${PROJECT_SOURCE_DIR}")

set(SOURCE_FILES
    open_tuner/open_tuner.cpp
    open_tuner/open_tuner_gui.cpp
    )

set (open_tuner_INCLUDE_DIR
    "/usr/include/python3.5/" #set to standard python Include dir which can work accross the systems
    "${PROJECT_BINARY_DIR}/include"
    )

include_directories(${open_tuner_INCLUDE_DIR})

add_executable(open_tuner ${SOURCE_FILES})