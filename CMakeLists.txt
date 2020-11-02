cmake_minimum_required(VERSION 3.10)

project(python-in-cpp)

if (WIN32)
	set(PYTHON_SIDE_PACKAGES "${CMAKE_HOME_DIRECTORY}/venv/Lib/site-packages")
	set(PYTHON_EXECUTABLE "${CMAKE_HOME_DIRECTORY}/venv/Scripts/python.exe")
	set(ENV{PYTHONPATH} "${PYTHON_SIDE_PACKAGES}")
	set(ENV{PATH} "${CMAKE_HOME_DIRECTORY}/venv/Scripts/;${CMAKE_HOME_DIRECTORY}/venv/Lib")
else()
	set(PYTHON_SIDE_PACKAGES "${CMAKE_HOME_DIRECTORY}/venv/lib/python3.8/site-packages")
	set(PYTHON_EXECUTABLE "${CMAKE_HOME_DIRECTORY}/venv/bin/python3")
	set(ENV{PYTHONPATH} "${PYTHON_SIDE_PACKAGES}")
	set(ENV{PATH} "${CMAKE_HOME_DIRECTORY}/venv/bin/;${CMAKE_HOME_DIRECTORY}/venv/lib")
endif()

message(STATUS "PYTHON_EXECUTABLE is now: ${PYTHON_EXECUTABLE}")
message(STATUS "ENV{PYTHONPATH} is now: $ENV{PYTHONPATH}")
message(STATUS "PATH is now: $ENV{PATH}")

add_subdirectory(pybind11)

add_executable(app main.cpp)
target_link_libraries(app PRIVATE pybind11::embed)
target_compile_definitions(app PRIVATE -DCUSTOM_SYS_PATH="${PYTHON_SIDE_PACKAGES}")