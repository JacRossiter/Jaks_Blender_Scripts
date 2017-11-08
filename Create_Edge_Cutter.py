import bpy

print("--"*40)
active = bpy.context.scene.objects.active

#Creates List of Selected Objects
objselection = []
for obj in bpy.context.selected_objects:
    objselection.append(obj)


bpy.ops.mesh.duplicate()
bpy.ops.mesh.separate(type='SELECTED')
bpy.ops.object.mode_set(mode='OBJECT')


for obj in bpy.context.selected_objects:
    if obj.name == active.name:
        obj.select =False
    else:
        bpy.context.scene.objects.active = obj

bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.mesh.select_all(action='TOGGLE')

bpy.ops.mesh.dissolve_limited(angle_limit=0.1)
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.convert(target='CURVE')
bpy.context.object.data.fill_mode = 'FULL'
bpy.context.object.data.bevel_depth = 2.3
bpy.context.object.data.taper_object = bpy.data.objects["BezierCurve"]
bpy.context.object.data.twist_smooth = 100

bpy.context.object.draw_type = 'WIRE'
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')


