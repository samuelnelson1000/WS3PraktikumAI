# search.py
# ---------------
# Created by Yaya Wihardi (yayawihardi@upi.edu) on 15/03/2020

# Fungsi search harus me-return path.
# Path berupa list tuples dengan format (row, col) 
# Path merupakan urutan states menuju goal.
# maze merupakan object dari Maze yang merepresentasikan keadaan lingkungan 
# beberapa method dari maze yang dapat digunakan:

# getStart() : return tuple (row, col) -> mendapatkan initial state
# getObjectives() : return list of tuple [(row1, col1), (row2, col2) ...] -> mendapatkan list goal state
# getNeighbors(row, col) : input posisi, return list of tuple [(row1, col1), (row2, col2) ...]
#                          -> mendapatkan list tetangga yg mungkin (expand/sucessor functiom)
# isObjective(row, col) : return true/false -> goal test function

import queue

def search(maze):
	fringe = queue.Queue()
	fringe.put(maze.getStart())
	explored = []
	parent = {}
	i = 0
	while (i < 20) and (not fringe.empty()):
		current = fringe.get()
		explored.append(current)
		row,col = current
		if maze.isObjective(row,col):
			return (parent)
		#lakukan ekspansi
		expand = maze.getNeighbors(row,col)
		for child in expand:
			if maze.isValidMove(child[0],child[1]):
				fringe.put(child)
				parent[child] = current
		i = i + 1		

	return parent
