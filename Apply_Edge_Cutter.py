import bpy


print("--"*40)
active = bpy.context.scene.objects.active

objselection = []

for obj in bpy.context.selected_objects:
    objselection.append(obj)

for obj in bpy.context.selected_objects:
    if obj.name == active.name:
        obj.select =False
    else:
        bpy.context.scene.objects.active = obj

bpy.ops.object.convert(target='MESH')

for obj in objselection:
    obj.select = True

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
bpy.context.object.modifiers["Subsurf"].levels = 1
bpy.context.object.modifiers["Subsurf"].show_only_control_edges = True


bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


active = bpy.context.scene.objects.active

for obj in bpy.context.selected_objects:
    if obj.name != active.name:
        bpy.context.scene.objects.active = obj
       
bpy.ops.hops.bool_difference(boolean_method='BMESH')
C.space_data.show_only_render = False

