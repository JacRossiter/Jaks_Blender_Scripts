import bpy

for ob in bpy.context.selected_objects:     # Loops through selected objects
        bpy.context.scene.objects.active = ob
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        #bpy.ops.mesh.dissolve_limited(angle_limit=0.001)
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
        bpy.ops.uv.smart_project(angle_limit=80, island_margin=0.01, user_area_weight=1)
        bpy.ops.object.mode_set(mode='OBJECT')