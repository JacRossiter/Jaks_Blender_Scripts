import bpy

for ob in bpy.context.scene.objects:
    bpy.context.scene.objects.active = ob
    bpy.ops.gpencil.palettecolor_remove()

    