import bpy
import bmesh


def add_box(width, height, depth):
    verts = [(+0.1, +0.1, -0.1),
             (+0.1, -0.1, -0.1),
             (-0.1, -0.1, -0.1),
             (-0.1, +0.1, -0.1),
             (+0.1, +0.1, +0.1),
             (+0.1, -0.1, +0.1),
             (-0.1, -0.1, +0.1),
             (-0.1, +0.1, +0.1),
             ]

    faces = [(0, 1, 2, 3),
             (4, 7, 6, 5),
             (0, 4, 5, 1),
             (1, 5, 6, 2),
             (2, 6, 7, 3),
             (4, 0, 3, 7),
            ]

    # apply size
    for i, v in enumerate(verts):
        verts[i] = v[0] * width, v[1] * depth, v[2] * height

    return verts, faces


from bpy.props import FloatProperty, BoolProperty, FloatVectorProperty


class AddNorthPole(bpy.types.Operator):
    bl_idname = "magnet.add_north"
    bl_label = "Add North Pole"
    bl_options = {'REGISTER', 'UNDO'}

    width = FloatProperty(
            name="Width",
            description="Box Width",
            min=0.01, max=100.0,
            default=1.0,
            )
    height = FloatProperty(
            name="Height",
            description="Box Height",
            min=0.01, max=100.0,
            default=1.0,
            )
    depth = FloatProperty(
            name="Depth",
            description="Box Depth",
            min=0.01, max=100.0,
            default=1.0,
            )

    # generic transform props
    view_align = BoolProperty(
            name="Align to View",
            default=False,
            )
    location = FloatVectorProperty(
            name="Location",
            subtype='TRANSLATION',
            )
    rotation = FloatVectorProperty(
            name="Rotation",
            subtype='EULER',
            )

    def execute(self, context):

        verts_loc, faces = add_box(self.width,
                                   self.height,
                                   self.depth,
                                   )

        mesh = bpy.data.meshes.new("NorthPole")

        bm = bmesh.new()

        for v_co in verts_loc:
            bm.verts.new(v_co)

        bm.verts.ensure_lookup_table()
        for f_idx in faces:
            bm.faces.new([bm.verts[i] for i in f_idx])

        bm.to_mesh(mesh)
        mesh.update()

        # add the mesh as an object into the scene with this utility module
        from bpy_extras import object_utils
        newNorth = object_utils.object_data_add(context, mesh, operator=self)

        if bpy.data.groups.get("northPoles", "") == "":
            bpy.data.groups.new("northPoles")
            bpy.data.groups["northPoles"].objects.link(newNorth.object)
        else:
            bpy.data.groups["northPoles"].objects.link(newNorth.object)
        
        newNorth.object.active_material = bpy.data.materials.new("northPole")
        newNorth.object.active_material.diffuse_color = (1,0,0)

        return {'FINISHED'}
