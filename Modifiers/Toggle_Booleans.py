import bpy

# Toggle Booleans

o = bpy.context.scene.objects.active
x = True

if o.modifiers[0].show_viewport:
    x = False

for m in o.modifiers:
    m.show_viewport = x