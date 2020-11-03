from conans import ConanFile, CMake, tools
from glob import glob
import os
import shutil


class CppCommonExamples(ConanFile):
    name = "examples"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    requires = ["cppcommon/cci.20201104"]
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
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
