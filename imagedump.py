import PIL
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

class ImageDump():
	# initilize program
	def __init__(self):
		# Data
		self.root = tk.Tk()
		self.source_directory = tk.StringVar()

		# Build UI
		self.browseLabel  = tk.Label( self.root,text='Base Directory:').pack(side='left')
		self.browseEntry  = tk.Entry( self.root, textvariable=self.source_directory).pack(side='left')
		self.browseButton = tk.Button(self.root, text='Browse', command=self.browse).pack(side='left')

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