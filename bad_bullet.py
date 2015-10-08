import pygame

class BadBullet():

    def __init__(self,width,height,x,y,color):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = 7
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

    def move(self):
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
