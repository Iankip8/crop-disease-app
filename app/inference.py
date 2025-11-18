from PIL import Image
import numpy as np
import io

async def predict(model, file):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).resize((224, 224))
    img_arr = np.array(img) / 255.0
    img_arr = np.expand_dims(img_arr, axis=0)

    preds = model.predict(img_arr)
    class_idx = np.argmax(preds)
    confidence = float(np.max(preds))

    return {"class": int(class_idx), "confidence": confidence}
