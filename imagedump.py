from PIL import Image, ImageTk
import tkinter as tk
from pprint import pprint

class ImageDump():

	# initilize program
	def __init__(self):

		# Data
		self.root = tk.Tk()
		x = self.root.winfo_screenwidth()
		y =	self.root.winfo_screenheight()
		self.root.geometry('{}x{}+{}+{}'.format(int(x/2),int(y/2),int(x/4),int(y/4)))
		self.source_directory = tk.StringVar()
		self.imageIndex = 0

		# Placeholder list of images
		self.images = []
		self.images.append(Image.open('cat1.jpeg').convert("RGB"))
		self.images.append(Image.open('cat2.jpeg').convert("RGB"))
		self.images.append(Image.open('cat3.jpeg').convert("RGB"))

		# Build listbox
		self.listbox = tk.Listbox(self.root)
		self.listbox.pack(fill="y", side='left')

		# remove click listeners from listbox to prevent user clicking for now
		self.listbox.bindtags((self.listbox, self.root, 'all'))

		for item in self.images:
			self.listbox.insert('end', item)

		# Build image canvas
		self.canvas = tk.Canvas(self.root,bg='grey',highlightthickness=0)
		self.currentImage = ImageTk.PhotoImage(self.images[self.imageIndex])

		w,h = self.canvas.winfo_width(),self.canvas.winfo_height()
		iw,ih = self.images[self.imageIndex].size

		self.canvasImage = self.canvas.create_image(w/2-iw/2,h/2-ih/2,image=self.currentImage,anchor='nw',tags="IMG")
		self.canvas.pack(fill="both", expand=True)
		self.canvas.bind('<Configure>', self.resize)

		# Build directory picker
		self.nextButton = tk.Button(self.root, text='Next', command=self.next).pack(side='bottom')

	# scale images to fit canvas
	def resize(self,event):

		# maths to find proper image size while maintaining aspect ratio
		w,h = event.width,event.height
		iw,ih = self.images[self.imageIndex].size
		ratio = min((w/iw),(h/ih))
		fitSize = (int(iw*ratio),int(ih*ratio))

		# remove and replace resized image
		if (iw > w or ih > h):
			image = self.images[self.imageIndex].resize(fitSize,Image.BILINEAR)
		else:
			image = self.images[self.imageIndex]

		# replace image
		self.currentImage = ImageTk.PhotoImage(image)
		self.canvas.delete(self.canvasImage)
		self.canvas.create_image(w/2,h/2,image=self.currentImage,tags="IMG")

	# switch to next image
	def next(self):
		# update current image
		self.imageIndex = self.imageIndex + 1 if self.imageIndex + 1 < len(self.images) else 0
		self.currentImage = ImageTk.PhotoImage(self.images[self.imageIndex])

		# handle listbox selection
		self.listbox.selection_clear(0,'end')
		self.listbox.selection_set(self.imageIndex)
		self.listbox.activate(self.imageIndex)

		# replace image
		w,h = self.canvas.winfo_width(),self.canvas.winfo_height()
		iw,ih = self.images[self.imageIndex].size
		self.canvasImage = self.canvas.create_image(w/2-iw/2,h/2-ih/2,image=self.currentImage,anchor='nw',tags="IMG")

	# start gui
	def run(self):
		self.root.title("ImageDump")
		self.root.deiconify()
		self.root.mainloop()

# that thing you do in python
if __name__ == "__main__":
	i = ImageDump()
	i.run()