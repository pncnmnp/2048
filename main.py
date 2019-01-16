import tkinter as tk
# board = [[0] * 4] * 4
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
root = tk.Tk()
for i in range(len(board)):
	for j in range(len(board)):
		tk.Label(root,text=board[i][j],height=5,width=10,borderwidth=2,relief="ridge").grid(row=i,column=j)
root.mainloop()