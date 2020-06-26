'''
Convex hull is a way to capture a set of points using another set of points that is preferable. In this case a continuous set that is convex and minimal, since convex and minimal is a property that’s always good to have.

There are many algorithms to find convex hull, but I like particularly this one.

Choose left-most point U and right-most point V. Both U and V reside on hull and UV forms a line that splits the set. On each side of UV choose the furthest point P, throw away all points inside triangle UVP and proceed recursively on UP and VP.
'''
import numpy as np

def split(u, v, points):
    # return points on left side of UV
    return [p for p in points if np.cross(p-u, v-u)<0]

def extend(u, v, points):
    if not points:
        return []

    # find furthest point W and split search to WV, UW
    w = min(points, key = lambda p: np.cross(p-u, v-u))
    p1,p2 = split(w,v,points), split(u,w, points)
    return extend(w, v, p1) + [w] + extend(u, w, p2)

def convex_hull(points):
    # find two hull points , U ,V and split  to left and rigth search
    u = min(points, key = lambda p :p[0])
    v = max(points, key = lambda p :p[0])
    left, right = split(u,v,points) , split(v,u,points)

    # find convex hull on each side
    return [v] + extend(u,v, left) + \
           [u] + extend(v,u, right) + [v]

points = np.random.rand(100,2)
x = np.array(convex_hull(points))

print(x)
