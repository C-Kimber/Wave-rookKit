import pygame
import random

class Baddie():

    def __init__(self,width,height,x,y,color, speed):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.new_x  = x
        self.new_y  = y
        self.speed  = speed
        self.color  = color
        self.alive  = True
        self.hit_points = 1
        self.vel = 0
        return


    def tick(self,back_wall,upper_wall,lower_wall, spaceship_position):
        self.new_x = self.x - self.speed
        if self.hit_points == 2:
            if self.y >= spaceship_position:
                self.vel -= .1
            else:
                self.vel += .1
            self.new_y = self.y + self.vel
        elif self.hit_points == 1 :
            if self.y >= spaceship_position:
                self.vel -= 1
            else:
                self.vel += 1
            self.new_y = self.y + self.vel
        elif self.hit_points >= 5:
            if self.y >= spaceship_position:
                self.vel -= .001
            else:
                self.vel += .001
            self.new_y = self.y + self.vel
        else:
            self.new_y = self.y + random.randint(-1,1)
        if self.new_x < back_wall:
            self.setAlive(False)
        else:
            self.x = self.new_x
        if self.new_y < upper_wall:
            self.new_y = upper_wall
            self.vel = 0
        elif self.new_y + self.height > lower_wall:
            self.new_y = lower_wall - self.height
            self.vel = 0
        self.y = self.new_y
        return self.alive



    def getAlive(self):
        return self.alive

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
    
    def draw(self, surface):
        rect = pygame.Rect( self.x, self.y, self.width, self.height )
        pygame.draw.rect(surface, self.color, rect)
        return
        
