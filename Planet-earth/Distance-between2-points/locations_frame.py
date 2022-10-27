import tkinter as tk
from tkinter import ttk

class Location_frame(ttk.Frame):
    def __init__(self, container, label_text):
        super().__init__(container)

        self.location_label = ttk.Label(self, text=label_text)
        self.location_label.pack(side=tk.LEFT, padx = 10, pady = 10, anchor='s')

        self.__location = ttk.Entry(self)
        self.__location.pack(side=tk.LEFT, padx = 10, pady = 10, anchor='s')
    
    @property
    def location(self):
        return self.__location.get()
