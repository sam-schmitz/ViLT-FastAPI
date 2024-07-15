#main.py
#The FastAPI app for the model

from model import model_pipeline

from fastapi import FastAPI, UploadFile
import io
from PIL import Image

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    #grab the image from the upload file
    content = image.file.read()     
    
    image = Image.open(io.BytesIO(content))
    #image = Image(image.file)
    
    result = model_pipeline(text, image)
    
    return result
