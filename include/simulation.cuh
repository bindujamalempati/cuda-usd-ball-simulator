#ifndef SIMULATION_CUH
#define SIMULATION_CUH

#include <cuda_runtime.h>

__global__ void simulate(float3* positions, float3* velocities, int numObjects, float dt);

#endif
