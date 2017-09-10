import bpy

i = bpy.data.images["UV Grid"].generated_width
bpy.data.images["UV Grid"].generated_width = i*2

bpy.data.images["UV Grid"].generated_height = i*2