cmake_minimum_required(VERSION 3.1)
project(examples)

include(conanbuildinfo.cmake)
conan_basic_setup()

if(WIN32 OR MSYS)
    include("../modules/vld.cmake")
endif()

file(GLOB EXAMPLE_HEADER_FILES "../examples/*.h")
file(GLOB EXAMPLE_INLINE_FILES "../examples/*.inl")
file(GLOB EXAMPLE_SOURCE_FILES "../examples/*.cpp")

foreach(EXAMPLE_SOURCE_FILE ${EXAMPLE_SOURCE_FILES})
    get_filename_component(EXAMPLE_NAME ${EXAMPLE_SOURCE_FILE} NAME_WE)
    if (("${EXAMPLE_NAME}" STREQUAL "memory_leaks") AND (WIN32 OR MSYS) AND (NOT LIBVLD_FOUND))
        continue()
    endif()

    set(EXAMPLE_TARGET "cppcommon-example-${EXAMPLE_NAME}")
    add_executable(${EXAMPLE_TARGET} ${EXAMPLE_HEADER_FILES} ${EXAMPLE_INLINE_FILES} "${EXAMPLE_SOURCE_FILE}")
    set_target_properties(${EXAMPLE_TARGET} PROPERTIES FOLDER "examples")
    conan_target_link_libraries(${EXAMPLE_TARGET})

    if ("${EXAMPLE_NAME}" STREQUAL "memory_leaks" AND (WIN32 OR MSYS))
        target_link_libraries(${EXAMPLE_TARGET} ${LIBVLD_LIBRARIES})
        target_include_directories(${EXAMPLE_TARGET} PRIVATE ${LIBVLD_INCLUDE_DIR})
    endif()

    install(TARGETS ${EXAMPLE_TARGET}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

    target_compile_features(${EXAMPLE_TARGET} PUBLIC cxx_std_17)
endforeach()
