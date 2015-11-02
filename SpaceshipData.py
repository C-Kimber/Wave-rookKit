import pygame
import random
import CONFIG
from spaceship import Spaceship
from baddie import *
from boss import Boss
from particle import *

from itertools import repeat

RED = (255,0,0)
DRED = (102,0,0)
BRED = (255,51,51)
ORANGE = (255,128,0)
DORANGE = (204,102,0)
YELLOW = (255,255,0)

class SpaceshipData:

    def __init__(self,width,height,frame_rate):
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.font3 = pygame.font.SysFont("monospace",10)
        self.font4 = pygame.font.SysFont("Times New Roman",72)
        self.frame_rate = frame_rate
        self.text_color = (255,0,0)
        self.width  = width
        self.height = height
        self.upper_limit = self.width/2

        self.buttonon = False

        self.spaceship_width = 20
        self.spaceship_height = 10
        self.spaceship_health = 300
        self.spaceship_speed = 7

        self.gamestate = CONFIG.GAME_STATE
        self.ministate = CONFIG.MINI_STATE

        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (0,255,255),self.spaceship_health)
        self.spaceship_y = self.spaceship.spaceshipPosition()[1]



        self.bullets = []
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (255,255,255)

        self.hbullets = []
        self.hbullet_width = 5
        self.hbullet_height = 5
        self.hbullet_color = (255,255,255)

        self.abullets = []
        self.abullet_width = 20
        self.abullet_height = 20
        self.abullet_color = (255,255,255)

        self.bombs = 3
        self.bomb = False
        self.boom =False
        self.bomb_radius = 20
        self.ba = 1

        self.stars = []
        self.star_width = 1
        self.star_height = 1
        self.star_direction = 'normal'
        self.star_color = (255,255,255)

        self.lasers = []
        self.laser_width =100
        self.laser_height = 5
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
        self.missile_width = 30
        self.missile_height = 10
        self.missile_color = (55,144,144)

        self.badBullets = []
        self.badBullet_width = 20
        self.badBullet_height = 20
        self.badBullet_color = (0,255,255)

        self.badLasers = []
        self.badLaser_width = 100
        self.badLaser_height = 30
        self.badLaser_color = (0,255,255)

        self.baddies = []
        self.baddie_width = 40
        self.baddie_height = 40
        self.baddie_color = (0,155,0)
        self.baddie_id = 0

        self.asteroids = []
        self.asteroid_width = random.randint(20, 60)
        self.asteroid_height = self.asteroid_width
        self.asteroid_color=(55,55,0)


        self.boss = []
        self.boss1_width = 400
        self.boss1_height = 600
        self.boss1_color = (55,0,0)

        self.turret1_width = 60
        self.turret1_height = 20
        self.turret1_color = (155,50,50)
        self.turrets = 0

        self.particles = [] * 100
        self.particle_width = 20
        self.particle_height = 20

        self.projectiles = []
        self.powerups = []

        self.particle_color=(255,255,255)
        self.particle_speed = .3
        self.f = ['up', 'down','left','right','upright','upleft','downright','downleft']
        self.c = [ORANGE,RED,DRED,BRED,ORANGE,DORANGE,YELLOW ]


        self.score = 0

        self.wave1 = True
        self.wave2 = False
        self.wave3 = False
        self.wave4 = False
        self.wave5 = False
        self.wave6 = False
        self.wave7 = False
        self.wave8 = False
        self.wave9 = False
        self.wave10 = False
        self.w1 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w2 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w3 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w4 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w5 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w6 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w7 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w8 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w9 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        self.w10 = [1,1,2,2,1,2,1,1,'p','p','p',4,'p','p',99,0]
        

        self.endGame = False
        self.winGame = False

        self.delay = 0
        self.shootDelay = 0
        self.laserDelay = 0
        self.laser_on = False

        self.badLaserDelay = 0

        self.a = -1

        self.ang = 9
        self.angby = .1



        self.invinsiblen = 0

        baddie_list = pygame.sprite.Group

        all_sprite_list = pygame.sprite.Group

        self.e = 0
        self.e_t = 0
        self.e_b = 0
        self.exploding = False

        self.startoggle = 3
        self.loadingn = 0

        self.paused = False

        self.millimax = 0

        self.fragmentgroup = pygame.sprite.Group()

        Fragment.groups = self.fragmentgroup
        return

    def doNothing(self):
        return True

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):

        if 1 in newbuttons:
            self.buttonon = True
        else:
            self.buttonon = False

        self.gamestate = CONFIG.GAME_STATE
        self.ministate = CONFIG.MINI_STATE

        if self.gamestate == 1:

            self.loadingn +=1
            if self.loadingn == 60:
                CONFIG.GAME_STATE = 2
                self.loadingn = 0


        if self.gamestate == 2 or self.gamestate == 3:
          if pygame.K_ESCAPE in newkeys:
            self.paused = not self.paused
            CONFIG.MINI_STATE = 1
          if self.paused == False:
            if pygame.K_LEFT in keys or pygame.K_a in keys:
                self.spaceship.moveLeft(self.spaceship_speed)
            if pygame.K_RIGHT in keys or pygame.K_d in keys:
                self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
            if pygame.K_UP in keys or pygame.K_w in keys:
                self.spaceship.moveUp(self.spaceship_speed+3)
            if pygame.K_DOWN in keys or pygame.K_s in keys:
                self.spaceship.moveDown(self.spaceship_speed+3,self.height)

            if pygame.K_i in newkeys:
                self.spaceship.invinsiblen = 200


            if pygame.K_LCTRL in newkeys:
                if self.bombs > 0:
                    if self.bomb_radius == 20:
                        self.bomb = True
                        self.bombs -= 1
            if self.bomb_radius >= 6000:
                self.boom = False
                self.bomb_radius = 20
                self.ba = 1

            self.particle_direction = random.choice(self.f)
            self.particle_color = random.choice(self.c)



            if pygame.K_p in newkeys:
                self.addBoss1()

            if pygame.K_u in keys:
                #for _ in range(random.randint(3,15)):
                self.spaceship.explode()
            if pygame.K_o in newkeys:
                self.spaceship.bullet_up += 1
                self.spaceship.missile_up += 1
                self.spaceship.laser_up += 1

            if self.e > 1:
                self.e = 0
            self.e += self.e_b

            if self.e == 1:
                self.e_t += 1
                self.particles.append(self.spaceship.explode(self.particle_width,self.particle_height,self.particle_color,self.particle_speed,self.particle_direction))
            if self.e_t > 50:
                self.e= 0
                self.e_t = 0
                self.e_b = 0


            self.shootDelay += 1

            self.invinsiblen -= 1

            if self.invinsiblen < 0:
                self.invinsiblen = 0
                self.spaceship.invinsible = False

            if self.invinsiblen > 0:
                self.spaceship.invinsible = True

            if self.shootDelay > 30:
                self.shootDelay = 0
            if self.hover(0,50,self.width,self.height-50):
                if  1 in buttons:

                    self.shootBullet(self.spaceship)
                    self.shootMissile(self.spaceship)
                    self.shootLaser(self.spaceship)
                    self.shootAngledBullet(self.spaceship)


            if pygame.K_SPACE in keys :
                self.shootBullet(self.spaceship)
                self.shootMissile(self.spaceship)
                self.shootLaser(self.spaceship)
                #self.shootAngledBullet(self.spaceship)



            if self.laserDelay >= 60:
                self.laserDelay = 0
            if self.laserDelay <= 0:
                self.laserDelay = 0

            if self.badLaserDelay >= 80:
                self.badLaserDelay = -30
            if self.badLaserDelay <= -30:
                self.badLaserDelay = -30

            """if self.ang > 3:
                self.angby *= -1
            if self.ang < .2:
                self.angby *= -1"""

            """if self.ang > 2.8:
                self.ang = .5
            if self.ang < .5:
                self.ang = 2.8"""

            self.delay += 1
            if self.delay >= 120:
                self.delay = 0
            if self.spaceship.health <= 0:
                del self.bullets[:]
                self.spaceship.setAlive(False)

            if len(self.boss) <= 0:
                if self.endGame == True:
                        self.winGame = True
            clock =pygame.time.Clock()
            milliseconds = clock.tick(self.frame_rate)  # milliseconds passed since last frame

            if milliseconds > self.millimax:
                self.millimax = milliseconds
            seconds = milliseconds / 1000.0

            self.fragmentgroup.update(seconds)

            if self.spaceship.health > 0:
                
                #wave fucntionality
                """if self.wave1 == True or self.wave2 == True or self.wave3 == True or self.wave4 == True or self.wave5 == True\
                 or self.wave6 == True or self.wave7 == True or self.wave8 == True or self.wave9 == True or self.wave10 == True:
                    if self.delay == 60:
                        self.a+=1
                        if self.wave1 == True:
                            i = self.w1[self.a]
                        elif self.wave2 == True:
                            i = self.w2[self.a]
                        elif self.wave3 == True:
                            i = self.w3[self.a]
                        elif self.wave4 == True:
                            i = self.w4[self.a]
                        elif self.wave5 == True:
                            i = self.w5[self.a]
                        elif self.wave6 == True:
                            i = self.w6[self.a]
                        elif self.wave7 == True:
                            i = self.w7[self.a]
                        elif self.wave8 == True:
                            i = self.w8[self.a]
                        elif self.wave9 == True:
                            i = self.w9[self.a]
                        elif self.wave10 == True:
                            i = self.w10[self.a]

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

                        elif i == 4:

                            self.addBoss1()

                        elif i == 'p':
                            self.doNothing()
                            
                        elif i == 'a':
                            for _ in range(10):
                                if random.randint(1, self.frame_rate/2) == 1:
                                    self.addAsteroid()

                        elif i == '1end':
                            self.wave1 = False
                        elif i == '2end':
                            self.wave2 = False
                        elif i == '3end':
                            self.wave3 = False
                        elif i == '4end':
                            self.wave4 = False
                        elif i == '5end':
                            self.wave5 = False
                        elif i == '6end':
                            self.wave6 = False
                        elif i == '7end':
                            self.wave7 = False
                        elif i == '8end':
                            self.wave8 = False
                        elif i == '9end':
                            self.wave9 = False
                        elif i == '10end':
                            self.wave10 = False
                            
                        elif i == '2start':
                            self.wave2 = True
                        elif i == '3start':
                            self.wave3 = True
                        elif i == '4start':
                            self.wave4 = True
                        elif i == '5start':
                            self.wave5 = True
                        elif i == '6start':
                            self.wave6 = True
                        elif i == '7start':
                            self.wave7 = True
                        elif i == '8start':
                            self.wave8 = True
                        elif i == '9start':
                            self.wave9 = True
                        elif i == '10start':
                            self.wave10 = True

                        elif i == 99:
                                self.endGame = True"""




            self.spaceship.tick()

            self.starry(self.startoggle)


            for bullet in self.bullets:
                bullet.moveBullet()
                bullet.checkBackWall(self.width)
                if not bullet.alive:
                    self.bullets.remove(bullet)
                    continue

            for h in self.hbullets:
                h.update(self.spaceship_y)

            for a in self.abullets:
                a.update(self.spaceship.x,self.spaceship.y)
                a.checkWall()
                if not a.alive:
                    self.abullets.remove(a)
                    continue
                #a.setAngle(self.ang)

            for b in self.boss:
                b.tick(0,0,self.height, 400,self.turrets)

            for star in self.stars:

                star.move(self.spaceship.x, self.spaceship.y)
                star.checkBackWall(50)
                if star.x <= 0:
                    star.alive = False
                    self.stars.remove(star)

            for p in self.particles:
                p.move()
                p.checkWalls(0,50,self.width,self.height)
                a =int(p.color[0]-p.vel)
                b= int(p.color[1]-p.vel)
                c=int(p.color[2]-p.vel)
                if a < 0:
                    a= 0
                if c < 0:
                    c= 0
                if b < 0:
                    b= 0

                p.color =(a,b,c)




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

            for a in self.asteroids:
                a.move()
                a.checkBackWall(0)

            for laz in self.badLasers:
                laz.moveLaser()
                laz.checkBackWall(0)

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



            self.spaceship_y = self.spaceship.spaceshipPosition()[1]
            for aster in self.asteroids:
                if not aster.alive:
                    continue
                if aster.hit != False:
                    aster.color = (255,55,55)
                x,y,w,h = aster.getDimensions()
                if w >= 35:
                    self.spaceship.checkHit(x,y,w,h)

                if self.spaceship.getHit():
                    aster.alive = False
                    self.spaceship.health -= 1
                    self.invinsiblen = 30
                    self.spaceship.invinsible = True
                    self.spaceship.hit = False
                for bullet in self.bullets:
                    if not bullet.alive:
                        continue
                    x,y,w,h = aster.getDimensions()
                    bullet.checkHit(x,y,w,h)
                    if bullet.hit == True:
                        bullet.hit = False
                        aster.alive = False
                        if w < 35:
                           aster.alive = False
                        else:
                            self.addSAsteroid(w/2,h/2,x+5,y-h/2,random.uniform(1,1.5))
                            self.addSAsteroid(w/2,h/2,x+5,y+h/2,random.uniform(1.9,2))



            for baddie in self.baddies:


                baddie.tick(0,0,self.height, self.height/2)
                #self.homingBullet(baddie)
                if self.bomb == True:
                   self.bomb = False
                   self.boom = True
                   if self.boom == True:
                       for bae in self.baddies:
                          bae.decreaseHitPoints(30)
                          self.explodeIt(bae)

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

                if baddie.behavior == 5 or baddie.behavior == 6:
                    if self.shootDelay == 6 or self.shootDelay == 12 or self.shootDelay == 18 or self.shootDelay == 24 or  self.shootDelay == 30:
                        self.badBullets.append(baddie.fire(self.badBullet_width,self.badBullet_height,self.badBullet_color))
                if baddie.behavior == 4:
                    if  self.shootDelay == 30:
                        self.badBullets.append(baddie.bossFire(self.badBullet_width,self.badBullet_height,self.badBullet_color))

            for b in self.boss:
                if not b.alive:
                    del self.boss[:]
                    self.score += 1000


                    continue

                self.badLaserDelay += 1


                if self.badLaserDelay >20:
                    if self.turrets <= 0:
                        self.badLasers.append(b.beam(self.badLaser_width, self.badLaser_height, self.badLaser_color,0,-b.height/2-50+(self.badLaserDelay*4)))
                        self.badLasers.append(b.beam(self.badLaser_width, self.badLaser_height, self.badLaser_color,0,b.height/2+50-(self.badLaserDelay*4)))

                    self.badLasers.append(b.beam(self.badLaser_width, self.badLaser_height, self.badLaser_color,0,-10))
                if self.turrets <= 0:
                    self.shootAngledBullet(b)

                for bullet in self.bullets:
                    if not bullet.alive:
                        continue
                    x,y,w,h = b.getDimensions()
                    bullet.checkHit(x,y,w,h)

                    if bullet.hit == True:

                        if b.canGetHit == True:
                            b.hit = True
                            self.hurtIt(b,1)
                        else:
                            b.fakeHit = True
                        self.explodeIt(bullet)
                        bullet.hit = False


                for laser in self.lasers:
                    if not laser.alive:
                        continue
                    x,y,w,h = b.getDimensions()
                    laser.checkHit(x,y,w,h)

                    if laser.hit == True:
                        laser.color = (255,255,255)
                        if b.canGetHit == True:
                            b.hit = True
                            self.hurtIt(b,.2)
                            laser.hit = False
                            if self.isTurret(b) == True:
                                self.turrets -= 1


                        else:
                            b.fakeHit = True
                            laser.hit=False
                        self.explodeIt(laser)
                        laser.hit = False
                for missile in self.missiles:
                    if not missile.alive:
                        continue
                    x,y,w,h = b.getDimensions()
                    missile.checkHit(x,y,w,h)

                    if missile.hit == True:

                        if b.canGetHit == True:
                            b.hit = True
                            self.hurtIt(b,3)
                            missile.hit = False

                        else:
                            b.fakeHit = True
                            missile.hit = False
                        self.explodeIt(missile)
                        missile.hit = False
                for blaser in self.badLasers:
                    if not blaser.alive:
                        continue
                    x,y,w,h = self.spaceship.getDimensions()
                    blaser.checkHit(x,y,w,h)
                    if blaser.hit == True:
                        blaser.hit = False
                        self.spaceship.health -= .02
                for bullet in self.abullets:
                    if not bullet.alive:
                        continue
                    x,y,w,h = self.spaceship.getDimensions()
                    bullet.checkHit(x,y,w,h)
                    if bullet.hit == True:
                        bullet.hit = False
                        #self.spaceship.health -= .5

            if self.bomb == True:
                   self.bomb = False
                   self.boom = True


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
                        l.setHit(False)
                        self.hurtIt(baddie, .2)
                        baddie.hit = False
                        if baddie.hit_points <= 0:
                            self.explodeIt(baddie)


            for missile in self.missiles:
                missile.moveMissile(self.misslen)



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
            live_badLasers = []
            live_hBullets = []
            live_lasers = []
            live_particles = []
            live_asteroids = []

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
            for a in self.asteroids:
                if a.alive:
                    live_asteroids.append(a)

            for m in self.mups:
                if m.alive:
                    live_mups.append(m)
            for p in self.particles:
                if p.alive:
                    live_particles.append(p)

            for b in self.bups:
                    if b.alive:
                        live_bups.append(b)
            for l in self.badLasers:
                if l.alive:
                    live_badLasers.append(l)

            for h in self.hbullets:
                if h.alive:
                    live_hBullets.append(h)
            for a in self.abullets:
                if a.alive:
                    live_hBullets.append(a)

            self.mups = live_mups
            self.bups = live_bups
            self.asteroids = live_asteroids
            self.badBullets = live_badBullets
            self.badLasers = live_badLasers
            self.bullets = live_bullets
            self.baddies = live_baddies
            self.missiles = live_missiles
            self.lasers = live_lasers
            self.projectiles = live_badBullets + live_missiles + live_bullets + live_lasers

            self.powerups =  live_mups + live_bups
            self.particles = live_particles

        return

    def starry(self, togglenumber):
        if togglenumber ==4:
            self.addStar(2,2,self.width,random.randint(50,self.height),(255,255,255),10,'normal')
            self.addStar(2,2,self.width,random.randint(50,self.height),(155,155,155),7,'normal')
            self.addStar(2,2,self.width,random.randint(50,self.height),(100,100,100),5,'normal')
            self.addStar(2,2,self.width,random.randint(50,self.height),(55,55,55),2,'normal')
        if togglenumber ==3:
            self.addStar(2,2,self.width,random.randint(50,self.height),(255,255,255),10,'normal')
            self.addStar(2,2,self.width,random.randint(50,self.height),(155,155,155),7,'normal')
            self.addStar(2,2,self.width,random.randint(50,self.height),(100,100,100),5,'normal')

        elif togglenumber == 2:
            self.addStar(2,2,self.width,random.randint(50,self.height),(255,255,255),10,'normal')
            self.addStar(2,2,self.width,random.randint(50,self.height),(155,155,155),7,'normal')


        elif togglenumber ==1:
            self.addStar(2,2,self.width,random.randint(50,self.height),(255,255,255),10,'normal')

    def addAsteroid(self):
        size = random.randint(40,90)
        new_baddie = Asteroid(size, size, self.width, random.randint(0,(self.height-self.baddie_height)), self.asteroid_color, 5, random.uniform(1,2))
        self.asteroids.append( new_baddie )
        return
    def addSAsteroid(self,width,height,x,y,angle):

        new_baddie = Asteroid(width, height, x, y, self.asteroid_color, 5, angle)
        self.asteroids.append( new_baddie )
        return

    def addBaddie(self, height):
        new_baddie = Baddie(self.baddie_id, self.baddie_width, self.baddie_height, self.width, height, self.baddie_color, 3, 0 )
        self.baddies.append( new_baddie )

        return

    def addStrongBaddie(self, height):
        new_baddie = Baddie(self.baddie_id,self.baddie_width, self.baddie_height, self.width, height, (155,0,0), 2, 1)
        new_baddie.setHitPoints(2)
        self.baddies.append(new_baddie)
        return

    def addBigBaddie(self):
        new_baddie = Baddie(self.baddie_id,self.baddie_width*5, self.baddie_height*5, self.width, 200, (55,0,0), 1, 3)
        new_baddie.setHitPoints(15)
        self.baddies.append(new_baddie)
        return

    def addBoss1(self):
        new_baddie = Boss(10,self.boss1_width, self.boss1_height, self.width, 100, self.boss1_color, 1, 4)
        new_baddie.setHitPoints(100)
        new_baddie.canGetHit = False
        self.boss.append(new_baddie)
        self.turrets = 0

        new_baddie = Baddie(11,self.turret1_width, self.turret1_height, self.width-20, 300, self.turret1_color, 1, 5)
        new_baddie.setHitPoints(1)
        new_baddie.isTurret = True
        self.baddies.append(new_baddie)

        self.turrets += 1

        new_baddie = Baddie(11,self.turret1_width, self.turret1_height, self.width-20, 500, self.turret1_color, 1, 6)
        new_baddie.setHitPoints(1)
        new_baddie.isTurret = True
        self.baddies.append(new_baddie)
        self.turrets += 1

    def addStar(self,width,height,x,y,color,speed,direction):
        new_star = Star(width,height,x,y,color,speed,direction)
        self.stars.append(new_star)
        return

    def shootBullet(self, who):
        #self.bullets.append(who.angleFire(0,))
        if self.shootDelay == 6 or self.shootDelay == 12 or self.shootDelay == 18 or self.shootDelay == 24 or self.shootDelay == 30:
            if who.bullet_up ==1:
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,'normal'))
            if who.bullet_up == 2:
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,'normal',0,-5))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,'normal',0,5))
            if who.bullet_up == 3     :
                self.bullets.append( who.fire(self.bullet_width,self.bullet_height,self.bullet_color,'normal'))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'up'))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'down'))
            if who.bullet_up == 4     :
                self.bullets.append( who.fire(self.bullet_width,self.bullet_height,self.bullet_color,'normal'))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'up'))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'down'))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'up2'))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color, 'down2'))

    def shootMissile(self, who):
        if self.spaceship.missile_up == 1:
            if self.shootDelay == 15:
                if self.misslen ==0:
                    self.misslen=1
                else:
                    self.misslen = 0
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0,-10))
            if self.shootDelay == 30 :

                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0,10))
        if who.missile_up == 2:
            if self.shootDelay == 15:
                if self.misslen ==0:
                    self.misslen=1
                else:
                    self.misslen = 0
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0,-10))
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0,-20,-2))
            if self.shootDelay == 30 :

                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0,10))
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0, 20,2))

    def shootLaser(self,who):

        if who.laser_up == 1:
                self.laserDelay += 1
                if self.laserDelay >20:
                    self.lasers.append(who.beam(self.laser_width, self.laser_height, self.laser_color))
        if who.laser_up == 2:
                self.laserDelay += 1
                if self.laserDelay >20:
                    self.lasers.append(who.beam(self.laser_width, self.laser_height, self.laser_color,0,-10))
                    self.lasers.append(who.beam(self.laser_width, self.laser_height, self.laser_color,0,10))

    def   shootAngledBullet(self,who):
        self.abullets.append(who.angleFire(self.abullet_width,self.abullet_height,self.abullet_color,self.ang))
        #self.ang += self.angby


    def button(self,x,y,w,h):
        mx, my =pygame.mouse.get_pos()
        if x <= mx <= x+w and y <= my <= y+h:
            if self.buttonon == True:

                return True

    def hover(self,x,y,w,h):
        mx, my =pygame.mouse.get_pos()
        if x <= mx <= x+w and y <= my <= y+h:
            return True

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

                    return b.hit
            else:
                x,y,h,w = a.getDimensions()
                collideE.checkHitFriendly(x,y,w,h)
                if collideE.hit == True:
                    a.setAlive(False)

                    a.hit = False

            return collideE.hit


    def ifCollide(self, collider, collideE, rhurt, ehurt):
        for a in collider:
            if not a.alive:
                continue
            if isinstance(collideE, list) == True:
                for b in collideE:
                    if not b.alive:
                        continue


                    x,y,h,w = a.getDimensions()
                    b.checkHit(x,y,w,h)
                    if b.hit == True:
                        a.hit = True
                        self.hurtIt(a,rhurt)
                        self.hurtIt(b,ehurt)

                        self.explodeIt(a)

                        self.explodeIt(collideE)

                        return b.hit

            else:
                x,y,h,w = a.getDimensions()
                collideE.checkHit(x,y,w,h)
                if collideE.hit == True:
                    a.hit = True

                    self.hurtIt(collideE,ehurt)
                    self.hurtIt(a,rhurt)


                    self.explodeIt(a)
                    self.explodeIt(collideE)


                    return collideE.hit

    def explodeIt(self, who):
        if hasattr(who, 'canBoom')==True:
            if hasattr(who,'hit_points')==True:
                if who.hit_points <= 0:

                    self.destroyBlast(who)
                else:
                    self.explode(who)
            else:
                self.destroyBlast(who)

    def explode(self,who):
        who.explode((who.x,who.y),random.choice(self.c))

    def destroyBlast(self,who):
        for _ in range(random.randint(3,15)):
            who.explode((who.x,who.y),random.choice(self.c))

    def hurtIt(self, who,much):
        if hasattr(who,'friendly')==True:
                pass
        else:
            if hasattr(who,'hit_points')==True:
                who.hit_points -= much
                if who.hit_points <= 0:
                    if self.isTurret(who) ==True:
                        self.turrets -= 1

            else:
                who.setAlive(False)
                if self.isTurret(who) ==True:
                    self.turrets -= 1

    def isTurret(self,who):
        if hasattr(who,'isTurret') == True:
            if who.isTurret == True:
                return True

    def newGame(self):
        del self.baddies[:]

        del self.bullets[:]
        del self.stars[:]
        del self.projectiles[:]
        del self.badBullets[:]
        del self.badLasers[:]
        del self.boss[:]
        del self.abullets[:]
        self.wave1 = True
        self.endGame = False
        self.winGame = False
        self.score = 0

        self.bombs = 3
        self.spaceship.setAlive(True)
        self.spaceship.health = 3
        self.spaceship.x = 0
        self.spaceship.y = self.height/2
        self.a = 0
        self.spaceship.bullet_up = 1
        self.spaceship.missile_up = 0
        self.spaceship.missile_up = 0

    def draw(self,surface):

        rect = pygame.Rect(0,0,self.width,self.height)



        surface.fill((0,0,0),rect )

        rect = pygame.Surface((self.width,50), pygame.SRCALPHA, 32)
        rect.fill((255, 255, 255, 50))
        surface.blit(rect, (0,0))

        self.spaceship.draw(surface)
        myfont = self.font2
        myfont1 = self.font
        myfont2 = self.font3
        label = myfont.render("Score "+str(self.score), 1, (255,255,0))
        surface.blit(label, (350, 20))
        label3 = myfont.render("Bombs "+str(self.bombs), 1, (255,255,0))
        surface.blit(label3, (250, 20))


        if self.boom == True:

            x,y = self.spaceship.spaceshipPosition()
            self.ba += 2
            self.bomb_radius += self.ba*2
            pygame.draw.circle(surface,  (155,0,0), (x,y), self.bomb_radius,10)
            pygame.draw.circle(surface, (255,0,0), (x,y), self.bomb_radius/2,5)
            pygame.draw.circle(surface, (255,255,0), (x,y), self.bomb_radius/3,3)
            pygame.draw.circle(surface, (255,255,155),(x,y),self.bomb_radius/4,3 )

            pygame.draw.circle(surface, (55,0,0), (x+50,y+50), self.bomb_radius, 10)
            pygame.draw.circle(surface, (255,0,0), (x+50,y-50), self.bomb_radius/2, 5)
            pygame.draw.circle(surface, (255,255,0), (x-50,y+50), self.bomb_radius/3, 3)
            pygame.draw.circle(surface, (255,255,155),(x-50,y-50),self.bomb_radius/4,3 )

        if self.spaceship.health > 0:
            rect = pygame.Rect( 20, 20, 50*self.spaceship.health, 20 )
            pygame.draw.rect(surface, (255,0,0), rect)



        for s in self.stars:
            s.draw(surface)

        for p in self.powerups:
            p.draw(surface)
        for L in self.badLasers:
            L.draw(surface)
        for b in self.boss:
            b.draw(surface)
            b.drawHealth(surface)
        for a in self.projectiles:
            a.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)
            # surf =  pygame.Surface((baddie.width, baddie.width))
            # rotatedSurf =  pygame.transform.rotate(surf, )
            # rotRect = rotatedSurf.get_rect()
            # surface.blit(rotatedSurf, rotRect)
        for l in self.particles:
            l.draw(surface)
        for h in self.hbullets:
            h.draw(surface)
        for h in self.abullets:
            h.draw(surface)
        for a in self.asteroids:
            a.draw(surface)
        self.fragmentgroup.draw(surface)


        if self.winGame == True:
            rect = pygame.Surface((self.width,self.height), pygame.SRCALPHA, 32)
            rect.fill((0, 0, 0, 200))
            surface.blit(rect, (0,0))

            rect = pygame.Surface((self.width,50), pygame.SRCALPHA, 32)
            rect.fill((255, 255, 255, 50))
            surface.blit(rect, (0,self.height/2))

            label1 = self.font.render("You Won!", 1, (255,255,0))
            surface.blit(label1, (600, self.height/2-200))


            rect = pygame.Rect( self.width/4-5, self.height/3, 80, 50 )


            x,y,w,h = rect
            if self.hover(x,y,w,h):
                pygame.draw.rect(surface, (155,155,155), rect)
            else:
                pygame.draw.rect(surface, (55,55,55), rect)
            if self.button(x,y,w,h):
                CONFIG.GAME_STATE = 1
                self.newGame()

            label1 = myfont1.render("Play Again", 1, (255,255,0))
            surface.blit(label1, (self.width/4, self.height/3))


            rect = pygame.Rect( self.width/1.5-5, self.height/3, 80, 50 )
            x,y,w,h = rect
            if self.hover(x,y,w,h):
                pygame.draw.rect(surface, (155,155,155), rect)
            else:
                pygame.draw.rect(surface, (55,55,55), rect)
            if self.button(x,y,w,h):
                pygame.quit()

            label1 = myfont1.render("Quit", 1, (255,255,0))
            surface.blit(label1, (self.width/1.5, self.height/3))

        if self.spaceship.health <= 0:

            rect = pygame.Surface((self.width,self.height), pygame.SRCALPHA, 32)
            rect.fill((0, 0, 0, 200))
            surface.blit(rect, (0,0))

            rect = pygame.Surface((self.width,50), pygame.SRCALPHA, 32)
            rect.fill((255, 255, 255, 50))
            surface.blit(rect, (0,self.height/2))

            label1 = self.font.render("Game Over", 1, (255,255,0))
            surface.blit(label1, (600, self.height/2-200))





            rect = pygame.Rect( 395, self.height/2, 100, 50 )
            x,y,w,h = rect
            if self.hover(x,y,w,h):
                pygame.draw.rect(surface, (155,155,155), rect)
            else:
                pygame.draw.rect(surface, (55,55,55), rect)
            if self.button(x,y,w,h):
                CONFIG.GAME_STATE = 0
                self.paused = False
                self.newGame()

            label1 = myfont.render("Menu", 1, (255,255,0))
            surface.blit(label1, (400, self.height/2))

            rect = pygame.Rect( 695, self.height/2, 80, 50 )
            x,y,w,h = rect
            if self.hover(x,y,w,h):
                pygame.draw.rect(surface, (155,155,155), rect)
            else:
                pygame.draw.rect(surface, (55,55,55), rect)
            if self.button(x,y,w,h):
                pygame.quit()

            label1 = myfont.render("Quit", 1, (255,255,0))
            surface.blit(label1, (700, self.height/2))


        rect = pygame.Rect( 880, 20, 20, 20 )
        pygame.draw.rect(surface, (155,155,155), rect)
        x,y,w,h = rect
        if self.button(x,y,w,h):
            self.startoggle += 1
            if self.startoggle == 4:
                self.startoggle = 0

        rect = pygame.Rect( 940, 20, 20, 20 )
        pygame.draw.rect(surface, (155,155,155), rect)
        x,y,w,h = rect
        if self.button(x,y,w,h):
            self.paused = not self.paused
            if self.ministate == 0:
                CONFIG.MINI_STATE = 1
            else:
                CONFIG.MINI_STATE = 0

        self.drawPaused(surface)
        return

    def menuDraw(self,surface):
        myfont1 = self.font
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )

        label1 = myfont1.render("Kimber's Space Adventure", 1, (255,255,0))
        surface.blit(label1, (self.width/3, self.height/8))

        rect = pygame.Rect( self.width/4-5, self.height/3, 80, 50 )


        x,y,w,h = rect
        if self.hover(x,y,w,h):
            pygame.draw.rect(surface, (155,155,155), rect)
        else:
            pygame.draw.rect(surface, (55,55,55), rect)
        if self.button(x,y,w,h):
            CONFIG.GAME_STATE = 1
            self.newGame()

        label1 = myfont1.render("Play", 1, (255,255,0))
        surface.blit(label1, (self.width/4, self.height/3))


        rect = pygame.Rect( self.width/1.5-5, self.height/3, 80, 50 )
        x,y,w,h = rect
        if self.hover(x,y,w,h):
            pygame.draw.rect(surface, (155,155,155), rect)
        else:
            pygame.draw.rect(surface, (55,55,55), rect)
        if self.button(x,y,w,h):
            pygame.quit()

        label1 = myfont1.render("Quit", 1, (255,255,0))
        surface.blit(label1, (self.width/1.5, self.height/3))


    def loadDraw(self,surface):
        myfont = self.font4
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill((0,0,0),rect )

        label1 = myfont.render("Loading", 1, (255,255,0))
        surface.blit(label1, (self.width/4, self.height/3))

    def drawPaused(self, surface):
        myfont = self.font
        if self.paused == True:

            rect = pygame.Surface((self.width,self.height-50), pygame.SRCALPHA, 32)
            rect.fill((0, 0, 0, 200))
            surface.blit(rect, (0,50))

            rect = pygame.Surface((600,600), pygame.SRCALPHA, 32)
            rect.fill((255, 255, 255, 50))
            surface.blit(rect, (300,200))
            #normal pause
            if self.ministate == 1:
                label1 = myfont.render("Paused", 1, (255,255,0))
                surface.blit(label1, (500, self.height/2-50))

                rect = pygame.Rect( 395, self.height/2, 100, 50 )
                x,y,w,h = rect
                if self.hover(x,y,w,h):
                    pygame.draw.rect(surface, (155,155,155), rect)
                else:
                    pygame.draw.rect(surface, (55,55,55), rect)
                if self.button(x,y,w,h):
                    CONFIG.GAME_STATE = 0
                    self.paused = False
                    self.newGame()


                label1 = myfont.render("Menu", 1, (255,255,0))
                surface.blit(label1, (400, self.height/2))

                rect = pygame.Rect( 695, self.height/2, 80, 50 )
                x,y,w,h = rect
                if self.hover(x,y,w,h):
                    pygame.draw.rect(surface, (155,155,155), rect)
                else:
                    pygame.draw.rect(surface, (55,55,55), rect)
                if self.button(x,y,w,h):
                    pygame.quit()

                label1 = myfont.render("Quit", 1, (255,255,0))
                surface.blit(label1, (700, self.height/2))



                rect = pygame.Rect( 700, self.height/2+100, 100, 50 )
                x,y,w,h = rect
                if self.hover(x,y,w,h):
                    pygame.draw.rect(surface, (155,155,155), rect)
                else:
                    pygame.draw.rect(surface, (55,55,55), rect)
                if self.button(x,y,w,h):
                    CONFIG.MINI_STATE = 2

                label1 = myfont.render("Options", 1, (255,255,0))
                surface.blit(label1, (700, self.height/2+100))

                rect = pygame.Rect( 400, self.height/2+100, 100, 50 )
                x,y,w,h = rect
                if self.hover(x,y,w,h):
                    pygame.draw.rect(surface, (155,155,155), rect)
                else:
                    pygame.draw.rect(surface, (55,55,55), rect)
                if self.button(x,y,w,h):
                    CONFIG.MINI_STATE = 0
                    self.paused = False

                label1 = myfont.render("Return", 1, (255,255,0))
                surface.blit(label1, (400, self.height/2+100))



            #Options
            elif self.ministate == 2:


                label1 = myfont.render("Options", 1, (255,255,0))
                surface.blit(label1, (500, self.height/2-50))
                rect = pygame.Rect( 395, self.height/2, 100, 50 )
                x,y,w,h = rect
                if self.hover(x,y,w,h):
                    pygame.draw.rect(surface, (155,155,155), rect)
                else:
                    pygame.draw.rect(surface, (55,55,55), rect)
                if self.button(x,y,w,h):
                    CONFIG.MINI_STATE = 1




                label1 = myfont.render("OK", 1, (255,255,0))
                surface.blit(label1, (400, self.height/2))

                rect = pygame.Rect( 695, self.height/2, 80, 50 )
                x,y,w,h = rect
                if self.hover(x,y,w,h):
                    pygame.draw.rect(surface, (155,155,155), rect)
                else:
                    pygame.draw.rect(surface, (55,55,55), rect)

                if self.button(x,y,w,h):
                    pass

                label1 = myfont.render("Mute", 1, (255,255,0))
                surface.blit(label1, (700, self.height/2))


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
