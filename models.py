

"""BlipForCondtional Generation came from Hugging Faces transfromers: for vision models
BlipPRocessor :converts raw inputs into tesnors that model can understand"
PIL or Pillow: used for image opertaions
"""
from transformers import BlipProcessor, BlipForConditionalGeneration
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
class TexttoSpeechModel(BaseModel):     #
    def __init__(self):
        #Inheritence :from parent constructor
        super().__init__("microsoft/VibeVoice-1.5B")
        #Using try except to about interruption
        try:
            #Load pipeline
            #Encapsulation :pipeline belongs to this class
            #Abstraction: Details are hidden,just method is shown
            self.pipeline=pipeline("text-to-speech",model=self.model_name)
        except Exception as e:
            print ("Could not load Text-to speech",e)
            self.pipeline=None 

     #Polymorphism:overrirding the base process models
    def process_input(self, input_data: str):
       
        if self.pipeline:
            try:
                #Encapsulation:wrapped inside an object
                output=self.pipeline(input_data)
                return "Audio generated successfully" 
            except Exception as e:
                return f"Error generating speech:{e}"
        else:                            #Return error message if pipeline is not loaded
            return("Text to image requires heavy dependencies")
    
    


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
