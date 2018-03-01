import bpy

bpy.ops.object.vertex_group_add()
bpy.ops.object.vertex_group_assign()

n = 10

while n > 0:
    n -= 1
    bpy.ops.mesh.select_random(percent=10, seed=n, action='DESELECT')
    bpy.ops.transform.translate(value=(0, 0, -0.005), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()

bpy.ops.object.vertex_group_select()
bpy.ops.object.vertex_group_remove(all=False)

