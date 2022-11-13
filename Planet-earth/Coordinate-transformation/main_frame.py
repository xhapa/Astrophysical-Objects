import numpy as np
import tkinter as tk
from tkinter import ttk
from astropy.coordinates import EarthLocation
from astropy import units as u

from Utilities.locations_frame import Location_frame

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
        self.location = Location_frame(self,'Location')
        self.location.pack(side=tk.LEFT)

        self.enter_button = ttk.Button(self, text = "Enter", style='TLabel', command= self.request_location)
        self.enter_button.pack(side=tk.LEFT, padx = 10, pady = 10, anchor='s')

        self.transform_button = ttk.Button(self, text = "Transform", style='TLabel', command= self.transform_coodinates)
        self.transform_button.pack(side=tk.LEFT, padx = 10, pady = 10, anchor='s')

        self.selected_coodinate_tr = tk.StringVar()
        self.transformation = ttk.Combobox(self, textvariable=self.selected_coodinate_tr)
        self.transformation['values'] = ('Geodetic', 'Geocentric')
        self.transformation['state'] = 'readonly'
        self.transformation.pack(side=tk.TOP, padx = 10, pady = 10, anchor='s')

        self.coodinateText = tk.StringVar()
        self.coodinateLabel = ttk.Label(self, textvariable = self.coodinateText)
        self.coodinateLabel.pack(side=tk.BOTTOM, padx = 10, pady = 10, anchor='s')

        self.transformText = tk.StringVar()
        self.transformLabel = ttk.Label(self, textvariable = self.transformText)
        self.transformLabel.pack(side=tk.BOTTOM, padx = 10, pady = 10, anchor='s')

        self.transformation.current()

    def request_location(self):
        if self.location.location!='':
            if self.selected_coodinate_tr.get() == 'Geocentric':
                self.point = EarthLocation.of_address(self.location.location)
                self.coodinateText.set(f'X: {self.point.geocentric[0]}  Y: {self.point.geocentric[1]}  Z:{self.point.geocentric[2]}')
            elif self.selected_coodinate_tr.get() == 'Geodetic':
                self.point = EarthLocation.of_address(self.location.location)
                self.coodinateText.set(f'Latitud: {self.point.geodetic.lat}  Longuitud: {self.point.geodetic.lon}')
        else:
            if self.selected_coodinate_tr.get() == 'Geocentric':
                self.point = EarthLocation.of_address('Bogota')
                self.coodinateText.set(f'X: {self.point.geocentric[0]}  Y: {self.point.geocentric[1]}  Z:{self.point.geocentric[2]}')
            elif self.selected_coodinate_tr.get() == 'Geodetic':
                self.point = EarthLocation.of_address('Bogota')
                self.coodinateText.set(f'Latitud: {self.point.geodetic.lat}  Longuitud: {self.point.geodetic.lon}')
                
    def transform_coodinates(self):
        if self.selected_coodinate_tr.get() == 'Geocentric':
            point = self.point.to_geodetic()
            self.transformText.set(f'Latitud: {point.lat}  Longuitud: {point.lon}')
        elif self.selected_coodinate_tr.get() == 'Geodetic':
            point = self.point.to_geocentric()
            self.transformText.set(f'X: {point[0]}  Y: {point[1]}  Z:{point[2]}')