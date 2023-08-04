import pygame
import os
import random as rd
from sys import exit
import libreria.variables as var


#SE INICIA PYGAME
pygame.init()

#SE LE DAN CARACTERISTICAS A LA VENTANA 
pygame.display.set_caption("Squared Away") #titulo
pygame.display.set_icon(var.programIcon) #icono

SCREEN = pygame.display.set_mode((var.WINDOW_WIDTH, var.WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()

tiempo_jugador_1 = tiempo_jugador_2 = tiempo_jugador_3 = tiempo_jugador_4 = 0            


def evalua_tiempo(tiempo_jugador, n):
    return 1000//n <= (pygame.time.get_ticks() - tiempo_jugador)

def izquierda_derecha(principal, secundario_1, secundario_2 , jugador_4):
    if principal.right <= jugador_4.left: # DERECHA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.right == secundario_1.left or principal.right == secundario_2.left):
            pass
        else:
            principal.x += var.VEL_TIUQUE

    elif principal.left >= jugador_4.right: #IZQUIERDA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.left == secundario_1.right or principal.left == secundario_2.right):
            pass
        else:
            principal.x -= var.VEL_TIUQUE

    elif principal.bottom <= jugador_4.top: #ABAJO
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.bottom == secundario_1.top or principal.bottom == secundario_1.top):
            pass
        else:
            principal.y += var.VEL_TIUQUE
    
    elif principal.top >= jugador_4.bottom: #ARRIBA
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.top == secundario_1.bottom or principal.top == secundario_2.bottom):
            pass
        else:
            principal.y -= var.VEL_TIUQUE
    
def arriba_abajo(principal, secundario_1, secundario_2 , jugador_4):
    if principal.bottom <= jugador_4.top: #ABAJO
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.bottom == secundario_1.top or principal.bottom == secundario_1.top):
            pass
        else:
            principal.y += var.VEL_TIUQUE
    
    elif principal.top >= jugador_4.bottom: #ARRIBA
        if (principal.centerx == secundario_1.centerx or principal.centerx == secundario_2.centerx) and (principal.top == secundario_1.bottom or principal.top == secundario_2.bottom):
            pass
        else:
            principal.y -= var.VEL_TIUQUE

    elif principal.right <= jugador_4.left: # DERECHA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.right == secundario_1.left or principal.right == secundario_2.left):
            pass
        else:
            principal.x += var.VEL_TIUQUE

    elif principal.left >= jugador_4.right: #IZQUIERDA
        if (principal.centery == secundario_1.centery or principal.centery == secundario_2.centery) and (principal.left == secundario_1.right or principal.left == secundario_2.right):
            pass
        else:
            principal.x -= var.VEL_TIUQUE
            
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
    SCREEN.blit(var.FONDO, (0,0))
    tiempo_restante_text = var.CUENTA_ATRAS_FONT.render(tiempo_restante, 1, var.YELLOW)
    SCREEN.blit(var.CHINCOL,(jugador_4.x, jugador_4.y))
    SCREEN.blit(var.TIUQUE,(jugador_1.x, jugador_1.y))
    SCREEN.blit(var.TIUQUE,(jugador_2.x, jugador_2.y))
    SCREEN.blit(var.TIUQUE,(jugador_3.x, jugador_3.y))
    SCREEN.blit(tiempo_restante_text, ((var.WINDOW_WIDTH/2) - (tiempo_restante_text.get_width()/2), 10))

    pygame.display.update()
    
def draw_winner(winner_text):
    draw_text = var.WINNER_FONT.render(winner_text, 1, var.ROJO, var.WHITE)
    SCREEN.blit(draw_text, (var.WINDOW_WIDTH/2 - draw_text.get_width() /
    2, var.WINDOW_HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.set_timer(pygame.USEREVENT, 0)
    pygame.time.delay(5000)

def play_game(dificultad = 'Media'):

    dificultades = {'Fácil': 8,
                    'Media': 9,
                    'Difícil': 10}
    
    numero_dificultad = dificultades.get(dificultad, 8)

    var.SONIDO_MOV_TIKTOK.play()
    global tiempo_jugador_4, tiempo_juego_actual
    tiempo_juego_actual = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    counter = 30
    tiempo_restante = "30"
    running = True
    winner_text = ""

    jugador_1 = var.TIUQUE.get_rect()
    jugador_2 = var.TIUQUE.get_rect(topright=(var.WINDOW_WIDTH, 0))
    jugador_3 = var.TIUQUE.get_rect(bottomleft=(0,var.WINDOW_HEIGHT))
    jugador_4 = var.CHINCOL.get_rect(bottomright=(var.WINDOW_WIDTH, var.WINDOW_HEIGHT))
    while running:
        CLOCK.tick(var.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            
            if event.type == pygame.USEREVENT:
                counter -= 1
                tiempo_restante = str(counter)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    var.SONIDO_MOV_TIKTOK.stop()
                    return
        
        keys_pressed = pygame.key.get_pressed()

        if evalua_tiempo(tiempo_jugador_4, numero_dificultad): #El segundo argumento de la función equivale a la velocidad del chinchol
            if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and jugador_4.x > 0:  # LEFT
                jugador_4.x -= var.VEL_CHINCHOL
                var.SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

            elif (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and jugador_4.x + + jugador_4.width < var.WINDOW_WIDTH:  # RIGHT  + VEL_TIUQUE 
                jugador_4.x += var.VEL_CHINCHOL
                var.SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

            elif (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and jugador_4.y  > 0:  # UP - VEL_TIUQUE
                jugador_4.y -= var.VEL_CHINCHOL
                var.SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

            elif (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and jugador_4.y  + jugador_4.height < var.WINDOW_HEIGHT:  # DOWN + VEL_TIUQUE
                jugador_4.y += var.VEL_CHINCHOL
                var.SONIDO_MOV_CHINCOL.play()
                tiempo_jugador_4 = pygame.time.get_ticks()

        if 2000 <= tiempo_juego_actual:
            movimientos_pc(jugador_1, jugador_2, jugador_3, jugador_4)

        tiempo_juego_actual = pygame.time.get_ticks() 
        
        draw_window(tiempo_restante, jugador_1,jugador_2,jugador_3,jugador_4)

        if counter == 0:
            winner_text = "gano el Chincol"
            var.SONIDO_VICTORIA.play()

        if -1 != jugador_4.collidelist([jugador_1, jugador_2, jugador_3]):
            winner_text = "ganaron los Tiuques"
            var.SONIDO_MOV_TIKTOK.stop()
            var.SONIDO_DERROTA.play()

        if winner_text != "":
            draw_winner(winner_text)
            break

    play_game(dificultad)

def display_menu(texto_seleccionado, dificultad):
    SCREEN.fill((0, 0, 0))
    titulo = var.gui_font.render("Bienvenido a Squared Away!", 1, var.YELLOW)
    SCREEN.blit(titulo, ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2), 120))

    dificultad_actual = var.italics_gui_font.render(f"La dificultad actual es: {dificultad}", 1, var.WHITE)
    SCREEN.blit(dificultad_actual, ((var.WINDOW_WIDTH//2) - (dificultad_actual.get_width()//2), 160))

    aplicaciones = ["Jugar", "Ajustar dificultad", "Salir"]
    
    for i in range(len(aplicaciones)):
        if texto_seleccionado == i:
            pygame.draw.polygon(SCREEN, var.WHITE, (((var.WINDOW_WIDTH//2) - (titulo.get_width()//2) - 30, 260 + i * 75 - 5),
                                                    ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2) - 30, 260 + i * 75 + 5),
                                                    ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2) - 25, 260 + i * 75)))
        texto_aplicacion = var.gui_font.render(aplicaciones[i], 1, var.WHITE)
        SCREEN.blit(texto_aplicacion, ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2), 235 + i * 75))
    pygame.display.update()

def cambiar_dificultad(dificultad):
    
    dificultades_to_idx = {"Fácil": 0,
                    "Media": 1,
                    "Difícil": 2}

    dificultad_seleccionada = dificultades_to_idx[dificultad]

    while True:
        SCREEN.fill((0, 0, 0))
        titulo = var.gui_font.render("SELECCIONA UNA DIFICULTAD", 1, var.YELLOW)
        SCREEN.blit(titulo, ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2), 145))

        dificultades = {0: "Fácil",
                        1: "Media",
                        2: "Difícil"}
        
        for i in range(len(dificultades.keys())):
            if dificultad_seleccionada == i:
                pygame.draw.polygon(SCREEN, var.WHITE, (((var.WINDOW_WIDTH//2) - (titulo.get_width()//2) - 30, 260 + i * 75 - 5),
                                                        ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2) - 30, 260 + i * 75 + 5),
                                                        ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2) - 25, 260 + i * 75)))
            texto_aplicacion = var.gui_font.render(dificultades[i], 1, var.WHITE)
            SCREEN.blit(texto_aplicacion, ((var.WINDOW_WIDTH//2) - (titulo.get_width()//2), 240 + i * 75))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    dificultad_seleccionada = dificultad_seleccionada - 1 if dificultad_seleccionada >= 1 else 2

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    dificultad_seleccionada = dificultad_seleccionada + 1 if dificultad_seleccionada <= 1 else 0

                if event.key == pygame.K_RETURN:
                    return dificultades[dificultad_seleccionada]

        pygame.display.update()

def main():

    CLOCK.tick(var.FPS)
    texto_seleccionado = 0
    dificultad = 'Fácil'

    while True:
        display_menu(texto_seleccionado, dificultad)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    texto_seleccionado = texto_seleccionado - 1 if texto_seleccionado >= 1 else 2

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    texto_seleccionado = texto_seleccionado + 1 if texto_seleccionado <= 1 else 0

                if event.key == pygame.K_RETURN:
                    if texto_seleccionado == 0:
                        play_game(dificultad)

                    elif texto_seleccionado == 1:
                        dificultad = cambiar_dificultad(dificultad)

                    elif texto_seleccionado == 2:
                        pygame.quit()
                        exit()

if __name__ == "__main__":
    main()