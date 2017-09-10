import bpy

if bpy.context.object.data.show_edge_bevel_weight == False:
    bpy.ops.transform.edge_bevelweight(value=0)
    bpy.context.object.data.show_edge_bevel_weight = False

elif bpy.context.object.data.show_edge_bevel_weight == True:
    bpy.ops.transform.edge_bevelweight(value=0)
    bpy.context.object.data.show_edge_bevel_weight = True