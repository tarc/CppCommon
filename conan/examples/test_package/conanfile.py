from conans import ConanFile, CMake, tools
import os

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def test(self):
        self.run("cppcommon-example-system_dll", run_environment=True)
        self.run("cppcommon-example-system_uuid", run_environment=True)
