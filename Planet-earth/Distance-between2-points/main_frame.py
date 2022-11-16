import numpy as np
import tkinter as tk
from tkinter import ttk
from astropy.coordinates import EarthLocation
from astropy import units as u

from Utilities.locations_frame import Location_frame
from Utilities.plot_frame import Plot_frame

class Main_frame(ttk.Frame):
    def __init__(self, container, style=None):  
        super().__init__(container, style= style)   
        self.container = container
        self.styles()
        self.widgets()

    def styles(self):
        self.style = ttk.Style()
        self.style.configure('Label1.TLabel', font=('courier', 15, 'bold'), background='#d4e8b9')  
        self.style.configure('TButton', background='#f4fcfb', font=('courier', 15, 'bold'))
        self.style.configure('Label2.TLabel', font=('courier', 20, 'bold'), background='#d4e8b9', foreground='black') 

    def widgets(self):
        self.title_label = ttk.Label(self, text='¿Qué tan lejos estamos?', style='Label2.TLabel')
        self.title_label.pack(side=tk.TOP, anchor='n', pady=25)
        
        self.plot_frame = Plot_frame(self.container)
        self.plot_frame.pack(side=tk.BOTTOM, padx=20, pady=20)

        self.distance_label = ttk.Label(self, text='La distancia entre ...', style='Label1.TLabel')
        self.distance_label.pack(side=tk.BOTTOM, ipadx = 10, ipady = 10, anchor='s')    

        self.location_a = Location_frame(self,'Primera Ubicación')
        self.location_a.pack(side=tk.LEFT, padx=10)
        self.location_b = Location_frame(self,'Segunda Ubicación')
        self.location_b.pack(side=tk.LEFT, padx=10)

        self.enter_button = ttk.Button(self, text = "Enter", style='TButton', command=self.request_locations)
        self.enter_button.pack(side=tk.LEFT, padx = 5, pady = 5, anchor='s', ipadx=30, ipady=15)

        self.calculate_button = ttk.Button(self, text = "Calcular", style='TButton', command=self.distance_between_2points)
        self.calculate_button.pack(side=tk.LEFT, padx = 5, pady = 5, anchor='s', ipadx=30, ipady=15)

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
        self.distance_label.config(text=f'La distancia entre {self.location_a.location} y {self.location_b.location} es de {self.distance}')