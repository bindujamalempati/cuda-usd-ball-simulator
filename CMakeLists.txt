cmake_minimum_required(VERSION 3.10)
project(CUDA_USD_SIM)

find_package(CUDA REQUIRED)
set(CMAKE_CXX_STANDARD 14)
include_directories(include)

cuda_add_executable(simulator
    src/main.cu
    src/simulation.cu
    src/usd_loader.cpp
)

# No need for set_target_properties for CUDA_ARCHITECTURES here.
