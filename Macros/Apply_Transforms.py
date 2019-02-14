"""apply_scale_to_multi-user_object.py: \
Loops through selection and applies the scale to multi-user objects. Relative size is preserved."""

__author__      = "nik10110"
__credits__     = ["Gandalf3", "Vader"]
__license__     = "MIT"
__version__     = "0.1.1"

preserve_relative_scale = True

import bpy

# Remember the initial selection and initially active object
active_obj = bpy.context.scene.objects.active
initial_selected=[]
for obj in bpy.context.selected_editable_objects:
    initial_selected.append(obj)

# Build an inverse mesh -> objects tree
mesh_owners = {}
for ob in bpy.data.objects:
    if ob.type == 'MESH':
        mesh_owners.setdefault(ob.data, []).append(ob)

# Apply scale to selected objects (and all objects using the same mesh)
selected = list(initial_selected)
for obj in selected:
    if obj.data is not None:
        # Remember the initial scale and object
        orig_scale = obj.scale.copy()
        orig_data = obj.data

        # Set active object and deselect the rest
        bpy.context.scene.objects.active = obj
        bpy.ops.object.select_all(action='DESELECT')
        obj.select = True

        # Make single user and apply scale
        bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True, material=False, texture=False, animation=False)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        # Keep the relative scale of the other objects using the same mesh
        for o in mesh_owners[orig_data]:
            if o != obj:
                if o in selected:
                    # No need to loop through the same mesh again
                    selected.remove(o)
                if preserve_relative_scale:
                    o.scale.x = o.scale.x/orig_scale.x
                    o.scale.y = o.scale.y/orig_scale.y
                    o.scale.z = o.scale.z/orig_scale.z
                else:
                    o.scale = 1,1,1
                o.select = True
        # Re-link to the scaled mesh
        bpy.ops.object.make_links_data(type='OBDATA')

# Reset active object and initial selection
bpy.context.scene.objects.active = active_obj
bpy.ops.object.select_all(action='DESELECT')
for o in initial_selected:
    o.select = True