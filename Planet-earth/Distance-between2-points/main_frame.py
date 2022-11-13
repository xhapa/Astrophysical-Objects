import numpy as np
import tkinter as tk
from tkinter import ttk
from astropy.coordinates import EarthLocation
from astropy import units as u

from Utilities.locations_frame import Location_frame
from Utilities.plot_frame import Plot_frame

class Main_frame(ttk.Frame):
    def __init__(self, container):  
        super().__init__(container)   
        self.container = container
        self.styles()
        self.widgets()

    def styles(self):
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Helvetica', 10))  

    def widgets(self):
        self.plot_frame = Plot_frame(self.container)
        self.plot_frame.pack(side=tk.TOP, pady=20, padx=20)

        self.location_a = Location_frame(self,'First Location')
        self.location_a.pack(side=tk.LEFT)
        self.location_b = Location_frame(self,'Second Location')
        self.location_b.pack(side=tk.LEFT)

        self.enter_button = ttk.Button(self, text = "Enter", style='TLabel', command=self.request_locations)
        self.enter_button.pack(side=tk.LEFT, padx = 10, pady = 10, anchor='s')

        self.calculate_button = ttk.Button(self, text = "Calculate", style='TLabel', command=self.distance_between_2points)
        self.calculate_button.pack(side=tk.LEFT, padx = 10, pady = 10, anchor='s')

        self.distance_label = ttk.Label(self, text='Distance is')
        self.distance_label.pack(side=tk.TOP, padx = 10, pady = 10, anchor='s')

    def request_locations(self):
        if self.location_a.location!='' and self.location_b.location!='':
            self.point_a = EarthLocation.of_address(self.location_a.location)
            self.point_b = EarthLocation.of_address(self.location_b.location)
            self.plot_frame.plot_point_world_map(self.point_a, self.point_b)
        else:
            self.point_a = EarthLocation.of_address('Bogota')
            self.point_b = EarthLocation.of_address('Bogota')
            self.plot_frame.plot_point_world_map(self.point_a, self.point_b)

    def distance_between_2points(self):
        earth_radius = 6373 #km
        b, a = (90-self.point_a.lat.value)*np.pi/180, (90-self.point_b.lat.value)*np.pi/180
        C = (self.point_b.lon.value - self.point_a.lon.value)*np.pi/180
        x = (np.sin(a)*np.cos(C)*np.sin(b)) + (np.cos(a)*np.cos(b))
        angle = np.arccos(x)

        self.distance = earth_radius*angle*u.kilometer
        self.distance_label.config(text=f'Distance is {self.distance}')