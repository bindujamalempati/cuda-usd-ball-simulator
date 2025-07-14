from pxr import Usd, UsdGeom, Gf
import os

# Adjust these paths
input_dir = "/mnt/c/Users/nisse/Downloads/cuda_usd_simulation/output_frames"
output_file = "/mnt/c/Users/nisse/Downloads/cuda_usd_simulation/animated_simulation.usd"

# Create new stage
stage = Usd.Stage.CreateNew(output_file)
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

# We'll track per-sphere prims
spheres = {}

# Loop through frames
for frame in range(50):
    filename = os.path.join(input_dir, f"frame_{frame:04d}.usd")
    frame_stage = Usd.Stage.Open(filename)
    
    for i in range(10):  # assuming 10 spheres
        path = f"/sphere_{i}"
        frame_prim = frame_stage.GetPrimAtPath(path)
        xform = UsdGeom.Xformable(frame_prim)
        translate_ops = xform.GetOrderedXformOps()
        
        if translate_ops:
            pos = translate_ops[0].Get()  # e.g., Gf.Vec3f(x, y, z)
        else:
            continue  # no position

        # Create sphere in output stage if not already done
        if path not in spheres:
            sphere = UsdGeom.Sphere.Define(stage, path)
            translate_op = sphere.AddTranslateOp()
            spheres[path] = translate_op

        # Add time-sampled position
        spheres[path].Set(pos, time=frame)
# Set global time settings
stage.SetStartTimeCode(0)
stage.SetEndTimeCode(49)
stage.SetTimeCodesPerSecond(24)
stage.SetFramesPerSecond(24)

# Save final animated USD
stage.GetRootLayer().Save()
print(f"✅ Animation written to: {output_file}")
