import bpy

for ob in bpy.context.selected_objects:     # Loops through selected objects
        bpy.context.scene.objects.active = ob
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        #bpy.ops.mesh.dissolve_limited(angle_limit=0.001)
        bpy.ops.uv.smart_project(angle_limit=10, island_margin=0, use_aspect=True, stretch_to_bounds=False)
        bpy.ops.object.mode_set(mode='OBJECT')