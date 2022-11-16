import numpy as np
import tkinter as tk
from tkinter import ttk
from astropy.coordinates import EarthLocation
from astropy import units as u

from Utilities.locations_frame import Location_frame

class Main_frame(ttk.Frame):
    def __init__(self, container, style=None):  
        super().__init__(container, style=style)   
        self.container = container
        self.styles()
        self.widgets()

    def styles(self):
        self.style = ttk.Style()
        self.style.configure('Label1.TLabel', font=('courier', 15, 'bold'), background='#2b3c46', foreground="white")  
        self.style.configure('TButton', background='#fffade', font=('courier', 15, 'bold'))
        self.style.configure('Label2.TLabel', font=('courier', 20, 'bold'), background='#2b3c46', foreground="white") 
        self.style.configure('TFrame', background='#2b3c46')

    def widgets(self):
        self.location = Location_frame(self,'Ubicación')
        self.location.pack(padx=50, pady=50, anchor='nw')

        self.enter_button = ttk.Button(self, text = "Enter", style='TButton', command= self.request_location)
        self.enter_button.pack(padx = 15, pady = 15, anchor='nw', ipadx=15, ipady=15)

        self.transform_button = ttk.Button(self, text = "Transform", style='TButton', command= self.transform_coodinates)
        self.transform_button.pack(padx = 15, pady = 15, anchor='nw', ipadx=15, ipady=15)

        self.selected_coodinate_tr = tk.StringVar()
        self.transformation = ttk.Combobox(self, textvariable=self.selected_coodinate_tr)
        self.transformation['values'] = ('Geodetic', 'Geocentric')
        self.transformation['state'] = 'readonly'
        self.transformation.pack(padx = 15, pady = 15, anchor='nw')

        self.coodinateText = tk.StringVar()
        self.coodinateText.set('...')
        self.coodinateLabel = ttk.Label(self, textvariable = self.coodinateText, style='Label1.TLabel')
        self.coodinateLabel.pack(padx = 10, pady = 10, anchor='s')

        self.transformText = tk.StringVar()
        self.transformText.set('...')
        self.transformLabel = ttk.Label(self, textvariable = self.transformText, style='Label1.TLabel')
        self.transformLabel.pack(padx = 10, pady = 10, anchor='s')

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