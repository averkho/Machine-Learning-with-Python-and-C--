cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

project(mds)

add_library(getData SHARED apps/getData.cpp)
add_library(getData::library ALIAS getData)

add_library(math SHARED apps/math.cpp)
add_library(math::library ALIAS math)

add_library(utils SHARED apps/utils.cpp)
add_library(utils::library ALIAS utils)

target_include_directories(getData PUBLIC ${PROJECT_SOURCE_DIR}/include)
target_include_directories(math PUBLIC ${PROJECT_SOURCE_DIR}/include)
target_include_directories(utils PUBLIC ${PROJECT_SOURCE_DIR}/include)

add_executable(main.exe main.cpp)

target_link_libraries(main.exe 
        PRIVATE 
        getData::library)

target_link_libraries(main.exe 
        PRIVATE 
        math::library)

target_link_libraries(main.exe 
        PRIVATE 
        utils::library)


       