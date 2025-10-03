

"""This file contains the main components for the GUI models  """
#Importing GUI library
import tkinter as tk
#Importting file dialogs,alerts,and widgets
from tkinter import filedialog, messagebox, ttk
#IMporting AI models
from models import TexttoSpeechModel, ImageCaptionModel
#importing and using decorators to log execution time
from decorators import log_time

#For model details
from utils import model_information



class AIApp(tk.Frame):
    """Using master widget to  make code modular better for control over GUI and Saclability"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Window title and size (set on master)
        self.master.title("Tkinter GUI - Assignment Software Now")
        self.master.geometry("1200x900")

        # Initialize models
        self.model1 = TexttoSpeechModel()  # Text-to-Speech model
        self.model2 = ImageCaptionModel()  # Image-to-Text model
        self.input_file = None              # To store uploaded file path

        # Building  GUI
        self.create_menu() #Creates Menu bar
        self.create_widget() # Creates Main GUI components
        self.pack(fill="both", expand=True) # Packing  the frame

    
    def create_menu(self):
        """Creates the top menu bar with File, Models, and Help."""
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Models menu
        model_menu = tk.Menu(menu_bar, tearoff=0)
        model_menu.add_command(label="Run Text-to-speech", command=self.run_model1)
        model_menu.add_command(label="Run Image to Text", command=self.run_model2)
        menu_bar.add_cascade(label="Models", menu=model_menu)

        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(
            label="About",
            command=lambda: messagebox.showinfo(
                "About", "Tkinter AI GUI\nFor Software Now Assignment 3"
            )
        )
        menu_bar.add_cascade(label="Help", menu=help_menu)

    # -------------------- Main Widgets --------------------
    def create_widget(self):
        """Creates main GUI widgets:model selection, input,buttons,output,info"""
        # Model selection frame
        selection_frame = tk.LabelFrame(self, text="Model Selection")
        selection_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(selection_frame, text="Select Model").pack(side="left", padx=5)
        self.model_select = ttk.Combobox(selection_frame, values=["Text-to-speech", "Image-to-text"]) #combobox for model selection
        self.model_select.current(0)
        self.model_select.pack(side="left", padx=5)
        self.model_select.bind("<<ComboboxSelected>>", self.show_model_information)  #updating information when a model is selected

        # User input frame
        input_frame = tk.LabelFrame(self, text="User Input")
        input_frame.pack(fill="x", padx=11, pady=10)

        # Text input for Text-to-Speech
        tk.Label(input_frame, text="Enter text for Text-to-Speech::").pack(anchor="w")
        self.text_input = tk.Entry(input_frame, width=60)
        self.text_input.pack(pady=5)

        # Image upload for Image-to-text
        tk.Label(input_frame, text="Upload Image for Captioning:").pack(anchor="w")
        tk.Button(input_frame, text="Browse", command=self.upload_files).pack(pady=5)

        # Buttons to run models
        button_frame = tk.Frame(input_frame)
        button_frame.pack(fill="x", pady=5)
        tk.Button(button_frame, text="Run Model 1", command=self.run_model1).pack(side="left", padx=5)
        tk.Button(button_frame, text="Run Model 2", command=self.run_model2).pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_output).pack(side="left", padx=5)

        # Model output frame
        output_frame = tk.LabelFrame(self, text="Model Output Section")
        output_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        self.output_text = tk.Text(output_frame, height=15, width=60)
        self.output_text.pack(pady=10)

        # Model information frame
        information_frame = tk.LabelFrame(self, text="Model Information")
        information_frame.pack(fill="both", expand=True, padx=10, pady=10)
        #Columns Label
        tk.Label(information_frame, text="Selected Model Information:").grid(row=0, column=0, sticky="w")
        tk.Label(information_frame, text="Object Oriented Concepts:").grid(row=0, column=1, sticky="w")
         #Information Text Boxes
        self.model_information_text = tk.Text(information_frame, height=10, width=40, fg="blue")
        self.model_information_text.grid(row=1, column=0, padx=5, pady=5)

        self.oop_information_text = tk.Text(information_frame, height=10, width=50)
        self.oop_information_text.grid(row=1, column=1, padx=5, pady=5)

        # Display initial info
        self.show_model_information()
        self.show_oop_information()

    # -------------------- File Upload --------------------
    def upload_files(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.input_file = file_path
            messagebox.showinfo("Image selected", f"File: {file_path}")

    # -------------------- Utility Functions --------------------
    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    # -------------------- Run Models --------------------
    @log_time
    def run_model1(self):
        """Run Text-to-Speech model"""
        enter_text = self.text_input.get()
        if not enter_text:         #If text is empty,shows error
            messagebox.showerror("Error", "Please enter text to convert")
            return
        result = self.model1.process_input(enter_text)
        self.output_text.insert(tk.END, f"\nModel 1 Output: {result}\n")   #show result

    @log_time
    def run_model2(self):
        """Run Image-to-Text model"""
        try:
            result = self.model2.process_input(self.input_file)
            self.output_text.insert(tk.END, f"\nModel 2 Output: {result}\n")
        except AttributeError:
            messagebox.showerror("Error", "Please upload an image")  #IF image is not uploaded/upload fail

    # -------------------- Display Model Info --------------------
    def show_model_information(self, event=None):
        selected = self.model_select.get()
        information = model_information()  # from utils.py
        self.model_information_text.delete(1.0, tk.END) #clears old information

        if selected == "Text-to-speech":
            self.model_information_text.insert(
                tk.END,
                f"{selected}\n"
                f"Model Name: facebook/mms-tts-eng\n"
                f"Category: Speech Generation\n"
                f"Description: {information['Text-to-Speech']}\n"
            )
        elif selected == "Image-to-text":
            self.model_information_text.insert(
                tk.END,
                f"{selected}\n"
                f"Model Name: Salesforce/blip-image-captioning-large\n"
                f"Category: Vision (Image Captioning)\n"
                f"Description: {information['Image-to-Text']}\n"
            )

    def show_oop_information(self):
        """Show OOP concepts used in the project"""
        oop_expl = (
            "- Multiple Inheritance: Through AIApp from Tkinter Tk\n"
            "- Encapsulation: BaseModel\n"
            "- Polymorphism: Method Overriding\n"
            "- Decorator: log_time"
        )
        self.oop_information_text.insert(tk.END, oop_expl)


