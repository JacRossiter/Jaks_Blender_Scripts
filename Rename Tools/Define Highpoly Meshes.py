import bpy

#Select two or more objects and execute. One object must have the suffix '_low'

print("---------------------------------------------------------")

# Detects Object with '_low' suffix, sets that object as active


# Toggle/Reveal all Layers
bpy.ops.view3d.layers(nr=0, extend=False)


for obj in bpy.context.selected_objects: # Loop through selection
    
    if "_low" in obj.data.name[-4:]: # Check Mesh Name
        bpy.context.scene.objects.active = obj
        
        lowpoly = obj.data.name
        obj.name = lowpoly
        print("Lowpoly Mesh =", lowpoly)
        
        # Removes '_low' suffix and adds '_high.000' to objects that are selected but not active
        
        lowpoly = lowpoly[:-4] + "_high.000"
        for o in bpy.context.selected_objects:
            if o.name != bpy.context.scene.objects.active.name:
                o.name = lowpoly
    


    elif "_low" in obj.name[-4:]: # Check Object Name
        bpy.context.scene.objects.active = obj
        
        lowpoly = bpy.context.scene.objects.active.name
        print("Lowpoly Mesh =", lowpoly)
        
        # Removes '_low' suffix and adds '_high.000' to objects that are selected but not active
        
        lowpoly = lowpoly[:-4] + "_high.000"
        for o in bpy.context.selected_objects:
            if o.name != bpy.context.scene.objects.active.name:
                o.name = lowpoly

# Toggle/Reveal all Layers
bpy.ops.view3d.layers(nr=0, extend=False)