import bpy

for obj in bpy.context.selected_objects:
    bpy.context.scene.objects.active = obj

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.mark_sharp(clear=True)
    bpy.ops.mesh.mark_seam(clear=True)
    bpy.ops.uv.seams_from_islands(mark_seams=True, mark_sharp=True)

    bpy.ops.object.mode_set(mode='OBJECT')
