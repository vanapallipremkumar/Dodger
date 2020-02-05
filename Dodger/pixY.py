import pygame,random,sys,os
from pygame.locals import *

print("(1) FULLSCREEN\n(2) Manual Size")
option=int(input("Enter Option : "))

import ctypes
user=ctypes.windll.user32
Maxwidth=user.GetSystemMetrics(0)
Maxheight=user.GetSystemMetrics(1)
del ctypes
width,height=0,0
clock = pygame.time.Clock()
FPS=30 #for how many frames need to run for a second
if(option==2):  
    while(width<400 or height<400):
        print("(400<WIDTH<=%d and 400<HEIGHT<=%d"%(Maxwidth,Maxheight))
        width=int(input("Width : "))
        height=int(input("Height : "))
        if(width>Maxwidth or height>Maxheight):
            width=0
            height=0

                # ---------------- Methods ------------------------ #
# Method for Terminate the Game
def terminate():
    pygame.quit()
    sys.exit()
# Method to Whether Player pressing any Key to Wait
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if(event.type==QUIT):
                terminate()
            if(event.type==KEYDOWN):
                if(event.key==K_ESCAPE):
                    terminate()
                return
# Method To draw Text one Screen
def drawText(text, font, surface, x, y,center,color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    if(center):
        textrect.center = (int(x), int(y))
    else:
        textrect.topleft= (int(x), int(y))
    surface.blit(textobj, textrect)

# Method to pause Game
def pauseGame(Game):
    while True:
        drawText("PAUSED",pygame.font.SysFont(None,int(width/18)),Game,width/2,height/2,True,(51,255,51))
        drawText("Press \"P\" to Continue",pygame.font.SysFont(None,int(width/40)),Game,width/2,height/2+height/15,True,(255,255,255))
        for event in pygame.event.get():
            if(event.type==QUIT): terminate()
            if(event.type==KEYUP):
                if(event.key==K_ESCAPE): terminate()
                if event.key==K_p:
                    return False
        pygame.display.update()
        clock.tick(1)
    
                # ---------------- DISPLAY ------------------------ #
pygame.init()
if(option==1):
    flags= pygame.FULLSCREEN | pygame.DOUBLEBUF
    Game=pygame.display.set_mode((0, 0),flags)
    width,height=Maxwidth,Maxheight
elif(option==2):
    Game=pygame.display.set_mode((width,height),pygame.DOUBLEBUF)
del option

                # ---------------- COLORS ------------------------ #
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)


                # ---------------- SIZES ------------------------ #
AstMinSize=int(width/60)
AstMaxSize=int(width/25)
PlayerMoveRate=int(width//100)
                # ---------------- PLAYER CREATING CLASS ------------------------ #
class Player(pygame.sprite.Sprite):
    def __init__(self, player,screen,begin,playerPos=None):
        super(Player, self).__init__()
        self.image = player
        self.dimension=(int(height/15),int(height/15))
        self.image = pygame.transform.scale(self.image,self.dimension)
        self.imrect=self.image.get_rect()
        if(begin):
            self.position=((width-self.imrect.width)/2,(height-self.imrect.height))
        else:
            self.position=playerPos
        screen.blit(self.image,self.position)
        self.rect = self.image.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.image)

                # ---------------- ENEMY CREATING CLASS ------------------------ #
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image,screen,minim,maxim,king):
        super(Enemy, self).__init__()
        self.image = image
        if(king):
            self.enemySize=int(height/7)
        else:
            self.enemySize=random.randint(AstMinSize,AstMaxSize)
        self.image=pygame.transform.scale(self.image,(self.enemySize,self.enemySize))
        self.position=(random.randint(0, width-self.enemySize), 0 - self.enemySize)
        screen.blit(self.image,self.position)
        self.speed=random.randint(minim,maxim)
        if(king):
            self.speed=maxim-minim
        self.rect = self.image.get_rect(center=self.position)
        self.mask = pygame.mask.from_surface(self.image)

                # ---------------- FRAME CAPTION ------------------------ #
pygame.display.set_caption("DODGER")

                # ---------------- SOUNDS ------------------------ #
gameOver=pygame.mixer.Sound("gameover.wav")
pygame.mixer.music.load("bgm.mid")

                # ---------------- IMAGES ------------------------ #

                # ---------------- UFO ------------------------ #
ufo=[pygame.image.load("ufo/1.png")]
ufo.append(pygame.image.load("ufo/2.png"))
ufo.append(pygame.image.load("ufo/3.png"))
ufo.append(pygame.image.load("ufo/4.png"))
ufo.append(pygame.image.load("ufo/5.png"))
ufo.append(pygame.image.load("ufo/6.png"))
                # ---------------- Asteroids ------------------------ #

aster=[pygame.image.load("asteroids/1.png")]
aster.append(pygame.image.load("asteroids/2.png"))
aster.append(pygame.image.load("asteroids/3.png"))
aster.append(pygame.image.load("asteroids/4.png"))
aster.append(pygame.image.load("asteroids/5.png"))
aster.append(pygame.image.load("asteroids/6.png"))
                # ---------------- Background ------------------------ #
backgrounds=[pygame.image.load("bg/1.png")]
backgrounds.append(pygame.image.load("bg/2.jpg"))
backgrounds.append(pygame.image.load("bg/3.jpg"))
backgrounds.append(pygame.image.load("bg/4.png"))
backgrounds.append(pygame.image.load("bg/5.png"))
backgrounds.append(pygame.image.load("bg/6.png"))

                # ---------------- START ------------------------ #
if(width==height):
    startBg=pygame.transform.scale(pygame.image.load("sameBg.png"),(width,height))
else:
    startBg=pygame.transform.scale(pygame.image.load("diffBg.png"),(width,height))
Game.blit(startBg,(0,0))
drawText('DODGER', pygame.font.SysFont(None, int(width/15),True), Game,width/2,height/2,True,(0,255,255))
drawText('Press a key to start', pygame.font.SysFont(None, int(width/20)), Game, width/2, (height / 2) + height//10,True,white)
pygame.display.update()
waitForPlayerToPressKey()
del startBg

ScoreFontSize=0
if(width<Maxwidth/2):
    ScoreFontSize=int(width/20)
else:
    ScoreFontSize=int(width/50)
topScore=0
while True:
    bg=pygame.transform.scale(backgrounds[0],(width,height))
    bg2=pygame.transform.rotate(bg,180)
    bgx=0
    bgy=height
    AstMinSpeed=3
    AstMaxSpeed=10
    NewAstRate=12
    ConstAstRate=12
    player=Player(ufo[0],Game,True,None)
    enemies=pygame.sprite.Group(Enemy(aster[0],Game,AstMinSpeed,AstMaxSpeed,False))
    all_enemies=pygame.sprite.Group(player,enemies)
    pause=left=right=up=down=False
    score=0
    level=0
    pygame.mixer.music.play(-1,0.0)
    hit=0
    levelNum=0
    levelInc=False
    levelx=0
    while True:
        score+=1
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    right = False
                    left = True
                if event.key == K_RIGHT or event.key == K_d:
                    left = False
                    right = True
                if event.key == K_UP or event.key == K_w:
                    down = False
                    up = True
                if event.key == K_DOWN or event.key == K_s:
                    up = False
                    down = True
    
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key==K_p:
                    pause=True
                    pygame.mixer.music.pause()
                    pause=pauseGame(Game)
                    pygame.mixer.music.unpause()
                if event.key == K_LEFT or event.key == K_a:
                    left = False
                if event.key == K_RIGHT or event.key == K_d:
                    right = False
                if event.key == K_UP or event.key == K_w:
                    up = False
                if event.key == K_DOWN or event.key == K_s:
                    down = False
        poss=player.image.get_rect()
        if left and (player.rect.centerx-(poss.width/2)-PlayerMoveRate)>= 0:
            player.rect.centerx-=PlayerMoveRate
        if right and (player.rect.centerx+(poss.width/2)+PlayerMoveRate)<= width:
            player.rect.centerx+=PlayerMoveRate
        if up and (player.rect.centery-(poss.height/2)-PlayerMoveRate)>= 0:
            player.rect.centery-=PlayerMoveRate
        if down and (player.rect.centery+(poss.height/2)+PlayerMoveRate)<= height:
            player.rect.centery+=PlayerMoveRate

        NewAstRate-=1
        if(score%100==0 and ConstAstRate>3):
            ConstAstRate-=1
        if(score%100==0):
            level+=1
            if(level==6):
                level=0
            player=Player(ufo[level],Game,False,(player.rect.centerx,player.rect.centery))
            AstMaxSpeed+=1
            enemies.add(pygame.sprite.Group(Enemy(aster[level],Game,AstMinSpeed,AstMaxSpeed,True)))
            bg=pygame.transform.scale(backgrounds[level],(width,height))
            bg2=bg
            levelNum+=1
            levelInc=True
        if(NewAstRate==0):
            NewAstRate=ConstAstRate
            enemies.add(pygame.sprite.Group(Enemy(aster[level],Game,AstMinSpeed,AstMaxSpeed,False)))
        all_enemies=pygame.sprite.Group(player,enemies)
        #spritecollide(sprite, group, dokill, collided = None)
        #The dokill argument is a bool.
        #If set to True, all Sprites that collide will be removed from the Group.
        if pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_mask):
            if(level%3==0 and hit<5):
                continue
            elif(score>topScore):
                topScore=score
            break
        for e in enemies:
            e.rect.centery+=(e.speed)
            position=e.image.get_rect()
            if((e.rect.centery-position.height/2)>height):
                enemies.remove(e)
        # Method to scroll background
        Game.blit(bg,(0,bgx))
        Game.blit(bg2,(0,bgy))
        if(levelx<=height and levelInc):
            levelx+=int(width/50)
            drawText(("Level %s"%(str(levelNum))),pygame.font.SysFont("comicsansms",int(height/5)),Game,levelx,int(height/2),True,white)
        if(levelx>=height):
            levelx=0
            levelInc=False
        bgx+=PlayerMoveRate
        bgy+=PlayerMoveRate
        if(bgx>=height):
            bgx=-1*(height-bgy)
        if(bgy>=height):
            bgy=-1*(height-bgx)
        all_enemies.draw(Game)
        drawText('Score : %s'%(int(score)),pygame.font.SysFont(None,ScoreFontSize),Game,10,10,False,white)
        drawText('Top Score: %s'%(int(topScore)),pygame.font.SysFont(None,ScoreFontSize),Game,10,30,False,white)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.mixer.music.stop()
    gameOver.play()
    drawText("%s"%(str(score)),pygame.font.SysFont(None,int(width/10)),Game,(width / 2), (height / 2)-height/10,True,(255,0,43))
    drawText('GAME OVER', pygame.font.SysFont(None, int(width/20)), Game, (width / 2), (height / 2),True,(85,0,255))
    drawText('Press a key to play again', pygame.font.SysFont(None, int(width/20)), Game, (width / 2), (height / 2)+height/10,True,white)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    # Stopping GameOver Sound
    gameOver.stop()
