import bpy

for obj in bpy.context.selected_objects:
    bpy.context.scene.objects.active = obj

    newName = (bpy.context.scene.objects.active.name+"_low"); bpy.context.scene.objects.active.name = newName