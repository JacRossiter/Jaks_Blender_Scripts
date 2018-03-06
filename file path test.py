import bpy
import os
import bmesh
import math
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, CollectionProperty
from bpy.types import Operator, OperatorFileListElement

current_selected_obj = bpy.context.selected_objects
active_ob = bpy.context.scene.objects.active
name = active_ob.name

current_unit_system = bpy.context.scene.unit_settings.system
bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.scale_length = 0.01







##### EXPORT SINGLE ASSET #####

# Set Transform Pivot
bpy.ops.view3d.snap_cursor_to_active()
bpy.context.space_data.pivot_point = 'CURSOR'


# Edit Transforms for Unity
for ob in current_selected_obj:
    if ob.type == 'MESH':
        bpy.context.scene.objects.active = ob

        # X-rotation fix
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.resize(value=(100, 100, 100))
        bpy.ops.transform.rotate(value = -1.5708, axis = (1, 0, 0), constraint_axis = (True, False, False), constraint_orientation = 'GLOBAL')
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.transform.rotate(value = 1.5708, axis = (1, 0, 0), constraint_axis = (True, False, False), constraint_orientation = 'GLOBAL')

#Create export folder
path = bpy.path.abspath('//Meshes/')
if not os.path.exists(path):
    os.makedirs(path)

# Revert Active Object
bpy.context.scene.objects.active = active_ob

# Export as One FBX
bpy.ops.export_scene.fbx(filepath=str(path + name + '.fbx'), version='BIN7400', ui_tab='MAIN', use_selection=True, global_scale=1, apply_unit_scale=True)

# Revert Transforms
for ob in current_selected_obj:
    if ob.type == 'MESH':
        bpy.context.scene.objects.active = ob
         
        # Revert Transforms
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.resize(value=(0.01, 0.01, 0.01))
        bpy.ops.transform.rotate(value = 1.5708, axis = (1, 0, 0), constraint_axis = (True, False, False), constraint_orientation = 'GLOBAL')
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.transform.rotate(value = -1.5708, axis = (1, 0, 0), constraint_axis = (True, False, False), constraint_orientation = 'GLOBAL')

        
# Revert Active Object
bpy.context.scene.objects.active = active_ob
