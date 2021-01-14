cmake_minimum_required (VERSION 3.0)

project (Lagrangian_Relax)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --std=c++11 -g -O0 -m64 -O -fPIC -fno-strict-aliasing -fexceptions -DNDEBUG -DIL_STD")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")

find_package(OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif()

#include paths
include_directories("xxx/boost_1_67_0/Build/include")
include_directories("xxx/LAPSO_Req")
include_directories("xxx/cplex/include")
include_directories("xxx/concert/include")

link_directories("xxx/cplex/lib/x86-64_linux/static_pic")
link_directories("xxx/concert/lib/x86-64_linux/static_pic")
link_directories("xxx/boost_1_67_0/Build/lib")

add_executable(OUTPUT_TARGET src/main.cpp src/ED.cpp src/LaPSO.cpp src/CpuTimer.cpp src/ArgParser.cpp src/anyoption.cpp src/VolVolume.cpp src/prep_mip.cpp src/djikstra.cpp)

target_link_libraries(OUTPUT_TARGET concert ilocplex cplex m pthread dl)
