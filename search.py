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
	path = []
	current = ()
	current = maze.getStart()
	row,col = current
	path.append(current)
	a = maze.getNeighbors(row,col)
	path.append(a[0])
	i = 1
	while ( (i < 10) and (not maze.isObjective(row,col))):
		current = maze.getNeighbors(row,col)
		row,col = current[0]
		path.append(current[0])
		i = i + 1

	return path
