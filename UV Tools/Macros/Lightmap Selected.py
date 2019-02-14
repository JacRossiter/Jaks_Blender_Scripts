import bpy

mode = bpy.context.active_object.mode

for ob in bpy.context.selected_objects:     # Loops through selected objects
        bpy.context.scene.objects.active = ob
        mesh = bpy.context.active_object.data

        if len(mesh.uv_textures.items()) == 0:
                bpy.ops.mesh.uv_texture_add()
                bpy.ops.mesh.uv_texture_add()
                mesh.uv_textures.active_index = 1
                activeUVmap = mesh.uv_textures.active
                activeUVmap.name = 'Lightmap'
                
                try:
                        if ('UV Grid', bpy.data.images['UV Grid']) in bpy.data.images.items():
                                bpy.ops.object.mode_set(mode='EDIT')
                                bpy.ops.mesh.select_all(action='SELECT')
                                bpy.context.object.draw_type = 'TEXTURED'
                                bpy.data.screens['UV Editing'].areas[1].spaces[0].image = bpy.data.images['UV Grid']
                                bpy.ops.mesh.select_all(action='DESELECT')
                                bpy.ops.object.mode_set(mode='OBJECT')

                except:
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.context.object.draw_type = 'TEXTURED'
                        bpy.context.space_data.viewport_shade = 'TEXTURED'
                        bpy.ops.image.new( name='UV Grid', generated_type = 'UV_GRID' )
                        bpy.data.screens['UV Editing'].areas[1].spaces[0].image = bpy.data.images['UV Grid']
                        bpy.data.images["UV Grid"].source = 'GENERATED'
                        bpy.data.images["UV Grid"].generated_width = 1024
                        bpy.data.images["UV Grid"].generated_height = 1024
                        bpy.ops.mesh.select_all(action='DESELECT')
                        bpy.ops.object.mode_set(mode='OBJECT')


        elif len(mesh.uv_textures.items()) == 1:
                bpy.ops.mesh.uv_texture_add()
                mesh.uv_textures.active_index = 1
                activeUVmap = mesh.uv_textures.active
                activeUVmap.name = 'Lightmap'

        elif len(mesh.uv_textures.items()) > 1:
                mesh.uv_textures.active_index = 1
                activeUVmap = mesh.uv_textures.active
                activeUVmap.name = 'Lightmap'

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.smart_project(angle_limit=36, island_margin=0.05, user_area_weight=0, use_aspect=True, stretch_to_bounds=True)

        bpy.ops.object.mode_set(mode='OBJECT')

        

if mode == 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')



