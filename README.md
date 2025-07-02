# Real-Time-Rock-Paper-Scissors-Recognition-Using-YOLOv5
Real-Time Rock, Paper, Scissors Recognition Using YOLOv5

This project is a real-time hand gesture recognition system built with **YOLOv5**, capable of detecting and classifying rock, paper, and scissors using a webcam feed.

> 🎓 This was my official school project, and it means a lot to me — it marks my hands-on dive into real-world AI development. I'm passionate about building smart systems, and this project reflects my interest in solving interactive problems using machine learning.

---

## 📌 Features

- ✅ Real-time detection of rock, paper, and scissors gestures
- 📸 Custom dataset creation with varied lighting and angles
- 🏷️ Manual image annotation using LabelImg and Label Studio
- 💻 Model trained locally on a personal laptop (YOLOv5, mAP@0.5 = 0.96)
- ⚡ Real-time webcam detection with OpenCV (20–30 FPS)
- 📄 Full documentation of setup, training, troubleshooting, and deployment

---

## 🛠️ Tools & Technologies

- Python 3.12  
- PyTorch  
- YOLOv5  
- OpenCV  
- LabelImg, Label Studio  
- Anaconda (virtual environment)  
- Windows (training environment)

---

## 📂 Project Structure

📂 rock-paper-scissors-yolov5/
├── 📂 datasets/
│   ├── 📂 images/
│   │   ├── 📂 train/
│   │   └── 📂 validation/
│   ├── 📂 labels/
│   │   ├── 📂 train/
│   │   └── 📂 validation/
│   ├── classes.txt       # Class names (e.g., rock, paper, scissors)
│   └── data.yaml         # Dataset config file for YOLOv5
├── 📂 models/
│   └── best.pt           # Trained model weights
├── 📂 scripts/
│   ├── train.py          # Training script
│   ├── detect.py         # Detection script
│   ├── split.py          # Optional: dataset splitter
│   └── gen-data-yaml.py  # Script to generate data.yaml

---

## 🧠 How It Works

1. **Data Collection**  
   Hand gesture images (rock, paper, scissors) were captured manually using a webcam.

2. **Annotation**  
   Bounding boxes were drawn manually using LabelImg and exported in YOLO format.

3. **Training**  
   - Model: YOLOv5s  
   - Epochs: 25  
   - Batch Size: 16  
   - Input Size: 640x640  
   - Achieved mAP@0.5: 0.96

4. **Deployment**  
   The trained model was used for live webcam detection using OpenCV on Windows.

   ---

## 🖼️ Project Highlights
![Training results](https://github.com/user-attachments/assets/55fb96c3-329c-421a-9bf0-5ae6e1547c7a)
![Detection Sample](https://github.com/user-attachments/assets/3007d3b5-88f0-4d16-8960-082c50b912f4)



## 📘 Technical Report

You can read the full technical documentation and implementation guide below:

📄 [Download the PDF Report](https://lnkd.in/dan4c9iP)
[Report.pdf](https://github.com/user-attachments/files/21011879/Report.pdf)


## 🚀 Run It Yourself

Follow the steps below to run the real-time Rock, Paper, Scissors recognition system on your own machine.

### 1. Clone this repo and install dependencies

```bash
git clone https://github.com/your-username/rock-paper-scissors-yolov5.git
cd rock-paper-scissors-yolov5
pip install -r requirements.txt
```
### 2. Download the Trained Model

The trained YOLOv5 model weights (`best.pt`) are too large to be stored on GitHub directly.

📦 [Download best.pt from Google Drive](https://drive.google.com/file/d/19mHGk3xd861rQr9898OXcm90axJWPQfQ/view?usp=drive_link)

After downloading, place the `best.pt` file into the `models/` directory in your project folder:

```plaintext
models/
└── best.pt
```

### 3. Run Real-Time Detection
Make sure your webcam is connected. Then run:

```bash
python scripts/detect.py --weights models/best.pt --source 0
```

`--source 0` refers to the webcam.

You can also test an image or video by changing the source:
`--source path/to/image.jpg` or `--source path/to/video.mp4`

### 4. Optional: Train the Model from Scratch
If you want to retrain the model using your own dataset:
```bash
python train.py --img 640 --batch 16 --epochs 50 --data datasets/data.yaml --weights models/best.pt
```
   Note: Make sure your dataset is correctly formatted and data.yaml is set up properly.


