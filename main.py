import pygame, random, time
from pygame.locals import *
from pygame import font


largura_tela = 400
altura_tela = 800
speed = 10
game_speed = 10
gravidade = 1

largura_base = 2 * largura_tela
altura_base = 100


largura_sabre = 80
altura_sabre = 500
sabre_gap = 200
contador = 0

black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)


class Passaro(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load("assets/asa_meio.png").convert_alpha()]

        self.speed = speed

        self.current_image = 0

        self.image = pygame.image.load("assets/asa_meio.png").convert_alpha() # Convert alpha é pra imagens png
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = largura_tela / 2
        self.rect[1] = altura_tela / 2

    def update(self):
        self.current_image = (self.current_image) # Esse % 3 é pra dizer que quando chegar em 3 elementos, vai resetar (0,1,2 - 0,1,2 - 0,1,2 - ...)

        self.speed += gravidade

        # Update na altura
        self.rect[1] += self.speed

    def voar(self):
        self.speed = -speed

class Sabre(pygame.sprite.Sprite):

    def __init__(self, invertido, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/sabre.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (largura_sabre, altura_sabre))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if invertido:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = altura_tela - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= game_speed        

class Base(pygame.sprite.Sprite):

    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("assets/base.png")
        self.image = pygame.transform.scale(self.image, (largura_base, altura_base))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = altura_tela - altura_base

    def update(self):
        self.rect[0] -= game_speed

def foraTela(sprite):
    return sprite.rect[0] < - (sprite.rect[2])

def sabresRandom(xpos):
    size = random.randint(100, 300)
    sabre = Sabre(False, xpos, size)
    sabre_invertido = Sabre(True, xpos, altura_tela - size - sabre_gap)
    return (sabre, sabre_invertido)

pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))

background = pygame.image.load("assets/background.png").convert_alpha()
background = pygame.transform.scale(background, (largura_tela, altura_tela))
background_user = pygame.image.load("assets/background_user.png").convert_alpha()

nave_grupo = pygame.sprite.Group()
nave = Passaro()
nave_grupo.add(nave) 

base_grupo = pygame.sprite.Group()
for i in range(2):
    base = Base(largura_base * i)
    base_grupo.add(base)

sabre_grupo = pygame.sprite.Group()
for i in range(2):
    sabres = sabresRandom(largura_tela * i + 800)
    sabre_grupo.add(sabres[0])
    sabre_grupo.add(sabres[1])


clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
        if event.type == KEYDOWN:
            if event.key == K_UP:
                nave.voar()

    
    tela.blit(background, (0, 0))

    nave_grupo.update()
    base_grupo.update()
    sabre_grupo.update()

    nave_grupo.draw(tela)
    sabre_grupo.draw(tela)
    base_grupo.draw(tela)
    

    pygame.display.update()   