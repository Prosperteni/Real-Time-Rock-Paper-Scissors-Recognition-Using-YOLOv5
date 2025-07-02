# Real-Time-Rock-Paper-Scissors-Recognition-Using-YOLOv5
Real-Time Rock, Paper, Scissors Recognition Using YOLOv5-Lite

This project is a real-time hand gesture recognition system built with **YOLOv5-Lite**, capable of detecting and classifying rock, paper, and scissors using a webcam feed.

> 🎓 This was my official school project, and it means a lot to me — it marks my hands-on dive into real-world AI development. I'm passionate about building smart systems, and this project reflects my interest in solving interactive problems using machine learning.

---

## 📌 Features

- ✅ Real-time detection of rock, paper, and scissors gestures
- 📸 Custom dataset creation with varied lighting and angles
- 🏷️ Manual image annotation using LabelImg and Label Studio
- 💻 Model trained locally on a personal laptop (YOLOv5-Lite, mAP@0.5 = 0.96)
- ⚡ Real-time webcam detection with OpenCV (20–30 FPS)
- 📄 Full documentation of setup, training, troubleshooting, and deployment

---

## 🛠️ Tools & Technologies

- Python 3.12  
- PyTorch  
- YOLOv5 / YOLOv5-Lite  
- OpenCV  
- LabelImg, Label Studio  
- Anaconda (virtual environment)  
- Windows (training environment)

---

## 📂 Project Structure

rock-paper-scissors-yolov5/
datasets/
├── 📂 images/
│   ├── 📂 train/
│   └── 📂 validation/
│
├── 📂 labels/
│   ├── 📂 train/
│   └── 📂 validation/
│
├── classes.txt               # Class names (e.g., rock, paper, scissors)
└── data.yaml                 # Dataset config file for YOLOv5
├── 📂 models/
│   └── best.pt                # Trained model weights
│
├── 📂 scripts/
│   ├── train.py               # Training script
│   ├── detect.py              # Detection script
│   ├── split.py               # Optional: dataset splitter
│   ├── gen-data-yaml.py       # Script to generate data.yaml
