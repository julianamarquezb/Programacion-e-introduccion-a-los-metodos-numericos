# -*- coding: utf-8 -*-
import pygame, sys
#Inicializando pygame
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
#titulo de la ventana
pygame.display.set_caption("juego")
width, height = 800, 600
speed = [1,1]
white = 255, 255, 255

balon = pygame.image.load("balon.png")
balonrect = balon.get_rect()
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(400,260)

#Bucle del juego
run = True
while run:
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        baterect = baterect.move(0,-1)
    if keys[pygame.K_DOWN]:
        baterect = baterect.move(0,1)
    if baterect.colliderect(balonrect):
        speed[0] = -speed[0]
        
    balonrect = balonrect.move(speed)
    
    if balonrect.left < 0 or balonrect.right > width:
        speed[0] = -speed[0]
    
    if balonrect.top < 0 or balonrect.bottom > height:
        speed[1] = -speed[1]
        
    screen.fill(white)
    screen.blit(balon, balonrect)
    pygame.display.flip()
    
pygame.quit()
