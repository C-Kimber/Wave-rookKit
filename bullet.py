import pygame
from pygame import *
from random import *
from math import *
import math
from particle import *
from particle import Fragment
import random


"""class AngledBullet():

    def __init__(self,width,height,x,y,color, angle):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 14
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.angle = angle
        return

    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return
    def checkWall(self):
        if (self.x + self.width) < 0 \
        or self.x > 1200\
        or self.y > 800\
        or self.y < 0:
             self.setAlive(False)

    def setAngle(self, angle):
        self.angle = angle

    def modularAngle(self,angle):
        self.angle += angle

    def update(self):
        self.x += math.sin(-self.angle) * self.speed
        self.y -= math.cos(-self.angle) * self.speed

        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return
    """
class AngledBullet():

    def __init__(self,width,height,x,y,color, angle):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 5
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.angle = angle
        return

    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return
    def checkWall(self):
        if (self.x + self.width) < 0 \
        or self.x > 1200\
        or self.y > 800\
        or self.y < 0:
             self.setAlive(False)

    def setAngle(self, angle):
        self.angle = angle

    def modularAngle(self,angle):
        self.angle += angle

    def update(self,x,y):
        print self.angle
        if y > self.y:
            self.angle = self.Angled2(x,y)
        else:
            self.angle = self.Angled1(x,y)


        self.y -= math.cos(self.angle) * (self.speed)
        if self.x > x:
           self.x += math.sin(self.angle) * (self.speed)
        else:
            self.x -= self.speed


        return

    def Angled1(self,x,y):
        dx = x - self.x
        dy = y - self.y
        angle = math.atan2(dy,dx) * math.pi #/ 180
        return angle
    def Angled2(self,x,y):
        dx = self.x - x
        dy = self.y - y
        angle = math.atan2(dy,dx) * math.pi #/ 180
        return angle


    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return


class Bullet():

    def __init__(self,width,height,x,y,color, direction='normal'):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 15
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.direction = direction
        return

    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True


        return

    def moveBullet(self):
        if self.direction == 'up':
            self.y -= self.speed/7
        if self.direction == 'down':
            self.y += self.speed/7
        if self.direction == 'up2':
            self.y -= self.speed/3
        if self.direction == 'down2':
            self.y += self.speed/3
        self.x += self.speed        #always move it along the x-axis
        return

    def setAlive(self,alive):
        self.alive = alive
        return
    
    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False
    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return


class Missile(Bullet):



    def __init__(self,width,height,x,y,color,eby):
        self.alive = True
        self.hit    = False
        self.eby = eby
        self.yvel = 0
        self.xvel = -10
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.canBoom = True

        return

    def moveMissile(self, y):

        self.n = 0
        self.xvel += 2
        if y == 0:

            if self.n == 1:
                self.yvel += -.5
            else:
                self.yvel += .025
        elif y == 1:

            if self.n == 1:
                self.yvel += .5
            else:
                self.yvel -= .025

        if self.xvel > 18:
            self.xvel = 18
        if self.yvel > 3:
            self.yvel = random.randint(-5,5)
            self.n = 1
        if self.yvel < -3:
            self.yvel = random.randint(-5,5)
            self.n = 1




        self.x += self.xvel

        self.y+= self.yvel +self.eby
        return

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)

    def checkHitBaddie(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return


    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

class Laser():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x-50
        self.y      = y
        self.speed  = 70
        self.color  = color
        self.radius = 0.4
        self.alive  = True
        self.hit    = False
        return




    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):

            self.hit = True

    def setHit(self, hit):
        self.hit = hit

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall+400:
            self.setAlive(False)
        return

    def moveLaser(self):
        self.x += self.speed
        self.y += random.uniform(-.5,.5)
        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def draw(self, surface):
        rect         = pygame.Rect( self.x, self.y, self.width, self.height )
        radius       = self.radius
        rect         = Rect(rect)
        color        = self.color
        color        = Color(*color)
        alpha        = color.a
        color.a      = 0
        pos          = rect.topleft
        rect.topleft = 0,0
        rectangle    = Surface(rect.size,SRCALPHA)

        circle       = Surface([min(rect.size)*2]*2,SRCALPHA)
        draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
        circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

        radius              = rectangle.blit(circle,(0,0))
        radius.bottomright  = rect.bottomright
        rectangle.blit(circle,radius)
        radius.topright     = rect.topright
        rectangle.blit(circle,radius)
        radius.bottomleft   = rect.bottomleft
        rectangle.blit(circle,radius)

        rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
        rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

        rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
        rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

        return surface.blit(rectangle,pos)

       # rect = pygame.Rect( self.x, self.y, self.width, self.height )
       # pygame.draw.rect(surface, self.color, rect)
        #return

class Lightning():

    def __init__(x,y,size,ang,count):
        pass

class BadBullet():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 14
        self.color  = color
        self.alive  = True
        self.hit    = False
        return

    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if self.x  < 0:
            self.setAlive(False)
        return

    def moveBullet(self):
        self.x -= self.speed
        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)

    def getDimensions(self):
        return self.x, self.y, self.height, self.width

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return


class BadMissile(BadBullet):



    def __init__(self,width,height,x,y,color):
        self.alive = True
        self.hit    = False
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


        return

    def moveMissile(self, y):

        self.n = 0
        self.xvel += 1
        if y == 0:
            self.yvel += .1
            if self.n == 1:
                self.yvel += -.2
        elif y == 1:
            self.yvel -= .1
            if self.n == 1:
                self.yvel += .2

        if self.xvel > 8:
            self.xvel = 8
        if self.yvel > 2:
            self.yvel = 0
            self.n = 1
        if self.yvel < -2:
            self.yvel = 0
            self.n = 1




        self.x -= self.xvel
        self.y+= self.yvel
        return

    def checkHitBaddie(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)


    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return



class BadLaser():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x-50
        self.y      = y
        self.speed  = -70
        self.color  = color
        self.radius = 0.4
        self.alive  = True
        self.hit    = False
        return




    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):

            self.hit = True

    def setHit(self, hit):
        self.hit = hit

    def checkBackWall(self,back_wall):
        if (self.x + self.width) < back_wall:
            self.setAlive(False)
        return

    def moveLaser(self):
        self.x += self.speed
        self.y += random.uniform(-.5,.5)
        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)

    def draw(self, surface):
        rect         = pygame.Rect( self.x, self.y, self.width, self.height )
        radius       = self.radius
        rect         = Rect(rect)
        color        = self.color
        color        = Color(*color)
        alpha        = color.a
        color.a      = 0
        pos          = rect.topleft
        rect.topleft = 0,0
        rectangle    = Surface(rect.size,SRCALPHA)

        circle       = Surface([min(rect.size)*2]*2,SRCALPHA)
        draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
        circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

        radius              = rectangle.blit(circle,(0,0))
        radius.bottomright  = rect.bottomright
        rectangle.blit(circle,radius)
        radius.topright     = rect.topright
        rectangle.blit(circle,radius)
        radius.bottomleft   = rect.bottomleft
        rectangle.blit(circle,radius)

        rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
        rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

        rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
        rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

        return surface.blit(rectangle,pos)

       # rect = pygame.Rect( self.x, self.y, self.width, self.height )
       # pygame.draw.rect(surface, self.color, rect)
        #return

"""class HomingBullet(object):
    def get_angle(self,origin, destination):


        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]
        return atan2(-y_dist, x_dist) % (2 * pi)

    def __init__(self, pos, target_pos, speed=2.5):
        self.pos = pos
        self.angle = self.get_angle((self.pos), (target_pos))
        self.speed = speed
        self.rect = pygame.Rect(0, 0, 2, 2)
        self.rect.center = pos
        self.alive = True

    def update(self, target_pos):
        self.angle = self.get_angle(self.pos, target_pos)
        self.pos = CONFIG.project(self.pos, self.angle, self.speed)
        self.rect.center = 200,200

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color("white"), self.rect)"""

class HomingBullet():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 14
        self.color  = color
        self.alive  = True
        self.hit    = False

        return

    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) > back_wall:
            self.setAlive(False)
        return

    def update(self,target_y):
        if self.y <= target_y:
            self.y += 5
        elif self.y >= target_y:
            self.y -= 5
        self.x -= self.speed        #always move it along the x-axis
        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def hitRectangle(self, x, y, w, h):
        if( ((self.x + self.width) >= x) and
            (self.x <= x + w) ):
            if( ((self.y + self.height) >= y) and
                (self.y <= y + h)) :
                return True
        return False

    def explode(self, poss,color):
        #return  Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)

    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return

