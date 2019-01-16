import tkinter as tk
# board = [[0] * 4] * 4
class Main:
	board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	root = tk.Tk()
	def display(self):
		for i in range(len(self.board)):
			for j in range(len(self.board)):
				tk.Label(self.root,text=self.board[i][j],height=5,width=10,borderwidth=2,relief="ridge").grid(row=i,column=j)
		self.root.mainloop()
m = Main()
m.display()