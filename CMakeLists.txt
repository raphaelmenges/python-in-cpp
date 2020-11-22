cmake_minimum_required(VERSION 3.10)

project(python-in-cpp)

if (WIN32) # Windows
	set(PYTHON_SIDE_PACKAGES "${CMAKE_HOME_DIRECTORY}/venv/Lib/site-packages")
	set(PYTHON_EXECUTABLE "${CMAKE_HOME_DIRECTORY}/venv/Scripts/python.exe")
	set(ENV{PYTHONPATH} "${PYTHON_SIDE_PACKAGES}")
	set(ENV{PATH} "${CMAKE_HOME_DIRECTORY}/venv/Scripts/;${CMAKE_HOME_DIRECTORY}/venv/Lib")
else() # macOS
	set(PYTHON_SIDE_PACKAGES "${CMAKE_HOME_DIRECTORY}/venv/lib/python3.8/site-packages")
	set(PYTHON_EXECUTABLE "${CMAKE_HOME_DIRECTORY}/venv/bin/python3")
	set(ENV{PYTHONPATH} "${PYTHON_SIDE_PACKAGES}")
	set(ENV{PATH} "${CMAKE_HOME_DIRECTORY}/venv/bin/;${CMAKE_HOME_DIRECTORY}/venv/lib") # not sure whether required for macOS
endif()

message(STATUS "PYTHON_EXECUTABLE is now: ${PYTHON_EXECUTABLE}")
message(STATUS "ENV{PYTHONPATH} is now: $ENV{PYTHONPATH}")
message(STATUS "PATH is now: $ENV{PATH}")

add_subdirectory(pybind11)

add_executable(app main.cpp)
target_link_libraries(app PRIVATE pybind11::embed)
target_compile_definitions(app PRIVATE -DCUSTOM_SYS_PATH="${PYTHON_SIDE_PACKAGES}")

if (WIN32) # Windows
	add_custom_command(TARGET app PRE_BUILD
	COMMAND ${CMAKE_COMMAND} -E copy_if_different
		"C:/Program Files/Python38/python38.dll"
		$<TARGET_FILE_DIR:app>)
endif()