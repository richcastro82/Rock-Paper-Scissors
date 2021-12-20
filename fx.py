import pygame

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
