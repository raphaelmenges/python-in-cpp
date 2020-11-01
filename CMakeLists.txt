cmake_minimum_required(VERSION 3.10)

project(python-in-cpp)

set(PYTHON_EXECUTABLE "${CMAKE_HOME_DIRECTORY}/venv/Scripts/python.exe")
set(ENV{PYTHONPATH} "${CMAKE_HOME_DIRECTORY}/venv/Lib/site-packages")
set(ENV{PATH} "${CMAKE_HOME_DIRECTORY}/venv/Scripts/;${CMAKE_HOME_DIRECTORY}/venv/Lib")

message(STATUS "PYTHON_EXECUTABLE is now: ${PYTHON_EXECUTABLE}")
message(STATUS "ENV{PYTHONPATH} is now: $ENV{PYTHONPATH}")
message(STATUS "PATH is now: $ENV{PATH}")

add_subdirectory(pybind11)

add_executable(app main.cpp)
target_link_libraries(app PRIVATE pybind11::embed)
target_compile_definitions(app PRIVATE -DCUSTOM_SYS_PATH="${CMAKE_HOME_DIRECTORY}/venv/Lib/site-packages")