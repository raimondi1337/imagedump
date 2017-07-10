import tkinter as tk
from tkinter import filedialog

class ImageDump(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		def get_source_directory(self):
			directory = filedialog.askdirectory()
			self.source_directory.set(directory)

		self.source_directory = tk.StringVar()
		self.source_directory.set('/')
		dir_box_label = tk.Label(self,text='Base Directory:').pack(side='left')
		dir_box = tk.Entry(self, textvariable=self.source_directory).pack(side='left')
		browse_button = tk.Button(self, text='Browse',command=lambda:get_source_directory(self)).pack(side='left')


if __name__ == "__main__":
	root = tk.Tk()
	ImageDump(root).pack(side="top", fill="both", expand=True)
	root.mainloop()