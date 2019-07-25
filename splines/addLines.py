import bpy
import linePlot

def makeBezierSpline(curve, points):
    spline = curve.splines.new("BEZIER")
    lenPoints = len(points)
    spline.bezier_points.add(lenPoints-1)
    for (index, point) in enumerate(points):
        bezier = spline.bezier_points[index]
        (bezier.co, bezier.handle_left_type, bezier.handle_right_type) = point
        
    return

class AddLines(bpy.types.Operator):
    bl_idname = "magnet.add_lines"
    bl_label = "Add magnetics lines"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        curve = bpy.data.curves.new("MyCurve", "CURVE")
        curveObject = bpy.data.objects.new("MagneticLines", curve)
        scene = bpy.context.scene
        scene.objects.link(curveObject)
        scene.objects.active = curveObject

        curve.dimensions = "3D"

        # [
        #   [
        #         (
        #             (0,0,0), 
        #             "AUTO", 
        #             "AUTO"
        #         ), 
        #         (
        #             (0,0,1), 
        #             "AUTO", 
        #             "AUTO"
        #         )
        #   ]
        # ]

        plottedLines = linePlot.plotNewLines()

        for line in plottedLines:
            makeBezierSpline(
                curve, 
                line
            )

        return {'FINISHED'} 