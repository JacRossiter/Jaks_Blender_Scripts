import bpy

bpy.ops.stored_views.save(index=-1)

bpy.ops.pme.screen_set(name="Default")
bpy.ops.stored_views.set(index=1)
bpy.ops.stored_views.delete(index=0)