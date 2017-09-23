import bpy
# This script wil delete all uvmaps in the selected objects that do not have the name 'UVMap'.
# Courtesy of Martin Durhuus for this more elegant version

for obj in bpy.context.selected_objects: # Creates list of uv maps that need deleting
    uvmaps = obj.data.uv_textures
    while len(uvmaps) > 1:
        if uvmaps[-1].name == 'UVMap':
            uvmaps.remove(uvmaps[0])
        else:
            uvmaps.remove(uvmaps[-1])