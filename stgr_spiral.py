import bpy, bmesh
import numpy as np
import blender_defs as bd
import time as tm
import sys
from progress_bar import progress


for o in bpy.data.objects:
    bd.remove(o.name)

r = 3
th = r*0.02
domename = 'dome'
bd.make_dome(r,th,domename)

h = r*2.5 # cone height
size = 0.15 # (0.125) size of each cone
v = 4 # verticies
psc = 4 # point scale
spsc = {3:1.25, # spacing scale
        4:1.5,
        5:1.75}

points = []
nn = 11**2 # number of stars
sa = 1.6   # (2.26)  angular scale for spiral
sr = 1.125 # (1.125) radial scale for spiral
i0 = 0.1   # intital offset
for j in range(nn):
    si = np.sqrt(j+i0)
    loc = [sr*si*np.cos(sa*si*np.pi),sr*si*np.sin(sa*si*np.pi)]

    points.append(int(np.random.random()*3+3))
    rang = np.random.random()*np.pi
    rrv = np.random.random()*0.4+0.6
    for i in range(points[-1]):
        bd.cone(size,h,v,'star{}{}'.format(j,i),rot=(np.pi,0,0))
        for vert in bpy.data.objects['star{}{}'.format(j,i)].data.vertices:
            if vert.co[2]<0:
                if abs(vert.co[1])>size/2 and np.sign(vert.co[1])==1:
                    vert.co[1]*=psc
                    vert.co[1]+=spsc[points[-1]]*size
                else:
                    vert.co[1]+=spsc[points[-1]]*size
                ang = np.arctan2(vert.co[1],vert.co[0])
                rv = np.sqrt(vert.co[1]**2+vert.co[0]**2)
                vert.co[0] = rrv*rv*np.cos(ang+rang+i*2*np.pi/points[-1]) + loc[0]
                vert.co[1] = rrv*rv*np.sin(ang+rang+i*2*np.pi/points[-1]) + loc[1]

t0 = tm.clock()
bd.active(domename)
for j in range(nn):
    for i in range(points[j]):
        bd.difference('star{}{}'.format(j,i))
        bd.remove('star{}{}'.format(j,i))

    progress(j,nn,t0,inc10=False)
