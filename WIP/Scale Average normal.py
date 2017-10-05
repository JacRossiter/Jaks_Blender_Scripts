import bpy

print("-"*60)
def updateMesh():
    bpy.ops.object.mode_set(toggle=True)
    bpy.ops.object.mode_set(toggle=True)

ob = bpy.context.active_object
vert_normal_list = []
vert_normal = []
averaged_normal = []
edge_normals = []


updateMesh()

for edge in ob.data.edges:
    if edge.select == True:
        for vert in edge.vertices:
            vert_normal_list.append(ob.data.vertices[vert].normal)
            vert_normal = [v[:] for v in vert_normal_list]
            
print(vert_normal)
        
        
        #print(vert_normal)
        #vert_a = vert_normal[0]
        #vert_b = vert_normal[1]
        #averaged_normal = [(x+y)/2 for x,y in zip(vert_a, vert_b)]
        #edge_normals.append(averaged_normal)
#print(edge_normals)


#edge_a = edge_normals[0]
#edge_b = edge_normals[1]
#averaged_edge_normal = [x+y for x,y in zip(edge_a, edge_b)]
#print(averaged_edge_normal)        
#print("Edges:")
#print(len(selected_edges),"Selected")

#print("Vertices:")
#print(len(selected_verts),"Selected")
