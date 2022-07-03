import pygame
import os
import random as rd
from sys import exit

#SE INICIA PYGAME
pygame.init()

#SE LE DAN CARACTERISTICAS A LA VENTANA 
pygame.display.set_caption("Squared Away") #titulo
programIcon = pygame.image.load(os.path.join('Assets', 'icon.ico'))
pygame.display.set_icon(programIcon) #icono

FPS = 60
WINDOW_HEIGHT = WINDOW_WIDTH = 600
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TAMANO_CUADRICULA = WINDOW_WIDTH/12

#IMAGENES
FONDO = pygame.image.load(os.path.join('Assets', 'fondo.png')).convert()
CHINCOL = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'chincol.png')),(TAMANO_CUADRICULA, TAMANO_CUADRICULA)).convert()
TIUQUE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Tiuque.png')),(2*TAMANO_CUADRICULA, 2*TAMANO_CUADRICULA)).convert()

#AUDIOS
SONIDO_VICTORIA = pygame.mixer.Sound(os.path.join('Assets', 'audios','Victoria.wav'))
SONIDO_DERROTA = pygame.mixer.Sound(os.path.join('Assets', 'audios','Derrota.wav'))
SONIDO_MOV_CHINCOL = pygame.mixer.Sound(os.path.join('Assets', 'audios','Movimiento Chincol.wav'))
SONIDO_MOV_TIKTOK = pygame.mixer.Sound(os.path.join('Assets', 'audios','Tiktok.wav'))
SONIDO_MOV_CHINCOL.set_volume(0.4)
#SONIDO_MOV_TRUEQUE = pygame.mixer.Sound(os.path.join('Assets', 'audios','Movimiento Tiuques.wav'))


#COLORES
ROJO = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255, 0)

#FUENTES
CUENTA_ATRAS_FONT = pygame.font.SysFont('comicsans', 50)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)
gui_font = pygame.font.Font(None,30)

#VELOCIDADES
VEL_CHINCHOL = 50
VEL_TIUQUE = 100

tiempo_jugador_1 = tiempo_jugador_2 = tiempo_jugador_3 = tiempo_jugador_4 = 0            


def evalua_tiempo(tiempo_jugador, n):
    return 1000//n <= (pygame.time.get_ticks() - tiempo_jugador)

def izquierda_derecha(principal, secundario_1, secundario_2 , jugador_4):
    if principal.right <= jugador_4.left: # DERECHA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.right == secundario_1.left or principal.right == secundario_2.left):
            pass
        else:
            principal.x += VEL_TIUQUE

    elif principal.left >= jugador_4.right: #IZQUIERDA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.left == secundario_1.right or principal.left == secundario_2.right):
            pass
        else:
            principal.x -= VEL_TIUQUE

    elif principal.bottom <= jugador_4.top: #ABAJO
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.bottom == secundario_1.top or principal.bottom == secundario_1.top):
            pass
        else:
            principal.y += VEL_TIUQUE
    
    elif principal.top >= jugador_4.bottom: #ARRIBA
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.top == secundario_1.bottom or principal.top == secundario_2.bottom):
            pass
        else:
            principal.y -= VEL_TIUQUE
    
def arriba_abajo(principal, secundario_1, secundario_2 , jugador_4):
    if principal.bottom <= jugador_4.top: #ABAJO
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.bottom == secundario_1.top or principal.bottom == secundario_1.top):
            pass
        else:
            principal.y += VEL_TIUQUE
    
    elif principal.top >= jugador_4.bottom: #ARRIBA
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.top == secundario_1.bottom or principal.top == secundario_2.bottom):
            pass
        else:
            principal.y -= VEL_TIUQUE

    elif principal.right <= jugador_4.left: # DERECHA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.right == secundario_1.left or principal.right == secundario_2.left):
            pass
        else:
            principal.x += VEL_TIUQUE

    elif principal.left >= jugador_4.right: #IZQUIERDA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.left == secundario_1.right or principal.left == secundario_2.right):
            pass
        else:
            principal.x -= VEL_TIUQUE
            
def movimientos_pc(jugador_1, jugador_2, jugador_3, jugador_4):
    global tiempo_jugador_1, tiempo_jugador_2, tiempo_jugador_3, tiempo_jugador_4
    if evalua_tiempo(tiempo_jugador_1, 1):
        direccion_movimiento = bool(rd.getrandbits(1)) #Genera un número que determinara si buscara primero para arriba/abajo o izquierda/derecha
        if direccion_movimiento:
            izquierda_derecha(jugador_1, jugador_2, jugador_3, jugador_4)
            #SONIDO_MOV_TRUEQUE.play()
            tiempo_jugador_1 = pygame.time.get_ticks()
        else:
            arriba_abajo(jugador_1, jugador_2, jugador_3, jugador_4)
            #SONIDO_MOV_TRUEQUE.play()
            tiempo_jugador_1 = pygame.time.get_ticks()

    if evalua_tiempo(tiempo_jugador_2, 1):
        direccion_movimiento = bool(rd.getrandbits(1)) #Genera un número que determinara si buscara primero para arriba/abajo o izquierda/derecha
        if direccion_movimiento:
            izquierda_derecha(jugador_2, jugador_1, jugador_3, jugador_4)
            tiempo_jugador_2 = pygame.time.get_ticks()
        else:
            arriba_abajo(jugador_2, jugador_1, jugador_3, jugador_4)
            tiempo_jugador_2 = pygame.time.get_ticks()
    
    if evalua_tiempo(tiempo_jugador_3, 1):
        direccion_movimiento = bool(rd.getrandbits(1)) #Genera un número que determinara si buscara primero para arriba/abajo o izquierda/derecha
        if direccion_movimiento:
            izquierda_derecha(jugador_3,jugador_1, jugador_2, jugador_4)
            tiempo_jugador_3 = pygame.time.get_ticks()
        else:
            arriba_abajo(jugador_3,jugador_1, jugador_2, jugador_4)
            tiempo_jugador_3 = pygame.time.get_ticks()

def draw_window(tiempo_restante,jugador_1,jugador_2,jugador_3, jugador_4):
    SCREEN.blit(FONDO, (0,0))
    tiempo_restante_text = CUENTA_ATRAS_FONT.render(tiempo_restante, 1, YELLOW)
    SCREEN.blit(CHINCOL,(jugador_4.x, jugador_4.y))
    SCREEN.blit(TIUQUE,(jugador_1.x, jugador_1.y))
    SCREEN.blit(TIUQUE,(jugador_2.x, jugador_2.y))
    SCREEN.blit(TIUQUE,(jugador_3.x, jugador_3.y))
    SCREEN.blit(tiempo_restante_text, ((WINDOW_WIDTH/2) - (tiempo_restante_text.get_width()/2), 10))

    pygame.display.update()
    
def draw_winner(winner_text):
    draw_text = WINNER_FONT.render(winner_text, 1, ROJO, WHITE)
    SCREEN.blit(draw_text, (WINDOW_WIDTH/2 - draw_text.get_width() /
    2, WINDOW_HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.set_timer(pygame.USEREVENT, 0)
    pygame.time.delay(5000)

def main():
    SONIDO_MOV_TIKTOK.play()
    global tiempo_jugador_4, tiempo_juego_actual
    tiempo_juego_actual = 0
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    counter = 30
    tiempo_restante = "30"
    running = True
    winner_text = ""

    jugador_1 = TIUQUE.get_rect()
    jugador_2 = TIUQUE.get_rect(topright=(WINDOW_WIDTH, 0))
    jugador_3 = TIUQUE.get_rect(bottomleft=(0,WINDOW_HEIGHT))
    jugador_4 = CHINCOL.get_rect(bottomright=(WINDOW_WIDTH, WINDOW_HEIGHT))
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            
            if event.type == pygame.USEREVENT:
                counter -= 1
                tiempo_restante = str(counter)
        
        keys_pressed = pygame.key.get_pressed()

        if evalua_tiempo(tiempo_jugador_4, 9): #El segundo argumento de la función equivale a la velocidad del chinchol
            if keys_pressed[pygame.K_a] and jugador_4.x > 0:  # LEFT
                jugador_4.x -= VEL_CHINCHOL
                SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

            elif keys_pressed[pygame.K_d] and jugador_4.x + + jugador_4.width < WINDOW_WIDTH:  # RIGHT  + VEL_TIUQUE 
                jugador_4.x += VEL_CHINCHOL
                SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

            elif keys_pressed[pygame.K_w] and jugador_4.y  > 0:  # UP - VEL_TIUQUE
                jugador_4.y -= VEL_CHINCHOL
                SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

            elif keys_pressed[pygame.K_s] and jugador_4.y  + jugador_4.height < WINDOW_HEIGHT:  # DOWN + VEL_TIUQUE
                jugador_4.y += VEL_CHINCHOL
                SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

        if 2000 <= tiempo_juego_actual:
            movimientos_pc(jugador_1, jugador_2, jugador_3, jugador_4)

        tiempo_juego_actual = pygame.time.get_ticks() 
        
        draw_window(tiempo_restante, jugador_1,jugador_2,jugador_3,jugador_4)

        if counter == 0:
            winner_text = "gano el Chincol"
            SONIDO_VICTORIA.play()

        if -1 != jugador_4.collidelist([jugador_1, jugador_2, jugador_3]):
            winner_text = "ganaron los Tiuques"
            SONIDO_MOV_TIKTOK.stop()
            SONIDO_DERROTA.play()

        if winner_text != "":
            draw_winner(winner_text)
            break       
    main()

if __name__ == "__main__":
    main()