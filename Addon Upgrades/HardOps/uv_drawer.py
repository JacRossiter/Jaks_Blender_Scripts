import bpy
from bgl import *
from mathutils import Vector
from .. graphics.rectangle import Rectangle
from .. overlay_drawer import show_custom_overlay, disable_active_overlays
from .. utils.blender_ui import get_location_in_current_3d_view, get_dpi_factor

class DrawObjectUVs(bpy.types.Operator):
    bl_idname = "hops.draw_object_uvs"
    bl_label = "Draw Object UVs"

    @classmethod
    def poll(cls, context):
        object = context.active_object
        if object is None: return False
        if object.type != "MESH": return False
        if object.mode != "OBJECT": return False
        if len(object.data.uv_layers) == 0: return False
        return True

    def execute(self, context):
        object = context.active_object

        disable_active_overlays()

        dpi_factor = get_dpi_factor()
        scale = 500 * dpi_factor
        margin = 30 * dpi_factor

        offset = get_location_in_current_3d_view("RIGHT", "BOTTOM",
                offset = Vector((-scale - margin, margin)) / 1,
                adapt_offset_to_dpi = False)

        uvs = get_uv_lines(object.data, offset, scale = scale)
        show_custom_overlay(draw_uvs,
            uvs = uvs, offset = offset, scale = scale,
            location_type = "CUSTOM",
            stay_time = 4,
            fadeout_time = 0.2)
        return {"FINISHED"}


def get_uv_lines(mesh, offset, scale):
    active_uv = mesh.uv_textures.active_index
    uv_layer = mesh.uv_layers[active_uv]
    uvs = [uv_loop.uv * scale + offset for uv_loop in uv_layer.data]

    uv_polygons = []
    append = uv_polygons.append
    for polygon in mesh.polygons:
        append([uvs[index] for index in polygon.loop_indices])

    return uv_polygons

def draw_uvs(display, uvs, offset, scale):
    transparency = display.transparency
    if transparency < 0.0001: return

    glEnable(GL_BLEND)

    dpi_factor = display.get_dpi_factor()

    bg = Rectangle(offset.x, offset.y, offset.x + scale, offset.y + scale)
    bg.color = (0, 0, 0, transparency * 0)
    bg.border_thickness = 2 * dpi_factor
    bg.border_color = (0, 0, 0, transparency / 8)
    bg.draw()

    glColor4f(0.8, 0.8, 0.8, transparency / 3)
    for polygon in uvs:
        glBegin(GL_POLYGON)
        for vertex in polygon:
            glVertex2f(*vertex)
        glEnd()
