from tkinter import CURRENT
from typing import List
from enum import Enum

class Direction(Enum):
    GO_UP = 1
    GO_DOWN = 2     
    GO_RIGHT = 3
    GO_LEFT = 4

def out_of_bound(x:int, y:int, matrix: List[List[int]]):
    return True if x < 0  and  x > len(matrix)-1 or y < 0  and  y > len(matrix)-1 else False


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix):
            return []
        x,y,result = 0, 0 , []
        DONE = False
        current_direction = Direction.GO_RIGHT

        while DONE != True :
            if current_direction == Direction.GO_RIGHT and not out_of_bound(x,y,matrix):
                if matrix[x][y] != 'X':
                    result.append(matrix[x][y])
                    matrix[x][y] = 'X'
                y+=1
                continue
            elif current_direction == Direction.GO_RIGHT and   (out_of_bound(x,y,matrix) or matrix[x][y] == 'X'):
                current_direction = Direction.GO_DOWN
                x+=1
                y-=1
                continue
            if current_direction == Direction.GO_DOWN and not out_of_bound(x,y,matrix):
                if matrix[x][y] != 'X':
                    result.append(matrix[x][y])
                    matrix[x][y] = 'X'
                x+=1
                continue
            elif current_direction == Direction.GO_DOWN and   (out_of_bound(x,y,matrix) or matrix[x][y] == 'X'):
                current_direction = Direction.GO_LEFT
                x-=1
                y-=1
                continue

            if current_direction == Direction.GO_LEFT and not out_of_bound(x,y,matrix):
                if matrix[x][y] != 'X':
                    result.append(matrix[x][y])
                    matrix[x][y] = 'X'
                y-=1
                continue
            elif current_direction == Direction.GO_LEFT and   (out_of_bound(x,y,matrix) or matrix[x][y] == 'X'):
                current_direction = Direction.GO_UP
                y+=1
                x-=1
                continue
            if current_direction == Direction.GO_UP and not out_of_bound(x,y,matrix):
                if matrix[x][y] != 'X':
                    result.append(matrix[x][y])
                    matrix[x][y] = 'X'
                x+=1
                continue
            elif current_direction == Direction.GO_UP and  (out_of_bound(x,y,matrix) or matrix[x][y] == 'X'):
                current_direction = Direction.GO_LEFT
                x-=1
                y-=1
        pass