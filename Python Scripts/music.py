#By: Jessica Ngyuium#
import pygame
def moobSound():
    pygame.mixer.init()
    pygame.mixer.music.load('wall-e1.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(1)
def robotMovementMusic():
    pygame.mixer.init()
    pygame.mixer.music.load('movement_sounds.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(1)
def sampleFoundSound():
    pygame.mixer.init()
    pygame.mixer.music.load('message.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(1)




