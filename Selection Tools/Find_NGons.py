import bpy
print("---------------------------------")

def updateMesh():
    bpy.ops.object.mode_set(toggle=True)
    bpy.ops.object.mode_set(toggle=True)
    
bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
updateMesh()
for obj in bpy.context.selected_objects:
    bpy.context.scene.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_face_by_sides(number=4, type='GREATER')   
    updateMesh()
    
    faces = bpy.context.object.data.polygons
    ngons = []
    
    for face in faces:
        if face.select:
            ngons.append(face)
            
    if len(ngons) != 0:
        print(obj.name,"has an NGon")
        bpy.ops.view3d.view_selected(use_all_regions=False)
        break
    else:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    
    print(obj.name,"has no NGon's")
    