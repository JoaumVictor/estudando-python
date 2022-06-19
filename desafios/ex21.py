import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load("rap.mp3")
pygame.mixer.music.play()
pygame.event.wait()

print("finish")
