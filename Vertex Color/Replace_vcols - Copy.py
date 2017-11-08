import bpy
import random

for ob in bpy.context.selected_objects:     # Loops through sselected objects
    bpy.context.scene.objects.active = ob   # Sets current object as active
    while len(ob.data.vertex_colors) > 0:   # Delete vcols
        bpy.ops.mesh.vertex_color_remove()
    
for mesh in bpy.context.selected_objects:
     # Create Vertex Color for each selected meshes
     # bpy.context.selected_objects[0].data.vertex_colors
     mesh.data.vertex_colors.new()

     # Get Total Length of Vertex Colors for each selected meshes
     # len(bpy.context.selected_objects[0].data.vertex_colors[0].data)
     totalVertCol = len(mesh.data.vertex_colors[0].data)
      
     # Iterate over every mesh vertex color and give it a single colour
     
     colR = random.random()
     colG = random.random()
     colB = random.random()

     for i in range(totalVertCol):
        mesh.data.vertex_colors[0].data[i].color = colR, colG, colB
