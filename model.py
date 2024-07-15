#model_starter.py
#Starter code from huggging face (https://huggingface.co/dandelin/vilt-b32-finetuned-vqa)
#A pytorch vision and language model that can process both images and text. 
#Can send the model an image and ask a question about it. The model 

from transformers import ViltProcessor, ViltForQuestionAnswering
#import requests
from PIL import Image

# 470MB
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# prepare image + question
#url = "http://images.cocodataset.org/val2017/000000039769.jpg"
#image = Image.open(requests.get(url, stream=True).raw)

#text = "How many cats are there?"

def model_pipeline(text: str, image: Image):
    
    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    return model.config.id2label[idx]

