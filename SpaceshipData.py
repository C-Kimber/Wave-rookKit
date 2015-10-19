import pygame
import random
import CONFIG
from spaceship import Spaceship
from baddie import Baddie
from particle import Star
from particle import Blast
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
        self.spaceship_health = 3
        self.spaceship_speed = 7

        self.gamestate = 0

        self.spaceship = Spaceship(self.spaceship_width,self.spaceship_height,0,(self.height / 2) - 10, (0,255,255),self.spaceship_health)
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
        self.missile_width = 15
        self.missile_height = 5
        self.missile_color = (55,144,144)

        self.badBullets = []
        self.badBullet_width = 5
        self.badBullet_height = 5
        self.badBullet_color = (0,255,255)

        self.baddies = []
        self.baddie_width = 40
        self.baddie_height = 40
        self.baddie_color = (0,155,0)
        self.baddie_id = 0


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
        self.w1 = [1,1,2,2,1,2,1,1,0]

        self.delay = 0
        self.shootDelay = 0
        self.laserDelay = 0
        self.laser_on = False

        self.a = -1

        self.bullet_up = 0
        self.missile_up = 1

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
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):

        if 1 in newbuttons:
            self.buttonon = True
        else:
            self.buttonon = False

        self.gamestate = CONFIG.GAME_STATE


        if self.gamestate == 1:

            self.loadingn +=1
            if self.loadingn == 60:
                CONFIG.GAME_STATE = 2
                self.loadingn = 0


        if self.gamestate == 2:
          if pygame.K_ESCAPE in newkeys:
            self.paused = not self.paused
          if self.paused == False:
            if pygame.K_LEFT in keys or pygame.K_a in keys:
                self.spaceship.moveLeft(self.spaceship_speed)
            if pygame.K_RIGHT in keys or pygame.K_d in keys:
                self.spaceship.moveRight(self.spaceship_speed,self.upper_limit)
            if pygame.K_UP in keys or pygame.K_w in keys:
                self.spaceship.moveUp(self.spaceship_speed+3)
            if pygame.K_DOWN in keys or pygame.K_s in keys:
                self.spaceship.moveDown(self.spaceship_speed+3,self.height)

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
                self.e_b +=1
            if pygame.K_o in newkeys:
                self.bullet_up += 1
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

            if  1 in buttons:
                if self.hover(0,50,self.width,self.height-50):
                    self.shootBullet(self.spaceship)
                    self.shootMissile(self.spaceship)
                    self.shootLaser(self.spaceship)
            if pygame.K_SPACE in keys :
                self.shootBullet(self.spaceship)
                self.shootMissile(self.spaceship)
                self.shootLaser(self.spaceship)

            if self.laserDelay >= 60:
                self.laserDelay = 0
            if self.laserDelay <= 0:
                self.laserDelay = 0

            self.delay += 1
            if self.delay >= 120:
                self.delay = 0
            if self.spaceship.health <= 0:
                del self.bullets[:]
                self.spaceship.setAlive(False)
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

            self.starry(self.startoggle)


            for bullet in self.bullets:
                bullet.moveBullet()
                bullet.checkBackWall(self.width)

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
                coin.move(self.spaceship.magnet,self.spaceship.x, self.spaceship.y)
                coin.checkBackWall(0)
                if not coin.alive:
                    continue
                x,y,h,w = coin.getDimensions()
                self.spaceship.checkHitFriendly(x,y,w,h)
                if self.spaceship.hit == True:
                    coin.setAlive(False)
                    self.spaceship.hit = False
                    self.coinn +=1




            self.spaceship_y = self.spaceship.spaceshipPosition()[1]
            for baddie in self.baddies:


                baddie.tick(0,0,self.height, self.spaceship_y)
                if self.bomb == True:
                   self.bomb = False
                   self.boom = True
                   if self.boom == True:
                       del self.baddies[:]

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
                        baddie.decreaseHitPoints(.2)
                        l.setHit(False)
                        baddie.hit = False
                        if baddie.hit_points <= 0:
                            if hasattr(baddie,'hasCoin')==True:
                                self.coins.append(baddie.package(self.coin_width, self.coin_height, self.coin_color,self.particle_direction))


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
            live_particles = []

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
            for p in self.particles:
                if p.alive:
                    live_particles.append(p)

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

    def addRandBaddie(self):

        new_baddie = Baddie(self.baddie_id, self.baddie_width, self.baddie_height, self.width, random.randint(0,(self.height-self.baddie_height)), self.baddie_color, 3, 0)
        self.baddies.append( new_baddie )


        return

    def addRandStrongBaddie(self):
        new_baddie = Baddie(self.baddie_id,self.baddie_width, self.baddie_height, self.width, random.randint(0, (self.height-self.baddie_height)), (155,0,0), 2, 1)
        new_baddie.setHitPoints(2)
        self.baddies.append(new_baddie)

        return

    def addBaddie(self, height):
        new_baddie = Baddie(self.baddie_id, self.baddie_width, self.baddie_height, self.width, height, self.baddie_color, 3, 0 )
        self.baddies.append( new_baddie )
        new_baddie.id
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

    def addStar(self,width,height,x,y,color,speed,direction):
        new_star = Star(width,height,x,y,color,speed,direction)
        self.stars.append(new_star)
        return

    def shootBullet(self, who):
        if self.shootDelay == 10 or self.shootDelay == 20 or self.shootDelay == 30:
            if who.bullet_up ==1:
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,'normal'))
            if who.bullet_up == 2:
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,0,5,'normal'))
                self.bullets.append(who.fire(self.bullet_width,self.bullet_height,self.bullet_color,0,-5,'normal'))
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
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0,-20))
            if self.shootDelay == 30 :

                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0,10))
                self.missiles.append(self.spaceship.launch(self.missile_width, self.missile_height, self.missile_color,0, 20))


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
                    if hasattr(a,'id')=='coin':
                        self.coinn+=1
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
                        self.coinIt(a)
                        self.coinIt(b)
                        return b.hit

            else:
                x,y,h,w = a.getDimensions()
                collideE.checkHit(x,y,w,h)
                if collideE.hit == True:
                    a.hit = True

                    self.hurtIt(collideE,ehurt)
                    self.hurtIt(a,rhurt)
                    self.coinIt(a)

                    self.explodeIt(a)
                    self.explodeIt(collideE)

                    return collideE.hit
    def coinIt(self,who):
        if hasattr(who,'hasCoin')==True:
            self.coins.append(who.package(self.coin_width, self.coin_height, self.coin_color,self.particle_direction))
    def explodeIt(self, who):
        if hasattr(who, 'canBoom')==True:

                self.particles.append(who.explode(self.particle_width,self.particle_height,self.particle_color,self.particle_speed,self.particle_direction))
    def hurtIt(self, who,much):
        if hasattr(who,'friendly')==True:
                pass
        else:
            if hasattr(who,'hit_points')==True:
                who.hit_points -= much
            else:
                who.setAlive(False)

    def newGame(self):
        del self.baddies[:]
        del self.coins[:]
        del self.bullets[:]
        del self.stars[:]
        del self.projectiles[:]
        del self.badBullets[:]
        self.wave1 = True
        self.score = 0
        self.coinn = 0
        self.bombs = 3
        self.spaceship.health = 3
        self.spaceship.x = 0
        self.spaceship.y = self.height/2
        self.a = 0
        self.spaceship.bullet_up = 1
        self.spaceship.missile_up = 0
        self.spaceship.missile_up = 0
        self.spaceship.setAlive(True)


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
        surface.blit(label, (480, 20))
        label2 = myfont.render("Coins "+str(self.coinn), 1, (255,255,0))
        surface.blit(label2, (350, 20))
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

        for s in self.stars:
            s.draw(surface)

        for p in self.powerups:
            p.draw(surface)
        for a in self.projectiles:
            a.draw(surface)
        for baddie in self.baddies:
            baddie.draw(surface)

        for l in self.particles:
            l.draw(surface)


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
