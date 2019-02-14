import bpy

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.wm.context_set_value(data_path="tool_settings.mesh_select_mode", value= "(False, False, True)")


bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.unwrap(method='CONFORMAL', margin=0)

for ob in bpy.context.selected_objects:     # Loops through selected objects
         bpy.context.scene.objects.active = ob
         bpy.ops.object.texel_density_set()
