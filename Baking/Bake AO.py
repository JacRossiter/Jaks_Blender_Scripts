import bpy


bpy.context.scene.world.light_settings.use_ambient_occlusion = True
bpy.context.scene.render.bake_type = 'AO'
bpy.context.scene.render.use_bake_normalize = True
bpy.ops.object.bake_image()
