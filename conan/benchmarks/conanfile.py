from conans import ConanFile, CMake, tools
from glob import glob
import os
import shutil


class CppCommonBenchmarks(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = ["cppcommon/1.0.0.0"]
    exports_sources = ["CMakeLists.txt"]
    _cmake = None

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def _configure_cmake(self):
        if not self._cmake:
            self._cmake = CMake(self)
            self._cmake.configure(build_folder=self._build_subfolder)
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join("bin", "test_package")
            self.run(bin_path, run_environment=True)
