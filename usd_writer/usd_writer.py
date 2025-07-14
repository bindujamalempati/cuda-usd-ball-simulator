from pxr import Usd, UsdGeom, Gf
import os

def write_frame(positions, frame_index):
    stage = Usd.Stage.CreateNew(f"../output_frames/frame_{frame_index:04d}.usd")
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.y)

    for i, pos in enumerate(positions):
        sphere = UsdGeom.Sphere.Define(stage, f"/sphere_{i}")
        sphere.AddTranslateOp().Set(Gf.Vec3f(*pos))
        sphere.GetRadiusAttr().Set(0.5)

    stage.GetRootLayer().Save()
if __name__ == "__main__":
    positions = [(i, 5 + i, 0.0) for i in range(10)]  # initial y-positions
    for frame in range(50):
        # Simulate falling: decrease y by 0.2 per frame
        positions = [(x, y - 0.2, z) for (x, y, z) in positions]
        write_frame(positions, frame)

