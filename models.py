#models used 

"""BlipForCondtional Generation came from Hugging Faces transfromers: for vision models
BlipPRocessor :converts raw inputs into tensor (is mulitdimensional array) that model can understand"
PIL or Pillow: used for image opertaions like save ,open etc
"""
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


class BaseModel:      #Base Class
    def __init__(self, model_name):
        self.model_name= model_name

    def process_input(self,input_data):
        raise NotImplementedError("Subclasses didn't override")
    
class VADERVideoModel(BaseModel):     #Model 1 VADER Video (Text-to-video)
    def __init__(self):
        super().__init__("zheyangqin/VADER_VideoCrafter_PickScore")
        ###  

    def process_input(self, input_data: str):
        return 
    


class ImageCaptionModel(BaseModel):          #Model 2 Image to text
    def __init__(self):
        super().__init__("Salesforce/blip-image-captioning-large")
        self.processor= BlipProcessor.from_pretrained(self.model_name)
        self.model=BlipForConditionalGeneration.from_pretrained(self.model_name)

    def process_input(self, input_data):
        image=Image.open(input_data).convert("RGB")
        inputs= self.processor(images=image, return_tensors="pt")
        out= self.model.generate(**inputs)
        caption= self.processor.decode(out[0],skip_special_tokens=True)
        return caption