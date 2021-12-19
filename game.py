import pygame, sys, random
from random import randint

# GAME LOGIC
#
# RUN GAME AND WAIT FOR USER INPUT
# USER INPUT > RUN METHOD >
# COLLECT USER INPUT
# RANDOM COMPUTER INPUT
# ASSIGN SCORE TO WINNER
# RESET USER IMAGES TO QUESTION MARK
# FINISH METHOD > BACK TO GAME TO WAIT FOR USER INPUT

pygame.init()

Win_Width=1200
Win_Height=800
Win_Size=(Win_Width, Win_Height)
bgColor=(40,80,120)
scoreText=pygame.font.SysFont('ComicSans', 60)
bg=pygame.image.load('assets/bg.png')

clock=pygame.time.Clock()
fps=30
screen=pygame.display.set_mode(Win_Size)


StartIcon=pygame.image.load('assets/unknown.png')
RestartIcon=pygame.transform.scale(pygame.image.load('assets/restart.png'),[75,75])
RockUser=pygame.image.load('assets/Rock.png')
PaperUser=pygame.image.load('assets/Paper.png')
ScissorsUser=pygame.image.load('assets/Scissors.png')
Rock=pygame.transform.scale(pygame.image.load('assets/Rock.png'),[100,100])
Paper=pygame.transform.scale(pygame.image.load('assets/Paper.png'),[100,100])
Scissors=pygame.transform.scale(pygame.image.load('assets/Scissors.png'),[100,100])
Choices=[RockUser, PaperUser, ScissorsUser]



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
RestartButton=Buttons(20, Win_Height-110,RestartIcon)

def DrawBaseElements():
    RockButton.draw()
    PaperButton.draw()
    ScissorsButton.draw()
    RestartButton.draw()
    pygame.draw.line(screen, (0,0,0),[Win_Width//2, Win_Height//2-60],[Win_Width//2, Win_Height//2+60], 5)




def main():
    userIn=StartIcon
    compIn=StartIcon

    while True:
        clock.tick(fps)
        pygame.display.update()
        screen.blit(bg,(0,0))

        DrawBaseElements()
        PLAYER1.draw(userIn)
        PLAYER2.draw(compIn)

        for event in pygame.event.get():
            pos=pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if RockButton.Hover(pos):
                    userIn=RockUser
                    compIn=random.choice(Choices)
                if PaperButton.Hover(pos):
                    userIn=PaperUser
                    compIn=random.choice(Choices)
                if ScissorsButton.Hover(pos):
                    userIn=ScissorsUser
                    compIn=random.choice(Choices)
                if RestartButton.Hover(pos):
                    userIn=StartIcon
                    compIn=StartIcon


if __name__=="__main__":
    main()
