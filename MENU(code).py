import pygame, os

# Path
current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, 'assets')  # The resource folder path
image_path = os.path.join(resource_path, 'menu')  # The image folder path
pygame.init()
pantalla=pygame.display.set_mode((900,600))
pygame.display.set_caption("Game")
reloj1=pygame.time.Clock()
play1=pygame.image.load(os.path.join(image_path, 'play.png'))
play2=pygame.image.load(os.path.join(image_path, 'play.png'))
options1=pygame.image.load(os.path.join(image_path, 'options1.png'))
options2=pygame.image.load(os.path.join(image_path, 'options1.png'))
exit1=pygame.image.load(os.path.join(image_path, 'exit1.png'))
exit2=pygame.image.load(os.path.join(image_path, 'exit1.png'))
fondo=pygame.image.load(os.path.join(image_path, 'menu.png'))
selecper=pygame.image.load(os.path.join(image_path, 'selecper.png'))
menuopt=pygame.image.load(os.path.join(image_path, 'menuopt.png'))
hombre=pygame.image.load(os.path.join(image_path, 'hombre.png'))
mujer=pygame.image.load(os.path.join(image_path, 'mujer.png'))
class Cursor(pygame.Rect):
        def __init__(self):
            pygame.Rect.__init__(self,0,0,1,1)
        def update(self):
            self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
            self.imagen_normal=imagen1
            self.imagen_seleccion=imagen2
            self.imagen_actual=self.imagen_normal
            self.rect=self.imagen_actual.get_rect()
            self.rect.left,self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal


        pantalla.blit(self.imagen_actual,self.rect)
def seleccionDePersonaje():
    global selecper
    seleccion = False
    boton1=Boton(play1,play2,346,161)
    boton2=Boton(options1,options2,33,11)
    boton3=Boton(exit1,exit2,814,17)
    cursor1=Cursor()
    while seleccion!=True:
        pantalla.blit(selecper, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    fondo=selecper
                if cursor1.colliderect(boton2.rect):
                    fondo=menuopt
                if cursor1.colliderect(boton3.rect):
                    return

            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla,cursor1)
        boton3.update(pantalla,cursor1)
        pygame.display.update()
# Opciones
def opciones():
    global menuopt
    seleccion = False
    boton3=Boton(exit1,exit2,814,17)
    cursor1=Cursor()
    while seleccion!=True:
        pantalla.blit(menuopt, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton3.rect):
                    return

            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        cursor1.update()
        boton3.update(pantalla,cursor1)
        pygame.display.update()
def main():
    global fondo

    boton1=Boton(play1,play2,346,161)
    boton2=Boton(options1,options2,33,11)
    boton3=Boton(exit1,exit2,814,17)
    cursor1=Cursor()


    salir=False

    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    seleccionDePersonaje()
                if cursor1.colliderect(boton2.rect):
                    opciones()
                if cursor1.colliderect(boton3.rect):
                    salir = True

            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        pantalla.blit(fondo, (0,0))
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla,cursor1)
        boton3.update(pantalla,cursor1)
        pygame.display.update()

    pygame.quit()

main()
