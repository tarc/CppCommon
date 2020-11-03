cmake_minimum_required(VERSION 3.1)
project(benchmarks)

include(conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB BENCHMARK_HEADER_FILES "../performance/*.h")
file(GLOB BENCHMARK_INLINE_FILES "../performance/*.inl")
file(GLOB BENCHMARK_SOURCE_FILES "../performance/*.cpp")

foreach(BENCHMARK_SOURCE_FILE ${BENCHMARK_SOURCE_FILES})
    get_filename_component(BENCHMARK_NAME ${BENCHMARK_SOURCE_FILE} NAME_WE)
    set(BENCHMARK_TARGET "cppcommon-performance-${BENCHMARK_NAME}")
    add_executable(${BENCHMARK_TARGET} ${BENCHMARK_HEADER_FILES} ${BENCHMARK_INLINE_FILES} "${BENCHMARK_SOURCE_FILE}")
    set_target_properties(${BENCHMARK_TARGET} PROPERTIES FOLDER "performance")

    set_target_properties(${BENCHMARK_TARGET} PROPERTIES FOLDER "benchmarks")
    conan_target_link_libraries(${BENCHMARK_TARGET})

    target_compile_features(${BENCHMARK_TARGET} PUBLIC cxx_std_17)
endforeach()
