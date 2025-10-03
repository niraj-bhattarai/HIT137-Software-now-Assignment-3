
"""BlipForCondtional Generation came from Hugging Faces transfromers: for vision models
BlipPRocessor :converts raw inputs into tesnors that model can understand"
PIL or Pillow: used for image opertaions
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


class BaseModel:      #Base Class
    def __init__(self, model_name):
        self.model_name= model_name
        self.pipeline=None 

    def process_input(self,input_data):
        raise NotImplementedError("Subclasses didn't override")
    
    #Text-to Speech Model
class TexttoSpeechModel(BaseModel):     #
    def __init__(self):
        super().__init__("microsoft/VibeVoice-1.5B")
        try:
            #Load pipeline
            self.pipeline=pipeline("text-to-speech",model=self.model_name)
        except Exception as e:
            print ("Could not load Text-to speech",e)
            self.pipeline=None 
 
    def process_input(self, input_data: str):

        if self.pipeline:
            try:
                output=self.pipeline(input_data)
                return "Audio generated succesfully" 
            except Exception as e:
                return f"Error generating speech:{e}"
        else:
            return("Text to image requires heavy dependencies")
    
    


class ImageCaptionModel(BaseModel):          #Model 2 Image to text
    def __init__(self):
        super().__init__("Salesforce/blip-image-captioning-large")
        try:
            self.pipeline= pipeline("image-to-text", model=self.model_name)
        except Exception as e:
            print("Could not load image captioning model")
            self.pipeline=None

    def process_input(self, input_data: str):
        
        if self.pipeline:
            try:
                result=self.pipeline(input_data)
                return result[0]["generated_text"]
            except Exception as e:
                return f"Error"
        else:
            return ("Image captioning model could not be loaded")
