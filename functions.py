from re import T
import pygame, random, time, sys
from pygame.locals import *
from pygame import font

def text_objects(texto, fonte):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('Freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, largeText)
    text_rect.center = ((largura_tela/2, altura_tela/2))
    tela.blit(text_surf, text_rect)
    pygame.display.update()

def game_over(contador):
    fundo = pygame.image.load('assets/fundo_gameover.png').convert_alpha()
    tela = pygame.display.set_mode((500, 800))
    tela.fill((0, 0, 255))
    gameover = "Você perdeu! Pontos: "
    pygame.font.init()
    font = pygame.font.get_default_font()
    font_sys = pygame.font.SysFont(font, 40)
    text_gameover = font_sys.render('Você perdeu! Pontos: ' +str(contador), 1, (255, 255, 255))
    tela.blit(fundo, (0, 0))
    tela.blit(text_gameover, (50, 400))
    pygame.display.update()
    time.sleep(2)

def font():
    base_font = pygame.fon.Font(None, 32)
    user_text = ''
    text_surface = base_font.render(user_text, True, (255, 255, 255))

def fora_tela(sprite):
    return sprite.rect[0] < - (sprite.rect[2])

def email():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([500, 800])
    base_font = pygame.font.Font(None, 32)
    user_text = ''

    input_rect = pygame.Rect(20, 400, 140, 32)
    color_active = pygame.Color("lightskyblue3")
    color_passive = pygame.Color('gray15')
    color = color_passive
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                else:
                    user_text += event.unicode 
        screen.fill((0,0,0))

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen,color,input_rect,2)

        text_surface = base_font.render(user_text, True, (255,255,255))
        screen.blit(text_surface,(input_rect.x + 5, input_rect.y +5))

        input_rect.w = max(50, text_surface.get_width() +10)

        pygame.display.flip()
        pygame.display.update()

    text_gameover = fontsys.render('E-mail: ', 1, (255,255,255))
    pygame.display.update()