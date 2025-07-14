#include "usd_loader.hpp"
#include <iostream>

bool loadUSD(const std::string& filename, std::vector<float3>& positions, std::vector<float3>& velocities) {
    for (int i = 0; i < 10; ++i) {
        positions.push_back({(float)i, 5.0f + i, 0.0f});
        velocities.push_back({0.0f, 0.0f, 0.0f});
    }
    std::cout << "Loaded 10 test spheres from " << filename << " (mocked)\n";
    return true;
}