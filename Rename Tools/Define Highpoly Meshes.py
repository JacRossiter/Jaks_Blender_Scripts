import bpy

#Select two or more objects and execute. One object must have the suffix '_low'

print("---------------------------------------------------------")

# Detects mesh with '_low' suffix, sets that object as active

for obj in bpy.context.selected_objects:
    if "_low" in obj.name[-4:]:
        bpy.context.scene.objects.active = obj
        
        lowpoly = bpy.context.scene.objects.active.name
        print("Lowpoly Mesh =", lowpoly)
        
        # Removes '_low' suffix and adds '_high.000' to objects that are selected but not active
        
        lowpoly = lowpoly[:-4] + "_high.000"
        for o in bpy.context.selected_objects:
            if o.name != bpy.context.scene.objects.active.name:
                o.name = lowpoly