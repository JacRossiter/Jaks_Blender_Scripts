import bpy

#Macro for adding marking seam/sharp and unwrapping the mesh. Uses Hard Ops to display a thumbnail of  the new UVs

bpy.ops.mesh.mark_seam(clear=True)
bpy.ops.mesh.mark_sharp(clear=True)
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.object.vertex_group_add()
bpy.ops.object.vertex_group_assign()
bpy.ops.mesh.reveal()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.unwrap()
bpy.ops.uv.pack_islands()
bpy.ops.object.vertex_group_deselect()
bpy.ops.mesh.hide(unselected=False)
bpy.ops.object.editmode_toggle()
bpy.ops.hops.draw_uv()
## ^^^Remove this if you do not have Hard Ops
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.vertex_group_remove(all=False)