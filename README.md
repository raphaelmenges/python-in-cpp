Project to test calls from C++ to Python.

Inspired by: <https://stackoverflow.com/questions/56904149/embedding-python-with-pybind11-virtual-environment-doesnt-work>

Comments: Creation of the virtual environment through CMake is difficult, because pybind11 likes to find Python itself. If one looks for Python before to create the virtual environment, pybind11 is likely to fail in strange ways. Idea: Create virtual environment in a wrapping Python script.

TODO: Describe how to create virtual environment