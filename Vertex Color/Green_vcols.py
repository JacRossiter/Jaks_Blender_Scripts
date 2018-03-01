import bpy
import random



def replace_vcols_object():
    # Remove vcols
    for ob in bpy.context.selected_objects:     # Loops through selected objects
        bpy.context.scene.objects.active = ob   # Sets current object as active
        while len(ob.data.vertex_colors) > 0:   # Delete vcols
            bpy.ops.mesh.vertex_color_remove()


    # Add vcols
    for mesh in bpy.context.selected_objects:
        bpy.context.scene.objects.active = ob   # Sets current object as active
        # Create Vertex Color for each selected meshes
        # bpy.context.selected_objects[0].data.vertex_colors
        mesh.data.vertex_colors.new()

    # Get Total Length of Vertex Colors for each selected meshes
    # len(bpy.context.selected_objects[0].data.vertex_colors[0].data)
        totalVertCol = len(mesh.data.vertex_colors[0].data)
    
    # Iterate over every mesh vertex color and give it a single colour
    
        colR = 0
        colG = 1
        colB = 0

        #bpy.data.brushes["Draw"].cursor_color_add = (1, 0, 0)


        for i in range(totalVertCol):
            mesh.data.vertex_colors[0].data[i].color = colR, colG, colB

def replace_vcols_edit():
    ob = bpy.context.scene.objects.active
    me = ob.data

    bpy.ops.object.vertex_group_add()
    bpy.ops.object.vertex_group_remove(all=True)
    ob.vertex_groups.new(name="Selection")

    bpy.ops.object.vertex_group_assign() #

    

    bpy.ops.mesh.select_all(action='INVERT')
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()


    selFaces = []
    for f in me.polygons:
        if f.select:
            selFaces.append(f)
    print(len(selFaces))

    if len(selFaces) == 0:
        bpy.ops.object.mode_set(mode='OBJECT')
        replace_vcols_object()
    
    else:
        bpy.ops.mesh.separate(type='SELECTED')
        bpy.ops.object.mode_set(mode='OBJECT')
        

        # Remove vcols
        while len(ob.data.vertex_colors) > 0:
            bpy.ops.mesh.vertex_color_remove()
            
        ob.data.vertex_colors.new()

        totalVertCol = len(ob.data.vertex_colors[0].data)

    # Iterate over every mesh vertex color and give it a single colour

        colR = 0
        colG = 1
        colB = 0

        for i in range(totalVertCol):
            ob.data.vertex_colors[0].data[i].color = colR, colG, colB

        
        bpy.ops.object.join()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=0.001, use_unselected=False)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()


# Object Mode
if bpy.context.active_object.mode == 'OBJECT':
    replace_vcols_object()

# Edit Mode
if bpy.context.active_object.mode == 'EDIT':
    replace_vcols_edit()
    