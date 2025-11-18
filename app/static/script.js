document.getElementById("upload-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const file = document.getElementById("image").files[0];
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    document.getElementById("result").innerText =
        `Prediction: ${data.prediction.class} (Confidence: ${data.prediction.confidence})`;
});
