import bpy
import random

# Get selected objects
selected_meshes = bpy.context.selected_objects

# Add Materials that respects the Vertex Color for 
# each selected and active objects

for mesh in selected_meshes:
    mat = bpy.data.materials.new('VertexMat')
    mat.use_vertex_color_paint = True
    mat.use_vertex_color_light = True
    mesh.data.materials.append(mat)
    
    # Tell Blender to Update the Material
    bpy.data.materials.is_updated = True

for mesh in selected_meshes:
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