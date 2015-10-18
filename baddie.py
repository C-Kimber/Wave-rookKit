import pygame
import random
from bullet import BadBullet
from bullet import BadMissile
from powerups import *
from particle import Blast

class Baddie(pygame.sprite.Sprite):
    def __init__(self,id,width,height,x,y,color, speed, behavior):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.id = id
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.speed  = speed
        self.color  = color
        self.alive  = True
        self.hit = False
        self.hit_points = 1
        self.vel = 0
        self.behavior = behavior
        self.shootDelay = 0
        self.hasCoin = True
        self.canBoom = True
        return

    def __getitem__(self, item):
        return item

    def getAlive(self):
        return self.alive

    def fire(self, width, height, color):
        if self.alive== True:
            return BadBullet(width,height,(self.x - self.width) , (self.y + self.height),color)

    def package(self, width, height, color,direction):
        return Coin(width,height,(self.x - self.width) , (self.y - (self.height /2) - (height/2)),color,direction)

    def explode(self, width, height, color,speed, direction):
        return Blast(self.x,self.y,width, height, color, speed, direction)

    def getDimensions(self):
        return self.x,self.y,self.width,self.height

    def setAlive(self,alive):
        self.alive = alive

    def setHitPoints(self, hit_points):
        self.hit_points = hit_points
        return

    def decreaseHitPoints(self, damage):
        self.hit_points = self.hit_points - damage
        if self.hit_points <= 0:
            self.setAlive(False)

    def tick(self,back_wall,upper_wall,lower_wall, spaceship_position):
        self.shootDelay += 1

        if self.hit_points <= 0:
            self.alive = False

        if self.shootDelay > 30:
            self.shootDelay = 0

        self.new_x = self.x - self.speed
        if self.behavior == 0:
            if self.y >= spaceship_position:
                self.vel -= .1
            else:
                self.vel += .1
            self.new_y = self.y + self.vel

        elif self.behavior == 1 :

            if self.x <= 400:

                self.new_x = 400

            if self.y >= spaceship_position:
                self.vel -= .5
            else:
                self.vel += .5
            self.new_y = self.y + self.vel


        elif self.behavior == 3:
            if self.y >= spaceship_position:
                self.vel -= .001
            else:
                self.vel += .001
            self.new_y = self.y + self.vel
            if self.shootDelay == 30:
                self.fire(20,20,(255,255,255))
        else:
            self.new_y = self.y + random.randint(-1,1)


        if self.new_x < back_wall:
            self.setAlive(False)
        else:
            self.x = self.new_x
        if self.new_y < upper_wall+50:
            self.new_y = upper_wall+50
            self.vel = 0
        elif self.new_y + self.height > lower_wall:
            self.new_y = lower_wall - self.height
            self.vel = 0
        self.y = self.new_y
        return self.alive
    
    def draw(self, surface):

        if self.hit == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, (255,255,255), rect)
            self.hit = False
        else:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, self.color, rect)

        return
        
