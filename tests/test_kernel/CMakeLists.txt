cmake_minimum_required(VERSION 3.4)
project(test_kernel)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(test_kernel)

set (TEST_KERNEL_ROOT ${PROJECT_SOURCE_DIR})

set(MAP_SOURCE_FILES
        data_gen.c
        map.c
        )

set (open_tuner_INCLUDE_DIR
        "${PROJECT_SOURCE_DIR}"
        )

set(REDUCE_SOURCE_FILES
        data_gen.c
        reduce.c
        )

include_directories(${open_tuner_INCLUDE_DIR})

add_executable(map ${MAP_SOURCE_FILES})

add_executable(reduce ${REDUCE_SOURCE_FILES})