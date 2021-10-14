import numpy as np
from math import sqrt

class Point:
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    
    def distance_to_center(self,center):
        return sqrt((center.x-self.x)**2 + (center.y-self.y)**2)
    def __str__(self):
        return 'P({:.2f}, {:.2f})'.format(self.x, self.y)

class Rectangle:
    def __init__(self,center,width,height):
        self.center = center
        self.width =  width
        self.height =  height
        self.west =  center.x -  width
        self.east =  width + center.x
        self.north = center.y - height
        self.south = height + center.y

    def contains_point(self,point):
        return self.west <= point.x  < self.east and self.north <= point.y <  self.south

    def intersects(self,region):
        return not (
            region.west > self.east or
            region.north > self.south or 
            region.east < self.west or 
            region.south < self.north 
        )

    def draw(self,ax,c="k",lw=1,**kwargs):
        x1,y1 = self.west , self.north
        x2,y2 = self.east,self.south  
        ax.plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1],c=c,lw=lw,**kwargs) 
    




class QuadTree:
    def __init__(self,boundary,capacity=4):
        self.boundary = boundary
        self.capacity =  capacity
        self.points = []
        self.divided = False 

    def divide_tree(self):
        center_x =  self.boundary.center.x
        center_y = self.boundary.center.y
        new_height = self.boundary.height/2
        new_width = self.boundary.width/2

        nw_rectangle = Rectangle(
            Point(
                center_x-new_width,
                center_y-new_height
            ),
            new_width,
            new_height
        ) 

        self.nw = QuadTree(nw_rectangle)

        ne_rectangle = Rectangle(
            Point(
                center_x + new_width,
                center_y - new_height
            ),
            new_width,
            new_height
        )
        self.ne = QuadTree(ne_rectangle )


        sw_rectangle = Rectangle(
            Point(
                center_x - new_width,
                center_y + new_height 
            ),
            new_width,
            new_height
        )
        self.sw = QuadTree(sw_rectangle )

        se_rectangle = Rectangle(
            Point(
                center_x + new_width,
                center_y + new_height
            ),
            new_width,
            new_height
        )

        self.se = QuadTree(se_rectangle)

    def insert(self,point):
        #if point is not within the range of the rectangle ignore it
        if not self.boundary.contains_point(point):
            return False

        #if the current children is not filled up
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.divided:
            self.divide_tree()
            self.divided = True

        return (self.se.insert(point)  or self.ne.insert(point) 
                    or self.sw.insert(point) or self.nw.insert(point))

    def query_region(self,region):
        found_points = []

        if not self.boundary.intersects(region):
            return []
        
        for point in self.points:
            if region.contains_point(point):
                found_points.append(point)
        
        if self.divided:
            found_points.extend(self.nw.query_region(region))
            found_points.extend(self.ne.query_region(region))
            found_points.extend(self.se.query_region(region))
            found_points.extend(self.sw.query_region(region))
        
        return found_points

    def query_radius(self,region,center):
        found_points = []

        if not self.boundary.intersects(region):
            return []
        
        for point in self.points:
            if region.contains_point(point) and point.distance_to_center(center) <= region.width:
                found_points.append(point)
        
        if self.divided:
            found_points.extend(self.nw.query_radius(region,center))
            found_points.extend(self.ne.query_radius(region,center))
            found_points.extend(self.se.query_radius(region,center))
            found_points.extend(self.sw.query_radius(region,center))
        
        return found_points

    def __len__(self):
        current_count = len(self.points)
        if self.divided:
            current_count += len(self.ne) + len(self.nw) + len(self.se) + len(self.sw)
        return current_count

    def draw(self,ax):
        self.boundary.draw(ax)
        if self.divided:
            self.ne.draw(ax)
            self.nw.draw(ax)
            self.se.draw(ax)
            self.sw.draw(ax)