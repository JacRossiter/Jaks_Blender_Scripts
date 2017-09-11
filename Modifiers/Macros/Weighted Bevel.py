import bpy

bpy.context.active_object.modifiers.new(name='Weighted Bevel', type='BEVEL')
bpy.context.object.modifiers["Weighted Bevel"].segments = 2
bpy.context.object.modifiers["Weighted Bevel"].profile = 1
bpy.context.object.modifiers["Weighted Bevel"].use_clamp_overlap = False
bpy.context.object.modifiers["Weighted Bevel"].limit_method = 'WEIGHT'