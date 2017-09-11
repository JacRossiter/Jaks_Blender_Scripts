import bpy

for o in bpy.context.selected_objects:
    bpy.context.scene.objects.active = o
    for mod in [m for m in o.modifiers if m.type == 'BEVEL']:
        o.modifiers[mod.name].show_viewport = True
        bpy.ops.object.modifier_apply( modifier = mod.name )