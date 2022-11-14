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
		#self.gameon()

	def constants(self):
		self.bodies = []
		self.G = 1000.0
		self.sun_mass = 50.0
		self.sun_size = 12
		self.sun_r = np.array([700, 330])
		self.sun_v = np.array([0, 0])
		self.sun_a = np.array([0, 0])

		sun = Body(self.sun_mass, self.sun_size, self.sun_r, self.sun_v, self.sun_a,'Sun', 'Yellow', True)
		self.bodies.append(sun)

	def init_bodies(self):
		for i in range(8):
			body = Body(1.0, 8, np.array([750+50*i, 330]), np.array([0, (-3)**(i+1)]), np.array([0,0]), f'P{i+1}', 'White')
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
			body.draw(self.canvas, self)

	# def gameon(self): #runs the physics in a loop until told to stop 
	# 	self.title("Calculating...")
	# 	i = 0
	# 	gamestate = 1
	# 	while gamestate == 1:
	# 		i += 1
	# 		self.calculate_trajectories()
	# 		self.updatescreen()

def main():
	app = App()
	app.mainloop()

if __name__=='__main__':
    main()