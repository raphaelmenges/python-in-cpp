#include <iostream>
#include <string>
#include <pybind11/embed.h>
#include <pybind11/numpy.h>
namespace py = pybind11;
using namespace pybind11::literals;

int main()
{
	std::cout << "Hello Python. Here is C++." << std::endl;

	py::scoped_interpreter guard{};

	py::module sys = py::module::import("sys");
	sys.attr("path").attr("insert")(0, CUSTOM_SYS_PATH);

	py::print("Hello, World from Python!");
	py::print(sys.attr("executable"));
	py::print(sys.attr("version"));
	py::print(sys.attr("path"));

	// Try for numpy
	auto np = py::module::import("numpy");
	py::print(np.attr("version"));
	py::array_t<float> arr = np.attr("ones")(3, "dtype"_a = "float32");
	py::print(py::repr(arr + py::int_(2)));

	// Try for nasty
	auto nasty = py::module::import("nasty");
	py::print(nasty.attr("__version__"));

	return 0;
}