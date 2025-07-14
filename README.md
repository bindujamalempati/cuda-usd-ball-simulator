Here’s a clean, human-friendly `README.md` for your **CUDA + USD Ball Simulation** project:

---

### ✅ `README.md`

```markdown
# 🎯 CUDA + USD Ball Simulation

This project simulates 10 balls falling under gravity using **CUDA** for high-performance parallel processing and exports the animation using **Pixar's USD (Universal Scene Description)** format. It produces animated 3D scenes that can be viewed in `usdview`.

---

## 📌 What This Project Does

- Simulates falling balls using physics (gravity, velocity, bounce)
- Uses CUDA to accelerate the simulation on GPU
- Writes 3D animated frames in USD format using Python
- Visualizes results with the interactive `usdview` viewer

---

## 🧰 Technologies Used

| Component | Purpose |
|----------|---------|
| **CUDA (C++)** | To simulate real-time motion of balls on GPU |
| **Pixar USD** | To represent 3D scenes and animations |
| **Python** | To write frame-by-frame animation data |
| **usdview** | To view and interact with the animation |

---

## 📂 Project Structure

```

cuda\_usd\_simulation/
│
├── include/                # CUDA header files
│   └── simulation.cuh
│
├── src/                    # CUDA + C++ source files
│   ├── main.cu             # Entry point: calls simulator
│   ├── simulation.cu       # Physics simulation logic
│   ├── usd\_loader.cpp/hpp  # Mock USD reader
│
├── usd\_writer/             # Python writer to export USD frames
│   └── usd\_writer.py
│
├── output\_frames/          # USD frames generated from simulation
│   └── frame\_0000.usd → frame\_0049.usd
│
├── CMakeLists.txt          # Build instructions
└── README.md               # This file

````

---

## 🚀 How to Run

### 1. Build the CUDA Simulator
```bash
cd build
cmake ..
make
````

### 2. Run the Simulation

```bash
./simulator
```

> This generates mock ball positions and prints:
> `Simulation done. Write frames using Python usd_writer.py`

### 3. Generate Animation Frames

```bash
cd ../usd_writer
python3 usd_writer.py
```

> This creates USD files like `frame_0000.usd`, `frame_0001.usd`, ... in `output_frames/`.

### 4. View the Animation

```bash
usdview ../output_frames/frame_0000.usd
```

> You’ll see a timeline slider at the bottom — hit ▶️ Play to watch the animation.

---

## 💡 Future Ideas (WIP)

* Make the balls bounce and disappear on floor contact
* Add interactivity: pull balls up before they fall
* Colorful ball themes
* Build it into a game 🎮 using real-time graphics engine

---

## 👩‍💻 Author

Binduja Malempati
*Graduate Student in Data Science*
[GitHub](https://github.com/bindujamalempati)

---

## 🌟 License

This project is for educational and non-commercial use.

```

---

Let me know when it’s pushed – I’ll help you polish the GitHub project description and **convert this to a perfect resume bullet** too.
```
