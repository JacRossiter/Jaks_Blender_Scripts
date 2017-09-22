import bpy

for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        bpy.ops.stored_views.save(index=-1)
        bpy.ops.pme.screen_set(name="UV Editing")
        bpy.ops.stored_views.set(index=1)
        bpy.ops.stored_views.delete(index=0)
        break