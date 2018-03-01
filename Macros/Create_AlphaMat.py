import bpy

ob = bpy.context.active_object

bpy.context.scene.render.engine = 'BLENDER_RENDER'
bpy.context.scene.game_settings.material_mode = 'GLSL'
bpy.context.scene.world.light_settings.use_environment_light = True

# Add Mat
mat = bpy.data.materials.new(name="AlphaMat")
if ob.data.materials:           
    ob.data.materials[0] = mat
else:
    ob.data.materials.append(mat)

# Add Tex
tex = bpy.data.textures.new("AlphaTex", 'IMAGE')
slot = mat.texture_slots.add()
slot.texture = tex

# Settings
bpy.context.object.active_material.use_transparency = True
bpy.context.object.active_material.alpha = 0
bpy.context.object.active_material.specular_intensity = 0
tex.use_preview_alpha = True
bpy.context.object.active_material.texture_slots[0].use_map_alpha = True
bpy.context.object.show_transparent = True
bpy.context.space_data.viewport_shade = 'TEXTURED'