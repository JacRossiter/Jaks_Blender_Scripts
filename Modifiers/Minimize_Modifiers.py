import bpy

# Minimise Modifiers

o = bpy.context.scene.objects.active
x = True

if o.modifiers[0].show_expanded:
    x = False


for m in o.modifiers:
    m.show_expanded = x

bpy.ops.object.editmode_toggle()
bpy.ops.object.editmode_toggle()

