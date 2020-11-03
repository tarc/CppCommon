from conans import CMake, tools
from base.conanfile import CppCommon as CppCommonBase


class CppCommon(CppCommonBase):
    options = {"fPIC": [True, False], "shared": [True, False], "tests": [True, False]}
    default_options = {"fPIC": True, "shared": False, "tests": False}
    exports = ["base/conanfile.py"]

    @property
    def _source_subfolder(self):
        return ".."

    def _configure_cmake(self):
        if not self._cmake:
            self._cmake = CMake(self)
            self._cmake.definitions["CPPCOMMON_MODULE"] = "OFF"
            self._cmake.definitions["CPPCOMMON_TESTS"] = "ON" if self.options.tests else "OFF"
            self._cmake.configure(build_folder=self._build_subfolder)
        return self._cmake

    def source(self):
        pass

    def requirements(self):
        super().requirements()
        if self.options.tests:
           self.requires("catch2/2.13.2")

    def build(self):
        for patch in self.conan_data.get("patches", {}).get(self.version, {}).get("local", []):
            tools.patch(**patch)
        cmake = self._configure_cmake()
        cmake.build()

        if self.options.tests:
            cmake.test(output_on_failure=True)
