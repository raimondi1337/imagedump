import PIL
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImageDump():

	# initilize program
	def __init__(self):

		# Data
		self.root = tk.Tk()
		x = self.root.winfo_screenwidth()
		y =	self.root.winfo_screenheight()
		self.root.geometry('{}x{}+{}+{}'.format(int(x/2),int(y/2),int(x/4),int(y/4)))
		self.source_directory = tk.StringVar()

		# Build image canvas
		self.canvas = tk.Canvas(self.root,bg='grey',highlightthickness=0)
		self.original = Image.open('Drawing.png').convert("RGB")
		self.image = ImageTk.PhotoImage(self.original)
		self.canvas.create_image(0,0,image=self.image,anchor='nw',tags="IMG")
		self.canvas.pack(fill="both", expand=True)
		self.canvas.bind('<Configure>', self.resize)

		# Build directory picker
		self.browseLabel  = tk.Label( self.root,text='Base Directory:').pack(side='left')
		self.browseEntry  = tk.Entry( self.root, textvariable=self.source_directory).pack(side='left',fill='x',expand=True)
		self.browseButton = tk.Button(self.root, text='Browse', command=self.browse).pack(side='left')

	# scale images to fit canvas
	def resize(self,event):

		# maths to find proper image size while maintaining aspect ratio
		w,h = event.width,event.height
		ow,oh = self.original.size
		ratio = min((w/ow),(h/oh))
		fitSize = (int(ow*ratio),int(oh*ratio))

		# remove and replace resized image
		self.image = self.original.resize(fitSize,Image.BILINEAR)
		self.image = ImageTk.PhotoImage(self.image)
		self.canvas.delete("IMG")
		self.canvas.create_image(w/2,h/2,image=self.image,tags="IMG")

	# get directory from user
	def browse(self):
		directory = filedialog.askdirectory()
		self.source_directory.set(directory)

	# start gui
	def run(self):
		self.root.title("ImageDump")
		self.root.deiconify()
		self.root.mainloop()


if __name__ == "__main__":
	i = ImageDump()
	i.run()