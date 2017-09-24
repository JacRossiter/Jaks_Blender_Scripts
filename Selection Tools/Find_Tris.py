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
    bpy.ops.mesh.select_face_by_sides(number=4, type='LESS')   
    updateMesh()
    
    faces = bpy.context.object.data.polygons
    tris = []
    
    for face in faces:
        if face.select:
            tris.append(face)
            
    if len(tris) != 0:
        print(obj.name,"has a Tri")
        bpy.ops.view3d.view_selected(use_all_regions=False)
        break
    else:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    
    print(obj.name,"has no Tris")
    