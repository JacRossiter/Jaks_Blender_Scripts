import bpy

bpy.ops.object.hide_view_clear()

path = bpy.path.abspath('//Meshes/')
if not os.path.exists(path):
    os.makedirs(path)

for group in bpy.data.groups:
    bpy.ops.object.select_all(action='DESELECT')
    for ob in group.objects:
        ob.select = True
    
    name = group.name
    bpy.ops.export_scene.fbx(filepath=str(path + name + '.fbx'), version='BIN7400', ui_tab='MAIN', use_selection=True, global_scale=1, apply_unit_scale=True)


    active_group = group

bpy.ops.object.select_all(action='DESELECT')
for ob in active_group.objects:
    ob.select = True
bpy.ops.object.hide_view_set(unselected=True)