import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image 

from main_frame import Main_frame

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title('Distance between two points')
		self.attributes('-fullscreen', True)

		self.style = ttk.Style()
		self.style.configure('Label2.TLabel', font=('courier', 20, 'bold'), background='#dfd5e5', foreground="white") 
		self.style.configure('TFrame', background='#d4e8b9')
		img = Image.open('Planet-earth/Distance-between2-points/background.png')
		self.bg = ImageTk.PhotoImage(img)
		self.background_label = tk.Label(self, image=self.bg)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		#self.geometry("700x500")	

		main_frame = Main_frame(self.background_label, style='TFrame')
		main_frame.pack(side=tk.TOP, pady=10)

def main():
	app = App()
	app.mainloop()

if __name__=='__main__':
    main()