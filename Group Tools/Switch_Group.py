import bpy

#bpy.ops.object.hide_view_clear()

for group in bpy.data.groups:
    for ob in group.objects:
        if ob.is_visible:
            pass
            #print(ob.name)
        else:
            print('nope')