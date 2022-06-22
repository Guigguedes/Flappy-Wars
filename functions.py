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

