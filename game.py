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


# Rock=pygame.transform(pygame.image.load('asseets/Rock.png'),50)
# RockRect=pygame.Rect()
#
# Paper=pygame.image.load('asseets/Paper.png')
# PaperRect=pygame.Rect()
#
# Scissors=pygame.image.load('asseets/Scissors.png')
# ScissorsRect=pygame.Rect()



def drawCanvas():
    pass



def main():
    while True:
        clock.tick(fps)
        pygame.display.update()
        screen.blit(bg,(0,0))
        pygame.draw.line(screen, (0,0,0), [600,0],[600,800], width=3)
        screen.blit(Ava1, avaRect)
        screen.blit(Ava2, avaRect2)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()





if __name__=="__main__":
    main()
