import bpy

print("-------------------------------------------")
print("-------------------START--------------------")
print("-------------------------------------------")

# How to use: Select two meshes, one mesh must have _low suffix!

for obj in bpy.context.scene.objects:
    obj.select = True


obj = bpy.context.object


# Detects mesh with '_low' suffix, sets that object as active

for obj in bpy.context.selected_objects:
    if "_low" in obj.name[-4:]:
        bpy.context.scene.objects.active = obj
        
        low = bpy.context.scene.objects.active
        
# Defines selected but not active objects

selected = bpy.context.selected_objects
selected.remove(low)

z = 0
inside_bounds = []

for obj in selected:
    
    high = selected[z]
            
    # Lowpoly Bounding Box Vertex Locations
        
    lowVert_list = [v[:] for v in low.bound_box]
    highVert_list = [v[:] for v in high.bound_box]

    lowVert1_loc = lowVert_list[0]
    lowVert1_locX = lowVert1_loc[0] * low.scale[0] + low.location[0]
    lowVert1_locY = lowVert1_loc[1] * low.scale[1] + low.location[1]
    lowVert1_locZ = lowVert1_loc[2] * low.scale[2] + low.location[2]

    highVert1_loc = highVert_list[0]
    highVert1_locX = highVert1_loc[0] * high.scale[0] + high.location[0]
    highVert1_locY = highVert1_loc[1] * high.scale[1] + high.location[1]
    highVert1_locZ = highVert1_loc[2] * high.scale[2] + high.location[2]
    
    lowVert2_loc = lowVert_list[6]
    lowVert2_locX = lowVert2_loc[0] * low.scale[0] + low.location[0]
    lowVert2_locY = lowVert2_loc[1] * low.scale[1] + low.location[1]
    lowVert2_locZ = lowVert2_loc[2] * low.scale[2] + low.location[2]

    highVert2_loc = highVert_list[6]
    highVert2_locX = highVert2_loc[0] * high.scale[0] + high.location[0]
    highVert2_locY = highVert2_loc[1] * high.scale[1] + high.location[1]
    highVert2_locZ = highVert2_loc[2] * high.scale[2] + high.location[2]

    print("Vertex 1")

    if highVert1_locX >= lowVert1_locX:
        print("X = Inside")
    else:
        print("X = Outside")
    
    if highVert1_locY >= lowVert1_locY:
        print("Y = Inside")
    else:
        print("Y = Outside")
    
    if highVert1_locZ >= lowVert1_locZ:
        print("Z = Inside")
    else:
        print("Z = Outside")
    
    print("Vertex 2")

    if highVert2_locX <= lowVert2_locX:
        print("X = Inside")
    else:
        print("X = Outside")
    
    if highVert2_locY <= lowVert2_locY:
        print("Y = Inside")
    else:
        print("Y = Outside")
    
    if highVert2_locZ <= lowVert2_locZ:
        print("Z = Inside")
    else:
        print("Z = Outside")    
    

    if highVert1_locX <= lowVert1_locX or highVert1_locY <= lowVert1_locY or highVert1_locZ <= lowVert1_locZ:
            print("Vertex 1 Failed")
    else:
        if highVert2_locX >= lowVert2_locX or highVert2_locY >= lowVert2_locY or highVert2_locZ >= lowVert2_locZ:
            print("Vertex 2 Failed")
        else:
            print("Success")
            inside_bounds.append(high)
    z += 1
    
print(inside_bounds)

# Deselects all
for o in bpy.context.selected_objects:
    o.select = False
    
# Selects objects within Bounding box    
for o in inside_bounds:
     o.select = True
    
#bpy.context.scene.cursor_location = (highVert1_locX, highVert1_locY, highVert1_locZ)
#bpy.context.scene.cursor_location = (highVert2_locX, highVert2_locY, highVert2_locZ)