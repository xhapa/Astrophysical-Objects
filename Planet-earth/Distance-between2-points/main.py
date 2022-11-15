import tkinter as tk
from tkinter import ttk

from main_frame import Main_frame

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Distance between two points')
		self.attributes('-fullscreen', True)
		self.configure(background='#dfd5e5')
		self.style = ttk.Style()
		self.style.configure('TFrame', background='#dfd5e5')
		#self.geometry("700x500")	

		main_frame = Main_frame(self, style='TFrame')
		main_frame.pack(side=tk.TOP, pady=10)

def main():
	app = App()
	app.mainloop()

if __name__=='__main__':
    main()