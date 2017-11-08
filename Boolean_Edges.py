import bpy

active = bpy.context.scene.objects.active

bpy.ops.mesh.duplicate()
bpy.ops.mesh.separate(type='SELECTED')

bpy.ops.object.mode_set(mode='OBJECT')


for obj in bpy.context.selected_objects:
    if obj.name != active.name:
        bpy.context.scene.objects.active = obj

bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.mesh.select_all(action='TOGGLE')

bpy.ops.mesh.dissolve_limited(angle_limit=0.1)

bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.object.convert(target='CURVE')
bpy.context.object.data.fill_mode = 'FULL'
bpy.context.object.data.bevel_depth = 2.3
bpy.context.object.data.taper_object = bpy.data.objects["BezierCurve"]
bpy.ops.object.convert(target='MESH')


# Bevel
bpy.ops.object.modifier_add(type='BEVEL')
bpy.context.object.modifiers["Bevel"].segments = 2
bpy.context.object.modifiers["Bevel"].profile = 1
bpy.context.object.modifiers["Bevel"].limit_method = 'ANGLE'
bpy.context.object.modifiers["Bevel"].angle_limit = 1.04371
bpy.context.object.modifiers["Bevel"].width = 0.04
bpy.context.object.modifiers["Bevel"].use_clamp_overlap = False


# SubSurf
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subsurf"].levels = 4

bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


active = bpy.context.scene.objects.active

for obj in bpy.context.selected_objects:
    if obj.name != active.name:
        bpy.context.scene.objects.active = obj
       
bpy.ops.hops.bool_difference(boolean_method='BMESH')


