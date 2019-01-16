import tkinter as tk
import random, time


# board = [[0] * 4] * 4
class Main:
	board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	root = tk.Tk()
	def key(self,event):
		print("Pressed",event.keysym)
	def wait_for_move(self):
		self.root.bind("<Up>",self.key)
		self.root.bind("<Down>",self.key)
		self.root.bind("<Left>",self.key)
		self.root.bind("<Right>",self.key)
	def display(self):
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				tk.Label(
				    self.root,
				    text=self.board[i][j],
				    height=5,
				    width=10,
				    borderwidth=2,
				    relief="ridge").grid(
				        row=i, column=j)
		self.root.update()

	def spawn(self):
		'''
			Randomly sets a single zero element in board to 2,4 or 8
		'''
		num = random.choice([2, 4, 8])
		index = [(i, j) for i in range(len(self.board))
		         for j in range(len(self.board))
		         ]  # Generate all possible rows and columns
		index = list(filter(lambda x: not self.board[x[0]][x[1]],
		                    index))  # Filter out non zero rows
		if len(index) > 0:
			index = random.choice(index)
			self.board[index[0]][index[1]] = num
		else:
			# Board is full
			pass


m = Main()
m.spawn()
m.display()
m.wait_for_move()
m.root.mainloop()