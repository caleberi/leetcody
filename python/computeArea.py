class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_1 = (ay2-ay1)*(ax2-ax1)
        area_2 = (by2-by1)*(bx2-bx1)
        
        x_i = (min(bx2,ax2)-max(ax1,bx1))
        y_i = (min(by2,ay2)-max(ay1,by1))
        
        intersect = ( x_i * y_i )
        if bx1 >= ax2 or ax1 >= bx2 or by1 >= ay2  or ay1 >= by2:
            intersect = 0
        return (area_1+area_2) - intersect