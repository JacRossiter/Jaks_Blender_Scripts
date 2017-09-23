import bpy
#print("-------------spacer-------------")
# This script wil delete all uvmaps in the selected objects that do not have the name 'UVMap' 


for obj in bpy.context.selected_objects:
    # Creates list of uv maps that need deleting
    uvtex = obj.data.uv_textures
    uv_delete = []
    for uvmap in uvtex:
        if uvmap.name != "UVMap":
            uv_delete.append(uvmap)
    #print(obj.name, "'s delete_uv list:")
    #for x in uv_delete:
    #    print(x)
    # Gets length of list and starts deleting in a desending order. This is because when you delete a uvmap it actually still exists but contains the name 'NGon Face'. 
    #-This uvmap's position in the list will be shifted. This rearranges the list and causes issues for us if we try to iterate through in a acending manner
    for i in range(len(uv_delete)):
        uv_delete.remove(uv_delete[-1])