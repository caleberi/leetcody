import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from quadtree import Point,Rectangle,QuadTree
import time

DPI = 72
np.random.seed(time.gmtime().tm_sec*200)

width, height = 600, 400

N = 1500
coords = np.random.randn(N, 2) * height/3 + (width/2, height/2)
points = [Point(*coord) for coord in coords]

domain = Rectangle(Point(width/2,height/2),width,height)
qtree  = QuadTree(domain,4)


for point in points:
    qtree.insert(point)

print('Number of points in the domain =', len(qtree))

fig = plt.figure(figsize=(700/DPI,500/DPI),dpi=DPI)
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)

ax.scatter([p.x for p in points], [p.y for p in points], s=4)
ax.set_xticks([])
ax.set_yticks([])


center_x = np.random.rand() * width
center_y = np.random.rand() * height

region_width = np.random.rand() * min(center_x,width-center_x)
region_height= np.random.rand() * min(center_y,width-center_y)

# region = Rectangle(Point(center_x,center_y),region_width,region_height)
# found_points = qtree.query_region(region)

found_points = []
radius = min(region_width,region_height) 
region = Rectangle(Point(center_x,center_y),radius,radius)
found_points = qtree.query_radius(region,Point(center_x,center_y) )

print('Number of points in the region =', len(found_points))

ax.scatter([p.x for p in found_points],
            [p.y for p in found_points],
            facecolors="none",
            edgecolors="r",s=32
)

region.draw(ax,c="r",lw=2)


ax.invert_yaxis()
plt.tight_layout()
plt.savefig("search-quad-tree.png",DPI=DPI)
plt.show()