import bpy


for obj in bpy.context.selected_objects:
    bpy.context.scene.objects.active = obj

    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.mark_seam(clear=False)
    bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.0139381)
    bpy.ops.object.editmode_toggle()