async function uploadImage() {

    const input = document.getElementById("imageInput");

    const file = input.files[0];

    if (!file) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();

    formData.append("image", file);

    const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    let html = "<h2>Detections</h2>";

    data.detections.forEach(det => {
        html += `
            <p>
                ${det.class} - Confidence: ${det.confidence}
            </p>
        `;
    });

    document.getElementById("result").innerHTML = html;

    document.getElementById("outputImage").src =
        `http://127.0.0.1:5000/output/${data.output_image}`;
}



