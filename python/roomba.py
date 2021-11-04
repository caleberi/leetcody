"""
A Roomba robot is currently sitting in a Cartesian plane at (0, 0). 
You are given a list of its moves that it will make, containing NORTH, SOUTH, WEST, and EAST.

Return whether after its moves it will end up in the coordinate (x, y).

Constraints

n ≤ 100,000 where n is length of moves

"""

class Solution:
    def solve(self, moves, x, y):
        direction ={
            "NORTH":(0,1),
            "SOUTH":(0,-1),
            "EAST":(1,0),
            "WEST":(-1,0)
        }
        start=(0,0)
        for move in moves:
            _x,_y=direction[move]
            start_x,start_y=start
            start=(start_x+_x,start_y+_y)
        return start[0]==x and start[1]==y
