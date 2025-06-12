cmake_minimum_required(VERSION 3.21)

project(primitives LANGUAGES C)

find_package(SDL3 REQUIRED)

if(ANDROID)
	add_library(primitives SHARED primitives.c)
	set_target_properties(primitives PROPERTIES OUTPUT_NAME main) # SDL requirement by default

	include(GNUInstallDirs)
	set(CMAKE_INSTALL_LIBDIR ${ANDROID_ABI})
	install(TARGETS primitives)
	if(ANDROID_STL MATCHES "_shared$")
		file(READ "${CMAKE_ANDROID_NDK}/meta/abis.json" ndkAbiInfo)
		string(JSON ANDROID_SYSROOT_LIB_SUBDIR GET "${ndkAbiInfo}" "${ANDROID_ABI}" "triple")

		set(stlLibName "${CMAKE_SHARED_LIBRARY_PREFIX}${ANDROID_STL}${CMAKE_SHARED_LIBRARY_SUFFIX}")
		install(FILES "${CMAKE_SYSROOT}/usr/lib/${ANDROID_SYSROOT_LIB_SUBDIR}/${stlLibName}"
			TYPE LIB
		)
	endif()
else()
	add_executable(primitives primitives.c)
endif()

target_link_libraries(primitives PRIVATE SDL3::SDL3)
