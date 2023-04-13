
cmake_minimum_required(VERSION 3.12)

# Pull in PICO SDK (must be before project)
include(pico_sdk_import.cmake)

project(pico-tflmicro C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 11)

pico_sdk_init()

add_library(pico-tflmicro "")

#This directory should contain "tensorflow" and "third_party" directories from tflite-micro
set(LIB_DIR /pico-sdk/tflite-micro/src)

target_include_directories(pico-tflmicro
  PUBLIC
  ${CMAKE_CURRENT_LIST_DIR}

  ${LIB_DIR}/
  ${LIB_DIR}/third_party/cmsis/CMSIS/DSP/Include
  ${LIB_DIR}/third_party/ruy
  ${LIB_DIR}/third_party/gemmlowp
  ${LIB_DIR}/third_party/kissfft
  ${LIB_DIR}/third_party/flatbuffers
  ${LIB_DIR}/third_party/cmsis/CMSIS/Core/Include
  ${LIB_DIR}/third_party/cmsis
  ${LIB_DIR}/third_party/flatbuffers/include
  ${LIB_DIR}/third_party/cmsis/CMSIS/NN/Include
)

target_compile_definitions(
  pico-tflmicro
  PUBLIC
  COMPILE_DEFINITIONS TF_LITE_DISABLE_X86_NEON=1
  COMPILE_DEFINITIONS TF_LITE_STATIC_MEMORY=1
  COMPILE_DEFINITIONS CMSIS_NN=1
)

set_target_properties(
  pico-tflmicro
  PROPERTIES
  COMPILE_FLAGS -fno-rtti
  COMPILE_FLAGS -fno-exceptions
  COMPILE_FLAGS -fno-threadsafe-statics
  COMPILE_FLAGS -nostdlib
)

target_link_libraries(
  pico-tflmicro
  pico_stdlib
)


file(GLOB_RECURSE SRC ${LIB_DIR}/*.c ${LIB_DIR}/*.cpp ${LIB_DIR}/*.cc ${LIB_DIR}/*.cxx ${LIB_DIR}/*.h ${LIB_DIR}/*.hpp)
target_sources(pico-tflmicro
	PRIVATE	
  ${SRC}
)



#add_subdirectory("Arducam/src")
add_subdirectory("person_detection_screen")

