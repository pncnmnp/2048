import tkinter as tk
import random, time


# board = [[0] * 4] * 4
class Main:
	def __init__(self):
		self.board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		self.root = tk.Tk()
		self.root.bind("<KeyPress>", self.key)

	@staticmethod
	def perform_move(l):
		for i in range(len(l)):
			if l[i] == 0:
				del l[i]
				l.insert(0, 0)
		if l.count(0) >= 3:
			return l
		n = l[1:]
		for i in range(len(l) - 1):
			if l[i] == n[i]:
				l[i] *= 2
				l[i + 1] = 0
		for i in range(len(l)):
			if l[i] == 0:
				del l[i]
				l.insert(0, 0)
		return l

	def key(self, event):
		if event.keysym == "Right":
			self.board = list(map(self.perform_move, self.board))

		if event.keysym == "Left":
			self.board = list(
			    map(lambda x: self.perform_move(x[::-1])[::-1], self.board))
		if event.keysym == "Up":
			transpose = lambda l_of_l:[list(l) for l in zip(*l_of_l)]
			self.board = list(map(lambda x: self.perform_move(x[::-1])[::-1],transpose(self.board)))
			self.board = transpose(self.board)

		if event.keysym == "Down":
			transpose = lambda l_of_l:[list(l) for l in zip(*l_of_l)]
			self.board = list(map(self.perform_move,transpose(self.board)))
			self.board = transpose(self.board)
		self.display()

	def display(self):
		self.spawn()
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
m.display()
m.root.mainloop()