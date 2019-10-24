import bpy

# Create UV Grid
try:
    if ('UV Grid', bpy.data.images['UV Grid']) in bpy.data.images.items():
        pass

except:
        bpy.ops.image.new( name='UV Grid', generated_type = 'UV_GRID' )
        bpy.data.screens['UV Editing'].areas[1].spaces[0].image = bpy.data.images['UV Grid']
        bpy.data.images["UV Grid"].source = 'GENERATED'
        bpy.data.images["UV Grid"].generated_width = 1024
        bpy.data.images["UV Grid"].generated_height = 1024


# Loops through selected objects
for ob in bpy.context.selected_objects:     
        bpy.context.scene.objects.active = ob
        mesh = bpy.context.active_object.data

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT') # Select all

        # UV0
        if len(mesh.uv_textures.items()) >= 1:
            mesh.uv_textures.active_index = 0
            activeUVmap = mesh.uv_textures.active
            activeUVmap.name = 'UV0'


        # UV1
        if len(mesh.uv_textures.items()) >= 2:
            mesh.uv_textures.active_index = 1
            activeUVmap = mesh.uv_textures.active
            activeUVmap.name = 'UV1'

            bpy.ops.object.texel_density_set()
        
        else:
            bpy.ops.mesh.uv_texture_add()
            mesh.uv_textures.active_index = 1
            activeUVmap = mesh.uv_textures.active
            activeUVmap.name = 'UV1'

            bpy.ops.object.texel_density_set()
            
        bpy.ops.object.mode_set(mode='OBJECT')
                

