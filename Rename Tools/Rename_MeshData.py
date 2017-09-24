import bpy

for obj in bpy.context.selected_objects:
    objName = obj.name
    me = obj.data
    meName = objName + '_SHAPE'
    me.name = meName