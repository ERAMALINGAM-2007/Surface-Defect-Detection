from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ultralytics import YOLO
import os
import cv2
import uuid

# =========================================
# Flask App Configuration
# =========================================

app = Flask(__name__)
CORS(app)

# =========================================
# Folder Configuration
# =========================================

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
MODEL_PATH = "model/best.pt"

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# =========================================
# Load YOLOv8 Model
# =========================================

model = YOLO(MODEL_PATH)


print("Model loaded successfully")
# =========================================
# Home Route
# =========================================

@app.route("/")
def home():
    return "YOLOv8 Surface Defect Detection API Running"

# =========================================
# Prediction Route
# =========================================

@app.route("/predict", methods=["POST"])
def predict():

    # Check image exists
    if "image" not in request.files:
        return jsonify({
            "success": False,
            "message": "No image uploaded"
        })

    file = request.files["image"]

    # Check filename
    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "Empty filename"
        })

    try:

        # Generate unique filename
        filename = str(uuid.uuid4()) + ".jpg"

        # Save uploaded image
        upload_path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(upload_path)

        # =========================================
        # Run YOLO Prediction
        # =========================================

        results = model(upload_path)

        result = results[0]

        # =========================================
        # Draw Bounding Boxes
        # =========================================

        annotated_frame = result.plot()

        output_path = os.path.join(OUTPUT_FOLDER, filename)

        cv2.imwrite(output_path, annotated_frame)

        # =========================================
        # Extract Detection Details
        # =========================================

        detections = []

        for box in result.boxes:

            cls_id = int(box.cls[0])

            confidence = float(box.conf[0])

            class_name = model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append({
                "class": class_name,
                "confidence": round(confidence, 2),
                "bounding_box": {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                }
            })

        # =========================================
        # Return Response
        # =========================================

        return jsonify({
            "success": True,
            "total_detections": len(detections),
            "detections": detections,
            "output_image": filename
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })

# =========================================
# Serve Output Images
# =========================================

@app.route("/output/<filename>")
def get_output_image(filename):

    return send_from_directory(
        OUTPUT_FOLDER,
        filename
    )

# =========================================
# Run Flask App
# =========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )