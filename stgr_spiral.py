import bpy, bmesh
import numpy as np

for o in bpy.data.objects:
    bpy.data.objects.remove(bpy.data.objects[o.name],True)


scale = 5

r = 2*scale
rth = 0.125*scale

chout = np.sqrt(2)*(r/2+rth)*0.995
chin = np.sqrt(2)*(r/2)*0.831
ch = r*(1+np.sqrt(2)/2)

subdiv = 6

bpy.ops.mesh.primitive_ico_sphere_add(size=r+rth,subdivisions=subdiv, view_align=False, enter_editmode=False, location=(0, 0, r), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.selected_objects[0].name = 'sph'
bpy.ops.mesh.primitive_ico_sphere_add(size=r,subdivisions=subdiv, view_align=False, enter_editmode=False, location=(0, 0, r), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.selected_objects[0].name = 'sphex'

bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=r+rth, depth=r, view_align=False, enter_editmode=False, location=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.selected_objects[0].name = 'base'

bpy.ops.mesh.primitive_cone_add(vertices=256, radius1=chin, depth=chin, view_align=False, enter_editmode=False, location=(0,0,ch+chout/2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.selected_objects[0].name = 'conein'

bpy.ops.mesh.primitive_cone_add(vertices=256, radius1=chout, depth=chout, view_align=False, enter_editmode=False, location=(0,0,ch+chout/2), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
bpy.context.selected_objects[0].name = 'coneout'

bpy.context.scene.objects.active = bpy.data.objects['sph']

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['base']
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'UNION'
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['coneout']
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['sphex']
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['conein']
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

bpy.data.objects.remove(bpy.data.objects['base'],True)
bpy.data.objects.remove(bpy.data.objects['sphex'],True)
bpy.data.objects.remove(bpy.data.objects['coneout'],True)
bpy.data.objects.remove(bpy.data.objects['conein'],True)

#
# h = r*3
# b = 0.36*scale
# sp = b*2
# nn = 13**2
# vs = 10
# locs = []
#
# sa = 2.26
# sr = 1.5
# i0 = 0.1
# for i in range(nn):
#     si = np.sqrt(i+i0)
#     locs.append([sr*sp*si*0.75*np.cos(sa*si*np.pi),sr*sp*si*0.75*np.sin(sa*si*np.pi)])
#
#
#
# for i in range(nn):
#
#     bpy.ops.mesh.primitive_cone_add(vertices=vs, radius1=b, depth=h, view_align=False, enter_editmode=False, location=(locs[i][0],locs[i][1], h/2), rotation=(0,np.pi,0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
#     bpy.context.selected_objects[0].name = 'cone{}'.format(i)
#     type='star'
#
#
#     mm=0
#     randsize = np.random.random()*0.4+0.6
#     randphi = np.random.random()*2*np.pi/5
#     for vert in bpy.data.objects['cone{}'.format(i)].data.vertices:
#         if vert.co[2]>0:
#             vert.co[0]+=locs[i][0]
#             vert.co[1]+=-locs[i][1]
#         else:
#             if (np.arctan2(vert.co[1],vert.co[0])+np.pi)%(2*np.pi/(vs/2))<2*np.pi/vs:
#                 vert.co[0]*=0.5*randsize
#                 vert.co[1]*=0.5*randsize
#             else:
#                 vert.co[0]*=randsize
#                 vert.co[1]*=randsize
#             vertr = np.sqrt(vert.co[0]**2+vert.co[1]**2)
#             vertphi = np.arctan2(vert.co[0],vert.co[1])+randphi
#             vert.co[0] = vertr*np.cos(vertphi)
#             vert.co[1] = vertr*np.sin(vertphi)
#         mm+=1
#
#     bpy.context.scene.objects.active = bpy.data.objects['sph']
#
#     bpy.ops.object.modifier_add(type='BOOLEAN')
#     bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
#     bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['cone{}'.format(i)]
#     bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
#
# mloc = [1.2*sp,-0.55*sp]
# rot = 18*np.pi/16
#
# bpy.ops.mesh.primitive_cone_add(vertices=4*vs, radius1=2.5*b, depth=h, view_align=False, enter_editmode=False, location=(mloc[0],mloc[1], h/2), rotation=(0,np.pi,0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
# bpy.context.selected_objects[0].name = 'cone{}'.format(nn)
#
# for vert in bpy.data.objects['cone{}'.format(nn)].data.vertices:
#     if vert.co[2]>0:
#         vert.co[0]+=mloc[0]
#         vert.co[1]+=-mloc[1]
#     else:
#         if vert.co[0]<0:
#             vert.co[0]*=-0.65
#         vertr = np.sqrt(vert.co[0]**2+vert.co[1]**2)
#         vertphi = np.arctan2(vert.co[0],vert.co[1])+rot
#         vert.co[0] = vertr*np.cos(vertphi)
#         vert.co[1] = vertr*np.sin(vertphi)
#
# bpy.context.scene.objects.active = bpy.data.objects['sph']
#
# bpy.ops.object.modifier_add(type='BOOLEAN')
# bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
# bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['cone{}'.format(nn)]
# bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
#
# for i in range(nn+1):
#     bpy.data.objects.remove(bpy.data.objects['cone{}'.format(i)],True)
# bpy.context.scene.update()
