import bpy

#Delete '_high' or '_low' Suffix

for obj in bpy.context.selected_objects:
    bpy.context.scene.objects.active = obj

    newName = (bpy.context.scene.objects.active.name)

    o = newName[-5:]

    if "_high" in o:    
        newName = newName[:-5]
    else:
        newName = newName[:-4]
        
    bpy.context.scene.objects.active.name = newName