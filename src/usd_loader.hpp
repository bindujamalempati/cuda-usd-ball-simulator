#ifndef USD_LOADER_HPP
#define USD_LOADER_HPP

#include <string>          // For std::string
#include <vector>          // For std::vector
#include <cuda_runtime.h>  // For float3

// Function to load positions and velocities from a USD file (mocked or real)
bool loadUSD(const std::string& filename, std::vector<float3>& positions, std::vector<float3>& velocities);

#endif
