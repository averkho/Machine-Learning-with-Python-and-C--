cmake_minimum_required(VERSION 3.5)

### c++11 standards
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(perceptron)

add_library(read_data SHARED 
            apps/read_data.cpp)
add_library(preprocessing SHARED 
            apps/preprocessing.cpp)
add_library(algorithms SHARED
            apps/algorithms.cpp)

add_library(read_data::library ALIAS read_data)
add_library(preprocessing::library ALIAS preprocessing)
add_library(algorithms::library ALIAS preprocessing)

target_include_directories(read_data
    PUBLIC 
        ${PROJECT_SOURCE_DIR}/include
)
target_include_directories(preprocessing
    PUBLIC 
        ${PROJECT_SOURCE_DIR}/include
)

target_include_directories(algorithms
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
target_link_libraries(main
    PRIVATE 
    preprocessing::library
)

target_link_libraries(main
    PRIVATE 
    algorithms::library
)

find_package(Armadillo REQUIRED)
include_directories(${ARMADILLO_INCLUDE_DIRS})
target_link_libraries(algorithms ${ARMADILLO_LIBRARIES})