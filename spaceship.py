import pygame
from bullet import *
from particle import Blast
from particle import Fragment


class Spaceship():

    def __init__(self,width,height,x,y,color, health):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        self.health = health
        self.alive = True
        self.hit = False
        self.invinsible = False
        self.cannonlvl = 0
        self.bullet_up = 1
        self.missile_up =0
        self.laser_up =0
        self.canBoom =True
        self.friendly = True
        self.magnet = 1
        self.pos = x,y
        return


    def spaceshipPosition(self):
        return self.x, self.y

    def isAlive(self):
        if self.health <= 0:
            self.setAlive(False)
    def health(self):
        return self.health

    def setAlive(self, alive):
        self.alive = alive
    def tick(self):
        pass #self.isAlive()

    def explode(self,poss, color):

        return Fragment(poss,color)


    def checkHit(self,x,y,w,h):
        if self.invinsible == False:
            if self.alive == True:
                if self.hitRectangle(x, y, w, h):
                    self.hit = True
    def checkHitFriendly(self, x,y,w,h):
        if self.alive == True:
            if self.hitRectangle(x, y, w, h):
                self.hit = True

    def getHit(self):
        return self.hit

    def moveLeft(self, dx):
        if self.alive == True:
            self.x -= dx
            # check the wall
            if self.x < 0:
                self.x = 0
        return

    def moveRight(self, dx, upper_limit):

        if self.alive == True:
            self.x += dx
            # check the wall
            if self.x > upper_limit:
                self.x = upper_limit
        return

    def moveUp(self, dy):
        if self.alive == True:
            self.y -= dy
            # check the wall
            if self.y < 50:
                self.y = 50
        return

    def moveDown(self, dy, board_height):
        if self.alive == True:
            self.y += dy
            # check the wall
            if self.y > board_height - self.height:
                self.y = board_height - self.height
        return

    def hitRectangle(self, x, y, w, h):
        if self.alive == True:
           if( ((self.x + self.width) >= x) and
               (self.x <= x + w) ):
               if( ((self.y + self.height) >= y) and
                   (self.y <= y + h)) :
                   return True
           return False

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def seekingFire(self,start_pos, target_pos, speed ):
        if self.alive == True:
            return HomingBullet(start_pos,target_pos,speed)

    def fire(self,width,height,color,direction,xoff=0,yoff=0,):
        if self.alive == True:
            return Bullet(width,height,(self.x + self.width + xoff) , (self.y + (self.height /2) - (height/2) + yoff),color,direction)


    def launch(self,width,height,color,xoff=0,yoff=0,eby=0):
        if self.alive== True:

            return Missile(width,height,(self.x + self.width + xoff) , (self.y + (self.height /2) - (height/2) + yoff),color,eby)

    def beam(self,width,height,color,xoff=0,yoff=0):
        if self.alive== True:
            return Laser(width,height,(self.x + self.width + xoff) , (self.y + (self.height /2) - (height/2) + yoff),color)

    def draw(self, surface):
        if self.alive == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            if self.invinsible == True:
                pygame.draw.rect(surface, (255,55,55), rect)
            else:
                pygame.draw.rect(surface, self.color, rect)

        return
        
