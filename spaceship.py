import pygame
from bullet import Bullet
from bullet import Missile


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
        self.isAlive()

    def checkHit(self,x,y,w,h):
        if self.alive == True:
            if self.hitRectangle(x, y, w, h):
                self.health -= 1
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
            if self.y < 0:
                self.y = 0
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


    def fire(self,width,height,color):
        if self.alive == True:
            return Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)


    def launch(self,width,height,color):
        if self.alive== True:
            return Missile(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)
    def draw(self, surface):
        if self.alive == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, self.color, rect)
        return
        
