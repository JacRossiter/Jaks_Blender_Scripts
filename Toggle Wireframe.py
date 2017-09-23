import bpy

ob = bpy.context.scene.objects.active

if ob.show_wire == True:
    for ob in bpy.context.selected_objects:
        ob.show_wire = False
    
elif ob.show_wire == False:
    for ob in bpy.context.selected_objects:
        ob.show_wire = True
        ob.show_all_edges = True
