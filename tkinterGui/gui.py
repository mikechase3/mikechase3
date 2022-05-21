"""
Docstring
"""


class GUI:
	"""
	Tkinter Application
	"""

	# Instance Vars

	def __init__(self, t):
		import tkinter as tk

		root = tk.Tk()
		root.title(t)
		name = tk.Label(root, text="Mike Chase")
		name.grid(row=10, column=10)
		root.mainloop()
		print("Done")

	def f(self):
		"""
		Literally just exist.
		:return: nothing
		:rtype:
		"""

		return "hello world"

