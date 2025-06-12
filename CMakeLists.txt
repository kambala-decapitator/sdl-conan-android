cmake_minimum_required(VERSION 3.21)

project(primitives LANGUAGES C)

find_package(SDL3 REQUIRED)

if(ANDROID)
	add_library(primitives SHARED primitives.c)
else()
	add_executable(primitives primitives.c)
endif()

target_link_libraries(primitives PRIVATE SDL3::SDL3)
