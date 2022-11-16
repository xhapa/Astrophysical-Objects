import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  

from main_frame import Main_frame

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Coodinate transformation')
		self.attributes('-fullscreen', True)
		#self.configure(background='#dfd5e5')
		self.style = ttk.Style()
		self.style.configure('Label2.TLabel', font=('courier', 20, 'bold'), background='#dfd5e5', foreground="white") 
		self.style.configure('TFrame', background='#2b3c46')
		img = Image.open('/home/xhapa/Documents/PROGRAMMING/Projects/Astrophysical-Objects/Planet-earth/Coordinate-transformation/background.png')
		self.bg = ImageTk.PhotoImage(img)
		self.background_label = tk.Label(self, image=self.bg)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

		#self.geometry("700x500")	

		self.title_label = ttk.Label(self.background_label, text='Ubiquemonos', style='Label2.TLabel')
		self.title_label.pack(side=tk.TOP, anchor='n', pady=25)

		main_frame = Main_frame(self.background_label, style='TFrame') #style='TFrame')
		main_frame.pack(side=tk.LEFT, pady=100, padx=50, anchor='nw')

def main():
	app = App()
	app.mainloop()

if __name__=='__main__':
    main()