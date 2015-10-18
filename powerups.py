import pygame
import random
import CONFIG

class Coin():

    def __init__(self,width,height,x,y,color,direction):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 3
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.friendly = True
        self.direction = direction
        self.vel = 5
        self.id = 'coin'
        return

    def checkHitSpaceship(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):

            self.hit = True

    def checkBackWall(self,back_wall):
        if self.x      < 0:
            self.setAlive(False)
        return

    def move(self,attractlvl,whox,whoy):
        self.vel -= self.speed

        if self.vel < 0:
            self.vel = 0
        if self.direction == 'up':
            self.y -= self.vel
        elif self.direction == 'down':
            self.y += self.vel
        elif self.direction == 'left':
            self.x -= self.vel
        elif self.direction == 'right':
            self.x += self.vel
        elif self.direction == 'upright':
            self.y -= self.vel
            self.x += self.vel
        elif self.direction == 'upleft':
            self.y -= self.vel
            self.x -= self.vel
        elif self.direction == 'downright':
            self.y += self.vel
            self.x += self.vel
        elif self.direction == 'downleft':
            self.y += self.vel
            self.x -= self.vel
        else:
            self.x += self.vel
        if self.vel <= 0:
            self.x -= self.speed
            self.y += random.uniform(-2,2)
        distance = CONFIG.Distance(whox,whoy,self.x,self.y)

        if distance <=  300*(attractlvl/2):

            if self.y < whoy:
                self.y += attractlvl * .5
            if self.y > whoy:
                self.y -= attractlvl * .5


        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def getHit(self):
        return self.hit

    def getDimensions(self):
        return self.x, self.y, self.height, self.width

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


class MissileUp(Coin):



    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 5
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.friendly = True
        self.iswhat = 'coin'
        return

    def checkHitSpaceship(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):

            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) < back_wall:
            self.setAlive(False)
        return

    def move(self):
        self.x += self.speed
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


class BulletUp(Coin):



    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 5
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.friendly = True
        return

    def checkHitSpaceship(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):
        if (self.x + self.width) < back_wall:
            self.setAlive(False)
        return

    def move(self):

        self.x += self.speed
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

