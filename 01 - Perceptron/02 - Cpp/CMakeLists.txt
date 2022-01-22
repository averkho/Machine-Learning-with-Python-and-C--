cmake_minimum_required(VERSION 3.5)

### c++11 standards
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(perceptron)

add_library(read_data SHARED 
            apps/read_data.cpp)

add_library(read_data::library ALIAS read_data)

target_include_directories(read_data
    PUBLIC 
        ${PROJECT_SOURCE_DIR}/include
)

add_executable(main
    apps/main.cpp
)

target_link_libraries(main
    PRIVATE 
        read_data::library
)