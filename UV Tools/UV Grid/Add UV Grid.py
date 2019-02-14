import bpy

bpy.context.space_data.viewport_shade = 'TEXTURED'

for ob in bpy.context.selected_objects:
    bpy.context.scene.objects.active = ob
    
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
        bpy.ops.image.new( name='UV Grid', generated_type = 'UV_GRID' )
        bpy.data.screens['UV Editing'].areas[1].spaces[0].image = bpy.data.images['UV Grid']
        bpy.data.images["UV Grid"].source = 'GENERATED'
        bpy.data.images["UV Grid"].generated_width = 1024
        bpy.data.images["UV Grid"].generated_height = 1024
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')