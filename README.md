Project to test calls from C++ to Python. Tested on Windows and macOS.

Inspired by: <https://stackoverflow.com/questions/56904149/embedding-python-with-pybind11-virtual-environment-doesnt-work>

Requires:
- Python 3.8 with Pip and virtualenv
- CMake >= 3.10
- Visual Studio 2015 or higher on Windows / CLang compiler on macOS

Generation:
- `python generate.py` to generate virtual environment
- Execute CMake to generate C++ solution