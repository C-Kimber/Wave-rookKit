import math
from math import sin, cos, pi, atan2
from game_mouse import Game





GAME_STATE  = 0
MINI_STATE = 0


def Distance(x,y,x2,y2):
    return math.sqrt(((x-x2)**2)+((y -y2)**2))

def get_angle(origin, destination):


    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return atan2(-y_dist, x_dist) % (2 * pi)

def project(pos, angle, distance):
    """Returns tuple of pos, projected distance at angle
    adjusted for pygame's y-axis.
    """




