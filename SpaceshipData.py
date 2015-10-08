import pygame
import random
from spaceship import Spaceship
from baddie import Baddie

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("monospace",10)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/3
        self.spaceship_width = 20
        self.spaceship_height = 10
        self.spaceship_health = 3
        self.spaceship_speed = 5

        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (255,255,255),self.spaceship_health)
        self.spaceship_y = self.spaceship.spaceshipPosition()[1]

        self.bullets = []
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (255,255,255)

        self.missiles = []
        self.misslen = 0
        self.missile_width = 15
        self.missile_height = 5
        self.missile_color = (55,44,44)

        self.badBullets = []
        self.badBullet_width = 5
        self.badBullet_height = 5
        self.badBullet_color = (0,255,255)

        self.baddies = []
        self.baddie_width = 20
        self.baddie_height = 20
        self.baddie_color = (0,155,0)
        self.score = 0

        self.wave1 = True
        self.w1 = [1,1,2,2,1,2,1,1,0]

        self.delay = 0
        self.shootDelay = 0

        self.a = -1
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):

        if pygame.K_LEFT in keys or pygame.K_a in keys:
            self.spaceship.moveLeft(self.spaceship_speed)
        if pygame.K_RIGHT in keys or pygame.K_d in keys:
            self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
        if pygame.K_UP in keys or pygame.K_w in keys:
            self.spaceship.moveUp(self.spaceship_speed)
        if pygame.K_DOWN in keys or pygame.K_s in keys:
            self.spaceship.moveDown(self.spaceship_speed,self.height)

        """if pygame.K_SPACE in newkeys or 1 in newbuttons:
            self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
            self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color))
            if self.misslen ==0:
                self.misslen=1
            else:
                self.misslen = 0"""

        self.shootDelay += 1

        if self.shootDelay > 30:
            self.shootDelay = 0


        if pygame.K_SPACE in keys or 1 in buttons:

            if self.shootDelay == 10 or self.shootDelay == 20 or self.shootDelay == 30:
                self.bullets.append(self.spaceship.fire(self.bullet_width,self.bullet_height,self.bullet_color))
            if self.shootDelay == 15:
                if self.misslen ==0:
                    self.misslen=1
                else:
                    self.misslen = 0
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color))
            if self.shootDelay == 30 :

                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color))

        self.delay += 1
        if self.delay >= 120:
            self.delay = 0

        if self.spaceship.health > 0:


            """ if random.randint(1, self.frame_rate/2) == 1:
                self.addRandBaddie()
            elif random.randint(1, self.frame_rate) == 1:
                self.addRandStrongBaddie()
            elif self.score == 1800:
                self.addBigBaddie()
                self.score += 5"""


            #wave fucntionality
            if self.wave1 == True:

                if self.delay == 60:


                    self.a+=1
                    i = self.w1[self.a]

                    #print i

                    if i == 1:

                        self.addBaddie(100)
                        self.addBaddie(200)
                        self.addBaddie(300)
                        self.addBaddie(400)
                        self.addBaddie(500)

                    elif i == 2:

                        self.addStrongBaddie(100)
                        self.addBaddie(200)
                        self.addStrongBaddie(300)
                        self.addBaddie(400)
                        self.addStrongBaddie(500)

                    elif i == 0:
                        self.wave1 = False




        self.spaceship.tick()


        for bullet in self.bullets:
            bullet.moveBullet()
            bullet.checkBackWall(self.width)

        for bbullet in self.badBullets:
            bbullet.moveBullet()
            bbullet.checkBackWall(0)
            if not bbullet.alive:
                continue
            x,y,h,w = bbullet.getDimenstions()
            self.spaceship.checkHit(x,y,h,w)
            if self.spaceship.hit == True:
                self.spaceship.hit = False
                self.spaceship_health -= 1


        self.spaceship_y = self.spaceship.spaceshipPosition()[1]
        for baddie in self.baddies:

            baddie.tick(0,0,self.height, self.spaceship_y)


            if not baddie.alive:
                continue
            x,y,w,h = baddie.getDimensions()
            n = y
            self.spaceship.checkHit(x,y,w,h)

            if self.spaceship.getHit():
                baddie.decreaseHitPoints(99)
                self.spaceship.hit = False
            if baddie.behavior == 3 or baddie.behavior == 1:
                if self.shootDelay == 10 or self.shootDelay == 20 or self.shootDelay == 30:
                    self.badBullets.append(baddie.fire(self.bullet_width,self.bullet_height,self.bullet_color))
        for missile in self.missiles:


            missile.moveMissile(self.misslen)




        for bullet in self.bullets:
            if not bullet.alive:
                continue
            for baddie in self.baddies:
                if not baddie.alive:
                    continue
                x,y,w,h = baddie.getDimensions()
                bullet.checkHit(x,y,w,h)

                if bullet.getHit():
                    bullet.setAlive(False)
                    baddie.decreaseHitPoints(1)
                    bullet.hit = False
                    self.score += 15

        for missile in self.missiles:
            if not missile.alive:
                continue
            for baddie in self.baddies:
                if not baddie.alive:
                    continue
                x,y,w,h = baddie.getDimensions()
                missile.checkHitBaddie(x,y,w,h)
                if missile.getHit():
                    missile.setAlive(False)
                    baddie.decreaseHitPoints(3)
                    missile.hit = False
                    self.score += 15

        live_bullets = []
        live_baddies = []
        live_missiles = []
        live_badBullets = []
        live_projectiles =[]
        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for bbullet in self.badBullets:
            if bbullet.alive:
                live_bullets.append(bbullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)
        for missile in self.missiles:
            if missile.alive:
                live_missiles.append(missile)

        self.badBullets = live_badBullets
        self.bullets = live_bullets
        self.baddies = live_baddies
        self.missiles = live_missiles

        return

    def addRandBaddie(self):
        new_baddie = Baddie( self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color, 3, 0)
        self.baddies.append( new_baddie )
                   
        return

    def addRandStrongBaddie(self):
        new_baddie = Baddie(self.baddie_width, self.baddie_height, self.width, random.randint(0, (self.height-self.baddie_height)), (155,0,0), 2, 1)
        new_baddie.setHitPoints(2)
        self.baddies.append(new_baddie)
        return

    def addBaddie(self, height):
        new_baddie = Baddie( self.baddie_width, self.baddie_height, self.width, height, self.baddie_color, 3, 0 )
        self.baddies.append( new_baddie )

        return

    def addStrongBaddie(self, height):
        new_baddie = Baddie(self.baddie_width, self.baddie_height, self.width, height, (155,0,0), 2, 1)
        new_baddie.setHitPoints(2)
        self.baddies.append(new_baddie)
        return

    def addBigBaddie(self):
        new_baddie = Baddie(self.baddie_width*5, self.baddie_height*5, self.width, 200, (55,0,0), 1, 3)
        new_baddie.setHitPoints(15)
        self.baddies.append(new_baddie)
        return

    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        self.spaceship.draw(surface)
        myfont = self.font2
        label = myfont.render("Score "+str(self.score), 1, (255,255,0))
        surface.blit(label, (480, 20))

        if self.spaceship.health == 3:
            rect = pygame.Rect( 20, 20, 20, 20 )
            pygame.draw.rect(surface, (255,0,0), rect)
            rect = pygame.Rect( 50, 20, 20, 20 )
            pygame.draw.rect(surface, (255,0,0), rect)
            rect = pygame.Rect( 80, 20, 20, 20 )
            pygame.draw.rect(surface, (255,0,0), rect)
        if self.spaceship.health == 2:
            rect = pygame.Rect( 50, 20, 20, 20 )
            pygame.draw.rect(surface, (255,0,0), rect)
            rect = pygame.Rect( 20, 20, 20, 20 )
            pygame.draw.rect(surface, (255,0,0), rect)
        if self.spaceship.health == 1:
            rect = pygame.Rect( 20, 20, 20, 20 )
            pygame.draw.rect(surface, (255,0,0), rect)


        for bullet in self.bullets:
            bullet.draw(surface)
        for missile in self.missiles:
            missile.draw(surface)
        for bbullet in self.badBullets:
            bbullet.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)
        return

    
    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return
