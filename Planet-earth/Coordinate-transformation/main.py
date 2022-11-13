import tkinter as tk
from tkinter import ttk

from main_frame import Main_frame

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Distance between two points')
		self.attributes('-fullscreen', True)
		#self.geometry("700x500")	

		main_frame = Main_frame(self)
		main_frame.pack(side=tk.BOTTOM, pady=40, padx=40)

def main():
	app = App()
	app.mainloop()

if __name__=='__main__':
    main()