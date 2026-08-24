# Surface Defect Detection using YOLOv8

A computer vision application for detecting and localizing industrial surface defects using a trained YOLO-based object detection model. The trained model is integrated with a Flask REST API and a lightweight HTML, CSS, and JavaScript frontend for image-based defect inspection.

---

## 📌 Problem Statement

Manual inspection of industrial surfaces can be time-consuming and may be affected by human error or inconsistency. Surface defects such as inclusions, oil spots, welding lines, punching holes, and other imperfections need to be identified accurately and localized for quality inspection.

This project aims to automate the inspection process using **deep-learning-based object detection**.

The system accepts an image of a surface, detects one or more defects, identifies their defect categories, calculates confidence scores, and draws bounding boxes around the detected regions.

---

## 🎯 Objectives

* Detect surface defects automatically from images.
* Identify the type of each detected defect.
* Locate defects using bounding boxes.
* Provide a confidence score for every detection.
* Deploy the trained model through a REST API.
* Provide a simple web interface for image upload and result visualization.
* Demonstrate an end-to-end computer vision inference pipeline.

---

## ✨ Features

### 🔍 Surface Defect Detection

The system uses a trained YOLO model to detect multiple defects within a single image.

For each detection, the system provides:

* Defect class
* Confidence score
* Bounding-box coordinates

### 🖼️ Annotated Image

The detected defects are drawn on the input image using the YOLO visualization functionality.

The resulting image can contain:

```text
Defect Name
Confidence Score
Bounding Box
```

### 🌐 Web Interface

The project includes a lightweight frontend built using:

* HTML
* CSS
* JavaScript

Users can select an image and send it to the backend for prediction.

### 🔌 REST API

The Flask backend exposes an API endpoint:

```text
POST /predict
```

which accepts an uploaded image and returns detection results in JSON format.

---

# 🏗️ System Architecture

```text
                    User
                     │
                     ▼
              Web Interface
           HTML + CSS + JavaScript
                     │
                     │ Image Upload
                     ▼
                Flask API
                     │
                POST /predict
                     │
                     ▼
              YOLOv8 Model
                     │
                     ▼
              Object Detection
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
        Class    Confidence   Bounding Box
          │          │          │
          └──────────┼──────────┘
                     │
                     ▼
              JSON Response
                     │
                     ├──────────────► Detection Information
                     │
                     ▼
              Annotated Image
                     │
                     ▼
                  Browser
```

---

# 🛠️ Technology Stack

| Category             | Technology                | Purpose                                   |
| -------------------- | ------------------------- | ----------------------------------------- |
| Programming Language | Python                    | Backend and ML integration                |
| Deep Learning        | YOLOv8                    | Surface defect object detection           |
| ML Framework         | Ultralytics               | YOLO model training and inference         |
| Computer Vision      | OpenCV                    | Image processing and saving output images |
| Backend              | Flask                     | REST API                                  |
| CORS                 | Flask-CORS                | Frontend-backend communication            |
| Frontend             | HTML                      | Web interface                             |
| Styling              | CSS                       | User interface styling                    |
| Client-side Logic    | JavaScript                | Image upload and API communication        |
| Dataset Format       | YOLO                      | Object detection annotations              |
| Dataset Source       | Roboflow-exported dataset | Annotated surface defect dataset          |
| Model Format         | `.pt`                     | Trained YOLO model weights                |

---

# 🤖 Machine Learning Model

The project uses a **YOLO-based object detection model**.

YOLO is suitable for this project because it can simultaneously provide:

```text
Object Class
     +
Bounding Box
     +
Confidence Score
```

Unlike image classification, which generally produces only a class prediction for an image, object detection allows multiple defects to be identified and localized within the same image.

---

## Why Object Detection?

Consider an image containing:

```text
        Surface Image
┌─────────────────────────┐
│                         │
│    [Oil Spot]           │
│                         │
│              [Crease]   │
│                         │
│       [Inclusion]       │
│                         │
└─────────────────────────┘
```

A classification model might only provide one overall class.

The object detection model can provide:

```text
Oil Spot      → Bounding Box + Confidence
Crease        → Bounding Box + Confidence
Inclusion     → Bounding Box + Confidence
```

This makes object detection more appropriate for the application.

---

# 📊 Dataset

The project uses a YOLO-format annotated surface-defect dataset.

The dataset contains:

| Dataset Split |    Images | Percentage |
| ------------- | --------: | ---------: |
| Training      |     1,710 |        75% |
| Validation    |       342 |        15% |
| Testing       |       228 |        10% |
| **Total**     | **2,280** |   **100%** |

The dataset contains **11 configured defect classes**.

---

## Defect Classes

The classes configured in `data.yaml` are:

| Class ID | Defect        |
| -------: | ------------- |
|        0 | crease        |
|        1 | crescent_gap  |
|        2 | d             |
|        3 | inclusion     |
|        4 | oil_spot      |
|        5 | punching_hole |
|        6 | rolled_pit    |
|        7 | silk_spot     |
|        8 | waist folding |
|        9 | water_spot    |
|       10 | welding_line  |

The class mapping is defined in:

```text
dataset/data.yaml
```

---

# 📁 Dataset Structure

```text
dataset/
│
├── data.yaml
├── split_dataset.py
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
└── test/
    ├── images/
    └── labels/
```

Each image has a corresponding YOLO annotation file.

Example:

```text
image001.jpg
image001.txt
```

---

# 🏷️ YOLO Annotation Format

Each annotation follows the YOLO format:

```text
class_id center_x center_y width height
```

The coordinates are normalized between `0` and `1`.

For example:

```text
3 0.52 0.43 0.20 0.15
```

means:

```text
Class ID     → 3
Center X     → 0.52
Center Y     → 0.43
Width        → 0.20
Height       → 0.15
```

---

# 🔀 Dataset Splitting

The project includes:

```text
dataset/split_dataset.py
```

The script divides the original dataset into:

```text
75% → Training
15% → Validation
10% → Testing
```

The images and their corresponding label files are moved into their respective directories.

> For reproducible dataset splitting, a fixed random seed should be used when generating a new split.

---

# ⚠️ Dataset Considerations

The dataset is not perfectly balanced.

Some classes contain considerably more annotations than others.

For example, the training annotations include approximately:

| Defect        | Training Bounding Boxes |
| ------------- | ----------------------: |
| inclusion     |                     643 |
| welding_line  |                     467 |
| crease        |                     371 |
| water_spot    |                     272 |
| oil_spot      |                     269 |
| crescent_gap  |                     236 |
| silk_spot     |                     195 |
| punching_hole |                     105 |
| rolled_pit    |                      66 |
| waist folding |                      54 |
| d             |                       0 |

The `d` class has no training annotations in the current training set, so meaningful learning of this class cannot be expected from the available training data.

This is an important dataset limitation and should be addressed before using the model in a production environment.

---

# 🧠 Transfer Learning

The project uses a pretrained YOLO model as the starting point for training.

Conceptually:

```text
Pretrained YOLO Model
          │
          ▼
Generic Visual Features
          │
          ▼
Surface Defect Dataset
          │
          ▼
Fine-Tuning
          │
          ▼
Surface Defect Detection Model
```

Transfer learning reduces the amount of training required compared with training a deep-learning model completely from random initialization.

---

# ⚙️ Model Training

The project uses the Ultralytics YOLO training interface.

A representative training command is:

```bash
yolo detect train data=dataset/data.yaml model=yolov8n.pt epochs=50 imgsz=640
```

### Parameters

| Parameter | Meaning                                |
| --------- | -------------------------------------- |
| `data`    | Dataset configuration file             |
| `model`   | Initial YOLO model weights             |
| `epochs`  | Number of training epochs              |
| `imgsz`   | Target image size used during training |

The trained model is saved as:

```text
best.pt
```

---

# 📦 Trained Model

The trained YOLO weights are stored in:

```text
backend/model/best.pt
```

The backend loads the model when the Flask application starts:

```python
model = YOLO(MODEL_PATH)
```

Loading the model once at startup avoids repeatedly loading the model for every API request.

---

# 🔄 Complete Prediction Workflow

```text
1. User selects an image
            │
            ▼
2. JavaScript creates FormData
            │
            ▼
3. POST request to /predict
            │
            ▼
4. Flask receives the image
            │
            ▼
5. Image is temporarily saved
            │
            ▼
6. YOLO model performs inference
            │
            ▼
7. Detection results are extracted
            │
            ├── Class
            ├── Confidence
            └── Bounding Box
            │
            ▼
8. YOLO generates annotated image
            │
            ▼
9. Annotated image is saved
            │
            ▼
10. Flask returns JSON response
            │
            ▼
11. JavaScript displays results
            │
            ▼
12. Browser displays annotated image
```

---

# 🖥️ Backend

The backend is implemented using **Flask**.

Main backend file:

```text
backend/app.py
```

---

## Flask Application

The application is initialized using:

```python
app = Flask(__name__)
```

CORS is enabled using Flask-CORS so that the frontend can communicate with the backend.

---

# 🔌 API Endpoints

## Health Check

```text
GET /
```

Returns:

```text
YOLOv8 Surface Defect Detection API Running
```

This can be used to verify that the Flask server is running.

---

## Prediction API

```text
POST /predict
```

### Input

The request should contain an image using the form-data field:

```text
image
```

Example:

```text
Content-Type: multipart/form-data
```

---

## Prediction Response

A successful response contains information similar to:

```json
{
  "success": true,
  "total_detections": 2,
  "detections": [
    {
      "class": "inclusion",
      "confidence": 0.92,
      "bounding_box": {
        "x1": 100,
        "y1": 50,
        "x2": 300,
        "y2": 200
      }
    }
  ],
  "output_image": "generated-image.jpg"
}
```

The exact detection values depend on the input image and model prediction.

---

# 🖼️ Output Image API

```text
GET /output/<filename>
```

This endpoint returns the annotated prediction image stored in the output directory.

---

# 🧩 Backend Processing

The prediction endpoint performs the following operations:

```text
Receive Image
     │
     ▼
Validate Upload
     │
     ▼
Generate Unique Filename
     │
     ▼
Save Image
     │
     ▼
YOLO Inference
     │
     ▼
Extract Results
     │
     ├── Class ID
     ├── Class Name
     ├── Confidence
     └── Bounding Box
     │
     ▼
Generate Annotated Image
     │
     ▼
Save Output
     │
     ▼
Return JSON
```

---

# 🌐 Frontend

The frontend is intentionally lightweight and uses:

```text
HTML
CSS
JavaScript
```

It does not require a frontend framework.

---

## Frontend Structure

```text
frontend/
│
├── index.html
├── script.js
└── style.css
```

---

# 📤 Image Upload Flow

The JavaScript frontend uses the browser's `FormData` API to send the selected image.

```text
File Input
    │
    ▼
JavaScript
    │
    ▼
FormData
    │
    ▼
fetch()
    │
    ▼
POST /predict
```

The backend processes the image and returns JSON.

---

# 📥 Displaying Results

After receiving the response, JavaScript displays:

* Total number of detections
* Detected class names
* Confidence scores
* Annotated output image

---

# 📂 Project Structure

```text
Surface-Defect-Detection/
│
├── backend/
│   ├── app.py
│   └── model/
│       └── best.pt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── model/
│   └── best.pt
│
├── dataset/
│   ├── data.yaml
│   ├── split_dataset.py
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   └── test/
│       ├── images/
│       └── labels/
│
├── Docs/
│
├── dataset.zip
└── README.md
```

---

# 🚀 Installation

## Prerequisites

Install:

* Python 3.9+
* pip
* Ultralytics
* Flask
* Flask-CORS
* OpenCV

---

## 1. Clone the Repository

```bash
git clone <repository-url>
cd Surface-Defect-Detection
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install flask flask-cors ultralytics opencv-python
```

If a `requirements.txt` file is provided, install dependencies using:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Navigate to the backend:

```bash
cd backend
```

Start the Flask server:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

# 🌐 Running the Frontend

Open:

```text
frontend/index.html
```

in a browser.

Then:

1. Select a surface image.
2. Click **Detect Defects**.
3. The frontend sends the image to Flask.
4. YOLO performs inference.
5. Detection results are returned.
6. The annotated image is displayed.

---

# 🧪 Example

### Input

```text
Surface Image
```

### Model Processing

```text
Image
  ↓
YOLO
  ↓
Defect Detection
```

### Output

```text
Defect: inclusion
Confidence: 0.92
Bounding Box: (x1, y1, x2, y2)
```

along with an annotated image showing the detected region.

---

# 📈 Evaluation Metrics

The important metrics for evaluating this object-detection model include:

### Precision

Measures how many predicted detections are correct.

```text
Precision = TP / (TP + FP)
```

### Recall

Measures how many actual defects are successfully detected.

```text
Recall = TP / (TP + FN)
```

### F1 Score

Balances precision and recall.

```text
F1 = 2 × Precision × Recall
     ───────────────────────
       Precision + Recall
```

### IoU

Intersection over Union measures overlap between the predicted bounding box and ground-truth bounding box.

```text
IoU = Intersection Area / Union Area
```

### mAP

Mean Average Precision is a commonly used object-detection evaluation metric.

Common variants include:

```text
mAP@50
mAP@50-95
```

> The repository does not contain sufficient original training-result artifacts to state a verified numerical mAP, precision, or recall value. Therefore, no unsupported performance number is reported here.

---

# 🔐 Security and Validation Considerations

The current implementation is primarily designed as a prototype.

For production deployment, the following should be added:

* File type validation
* File size limits
* MIME-type validation
* Proper HTTP status codes
* Restricted CORS origins
* Input sanitization
* Temporary-file cleanup
* API rate limiting
* Authentication/authorization
* Error logging
* Monitoring

---

# ⚠️ Current Limitations

### 1. Dataset imbalance

Some defect categories contain significantly fewer annotations than others.

### 2. No live industrial integration

The system is not currently connected to:

* Industrial cameras
* Manufacturing PLC systems
* Production-line automation
* Quality-control databases

---

# 🔮 Future Improvements

Possible improvements include:

### 🤖 Machine Learning

* Add more training samples for minority classes.
* Balance the dataset.
* Improve annotation quality.
* Experiment with larger YOLO models.
* Tune confidence and IoU thresholds.
* Perform systematic hyperparameter optimization.
* Add stronger data augmentation.
* Evaluate per-class performance.

### 📷 Real-Time Detection

Integrate an industrial camera:

```text
Industrial Camera
       ↓
Live Video Stream
       ↓
YOLO Model
       ↓
Defect Detection
       ↓
Quality Control System
```

### 🌐 Web Application

* Add authentication.
* Add prediction history.
* Add image deletion.
* Add dashboard and analytics.
* Add per-class statistics.
* Add downloadable inspection reports.

### ⚡ Backend

* Add proper request validation.
* Add API rate limiting.
* Add structured logging.
* Add asynchronous processing.
* Use production WSGI deployment.
* Add automated cleanup of temporary files.

### ☁️ Deployment

The application could be deployed using:

```text
Frontend
   ↓
Web Server
   ↓
Flask API
   ↓
GPU-enabled Model Server
```

---

# 🧠 Technical Concepts Demonstrated

This project demonstrates practical knowledge of:

* Computer Vision
* Deep Learning
* Object Detection
* YOLO
* Transfer Learning
* Image Annotation
* Dataset Splitting
* Model Inference
* Bounding Boxes
* Confidence Scores
* IoU
* Non-Maximum Suppression
* Precision
* Recall
* mAP
* REST APIs
* Flask
* HTTP POST requests
* Multipart form-data
* JSON
* JavaScript Fetch API
* OpenCV
* Model Deployment

---

# 🎓 Learning Outcomes

Through this project, the following concepts were implemented practically:

1. Preparing an object-detection dataset.
2. Working with YOLO annotation format.
3. Training a YOLO-based detection model.
4. Loading trained model weights.
5. Performing image inference.
6. Extracting class predictions.
7. Extracting confidence scores.
8. Extracting bounding boxes.
9. Generating annotated images.
10. Building a Flask REST API.
11. Connecting a frontend to a machine-learning backend.
12. Returning ML predictions as JSON.
13. Building an end-to-end computer-vision application.

---

# 📌 Project Summary

**Surface Defect Detection** is an end-to-end computer vision project that applies YOLO-based object detection to industrial surface inspection.

The system follows:

```text
Annotated Dataset
       ↓
YOLO Model Training
       ↓
Trained best.pt
       ↓
Flask REST API
       ↓
Image Upload
       ↓
YOLO Inference
       ↓
Defect Class
       +
Confidence
       +
Bounding Box
       ↓
Annotated Image
       ↓
Web Interface
```

The project demonstrates the integration of a **deep-learning computer-vision model with a web-based application**, transforming a trained object-detection model into a usable defect-inspection system.
