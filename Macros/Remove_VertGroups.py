import bpy
for ob in bpy.context.selected_editable_objects:
    for vgroup in ob.vertex_groups:
        ob.vertex_groups.remove(vgroup)