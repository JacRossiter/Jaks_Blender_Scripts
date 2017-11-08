import bpy

bpy.context.active_object.modifiers.new(name='Weighted Bevel Smooth', type='BEVEL')
bpy.context.object.modifiers["Weighted Bevel Smooth"].segments = 24
bpy.context.object.modifiers["Weighted Bevel Smooth"].profile = .5
bpy.context.object.modifiers["Weighted Bevel Smooth"].use_clamp_overlap = False
bpy.context.object.modifiers["Weighted Bevel Smooth"].limit_method = 'WEIGHT'