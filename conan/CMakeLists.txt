cmake_minimum_required(VERSION 3.4)
project(cmake_wrapper)

include(${CMAKE_CURRENT_BINARY_DIR}/../conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

if(WIN32 AND BUILD_SHARED_LIBS)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()

iF(CPPCOMMON_TESTS)
    enable_testing()
endif()

add_subdirectory(.. cppcommon)
