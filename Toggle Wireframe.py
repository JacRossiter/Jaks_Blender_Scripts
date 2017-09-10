import bpy

ob = bpy.context.scene.objects.active

if ob.show_wire == True:
    for obj in bpy.context.selected_objects:
        obj.show_wire = False
        obj.show_all_edges = False

    
elif ob.show_wire == False:
    for obj in bpy.context.selected_objects:
        obj.show_wire = True
        obj.show_all_edges = True
