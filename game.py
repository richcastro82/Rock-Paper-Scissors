import pygame, sys, random
from random import randint

pygame.init()

Win_Width=1200
Win_Height=800
Win_Size=(Win_Width, Win_Height)
bgColor=(40,80,120)

clock=pygame.time.Clock()
fps=30
screen=pygame.display.set_mode(Win_Size)


Ava1=pygame.image.load('asseets/Paper.png')
Ava2=pygame.image.load('asseets/unknown.png')

avaRect=pygame.Rect(Win_Width//4-125,Win_Height//2-125,50,50)
avaRect2=pygame.Rect(Win_Width//4*3-90, Win_Height//2-125,50,50)


bg=pygame.image.load('asseets/bg.png')





# GAME LOGIC
#
# RUN GAME AND WAIT FOR USER INPUT
# USER INPUT > RUN METHOD >
# COLLECT USER INPUT
# RANDOM COMPUTER INPUT
# ASSIGN SCORE TO WINNER
# RESET USER IMAGES TO QUESTION MARK
# FINISH METHOD > BACK TO GAME TO WAIT FOR USER INPUT












RockUser=pygame.image.load('asseets/Rock.png')
PaperUser=pygame.image.load('asseets/Paper.png')
ScissorsUser=pygame.image.load('asseets/Scissors.png')
Rock=pygame.transform.scale(pygame.image.load('asseets/Rock.png'),[100,100])
RockRect=pygame.Rect(Win_Width//2-160, Win_Height-150,100,100)
#
Paper=pygame.transform.scale(pygame.image.load('asseets/Paper.png'),[100,100])
PaperRect=pygame.Rect(Win_Width//2-50, Win_Height-150,100,100)
#
Scissors=pygame.transform.scale(pygame.image.load('asseets/Scissors.png'),[100,100])
ScissorsRect=pygame.Rect(Win_Width//2+60, Win_Height-150,100,100)

class Buttons:
    def __init__(self,x,y,image):
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


    def draw(self, image):
        playerRect=pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(image, playerRect)


PLAYER1=Player(Win_Width//4-125,Win_Height//2-125)
PLAYER2=Player(Win_Width//4*3-90, Win_Height//2-125)
RockButton=Buttons(Win_Width//2-160, Win_Height-150, Rock)
PaperButton=Buttons(Win_Width//2-50, Win_Height-150, Paper)
ScissorsButton=Buttons(Win_Width//2+60, Win_Height-150, Scissors)

def DrawBaseElements():
    RockButton.draw()
    PaperButton.draw()
    ScissorsButton.draw()




def main():
    userIn=Ava2

    while True:
        clock.tick(fps)
        pygame.display.update()
        screen.blit(bg,(0,0))
        DrawBaseElements()
        PLAYER1.draw(userIn)
        PLAYER2.draw(Ava2)
        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if RockButton.Hover(pos):
                    userIn=RockUser
                    PLAYER1.draw(userIn)
                if PaperButton.Hover(pos):
                    userIn=PaperUser
                    PLAYER1.draw(userIn)
                if ScissorsButton.Hover(pos):
                    userIn=ScissorsUser
                    PLAYER1.draw(userIn)







if __name__=="__main__":
    main()
