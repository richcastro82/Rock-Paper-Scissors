# RICHARD CASTRO
# DECEMBER 2021
# ROCK-PAPER-SCISSOR GAME GRAPHICAL INTERFACE VERSION

import pygame, sys, random
from random import randint
pygame.init()

fps=30
Win_Width=1200
Win_Height=800
Win_Size=(Win_Width, Win_Height)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(Win_Size)
scoreFont=pygame.font.SysFont('ComicSans', 60)
bg=pygame.image.load('assets/bg.png')
RockUser=pygame.image.load('assets/Rock.png')
PaperUser=pygame.image.load('assets/Paper.png')
StartIcon=pygame.image.load('assets/unknown.png')
ScissorsUser=pygame.image.load('assets/Scissors.png')
Rock=pygame.transform.scale(pygame.image.load('assets/Rock.png'),[100,100])
Paper=pygame.transform.scale(pygame.image.load('assets/Paper.png'),[100,100])
Scissors=pygame.transform.scale(pygame.image.load('assets/Scissors.png'),[100,100])
RestartIcon=pygame.transform.scale(pygame.image.load('assets/restart.png'),[75,75])
Choices=[RockUser, PaperUser, ScissorsUser]


class GamePanel:
    def __init__(self, x, y, image):
        self.x=x
        self.y=y
        self.width=100
        self.height=100
        self.image=image
    def draw(self):
        drawRect=pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.image, drawRect)
    def Hover(self, pos):
        if pos[0]>self.x and pos[0]<self.x+self.width:
            if pos[1]>self.y and pos[1]<self.y+self.height:
                return True
        return False

class Player:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.width=210
        self.height=210
        self.score=0
    def draw(self, image):
        playerRect=pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(image, playerRect)
    def CountScore(self, x, y):
        self.d=x
        self.f=y
        scoreText=str(self.score)
        scoreRect=pygame.Rect(self.d, self.f,100,100)
        scoreDisplay=scoreFont.render(scoreText, True, (200,40,40))
        scoreRect=scoreDisplay.get_rect(center=(self.d, self.f))
        screen.blit(scoreDisplay, scoreRect)



class Game:
    def __init__(self):
        self.P1=Player(Win_Width//4-125,Win_Height//2-125)
        self.P2=Player(Win_Width//4*3-90, Win_Height//2-125)
        self.RockButton=GamePanel(Win_Width//2-160, Win_Height-150, Rock)
        self.PaperButton=GamePanel(Win_Width//2-50, Win_Height-150, Paper)
        self.ScissorsButton=GamePanel(Win_Width//2+60, Win_Height-150, Scissors)
        self.RestartButton=GamePanel(20, Win_Height-110,RestartIcon)
    def DrawBaseElements(self):
        self.RockButton.draw()
        self.PaperButton.draw()
        self.ScissorsButton.draw()
        self.RestartButton.draw()
        pygame.draw.line(screen, (0,0,0),[Win_Width//2, Win_Height//2-60],[Win_Width//2, Win_Height//2+60], 5)
    def ResetBoard(self):
        userIn=StartIcon
        compIn=StartIcon
        self.P1.score=0
        self.P2.score=0
    def Process(self, userIn, compIn):
        if userIn == compIn:
            pass
        if userIn == RockUser:
            if compIn == ScissorsUser:
                self.P1.score+=1
            elif compIn == PaperUser:
                self.P2.score+=1
        if userIn == PaperUser:
            if compIn == ScissorsUser:
                self.P2.score+=1
            elif compIn == RockUser:
                self.P1.score+=1
        if userIn == ScissorsUser:
            if compIn == PaperUser:
                self.P1.score+=1
            elif compIn == RockUser:
                self.P2.score+=1



def main():
    userIn=StartIcon
    compIn=StartIcon
    RUNTIME=Game()
    print(RUNTIME.P1.score)
    while True:
        clock.tick(fps)
        pygame.display.update()
        screen.blit(bg,(0,0))
        RUNTIME.DrawBaseElements()
        RUNTIME.P1.draw(userIn)
        RUNTIME.P2.draw(compIn)
        RUNTIME.P1.CountScore(480,400)
        RUNTIME.P2.CountScore(700,400)
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if RUNTIME.RockButton.Hover(pos):
                    userIn=RockUser
                    compIn=random.choice(Choices)
                    RUNTIME.Process(userIn, compIn)
                if RUNTIME.PaperButton.Hover(pos):
                    userIn=PaperUser
                    compIn=random.choice(Choices)
                    RUNTIME.Process(userIn, compIn)
                if RUNTIME.ScissorsButton.Hover(pos):
                    userIn=ScissorsUser
                    compIn=random.choice(Choices)
                    RUNTIME.Process(userIn, compIn)
                if RUNTIME.RestartButton.Hover(pos):
                    userIn=StartIcon
                    compIn=StartIcon
                    RUNTIME.P1.score=0
                    RUNTIME.P2.score=0


if __name__=="__main__":
    main()
