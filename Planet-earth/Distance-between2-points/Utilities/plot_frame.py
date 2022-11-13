import tkinter as tk
from tkinter import ttk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import geopandas as gpd

class Plot_frame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.styles()
        self.widgets()
    
    def styles(self):
        pass

    def widgets(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().pack(ipadx=20, ipady=20, expand=False, side=tk.TOP, anchor='center')
        self.canvas.draw()
    
    def plot_point_world_map(self, point_a, point_b):
        plt.cla()      
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        x = np.array([point_a.lon.value, point_b.lon.value])
        y = np.array([point_a.lat.value, point_b.lat.value])
        world.plot(color="lightgrey", ax=self.ax)
        plt.plot(x, y,'o-')
        plt.xlim([-180, 180])
        plt.ylim([-90, 90])         