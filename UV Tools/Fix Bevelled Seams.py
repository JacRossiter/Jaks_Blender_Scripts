import bpy

#This Script will apply a bevel modifier and correct the UVs based on UV Islands. 

ob = bpy.context.active_object
me = ob.data

selFaces = []

for areas in bpy.context.screen.areas:
    if areas.type == "VIEW_3D":
        break
        

#Apply bevel and remove seams
#bpy.ops.object.mode_set(mode="OBJECT")
#bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Bevel")
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.mark_seam(clear=True)
bpy.ops.mesh.select_all(action='DESELECT')

#create list of polygons
for f in me.polygons:
    bpy.ops.object.mode_set(mode="EDIT")
    selFaces.append(f)

#loop through polygons and perform operation    
for s in selFaces:
    bpy.ops.object.mode_set(mode="OBJECT")
    s.select = True
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_linked(delimit={'UV'})
    
    #Remove UV island from list of polygons
    #for f in selFaces:
    #    if f.select:
    #        selFaces.remove(f)
            
    bpy.ops.mesh.region_to_loop()
    bpy.ops.mesh.mark_seam()
    bpy.ops.mesh.select_all(action='DESELECT')
#bpy.ops.object.mode_set(mode="EDIT")
#bpy.ops.mesh.select_all(action='SELECT')
#bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.035)
#bpy.ops.mesh.select_all(action='DESELECT')