#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
from Tkconstants import FALSE

 
# Variables
WIDTH = 800
HEIGHT = 600
MposX =20
MposY =430
VelocidadX = 3
VelocidadY = 3

cont=6
direc=True
i=0
xixf={}#xinicial y xfinal
Rxixf={}

parabola={}
salto = False

salto_Par=False

#===========================================================


#======================TECLADO===================================
#================================================================
def teclado():
    
    
    global MposX
    global cont, direc,salto, salto_Par
    
     
    
    teclado = pygame.key.get_pressed()
    
    if teclado[K_q] and teclado[K_RIGHT] and salto_Par==False:
        salto_Par=True
    elif teclado[K_q] and teclado[K_LEFT] and salto_Par==False:
        salto_Par=True
         
    elif teclado[K_RIGHT]and salto==False and salto_Par==False:
        MposX+=4
        cont+=1
        direc=True
    elif teclado[K_LEFT]and salto==False and salto_Par==False:
        MposX-=4
        cont+=1
        direc=False
    elif teclado[K_q] and salto==False and salto_Par==False:
        salto=True           
    else :
         cont=4
         
    return 

    
    

#===================SPRITE===============================
#=======================================================
def sprite():

    global cont
 
    xixf[0]=(0,0,44,110)
    xixf[1]=(50,0,44,110)
    xixf[2]=(94,0,44,110)
    xixf[3]=(144,0,44,110)
    
    Rxixf[0]=(155,0,44,110)
    Rxixf[1]=(105,0,44,110)
    Rxixf[2]=(55,0,44,110)
    Rxixf[3]=(5,0,44,110)
    
    p=4
    
    global i
        
    if cont==p:
        i=0

    if cont==p*2:
        i=1
    
    if cont==p*3:
        i=2
    
    if cont==p*4:
        i=3
        cont=0
    
    return


def main():
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guardian del Aire")
    
    aux1 = pygame.Rect(0,430,2,600)
    aux2 = pygame.Rect(830,430,2,600)


    plataforma = pygame.image.load("imagenes/plataform.png")
    plataforma1 = pygame.Rect(461,350,285,10)
    fondo = pygame.image.load("imagenes/fondo.png")          
    sprit = pygame.image.load("imagenes/sprite.png")
    enemigo = pygame.image.load("imagenes/gumy.png")
    #palma = pygame.image.load("imagenes/palma.png")
    #corazon = pygame.image.load("imagenes/corazon.png")
    player = sprit.get_rect()
    player.width = 80
    mario_inv=pygame.transform.flip(mario,True,False);
     
    clock = pygame.time.Clock()
    
    global salto_Par  
    bajada=False
    bajada_Par=False

    # el bucle principal del juego
    while True:
        player.x = MposX
        player.y = MposY
        time = clock.tick(60)
        
        sprite()
        teclado()
        
       
    
        pygame.draw.rect(screen,(180,70,70),plataforma1)
        fondo = pygame.transform.scale(fondo, (800, 600))   
        screen.blit(fondo, (0,0))

        screen.blit(plataforma,(600,400))
        screen.blit(plataforma,(200,300))
        screen.blit(plataforma,(50,100))
        screen.blit(plataforma,(450,200))
        screen.blit(plataforma,(600,60))
        screen.blit(plataforma,(400,350))

        screen.blit(enemigo,(615,395))
        screen.blit(enemigo,(215,295))
        screen.blit(enemigo,(65,95))
        screen.blit(enemigo,(620,55))
        
        global MposX,MposY,salto
        
        if direc==True and salto==False: 
            screen.blit(mario, ( MposX, MposY),(xixf[i]))
    
        if direc==False and salto==False: 
            screen.blit(mario_inv, ( MposX, MposY),(Rxixf[i]))
        
       
       #salto normal
        if salto==True:            
            
            if direc==True:
                screen.blit(mario, ( MposX, MposY),(xixf[1]))
            if direc==False:
                screen.blit(mario_inv, ( MposX, MposY),(Rxixf[1]))   
            
            if bajada==False:
                MposY-=10               
                
            if bajada==True:
                MposY+=10              
            
            if MposY<=350:
                bajada=True
            
            if MposY==430:
                bajada=False
                salto=False
               
            
            
        #==============================   
        
        #SALTO PARABOLICO
        if salto_Par==True and direc==True:            
            
            screen.blit(sprit, ( MposX, MposY),(xixf[1]))
            
            if bajada_Par==False:
                MposY-=10
                MposX+=2
                
            if bajada_Par==True:
                MposY+=10
                MposX+=2
            
            if MposY==330:
                bajada_Par=True
            
            if MposY==430:
                bajada_Par=False
                salto_Par=False

        elif salto_Par==True and direc==FALSE:            
            
            screen.blit(sprit_inv, ( MposX, MposY),(Rxixf[1]))
            
            if bajada_Par==False:
                MposY-=10
                MposX-=2
                
            if bajada_Par==True:
                MposY+=10
                MposX-=2
            
            if MposY==330:
                bajada_Par=True
            
            if MposY==430:
                bajada_Par=False
                salto_Par=False   
    
        pygame.display.flip()
        
        if aux1.colliderect(player):
            MposX += 4
        if aux2.colliderect(player):
            MposX -= 4
        
        # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    return 0



 
if __name__ == '__main__': 
    main()
