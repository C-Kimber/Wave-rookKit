import math
from math import sin, cos, pi, atan2
import math
from game_mouse import Game





GAME_STATE  = 0
MINI_STATE = 0
GRAD = math.pi / 180


def Distance(x,y,x2,y2):
    return math.sqrt(((x-x2)**2)+((y -y2)**2))



def project(pos, angle, distance):
    """Returns tuple of pos, projected distance at angle
    adjusted for pygame's y-axis.
    """




