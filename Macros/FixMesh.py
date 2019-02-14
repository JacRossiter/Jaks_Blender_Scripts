import bpy

bpy.ops.object.join()

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')

bpy.ops.mesh.remove_doubles(threshold=0.010001)
bpy.ops.mesh.separate(type='LOOSE')

bpy.ops.object.mode_set(mode='OBJECT')



#for obj in bpy.context.selected_objects:
    #bpy.context.scene.objects.active = obj
    