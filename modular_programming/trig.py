import math

def get_sine(x):
    #x is in degrees
    angle_rad = math.radians(x)
    angle_sine = math.sin(angle_rad)

    return angle_rad

def get_tan(x):
    angle_rad = math.radians(x)
    angle_tan = math.tan(angle_rad)

    return angle_rad