import bpy
if len(bpy.context.selected_objects) > 0 and len(bpy.context.selected_objects) < 2:
    print('success')