import math

class Point:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
        
        if math.isnan(self.X):
            print("Point.X must be a number")
        
        if math.isnan(self.Y):
            print("Point.Y must be a number")
        
        if math.isnan(self.Z):
            print("Point.Z must be a number")


def getDistance(point1,point2):
    if not isinstance(point1, Point):
        print("getDistance error: point1 must be an instance of Point")
    if not isinstance(point2, Point):
        print("getDistance error: point2 must be an instance of Point")

    deltaX = point2.X - point1.X
    deltaY = point2.Y - point1.Y
    deltaZ = point2.Z - point1.Z
    return math.sqrt(
        math.pow(deltaX, 2) +
        math.pow(deltaY, 2) +
        math.pow(deltaZ, 2)
    )

# getBaseVector gets the ratio of the sides to the hypotenuse as an instance of Point for the relative vector between 2 points. Point(x/h, y/h, z/h)
def getBaseVector(point1, point2):
    if not isinstance(point1, Point):
        print("getBaseVector error: point1 must be an instance of Point")
        return
    if not isinstance(point2, Point):
        print("getBaseVector error: point2 must be an instance of Point")
        return

    distance = getDistance(point1, point2)

    deltaX = point2.X - point1.X
    deltaY = point2.Y - point1.Y
    deltaZ = point2.Z - point1.Z

    return Point(deltaX/distance, deltaY/distance, deltaZ/distance)

# addPoints adds to points together with the math of a vector or matrix [x_1 + x_2, y_1 + y_2, z_1 + z_2]
def addPoints(point1, point2):
    if not isinstance(point1, Point):
        print("addPoints error: point1 must be an instance of Point")
        return
    if not isinstance(point2, Point):
        print("addPoints error: point2 must be an instance of Point")
        return

    newPoint = Point(
        point1.X + point2.X,
        point1.Y + point2.Y,
        point1.Z + point2.Z
    )
    
    return newPoint

# getScalarMultiple gets the point passed with each component of the point multiplied by the multiple
def getScalarMultiple(multiple, point1):
    if math.isnan(multiple):
        print("getScalerMultiple error: multiple must be a number")
        return
    
    if not isinstance(point1, Point):
        print("getScalerMultiple error: point1 must be an instance of Point")
        return
    
    return Point(multiple * point1.X, multiple * point1.Y, multiple * point1.Z)
