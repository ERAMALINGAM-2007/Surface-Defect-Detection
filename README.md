# Surface Defect Detection Using YOLOv8

A deep learning-based web application for detecting industrial surface defects using the YOLOv8 object detection model. The system identifies multiple types of defects from uploaded images and displays detection results with bounding boxes and confidence scores.

---

# Features

* YOLOv8-based defect detection
* Multiple defect class support
* Image upload through web interface
* Real-time prediction using Flask backend
* Bounding box visualization
* Confidence score display
* REST API integration
* Modern frontend UI

---

# Defect Classes

The model is trained to detect the following defects:

1. Crease
2. Crescent Gap
3. D
4. Inclusion
5. Oil Spot
6. Punching Hole
7. Rolled Pit
8. Silk Spot
9. Waist Folding
10. Water Spot
11. Welding Line

---

# Tech Stack

## Deep Learning

* YOLOv8
* PyTorch
* OpenCV

## Backend

* Flask
* Flask-CORS

## Frontend

* HTML
* CSS
* JavaScript

## Dataset

* Roboflow Dataset

---

# Project Structure

```bash
Surface-Defect-Detection/
│
├── backend/
│   ├── app.py
│   ├── uploads/
│   ├── outputs/
│   └── model/
│       └── best.pt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── data.yaml
│
├── runs/
├── venv/
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/ERAMALINGAM-2007/Surface-Defect-Detection.git
```

## 2. Navigate to Project

```bash
cd Surface-Defect-Detection
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install flask
pip install flask-cors
pip install ultralytics
pip install opencv-python
pip install pillow
pip install torch torchvision torchaudio
```

---

# Model Training

Train the YOLOv8 model using:

```bash
yolo detect train data=dataset/data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

---

# Run Flask Backend

Navigate to backend folder:

```bash
cd backend
```

Run backend server:

```bash
python app.py
```

Backend will run at:

```bash
http://127.0.0.1:5000
```

---

# Run Frontend

Open:

```bash
frontend/index.html
```

in your browser.

---

# API Endpoint

## Predict Defects

### Endpoint

```bash
POST /predict
```

### Input

* Image file

### Output

* Detected defects
* Confidence scores
* Output image with bounding boxes

---

# Evaluation Metrics

The model performance is evaluated using:

* Precision
* Recall
* mAP50
* mAP50-95
* F1 Score
* Confusion Matrix

Validation command:

```bash
yolo detect val model=runs/detect/train/weights/best.pt data=dataset/data.yaml
```

---

# Sample Workflow

```text
Image Upload
      ↓
Flask Backend
      ↓
YOLOv8 Prediction
      ↓
Defect Detection
      ↓
Bounding Box Output
```

---

# Future Improvements

* Webcam defect detection
* Live video analysis
* React frontend
* Cloud deployment
* User authentication
* Detection history storage
* Real-time monitoring dashboard

---

# Author

ERAMALINGAM S

---

# License

This project is developed for educational and research purposes.
