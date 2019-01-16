import tkinter as tk
import random
# board = [[0] * 4] * 4
class Main:
	board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	root = tk.Tk()
	def display(self):
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				tk.Label(self.root,text=self.board[i][j],height=5,width=10,borderwidth=2,relief="ridge").grid(row=i,column=j)
		self.root.update()
	def spawn(self):
		num = random.choice([2,4,8])		
		ind = lambda : random.randint(0,len(self.board)-1)
		# TODO: Replace while True with something clever like choosing from all zeroed squares
		while True:
			if self.board[ind()][ind()] == 0:
				self.board[ind()][ind()] = num
				break
m = Main()
m.display()
m.spawn()
m.display()
m.root.mainloop()