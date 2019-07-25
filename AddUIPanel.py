import bpy
import northPole
import southPole
import lineSpawner
import addLines


class MagneticLinesUI(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Magnetic lines"
    bl_idname = "OBJECT_PT_magnetic_lines"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        # add north pole 
        row = layout.row()
        row.operator("magnet.add_north")
        # add south pole
        row = layout.row()
        row.operator("magnet.add_south")
        # add line spawner
        row = layout.row()
        row.operator("magnet.add_line_spawner")
        # grow lines
        row = layout.row()
        row.operator("magnet.add_lines")


def register():
    bpy.utils.register_class(MagneticLinesUI)
    bpy.utils.register_class(northPole.AddNorthPole)
    bpy.utils.register_class(southPole.AddSouthPole)
    bpy.utils.register_class(lineSpawner.AddLineSpawner)
    bpy.utils.register_class(addLines.AddLines)
    


def unregister():
    bpy.utils.unregister_class(MagneticLinesUI)


if __name__ == "__main__":
    
    register()
