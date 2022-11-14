import tkinter as tk
from tkinter import ttk
import numpy as np
from itertools import combinations
import math

from main_frame import Main_frame
from body import Body

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Universal gravitation')
		self.attributes('-fullscreen', True)
		#self.geometry("700x500")	

		self.constants()
		self.init_bodies()
		self.center_of_mass()

		main_frame = Main_frame(self)
		main_frame.pack()

		self.canvas = tk.Canvas(self, width=1400, height=800, bg="black")
		self.canvas.pack()	

		self.update_screen()
		self.gameon()

	def constants(self):
		self.bodies = []
		self.sun_mass = 1.98892 * 10**30
		self.sun_size = 12
		self.sun_r = np.array([0, 0], dtype=float)
		self.sun_v = np.array([0, 0], dtype=float)

		sun = Body(self.sun_mass, self.sun_size, self.sun_r, self.sun_v,'Sun', 'Yellow', True)
		self.bodies.append(sun)

	def init_bodies(self):
		masses = [5.9742 * 10**24, 6.39 * 10**23 , 3.30 * 10**23, 4.8685 * 10**24] 
		vels = [29.783 * 1000, 24.077 * 1000, -47.4 * 1000, -35.02 * 1000]
		dis = [-1, -1.524, 0.387, 0.723]
		for i, elem in enumerate(list(zip(masses, vels, dis))):
			body = Body(elem[0], 8, np.array([elem[2]*Body.AU, 0], dtype=float), np.array([0, elem[1]], dtype=float),f'P{i+1}', 'White')
			self.bodies.append(body)
		
	def center_of_mass(self):
		m_total = 0
		m_pos = np.zeros((2,), dtype=float)
		for body in self.bodies:
			m_total+=body.mass
			m_pos+=body.mass*body.pos

		self.rcm = m_pos/m_total
	
	def update_screen(self):
		for body in self.bodies:
			body.update_position(self.bodies)
			body.draw(self.canvas, self)

	def gameon(self): #runs the physics in a loop until told to stop 
		self.title("Calculating...")
		i = 0
		gamestate = 1
		while gamestate == 1:
			i += 1
			self.update_screen()

def main():
	app = App()
	app.mainloop()

if __name__=='__main__':
    main()