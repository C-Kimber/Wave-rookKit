import pygame
import random
import CONFIG


class Fragment(pygame.sprite.Sprite):
        """a fragment of an exploding Bird"""
        gravity = False # fragments fall down ?
        def __init__(self, pos, color):
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.a = 1
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.image = pygame.Surface((50,50))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, (color), (25,25), random.randint(5,10))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.lifetime =  random.uniform(.1,.5) # max 6 seconds
            self.time = 0.0

            self.fragmentmaxspeed = (random.randint(1000,2000)*self.a) # try out other factors !
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)


        def update(self, seconds):
            self.time += seconds
            self.a += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds

            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)

class Star():

    def __init__(self,width,height,x,y,color,speed, direction='normal'):
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.speed  = speed
        self.color  = color
        self.alive  = True
        self.hit    = False
        self.direction = direction
        self.force = 0
        return

    def checkHit(self,x,y,w,h):
        if self.hitRectangle(x, y, w, h):
            self.setAlive(False)
            self.hit = True

    def checkBackWall(self,back_wall):

        if self.x <= 400:
            self.alive = False

        return

    def move(self,whox,whoy):
        if self.direction == 'up':
            self.y -= self.speed/7
        if self.direction == 'down':
            self.y += self.speed/7
        if self.direction == 'up2':
            self.y -= self.speed/3
        if self.direction == 'down2':
            self.y += self.speed/3
        self.x -= self.speed        #always move it along the x-axis
        distance = CONFIG.Distance(whox,whoy,self.x,self.y)
        if self.color == (255,255,255):
            self.force = .4
        if self.color == (155,155,155):
            self.force = .3
        if self.color == (100,100,100):
            self.force = .2
        if self.color == (55,55,55):
            self.force = .1

        if distance <=  100:

            if self.y < whoy:
                self.y +=  self.force
            if self.y > whoy:
                self.y -= self.force
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

class Blast():

    def __init__(self,x,y,w,h,color,speed,direction):
        self.x = x
        self.y = y
        self.width = w * 4
        self.height = h *4
        self.speed = speed
        self.direction = direction
        self.color = color
        self.alive = True
        self.hit = False
        self.vel = 10
        n =int((self.height+self.width)/20)
        m = int((self.height+self.width)/6)
        self.radius = random.randint(n,m)
        return


    def move(self):
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
            self.x += self.vel        #always move it along the x-axis
            
        a =int(self.color[0]-self.vel)
        b= int(self.color[1]-self.vel)
        c=int(self.color[2]-self.vel)
        if a < 0:
            a= 0
        if c < 0:
            c= 0
        if b < 0:
            b= 0

        self.color =(a,b,c)

        if self.color == (0,0,0):
            self.alive = False
        return

    def setAlive(self,alive):
        self.alive = alive
        return
    def checkWalls(self,left, top, right, bottom):
        if self.x < left:
            self.x = left
        if self.x-self.width > right:
            self.x = right-self.width
        if self.y+self.height > bottom:
            self.y = bottom+self.height
        if self.y < top:
            self.y = top


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
       # rect = pygame.Rect( self.x, self.y, self.width, self.height )
       # pygame.draw.rect(surface, self.color, rect)


        pygame.draw.circle(surface, self.color,(int(self.x),int(self.y)),self.radius)
        return




