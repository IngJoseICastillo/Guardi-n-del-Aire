import pygame, os, player, time, enemigo
from pygame.locals import *
#Inicizalizar
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
# Path
current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, 'assets')  # The resource folder path
image_path = os.path.join(resource_path, 'menu')  # The image folder path
#Pantalla
pygame.display.set_caption("Juego Feo")
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)

#pause
def Pause(n):
    pause = True
    option = 0
    while pause:
        clock.tick(30)
        screen.blit(menu.BackGround.image, BackGround.rect)
        screen.blit(menu.play1, (418, 103))
        screen.blit(menu.back1, (296, 251))
        screen.blit(menu.exit1, (562, 238))
        screen.blit(menu.pause, (772, 12))
        if option == 0:
            menu.Bordes(screen, [540, 310])
        if option == 1:
            menu.Bordes(screen, [540, 430])
        if option == 2:
            menu.Bordes(screen, [540, 550])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                option = menu.Ciclo2(option)
            if e.type == pygame.KEYUP and e.key == pygame.K_DOWN:
                option = menu.Ciclo1(option)
            if e.type == pygame.KEYDOWN and (e.key == pygame.K_SPACE or e.key == pygame.K_RETURN):
                if option == 0:
                    return True
                if option == 1:
                    if n == 0:
                        level1.restart()
                    if n == 1:
                        level2.restart()
                    if n == 2:
                        level3.restart()
                    return True
                if option == 2:
                    return False
        pygame.display.flip()
#Juego
bg_image = pygame.image.load("assets/fondolevel1.png")
arbol1 = pygame.image.load("assets/arbol1.png")
arbol2 = pygame.image.load("assets/arbol2.png")
arbol3 = pygame.image.load("assets/arbol3.png")
Player = player.Mono((900/2, 450))
Playar = player.Mona((900/2, 450))
#Fondos
running = True
#Clases
class Ranura(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/ranura.png")
        self.ran1 = self.image.get_rect()
        self.ran1.x = 61
        self.ran1.y = 524
        self.ran2 = self.image.get_rect()
        self.ran2.x = 299
        self.ran2.y = 524
        self.ran3 = self.image.get_rect()
        self.ran3.x = 539
        self.ran3.y = 524
        self.ran4 = self.image.get_rect()
        self.ran4.x = 772
        self.ran4.y = 524
class Pasto(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/pasto.png")
pasto = Pasto()

class Jarron(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/jarron.png")
jarron = Jarron()
nube = enemigo.Enemigo(0, 30)


def Nivel1(sexo):
    global running
    avance = True
    running = True
    ranura = Ranura()
    jugador = False
    a1= False
    a2= False
    a3= False
    a4= False
    a5= False
    a = False
    b = False
    c = False
    d = False
    f = False
    score = 0
    segundos = 40
    dt0 = time.time()
    tiempo = 0
    while running:
        avance = nube.Movimiento(avance)
        segundos = dt0 - time.time()
        segundos += 40
        for eventos in pygame.event.get():
            jugador = True
            if eventos.type == pygame.QUIT:
                running = False
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_ESCAPE:
                running = False
        screen.blit(bg_image,(0,0))
        screen.blit(pause, (772, 12))
        screen.blit(ranura.image, (61, 524))
        screen.blit(ranura.image, (299, 524))
        screen.blit(ranura.image, (539, 524))
        screen.blit(ranura.image, (772, 524))
        screen.blit(pasto.image, (250, 549))
        screen.blit(pasto.image, (784, 568))
        screen.blit(pasto.image, (80, 540))
        screen.blit(jarron.image, (23, 516))
        screen.blit(jarron.image, (354, 548))
        screen.blit(jarron.image, (756, 504))
        screen.blit(jarron.image, (860, 509))
        if a1:
            if time.time() > a1Future:
                screen.blit(arbol2, (74,447))
                if not a:
                    a1Fut = time.time() + 5
                    a = True
            else:
                screen.blit(arbol1, (74,472))
        if a2:
            if time.time() > a2Future:
                screen.blit(arbol2, (312,447))
                if not b:
                    a2Fut = time.time() + 5
                    b = True
            else:
                screen.blit(arbol1, (312,472))
        if a3:
            if time.time() > a3Future:
                screen.blit(arbol2, (549,447))
                if not c:
                    a3Fut = time.time() + 5
                    c = True
            else:
                screen.blit(arbol1, (549,472))
        if a4:
            if time.time() > a4Future:
                screen.blit(arbol2, (785,447))
                if not d:
                    a4Fut = time.time() + 5
                    d = True
            else:
                screen.blit(arbol1, (785,472))

        if a and time.time() > a1Fut:
            screen.blit(arbol3, (57,409))
            a1 = False
        if b and time.time() > a2Fut:
            screen.blit(arbol3, (294,409))
            a2 = False
        if c and time.time() > a3Fut:
            screen.blit(arbol3, (534,409))
            a3 = False
        if d and time.time() > a4Fut:
            screen.blit(arbol3, (768,409))
            a4 = False

        xd = "Puntuacion: " + str(score)
        if segundos == 0:
            xd2 = "SOBREVIVISTE!"
            tiempos = font.render(xd2, 1, (255, 255, 255))
            screen.blit(tiempos, (400, 300))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (80, 10, (300 * segundos) / 40, 30))
        if jugador:
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                tiempo += 0.01
                if Player.rect.colliderect(ranura.ran1):
                    if tiempo >= 1.5:
                        if not a1:
                            a1 = True
                            score += 20
                            a1Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran2):
                    if tiempo >= 1.5:
                        if not a2:
                            a2 = True
                            score += 20
                            a2Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran3):
                    if tiempo >= 1.5:
                        if not a3:
                            a3 = True
                            score += 20
                            a3Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran4):
                    if tiempo >= 1.5:
                        if not a4:
                            a4 = True
                            score += 20
                            a4Future = time.time() + 5
            else:
                tiempo = 0
            if sexo == 'hombre':
                screen.blit(Player.image, Player.rect)
                Player.handle_event(eventos)
            if sexo == 'mujer':
                screen.blit(Playar.image, Player.rect)
                Player.handle_event(eventos)
                Playar.handle_event(eventos)
        screen.blit(nube.image, (nube.nube))
        nube.ataque()
        if len(nube.listaRayos) > 0:
            for x in nube.listaRayos:
                screen.blit(nube.rayo, x)
                nube.trayectoria(x)
        print len(nube.listaRayos)
        pygame.display.flip()
        clock.tick(80)

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

    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal


        screen.blit(self.imagen_actual,self.rect)
reloj1=pygame.time.Clock()
play1=pygame.image.load(os.path.join(image_path, 'play1.png'))
play2=pygame.image.load(os.path.join(image_path, 'play2.png'))
options1=pygame.image.load(os.path.join(image_path, 'options1.png'))
options2=pygame.image.load(os.path.join(image_path, 'options2.png'))
exit1=pygame.image.load(os.path.join(image_path, 'exit1.png'))
exit2=pygame.image.load(os.path.join(image_path, 'exit2.png'))
fondo=pygame.image.load(os.path.join(image_path, 'menu.png'))
selecper=pygame.image.load(os.path.join(image_path, 'selecper.png'))
menuopt=pygame.image.load(os.path.join(image_path, 'menuopt.png'))
hombre1=pygame.image.load(os.path.join(image_path, 'hombre2.png'))
hombre2=pygame.image.load(os.path.join(image_path, 'hombre1.png'))
mujer1=pygame.image.load(os.path.join(image_path, 'mujer1.png'))
mujer2=pygame.image.load(os.path.join(image_path, 'mujer2.png'))
back1=pygame.image.load(os.path.join(image_path, 'back1.png'))
back2=pygame.image.load(os.path.join(image_path, 'back2.png'))
sound1=pygame.image.load(os.path.join(image_path, 'sound1.png'))
notsound1=pygame.image.load(os.path.join(image_path, 'notsound1.png'))
sound2=pygame.image.load(os.path.join(image_path, 'sound2.png'))
notsound2=pygame.image.load(os.path.join(image_path, 'notsound2.png'))
complet=pygame.image.load(os.path.join(image_path, 'complet.png'))
pause=pygame.image.load(os.path.join(image_path, 'pause.png'))

def seleccionDePersonaje():
    global selecper
    seleccion = False
    boton1=Boton(hombre1,hombre2,113,187)
    boton2=Boton(mujer1,mujer2,490,187)
    boton3=Boton(exit1,exit2,814,17)
    cursor1=Cursor()
    while seleccion!=True:
        screen.blit(selecper, (0,0))
        for eventos in pygame.event.get():
            if eventos.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    seleccion = True
                    Nivel1("hombre")
                if cursor1.colliderect(boton2.rect):
                    seleccion = True
                    Nivel1("mujer")
                if cursor1.colliderect(boton3.rect):
                    return
            if eventos.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
# Opciones
def opciones():
    global menuopt
    seleccion = False
    boton3=Boton(back1,back2,33,25)
    boton2=Boton(sound1,sound2,284,214)
    boton1=Boton(notsound1,notsound2,492,214)

    cursor1=Cursor()
    while seleccion!=True:
        screen.blit(menuopt, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton3.rect):
                    return

            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
def Menu():
    boton1=Boton(play1,play2,404,249)
    boton2=Boton(options1,options2,33,11)
    boton3=Boton(exit1,exit2,814,17)
    cursor1=Cursor()
    salir=False
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    seleccionDePersonaje()
                if cursor1.colliderect(boton2.rect):
                    opciones()
                if cursor1.colliderect(boton3.rect):
                    salir = True
            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        screen.blit(fondo, (0,0))
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
    pygame.quit()


Menu()
