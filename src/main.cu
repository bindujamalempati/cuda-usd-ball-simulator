#include "simulation.cuh"
#include "usd_loader.hpp"
#include <vector>
#include <iostream>

int main() {
    std::vector<float3> positions, velocities;
    loadUSD("assets/scene.usd", positions, velocities);

    int N = positions.size();
    float3 *d_pos, *d_vel;
    cudaMalloc(&d_pos, N * sizeof(float3));
    cudaMalloc(&d_vel, N * sizeof(float3));
    cudaMemcpy(d_pos, positions.data(), N * sizeof(float3), cudaMemcpyHostToDevice);
    cudaMemcpy(d_vel, velocities.data(), N * sizeof(float3), cudaMemcpyHostToDevice);

    float dt = 0.016f;
    for (int frame = 0; frame < 50; ++frame) {
        simulate<<<(N+255)/256, 256>>>(d_pos, d_vel, N, dt);
        cudaDeviceSynchronize();
    }

    cudaMemcpy(positions.data(), d_pos, N * sizeof(float3), cudaMemcpyDeviceToHost);
    cudaFree(d_pos); cudaFree(d_vel);
    std::cout << "Simulation done. Write frames using Python usd_writer.py\n";
    return 0;
}