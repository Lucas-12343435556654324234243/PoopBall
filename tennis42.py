import pygame
import math
import random
#initialization and checks
pygame.init()
pygame.font.init()
pygame.display.init()
screen = pygame.display.set_mode((1920,1080))
print(pygame.display.get_init())
Clock = pygame.time.Clock()
#constants and variables and objects
green = (10,255,15)
black = (0,0,0)
white =(255,255,255)
gravity = 0.8
bouncefactor = 1
impulse = 14
drag = 0.99

font = pygame.font.SysFont('futura', 30)

title_img = pygame.image.load('TitleFrame.png').convert()
class ball: # GAME OBJECTS
    def __init__(self, xcord, ycord, xvel, yvel, hight,width):  #vel is in pixels per tick (60 ticks per second)
        self.xcord = xcord
        self.ycord = ycord
        self.hight = hight
        self.width = width
        self.xvel = xvel
        self.yvel = yvel

class court:
    def __init__(self, xcord, ycord, hight, width):
        self.xcord = xcord
        self.ycord = ycord
        self.hight = hight
        self.width = width

Court1 = court(80, 880, 300, 2000)  #court inital paramiters
Courtwall  = court(1620, 20, 1080,500)


horioffset = 640
vertoffset = 320





#GAME LOOP
bouncecounter = 0
scorecount = 0
begin = False 
start = False
running = True
while running: #Quit Loop
    
    for event in pygame.event.get(): #EVENT HANDLER
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB: #escape to menue key
                start = False
            if event.key == pygame.K_SPACE: # start game key
                begin = True
                randomnum = random.randint(0,15)          #CREATES RANDOM NUMBER
            if event.key == pygame.K_ESCAPE: #kill key
                running = False


    mousepos = pygame.mouse.get_pos() #Gets mouse cordinates as a tuple
    mousepress = pygame.mouse.get_pressed() #gets moused pressed
    
    
    if start == False: # Menue LOOP
        screen.blit(title_img, (810, 540 ))
        text1 = font.render('Click SPACE to begin', True, green)
        text2 = font.render('Click ESCAPE to exit game', True, green)
        text3 = font.render('So easy an idiot can play it!', True, green)
        text4 = font.render('I guess not...', True, green)
        text5 = font.render("At least you're mommy's little dummy...", True, green)
        text6 = font.render("It can't be that hard can it?", True, green)
        text7 = font.render("I think tic tac toe might be more your speed...", True, green)
        text8 =font.render("[REDACTED]", True, green)
        text9 =font.render("Let me guess, is Mercury in retrograde again?", True, green)
        text10 =font.render("Hi Idiot, my name's Dad...", True, green)
        text11 =font.render("I have no mouth and I must scream...", True, green)
        text12 =font.render("Daisy, Daisy, give me your afternoon...", True, green)
        text13 =font.render("R2 is that you?", True, green)
        text14 =font.render("I'm sorry Dave, I'm afraid I can't do that...", True, green)
        text15 =font.render("BEEP, BOOP...", True, green)
        text16 =font.render("Well here we are again...", True, green)
        text17 =font.render("I AM NOT A MORRON!", True, green)
        text18 =font.render("Android hell is a real place...", True, green)
        text19 =font.render("You mad bro?", True, green)

        screen.blit(text1, (810,700))
        screen.blit(text2, (810,730))
        
        if bouncecounter == 0:
            screen.blit(text3, (810,760))

        if bouncecounter == 2:
            
        
            if randomnum == 0:
                screen.blit(text3, (810,760))    
                screen.blit(text4, (810,780))
            elif randomnum == 1:
                screen.blit(text5, (810,760))
            elif randomnum == 2:
                screen.blit(text6, (810,760))
            elif randomnum == 3:
                screen.blit(text7, (810,760))
            elif randomnum == 4:
                screen.blit(text8, (810,760))
            elif randomnum == 5:
                screen.blit(text9, (810,760))
            elif randomnum == 6:
                screen.blit(text10, (810,760))
            elif randomnum == 7:
                screen.blit(text11, (810,760))
            elif randomnum == 8:
                screen.blit(text12, (810,760))
            elif randomnum == 9:
                screen.blit(text13, (810,760))
            elif randomnum == 10:
                screen.blit(text14, (810,760))
            elif randomnum == 11:
                screen.blit(text15, (810,760))
            elif randomnum == 12:
                screen.blit(text16, (810,760))
            elif randomnum == 13:
                screen.blit(text17, (810,760))
            elif randomnum == 14:
                screen.blit(text18, (810,760))
            elif randomnum == 15:
                screen.blit(text19, (810,760))
        if begin == True:    # BEGINS GAME AND RESETS ALL Flags
            Ball1 = ball(1310, 540, -1, 0, 10,10)
            start = True    #sets start flag to True to begin the game
            begin = False   #resets begin gmae flag
            bounce = True   #resets bounce flag
            scorecount = 0
            bouncecounter = 0
            
    if start == True : #Playing LOOP
        
        ballhit = pygame.Rect(Ball1.xcord, Ball1.ycord, Ball1.width, Ball1.hight)   #ball hit box
        courthit = pygame.Rect(Court1.xcord, Court1.ycord, Court1.width, Court1.hight)  #court hit box
        courthitwall = pygame.Rect(Courtwall.xcord, Courtwall.ycord, Courtwall.width, Courtwall.hight)  #courtwall hit box
        pygame.draw.rect(screen, green, (Ball1.xcord, Ball1.ycord, Ball1.width, Ball1.hight))  #drawing the ball to the screen
        pygame.draw.rect(screen, green, (Court1.xcord, Court1.ycord, Court1.width, Court1.hight))  #drawing the court to the screen
        pygame.draw.rect(screen, green, (Courtwall.xcord, Courtwall.ycord, Courtwall.width, Courtwall.hight))  #drawing the courtwall to the screen
        collisionfloor = ballhit.colliderect(courthit)  #checking for collitions, returns a boolen value
        collisionwall = ballhit.colliderect(courthitwall)

        
        if mousepress[0] == True and bounce == True:
            xleg = Ball1.xcord - mousepos[0]
            yleg = Ball1.ycord - mousepos[1]
            angle =  math.atan2(yleg, xleg)
            ximpulse = math.cos(angle) * impulse
            yimpulse = math.sin(angle) * impulse
            Ball1.xvel = -(Ball1.xvel - ximpulse)
            Ball1.yvel = -(Ball1.yvel - yimpulse)
            print("ximpulse" + str(ximpulse))
            print("yimpulse" + str(yimpulse))
            bounce = False
        if collisionfloor:               #handles bouncing of ball of court floor
            
            Ball1.yvel = -Ball1.yvel * bouncefactor
            bouncecounter = bouncecounter + 1

        if collisionwall:               #handles bouncing of ball of court wall
            bounce = True
            #Ball1.yvel = -Ball1.yvel * bouncefactor
            Ball1.xvel = -Ball1.xvel * bouncefactor
            scorecount = scorecount + 1
            bouncecounter = 0

        if Ball1.xcord <= 0:                             #boarder bounce
            Ball1.xvel = -Ball1.xvel * bouncefactor
        #if Ball1.xcord >= 640:
            Ball1.xvel = -Ball1.xvel * bouncefactor
        if Ball1.ycord <= 0:
            Ball1.yvel = -Ball1.yvel * bouncefactor
        #if Ball1.ycord >= 480:
            Ball1.yvel = -Ball1.yvel * bouncefactor
        
        Ball1.yvel = (1/2* (gravity * gravity) + Ball1.yvel)  # gravity EQ
        Ball1.xvel = Ball1.xvel * drag
        
        
        
        
        
        
        
        
        Ball1.xcord = Ball1.xcord + Ball1.xvel #velocity block updater
        Ball1.ycord = Ball1.ycord + Ball1.yvel

                    
    
        score1 = font.render('SCORE: ' + str(scorecount) +'       If the ball bounces twice you LOSE', True, black) #displays score count
        screen.blit(score1, (200,900))

        if bouncecounter == 2: #handles loose condition
            start = False
            print("loose")
            

    Clock.tick(60)    #keeps constant frame rate 
    pygame.display.update() #final screen update
    screen.fill(black)    #resets screen
pygame.quit()


