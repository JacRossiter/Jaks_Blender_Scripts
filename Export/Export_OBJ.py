
import bpy
import os


path = "E:/Work/Personal/2019/Overlord/WorkFiles/Highpoly//"

if not os.path.exists(path):
    os.makedirs(path)


for ob in bpy.context.selected_objects:
    bpy.context.scene.objects.active = ob

    name = ob.data.name + '_high'

    bpy.ops.ed.undo_push() # Add undo State
    
    #bpy.context.object.modifiers["Triangulate"].show_viewport = False
    #bpy.context.object.modifiers["Triangulate"].show_render = False


    
    bpy.ops.object.location_clear(clear_delta=False) # Move to Center

    bpy.ops.export_scene.obj(filepath=str(path + name + '.obj'), check_existing=True, global_scale=100.0, use_materials=False, use_blen_objects=True, use_triangles=False, use_selection=True) # Export

    bpy.ops.ed.undo() # Reset Position

