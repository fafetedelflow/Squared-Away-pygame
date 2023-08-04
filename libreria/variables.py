#ARCHIVO DE VARIABLES

#IMPORTS
import pygame
import os
pygame.init()

#VARIABLES
FPS = 60
WINDOW_HEIGHT = WINDOW_WIDTH = 600
TAMANO_CUADRICULA = WINDOW_WIDTH//12

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#ICONOS
programIcon = pygame.image.load(os.path.join('.', 'Assets', 'icon.ico'))

#IMAGENES
FONDO = pygame.image.load(os.path.join('.','Assets', 'fondo.png')).convert()
CHINCOL = pygame.transform.scale(pygame.image.load(os.path.join('.','Assets', 'chincol.png')),(TAMANO_CUADRICULA, TAMANO_CUADRICULA)).convert()
TIUQUE = pygame.transform.scale(pygame.image.load(os.path.join('.', 'Assets', 'Tiuque.png')),(2*TAMANO_CUADRICULA, 2*TAMANO_CUADRICULA)).convert()

#AUDIOS
SONIDO_VICTORIA = pygame.mixer.Sound(os.path.join('.','Assets', 'audios','Victoria.wav'))
SONIDO_DERROTA = pygame.mixer.Sound(os.path.join('.','Assets', 'audios','Derrota.wav'))
SONIDO_MOV_CHINCOL = pygame.mixer.Sound(os.path.join('.','Assets', 'audios','Movimiento Chincol.wav'))
SONIDO_MOV_TIKTOK = pygame.mixer.Sound(os.path.join('.','Assets', 'audios','Tiktok.wav'))
SONIDO_MOV_CHINCOL.set_volume(0.4)
#SONIDO_MOV_TRUEQUE = pygame.mixer.Sound(os.path.join('Assets', 'audios','Movimiento Tiuques.wav'))


#FUENTES
CUENTA_ATRAS_FONT = pygame.font.SysFont('comicsans', 50)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)
gui_font = pygame.font.SysFont('comicsans',30)
italics_gui_font = pygame.font.SysFont('comicsans', 20, italic = True)

#COLORES
ROJO = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255, 0)

#VELOCIDADES
VEL_CHINCHOL = 50
VEL_TIUQUE = 100