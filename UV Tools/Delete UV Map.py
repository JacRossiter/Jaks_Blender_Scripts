import bpy
# This script wil delete all uvmaps in the selected objects that do not have the name 'UVMap' 

for obj in bpy.context.selected_objects: # Creates list of uv maps that need deleting
    uvmap = obj.data.uv_textures
    unwanted_uv = []
    for uv in uvmap:
        if uv.name != "UVMap":
            unwanted_uv.append(uv)
    x = len(unwanted_uv)-1
    for uv in unwanted_uv:
        uvmap.remove(unwanted_uv[x])
        x = x-1