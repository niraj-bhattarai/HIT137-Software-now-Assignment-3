#gui 
# defines tkinter gui

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from models import VADERVideoModel, ImageCaptionModel
from decorators import log_time
from utils import model_information


class AIApp(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)
        #title for the frame
        self.title("Tkinter GUI - Assignment Software Now")

        #Setting the window sizd
        self.geometry("900x700")

        #Initializing two models
        self.model1=VADERVideoModel()
        self.model2=ImageCaptionModel()
        self.input_file=None   #For the uploaded files

        self.create_menu()
        self.create_widget() #Building GUI components

    def create_menu(self):    #MENU BAR
        menu_bar=tk.Menu(self)
        self.config(menu=menu_bar)

        #File menu
        file_menu=tk.Menu(menu_bar,tearoff=0)
        file_menu.add_command(label="Exit",command=self.quit)
        menu_bar.add_cascade(label="File",menu=file_menu)

        #Model menu
        model_menu=tk.Menu(menu_bar,tearoff=0)
        model_menu.add_command(label="Run Text-to-video",command=self.run_model1)
        model_menu.add_command(label="Run Image to Text",command=self.run_model2)
        menu_bar.add_cascade(label="Models",menu=model_menu)

        #Help menu
        help_menu=tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About",command=lambda: messagebox.showinfo("About","Tkinter AI GUI\nFor Software Now Assignment 3"))
        menu_bar.add_cascade(label="Help",menu=help_menu)



    def create_widget(self):          #Main Widgets

        selection_frame=tk.LabelFrame(self,text="Model Selection")
        selection_frame.pack(fill="x",padx=10,pady=5)

        tk.Label(selection_frame,text="Select Model").pack(side="left",padx=5)
        self.model_select=ttk.Combobox(selection_frame,values=["Text-to-video","Image-to-text"])
        self.model_select.current(0)
        self.model_select.pack(side="left",padx=5)

        tk.Button(selection_frame,text="Run Model",command=self.run_model1).pack(side="left",padx=5)
        

        #Showing input and output

        io_frame=tk.Frame(self)
        io_frame.pack(fill="both",expand=True,padx=11,pady=5)

        #User input

        input_frame=tk.LabelFrame(io_frame,text="User Input")
        input_frame.pack(side="left",fill="both",expand=True,padx=5,pady=5)
        

        self.input_type=tk.StringVar(value="Text")
        tk.Radiobutton(input_frame,text="Text",variable=self.input_type,value="Text").pack(anchor="w")
        tk.Radiobutton(input_frame,text="Image",variable=self.input_type,value="Image").pack(anchor="w")

        tk.Button(input_frame,text="Browse",command=self.upload_files).pack(pady=5)
        

        self.input_text=tk.Text(input_frame,height=5, width=50)
        self.input_text.pack(pady=5)

        tk.Button(input_frame,text="Run Model 1",command=self.run_model1).pack(side="left",padx=5)
        tk.Button(input_frame,text="Run Model 2",command=self.run_model2).pack(side="left",padx=5)
        tk.Button(input_frame,text="Clear",command=self.clear_output).pack(side="left",padx=5)

        output_frame=tk.LabelFrame(io_frame,text="Model Output Section")
        output_frame.pack(side="right",fill="both",expand=True,padx=5,pady=5)

        self.output_text=tk.Text(output_frame,height=15,width=60)
        self.output_text.pack(pady=10)

       #For the Model information
        information_frame=tk.LabelFrame(self,text="Model Information")
        information_frame.pack(fill="both",expand=True,padx=10,pady=10)

        tk.Label(information_frame,text="Selected Model Information:").grid(row=0,column=0,sticky="w")
        tk.Label(information_frame,text="Object Oriented Concepts:").grid(row=0,column=1,sticky="w")



        self.model_information_text=tk.Text(information_frame, height=10, width=15, fg="blue")
        self.model_information_text.grid(row=1,column=0,padx=5,pady=5)

        self.oop_information_text=tk.Text(information_frame,height=10,width=50)
        self.oop_information_text.grid(row=1,column=1,padx=5,pady=5)

        self.show_model_information()
        self.show_oop_information()


    def upload_files(self):   #allowing users to upload or select an image to generate text

        file_path= filedialog.askopenfilename(filetypes=[("Image files","*.jpg *.jpeg *.png")])
        if file_path:
            self.input_file = file_path
            messagebox.showinfo("Image selected",f"File: {file_path}")

    def load_model(self):
        selected=self.model_select.get()
        messagebox.showinfo("Model Selected",f"Selected Model: {selected}")

    def clear_output(self):
        self.output_text.delete(1.0,tk.END)


    @log_time
    def run_model1(self):
    #Running Model 1 i.e TExt-to-Video
        result= self.model1.process_input("A horse running")
        self.output_text.insert(tk.END, f"\nModel 1 Text-to-Video (VADER) Output:\n{result}\n")

    @log_time
    def run_model2(self):
      #Running Model 2 Image to Text
        if not self.input_file:
            messagebox.showerror("Error","Please upload an image first.")
            return
        
        result=self.model2.process_input(self.input_file)
        self.output_text.insert(tk.END, f"\nModel 2 Image to Text Output:\n{result}\n")


    def show_model_information(self):
         #Displaying model descriptions 

        information= model_information()
        self.model_information_text.insert(tk.END, "Model Information:\n\n")
        for k,v in information.items():
            self.model_information_text.insert(tk.END, f"{k}: {v}\n\n")

    def show_oop_information(self):
        oop_expl=(
            "-Multiple Inheritance: Through AIApp from Tkinter Tk\n"
            "-Encapsulation:BaseModel\n"
            "-Polymorphism:"
            "-Method Overriding"
            "-Decoratore: log time"
        )
        self.oop_information_text.insert(tk.END,oop_expl)



