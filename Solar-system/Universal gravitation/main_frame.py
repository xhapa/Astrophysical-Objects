import numpy as np
import tkinter as tk
from tkinter import ttk

class Main_frame(ttk.Frame):
    def __init__(self, container):  
        super().__init__(container, width = 1000, height = 70)   
        self.container = container
        self.styles()
        self.widgets()

    def styles(self):
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 10))  

    def widgets(self):
        pass