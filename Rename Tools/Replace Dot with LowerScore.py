import bpy

#Select two or more objects and execute. One object must have the suffix '_low'

print("---------------------------------------------------------")

# Detects mesh with '_low' suffix, sets that object as active

for obj in bpy.context.selected_objects:
    if "." in obj.name[-5:]:
        obj.name = obj.name.replace(".", "_")
        obj.name = obj.name + "_GEO"