import pygame
import random
from bullet import BadBullet
from bullet import BadMissile
from bullet import BadLaser
from powerups import *
from particle import Blast

class Boss(pygame.sprite.Sprite):
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
        self.fakeHit = False
        self.hit_points = 100
        self.vel = 0
        self.behavior = behavior
        self.shootDelay = 0
        self.hasCoin = True
        self.canBoom = True
        self.canGetHit = True
        return

    def __getitem__(self, item):
        return item

    def getAlive(self):
        return self.alive

    def fire(self, width, height, color):
        if self.alive== True:
            return BadBullet(width,height,(self.x - self.width) , (self.y + self.height),color)

    def bossFire(self, width, height, color):
        if self.alive== True:
            return BadBullet(width,height,self.x  , ((self.y + self.height)/2),color)



    def explode(self, poss, color,):
        #return Blast(self.x,self.y,width, height, color, speed, direction)
        return Fragment(poss,color)
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

    def beam(self,width,height,color,xoff=0,yoff=0):
        if self.alive== True:
            return BadLaser(width,height,(self.x + xoff) , (self.y + (self.height /2) - (height/2) + yoff),color)

    def tick(self,back_wall,upper_wall,lower_wall, spaceship_position,turrets):
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

        elif self.behavior == 4:

            if self.y <= 51:
                self.y = 51
                self.vel *=-1
            elif self.y >= 200:
                self.y = 200
                self.vel *= -1
            else: self.vel -=.001
            self.new_y = self.y+self.vel
            if self.shootDelay == 30:
                pass#self.fire(20,20,(255,255,255))
            if self.x <= 800:
                self.speed = 0
            if self.hasTurrets(turrets) == True:
                self.canGetHit = True
            else:
                self.canGetHit = False
        elif self.behavior == 5:

            if self.y <= 75:
                self.y = 76
                self.vel *=-1
            elif self.y >= 425:
                self.y = 424
                self.vel *= -1
            else: self.vel -= 1
            self.new_y = self.y+self.vel
            if self.shootDelay == 30:
                self.fire(20,20,(255,255,255))
            if self.x <= 700:
                self.speed = 0

        elif self.behavior == 6:

            if self.y <= 400:
                self.y = 400
                self.vel *=-1
            elif self.y >= 695:
                self.y = 695
                self.vel *= -1
            else: self.vel +=1
            self.new_y = self.y+self.vel
            if self.shootDelay == 30:
                self.fire(20,20,(255,255,255))
            if self.x <= 700:
                self.speed = 0

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
    
    def hasTurrets(self, turrets):
        if turrets  <= 0:
            return True
    
    def draw(self, surface):

        if self.hit == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, (155,55,55), rect)
            self.hit = False
        elif self.fakeHit == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, (55,20,20), rect)
            self.fakeHit = False
        else:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, self.color, rect)

        return

    def drawHealth(self,surface):
        rect = pygame.Rect( 100, 45, 8*self.hit_points, 20 )
        pygame.draw.rect(surface, (155,55,55), rect)
        return
        
