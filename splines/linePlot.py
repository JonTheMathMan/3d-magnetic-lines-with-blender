import bpy
import math
import lineCalc

def getNextLinePoint(point1):
    if not isinstance(point1, lineCalc.Point):
        print("getNextLinePoint error: point1 must be an instance of Point")
        return

    if bpy.data.groups.get("northPoles", "") == "":
        print("getNextLinePoint error: no objects in northPoles group")
        return

    if bpy.data.groups.get("southPoles", "") == "":
        print("getNextLinePoint error: no objects in southPoles group")
        return

    repellingVectors = []
    for north in bpy.data.groups["northPoles"].objects:
        northAsPoint = lineCalc.Point(north.location[0], north.location[1], north.location[2])

        # get the relative vector's ratio of sides to hyptonuse as a new vector
        baseVector = lineCalc.getBaseVector(point1, northAsPoint)

        # get inverse square magnatude of the relative vector as a new vector
        inverseSquare = lineCalc.getScalarMultiple(
            1/math.pow(
                lineCalc.getDistance(point1, northAsPoint),
                2
                ),
            baseVector
            )

        # reverse the direction of the inverseSquare vector because the line is repelled by north
        negativeInverseSquare = lineCalc.getScalarMultiple(-1, inverseSquare)

        # hold in array for summing up the final vector direction to move the next line point in
        repellingVectors.append(negativeInverseSquare)
    

    attractingVectors = []
    for south in bpy.data.groups["southPoles"].objects:
        southAsPoint = lineCalc.Point(south.location[0], south.location[1], south.location[2])

        # get the relative vector's ratio of sides to hyptonuse as a new vector
        baseVector = lineCalc.getBaseVector(point1, southAsPoint)

        # get inverse square magnatude of the relative vector as a new vector
        inverseSquare = lineCalc.getScalarMultiple(
            1/math.pow(
                lineCalc.getDistance(point1, southAsPoint),
                2
                ),
            baseVector
            )
        
        # hold in array for summing up the final vector direction to move the next line point in
        attractingVectors.append(inverseSquare)
    
    # summing to get the final direction to move the next line point in
    repellingVector = lineCalc.Point(0,0,0)
    for repelling in repellingVectors:
        repellingVector = lineCalc.addPoints(repellingVector, repelling)
    
    attractingVector = lineCalc.Point(0,0,0)
    for attracting in attractingVectors:
        attractingVector = lineCalc.addPoints(attractingVector, attracting)
    
    finalVector = lineCalc.addPoints(repellingVector, attractingVector)

    # take the baseVector of the finalVector so that the line point can move a set distance
    baseFinalVector = lineCalc.getBaseVector(lineCalc.Point(0,0,0), finalVector)

    # move 0.1 in direction of the final vector
    return lineCalc.addPoints(point1, lineCalc.getScalarMultiple(0.1, baseFinalVector))

def getPointForBezier(point1):
    if not isinstance(point1, lineCalc.Point):
        print("getPointForBezier error: point1 must be an instance of Point")
        return
    
    return (
            (point1.X, point1.Y, point1.Z), 
            "AUTO", 
            "AUTO"
        )

def getSouthsAsLinePoints():
    if bpy.data.groups.get("southPoles", "") == "":
        print("getSouthsAsLinePoints error: no objects in southPoles group")
        return

    souths = bpy.data.groups["southPoles"].objects
    southPoints = []
    for southPole in souths:
        southPoints.append(
            lineCalc.Point(
                southPole.location[0],
                southPole.location[1],
                southPole.location[2]
                )
            )
    return southPoints

def plotNewLines():
    if bpy.data.groups.get("lineSpawners", "") == "":
        print("plotNewLines error: no objects in lineSpawners group")
        return

    southPoints = getSouthsAsLinePoints()
    
    # lineSegments are not euclidean lines segments - they are just start to stop of each spline curve.
    lineSegments = []
    for spawner in bpy.data.groups["lineSpawners"].objects:
        spawnerAsPoint = lineCalc.Point(spawner.location[0], spawner.location[1], spawner.location[2])

        count = 0
        segment = [getPointForBezier(spawnerAsPoint)]
        currentPoint = spawnerAsPoint
        stopOnContact = False
        while count < 300 and not stopOnContact:
            currentPoint = getNextLinePoint(currentPoint)
            pointForBezier = getPointForBezier(currentPoint)
            segment.append(pointForBezier)
            count += 1
            for south in southPoints:
                if lineCalc.getDistance(currentPoint, south) < 0.2:
                    stopOnContact = True
        
        lineSegments.append(segment)
    
    return lineSegments