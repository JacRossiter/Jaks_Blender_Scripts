import bpy

for ob in bpy.context.selected_objects:     # Loops through sselected objects
    bpy.context.scene.objects.active = ob   # Sets current object as active
    while len(ob.data.vertex_colors) > 0:   # Delete vcols
        bpy.ops.mesh.vertex_color_remove()