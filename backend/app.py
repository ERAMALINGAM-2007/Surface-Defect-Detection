from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ultralytics import YOLO
import os
import cv2
import uuid

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load YOLO model
model = YOLO("model/best.pt")

@app.route("/")
def home():
    return "YOLOv8 Defect Detection API Running"

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]

    filename = str(uuid.uuid4()) + ".jpg"

    upload_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(upload_path)

    # Run prediction
    results = model(upload_path)

    result = results[0]

    # Draw detections
    annotated_frame = result.plot()

    output_path = os.path.join(OUTPUT_FOLDER, filename)

    cv2.imwrite(output_path, annotated_frame)

    detections = []

    for box in result.boxes:

        cls_id = int(box.cls[0])

        confidence = float(box.conf[0])

        class_name = model.names[cls_id]

        detections.append({
            "class": class_name,
            "confidence": round(confidence, 2)
        })

    return jsonify({
        "detections": detections,
        "output_image": filename
    })

@app.route("/output/<filename>")
def get_output_image(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)