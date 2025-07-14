# CUDA-Accelerated USD Physics Simulation

This project simulates rigid body motion (e.g., falling and bouncing spheres) using CUDA for computation and USD (Universal Scene Description) for 3D input/output.

## Steps
1. Load scene (or mock data).
2. Run physics simulation with CUDA.
3. Export each frame's result to `.usd` file.
4. Visualize using usdview or Omniverse.

## Requirements
- CUDA Toolkit
- USD SDK + Python pxr module

Run simulation:
```bash
./simulator
python3 usd_writer/usd_writer.py  # Write output frames if scripted
usdview output_frames/frame_0001.usd
```