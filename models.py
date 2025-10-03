

"""BlipForCondtional Generation came from Hugging Faces transfromers: for vision models
BlipPRocessor :converts raw inputs into tesnors that model can understand"
PIL or Pillow: used for image opertaions
"""
from transformers import BlipProcessor, BlipForConditionalGeneration
import pyttsx3  # fallback option (offline TTS)
from PIL import Image
from transformers import pipeline


"""OOP(object oriented programming) concepts demonstrated"""


"""Demonstrates abstraction base model for the AI """
class BaseModel:     
    def __init__(self, model_name):
        self.model_name= model_name #Encapsulation: data is inside the object
        self.pipeline=None #Encapsulation varibale (internal) is hidden from outside use

    def process_input(self,input_data):
        #Ploymorphism :it forces subclass to override with their implementation
        raise NotImplementedError("Subclasses didn't override") #it raises and Error if it is not overriden
    
#Text-to Speech Model
#Demnonstrates the inheritence inherited form base model class
lass TexttoSpeechModel(BaseModel):    
    def __init__(self):
        # Inheritance: Calls parent class constructor
        super().__init__("facebook/mms-tts-eng")   #Use a stable TTS model instead of VibeVoice

        try:
            # Abstraction: hiding pipeline setup, exposing only class methods
            self.pipeline = pipeline("text-to-speech", model=self.model_name)
        except Exception as e:
            print("Could not load Hugging Face Text-to-Speech model:", e)
            self.pipeline = None   # Will fallback later

    # Polymorphism: overriding base process_input
    def process_input(self, input_data: str):
        if self.pipeline:
            try:
                # Encapsulation: audio generation handled internally
                output = self.pipeline(input_data)
                # Save audio file output
                with open("output.wav", "wb") as f:
                    f.write(output["audio"])
                return "Audio generated successfully → saved as output.wav"
            except Exception as e:
                return f" Error generating speech: {e}"
        else:
            # Fallback: use pyttsx3 for offline speech
            try:
                engine = pyttsx3.init()
                engine.save_to_file(input_data, "output_fallback.wav")
                engine.runAndWait()
                return "Hugging Face TTS unavailable → Fallback voice saved as output_fallback.wav"
            except Exception as e:
                return f"No TTS available: {e}"

    


 #Model 2 Image to text
class ImageCaptionModel(BaseModel):         
    def __init__(self):            #Inheritance: calling parent constructor
        super().__init__("Salesforce/blip-image-captioning-large")
        try:            #Encapsulation and abstraction: pipeline handles the model internally
            self.pipeline= pipeline("image-to-text", model=self.model_name)
        except Exception as e:
            print("Could not load image captioning model")    #Printing error in case model could not be loaded
            self.pipeline=None


#Pilymorphism: overriding base case class to process image.
    def process_input(self, input_data: str):
        if self.pipeline:
            try:      #Use of pipeline to generate caption from input image
                result=self.pipeline(input_data)
                return result[0]["generated_text"]    #Returns the generated text from pipeline
            except Exception as e:
                return f"Error"         #Error handling in process.
        else:                            #Returns message if pipeline is not loaded.
            return ("Image captioning model could not be loaded")
