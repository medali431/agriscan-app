from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True, "service": "AgriScan API"}

@app.post("/diagnose")
async def diagnose(image: UploadFile = File(...)):
    content = await image.read()
    img = Image.open(io.BytesIO(content))
    # TODO: passer le tensor au modèle IA
    return {"diagnosis": "plant_healthy", "confidence": 0.83}
