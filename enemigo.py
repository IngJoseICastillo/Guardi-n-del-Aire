import pygame
from random import randint

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.image = pygame.image.load("assets/nube.png")
        self.rayo = pygame.image.load("assets/rayo.png")
        self.rect = self.rayo.get_rect()
        self.nube = self.image.get_rect()
        self.listaRayos = []
        self.velocidad = 1
        self.nube.left = posX
        self.nube.top = posY
        self.rangoDisparo = 5

    def Movimiento(self, avance):
        if avance:
            if self.nube.x >= 800:
                avance = False
                return avance
            else:
                self.nube.x += 1
                return avance
        else:
            if self.nube.x <= 0:
                avance = True
                return avance
            else:
                self.nube.x -= 1
                return avance
    def ataque(self):
        if (randint(0,300)<self.rangoDisparo):
            self.disparo()
    def disparo(self):
        x,y  = self.nube.center
        y += 20
        miProyectil = pygame.Rect((x, y), (20, 20))
        self.listaRayos.append(miProyectil)
    def trayectoria(self, rayo):
        if rayo.y < 600:
            rayo.y += 5
        else:
            del rayo
