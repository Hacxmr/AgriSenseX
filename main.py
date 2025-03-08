from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io

app = FastAPI()

@app.post("/analyze-soil/")
async def analyze_soil(file: UploadFile = File(...)):
    try:
        # Read image file
        image = Image.open(io.BytesIO(await file.read()))
        
        # Simulated model output (Replace with actual ML model inference)
        recommended_crop = "Wheat"  # Example output
        
        return {"recommended_crop": recommended_crop}
    except Exception as e:
        return {"error": str(e)}
