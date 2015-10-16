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
        self.upper_limit = self.width/2
        self.spaceship_width = 20
        self.spaceship_height = 10
        self.spaceship_health = 3
        self.spaceship_speed = 5

        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (255,255,255),self.spaceship_health)
        self.spaceship_y = self.spaceship.spaceshipPosition()[1]

        self.coins = []
        self.coinn = 0
        self.coin_width = 10
        self.coin_height = 10
        self.coin_color = (255,255,0)

        self.bullets = []
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (255,255,255)

        self.lasers = []
        self.laser_width = 80
        self.laser_height = 10
        self.laser_color = (255,55,55)

        self.bups = []
        self.bup_width = 8
        self.bup_height = 8
        self.bup_color = (144,144,144)

        self.mups = []
        self.mup_width = 8
        self.mup_height = 8
        self.mup_color = (144,144,144)

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
        self.laserDelay = 0

        self.a = -1

        self.bullet_up = 0
        self.missile_up = 1


        self.invinsiblen = 0
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

        self.invinsiblen -= 1

        if self.invinsiblen < 0:
            self.invinsiblen = 0
            self.spaceship.invinsible = False

        if self.invinsiblen > 0:
            self.spaceship.invinsible = True

        if self.shootDelay > 30:
            self.shootDelay = 0


        if pygame.K_SPACE in keys or 1 in buttons:
            self.shootBullet(self.spaceship)
            self.shootMissile(self.spaceship)
            self.shootLaser(self.spaceship)

        if self.laserDelay >= 90:
            self.laserDelay = -20

        self.delay += 1
        if self.delay >= 120:
            self.delay = 0

        if self.spaceship.health > 0:


           # if random.randint(1, self.frame_rate/2) == 1:
            #    self.addRandStrongBaddie()


            #wave fucntionality

            if self.wave1 == True:

                if self.delay == 60:


                    self.a+=1
                    i = self.w1[self.a]



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

        for laser in self.lasers:
            laser.moveLaser()
            laser.checkBackWall(self.width)

        for m in self.mups:
            m.move()
            m.checkBackwall(0)

        for b in self.bups:
            b.move()
            b.checkBackwall(0)

        for bbullet in self.badBullets:
            bbullet.moveBullet()
            bbullet.checkBackWall(0)

        for bbullet in self.badBullets:
            if not bbullet.alive:
                continue
            x,y,h,w = bbullet.getDimensions()
            self.spaceship.checkHit(x,y,h,w)
            if self.spaceship.hit == True:
                self.spaceship.hit = False
                self.spaceship.invinsible = True
                self.invinsiblen = 30
                self.spaceship.health -= 1
                bbullet.setAlive(False)

        for coin in self.coins:
            coin.move()
            coin.checkBackWall(0)




        self.spaceship_y = self.spaceship.spaceshipPosition()[1]
        for baddie in self.baddies:

            baddie.tick(0,0,self.height, self.spaceship_y)


            if not baddie.alive:
                continue
            if baddie.hit != False:
                baddie.color = (255,55,55)
            x,y,w,h = baddie.getDimensions()
            self.spaceship.checkHit(x,y,w,h)

            if self.spaceship.getHit():
                baddie.decreaseHitPoints(99)
                self.spaceship.health -= 1
                self.invinsiblen = 30
                self.spaceship.invinsible = True
                self.spaceship.hit = False
            if baddie.behavior == 3 or baddie.behavior == 1:
                if self.shootDelay == 15:
                    self.badBullets.append(baddie.fire(self.badBullet_width,self.badBullet_height,self.badBullet_color))
        for l in self.lasers:
            if not l.alive:
                continue

            for baddie in self.baddies:
                if not baddie.alive:
                    continue
                x,y,w,h = baddie.getDimensions()
                l.checkHit(x,y,w,h)
                if l.getHit():
                    baddie.hit = True
                    baddie.decreaseHitPoints(.2)
                    l.setHit(False)
                    baddie.hit = False
                    if baddie.hit_points <= 0:
                        if hasattr(baddie,'hasCoin')==True:
                            self.coins.append(baddie.package(self.coin_width, self.coin_height, self.coin_color))


        for missile in self.missiles:
            missile.moveMissile(self.misslen)

        if self.ifFreindlyCollide(self.coins, self.spaceship):
            self.score += 0
            self.coinn += 1

        if self.ifFreindlyCollide(self.mups,self.spaceship):
            self.score +=0

        if self.ifFreindlyCollide(self.bups,self.spaceship):
            self.score += 0

        if self.ifCollide(self.baddies, self.bullets, 1,0):
            self.score += 15


        if self.ifCollide(self.baddies, self.missiles,3,0):
            self.score += 15

        if self.ifFreindlyCollide(self.mups, self.spaceship):
            self.missile_up += 1


        live_mups = []
        live_bups = []
        live_bullets = []
        live_baddies = []
        live_missiles = []
        live_badBullets = []
        live_coins = []
        live_lasers = []

        for bullet in self.bullets:
            if bullet.alive:
                live_bullets.append(bullet)
        for laser in self.lasers:
            if laser.alive:
                live_lasers.append(laser)
        for bbullet in self.badBullets:
            if bbullet.alive:
                live_badBullets.append(bbullet)
        for baddie in self.baddies:
            if baddie.alive:
                live_baddies.append(baddie)
        for missile in self.missiles:
            if missile.alive:
                live_missiles.append(missile)
        for coin in self.coins:
            if coin.alive:
                live_coins.append(coin)
        for m in self.mups:
            if m.alive:
                live_mups.append(m)

        for b in self.bups:
                if b.alive:
                    live_bups.append(b)

        self.mups = live_mups
        self.bups = live_bups
        self.badBullets = live_badBullets
        self.bullets = live_bullets
        self.baddies = live_baddies
        self.missiles = live_missiles
        self.lasers = live_lasers
        self.projectiles = live_badBullets + live_missiles + live_bullets + live_lasers
        self.coins = live_coins
        self.powerups = live_coins + live_mups + live_bups
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

    def shootBullet(self, who):
        if self.shootDelay == 10 or self.shootDelay == 20 or self.shootDelay == 30:
            if who.bullet_up == 0:
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color))
            if who.bullet_up == 1:
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,0,5))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,0,-5))

    def shootMissile(self, who):
        if self.spaceship.missile_up == 0:
            if self.shootDelay == 15:
                if self.misslen ==0:
                    self.misslen=1
                else:
                    self.misslen = 0
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color))
            if self.shootDelay == 30 :

                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color))


    def shootLaser(self,who):
        if who.laser_up == 0:
                self.laserDelay += 1
                if self.laserDelay >10:
                    self.lasers.append(who.beam(self.laser_width, self.laser_height, self.laser_color))

    def button(self,x,y,w,h):
        mx, my =pygame.mouse.get_pos()
        if x <= mx <= x+w and y <= my <= y+h:
            pass


    def ifFreindlyCollide(self, collider, collideE):
        for a in collider:
            if not a.alive:
                continue
            if isinstance(collideE, list) == True:
                for b in collideE:
                    if not b.alive:
                        continue

                    x,y,h,w = a.getDimensions()
                    b.checkHitFriendly(x,y,w,h)
                    if b.hit == True:
                        a.setAlive(False)
                        b.hit = False
                        return b.hit
            else:
                x,y,h,w = a.getDimensions()
                collideE.checkHitFriendly(x,y,w,h)
                if collideE.hit == True:
                        a.setAlive(False)
                        collideE.hit = False
                if collideE.alive == False:
                    collideE.hit = False
                    return collideE.hit


    def ifCollide(self, collider, collideE, rhurt=1, ehurt=1):
        for a in collider:
            if not a.alive:
                continue
            if isinstance(collideE, list) == True:
                for b in collideE:
                    if not b.alive:
                        continue

                    if hasattr(a, 'friendly'):
                        if a.friendly == True:
                            pass
                    else:
                        pass

                    x,y,h,w = a.getDimensions()
                    b.checkHit(x,y,w,h)
                    if b.hit == True:
                        if hasattr(b,'hit_points')==True:
                            b.hit_points -= ehurt

                        else:
                            b.setAlive(False)
                        if hasattr(a,'hit_points')==True:
                            a.hit_points -= rhurt

                        else:
                            a.setAlive(False)
                        #if a.alive == False:

                        if hasattr(a,'hasCoin')==True:

                            self.coins.append(a.package(self.coin_width, self.coin_height, self.coin_color))
                        return b.hit
            else:
                x,y,h,w = a.getDimensions()
                collideE.checkHit(x,y,w,h)
                if collideE.hit == True:
                    if hasattr(collideE,'hit_points')==True:
                        collideE.hit_points -= ehurt
                    else:
                        collideE.setAlive(False)
                    if hasattr(a,'hit_points')==True:
                        a.hit_points -= rhurt
                    else:
                        a.setAlive(False)
                if collideE.alive == False:
                    if hasattr(a,'hasCoin')==True:
                        self.coins.append(collideE.package(self.coin_width, self.coin_height, self.coin_color))
                    return collideE.hit




    def draw(self,surface):
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )
        self.spaceship.draw(surface)
        myfont = self.font2
        myfont1 = self.font
        myfont2 = self.font3
        label = myfont.render("Score "+str(self.score), 1, (255,255,0))
        surface.blit(label, (480, 20))
        label2 = myfont.render("Coins "+str(self.coinn), 1, (255,255,0))
        surface.blit(label2, (350, 20))
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


        for p in self.powerups:
            p.draw(surface)
        for a in self.projectiles:
            a.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)

        if self.spaceship.health <= 0:
            label1 = myfont1.render("Game Over", 1, (255,255,0))
            surface.blit(label1, (self.width/3, self.height/2))
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
