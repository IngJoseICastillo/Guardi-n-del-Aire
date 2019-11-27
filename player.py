import pygame

salto = False
bajada = False
class Mono(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('assets/player.png')
        self.sheet.set_clip(pygame.Rect(1, 3, 43, 110))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (151, 118, 43, 108), 1: (102, 118, 48, 108), 2: (53, 118, 43, 108), 3: (1, 118, 48, 108) }
        self.right_states = { 0: (1, 3, 43, 108), 1: (46, 3, 48, 108), 2: (97, 3, 43, 108), 3: (142, 3, 48, 108) }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            if self.rect.x > 10:
                self.clip(self.left_states)
                self.rect.x -= 5
        if direction == 'right':
            if self.rect.x < 842:
                self.clip(self.right_states)
                self.rect.x += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, e):
        global salto
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                self.update('left')
            if e.key == pygame.K_RIGHT:
                self.update('right')
            if e.key == pygame.K_UP and self.rect.y == 450:
                salto = True
        if e.type == pygame.KEYUP:

            if e.key == pygame.K_LEFT:
                self.update('stand_left')
            if e.key == pygame.K_RIGHT:
                self.update('stand_right')
            if e.key == pygame.K_UP:
                salto = False
        self.brinco()

    def brinco(self):
        global salto, bajada
        if not bajada:
            if self.rect.y < 450 and self.rect.y >= 350:
                self.rect.y -= 5
            if salto and self.rect.y == 450:
                self.rect.y -= 5
            if not salto and self.rect.y == 345:
                bajada = True

        else:
            if self.rect.y < 450:
                self.rect.y += 5
            if self.rect.y == 450:
                bajada = False

class Mona(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('assets/playar.png')
        self.sheet.set_clip(pygame.Rect(1, 3, 43, 110))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (151, 118, 43, 108), 1: (102, 118, 48, 108), 2: (53, 118, 43, 108), 3: (1, 118, 48, 108) }
        self.right_states = { 0: (1, 3, 43, 108), 1: (46, 3, 48, 108), 2: (97, 3, 43, 108), 3: (142, 3, 48, 108) }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            if self.rect.x > 10:
                self.clip(self.left_states)
                self.rect.x -= 5
        if direction == 'right':
            if self.rect.x < 842:
                self.clip(self.right_states)
                self.rect.x += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, e):
        global salto
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                self.update('left')
            if e.key == pygame.K_RIGHT:
                self.update('right')
        if e.type == pygame.KEYUP:

            if e.key == pygame.K_LEFT:
                self.update('stand_left')
            if e.key == pygame.K_RIGHT:
                self.update('stand_right')
