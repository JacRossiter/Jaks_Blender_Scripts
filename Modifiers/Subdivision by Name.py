import bpy

# Adds/Sets subdivision modifier to have the same number of levels as the '_subd' as definied in the object name. 
# Works for all selected objects.
for obj in bpy.context.selected_objects:
    bpy.context.scene.objects.active = obj
    subd_flag = False

    if "_subd1" in obj.name:
        subd_level = 1
    elif "_subd2" in obj.name:
        subd_level = 2
    elif "_subd3" in obj.name:
        subd_level = 3
    elif "_subd4" in obj.name:
        subd_level = 4
    elif "_subd5" in obj.name:
        subd_level = 5
    elif "_subd6" in obj.name:
        subd_level = 6
    elif "_subd7" in obj.name:
        subd_level = 7
    elif "_subd8" in obj.name:
        subd_level = 8
    elif "_subd9" in obj.name:
        subd_level = 9
    elif "_subd10" in obj.name:
        subd_level = 10

    for mod in [m for m in obj.modifiers if m.type == 'SUBSURF']:
        obj.modifiers[mod.name].show_viewport = True
        bpy.context.object.modifiers[mod.name].levels = subd_level
        bpy.context.object.modifiers[mod.name].render_levels = subd_level

        subd_flag = True

    if subd_flag == False:
        bpy.ops.object.modifier_add(type='SUBSURF')
        bpy.context.object.modifiers['Subsurf'].levels = subd_level
        bpy.context.object.modifiers['Subsurf'].render_levels = subd_level
        bpy.context.object.modifiers['Subsurf'].show_only_control_edges = True