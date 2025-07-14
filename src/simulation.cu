#include "simulation.cuh"

__global__ void simulate(float3* positions, float3* velocities, int numObjects, float dt) {
    int i = threadIdx.x + blockIdx.x * blockDim.x;
    if (i < numObjects) {
        velocities[i].y -= 9.8f * dt;
        positions[i].x += velocities[i].x * dt;
        positions[i].y += velocities[i].y * dt;
        positions[i].z += velocities[i].z * dt;

        float radius = 0.5f;
        if (positions[i].y < radius) {
            positions[i].y = radius;
            velocities[i].y *= -0.8f;
        }
    }
}