import pygame
import random
import sys

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Recolección")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.SysFont(None, 36)
font_title = pygame.font.SysFont(None, 60)
font_option = pygame.font.SysFont(None, 40)

# Cargar imágenes
fondo = pygame.image.load("Imagenes/Simpson.png")
fondo = pygame.transform.scale(fondo, (800, 600))

jugador_img = pygame.image.load("Imagenes/Homero.jpg")
jugador_img = pygame.transform.scale(jugador_img, (70, 70))

item_img = pygame.image.load("Imagenes/Dona.png")
item_img = pygame.transform.scale(item_img, (40, 40))

# Jugador
player_size = 70
player_x = 400
player_y = 300
player_speed = 5

# Objetos
items = []
item_size = 40
item_frequency = 30  # entre más bajo, más rápido aparecen

# Puntuación
score = 0

# MENÚ DE DIFICULTAD 
def menu_dificultad():
    global player_speed, item_frequency
    while True:
        screen.fill(BLACK)
        titulo = font_title.render("Escoge un nivel de dificultad:", True, WHITE)
        opcion1 = font_option.render("1. Fácil", True, WHITE)
        opcion2 = font_option.render("2. Medio", True, WHITE)
        opcion3 = font_option.render("3. Difícil", True, WHITE)

        screen.blit(titulo, (400 - titulo.get_width()//2, 150))
        screen.blit(opcion1, (400 - opcion1.get_width()//2, 250))
        screen.blit(opcion2, (400 - opcion2.get_width()//2, 300))
        screen.blit(opcion3, (400 - opcion3.get_width()//2, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:   # Fácil
                    player_speed = 5
                    item_frequency = 40
                    return
                elif event.key == pygame.K_2: # Medio
                    player_speed = 7
                    item_frequency = 25
                    return
                elif event.key == pygame.K_3: # Difícil
                    player_speed = 9
                    item_frequency = 15
                    return


#BUCLE PRINCIPAL 
running = True
menu_dificultad()

while running:
    screen.blit(fondo, (0, 0))  # Fondo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 800 - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < 600 - player_size:
        player_y += player_speed

    # Generar objetos
    if random.randint(1, item_frequency) == 1:
        items.append([random.randint(0, 800 - item_size),
                      random.randint(0, 600 - item_size)])

    # Recolectar objetos
    for item in items[:]:
        if (player_x < item[0] + item_size and
            player_x + player_size > item[0] and
            player_y < item[1] + item_size and
            player_y + player_size > item[1]):
            items.remove(item)
            score += 1

    # Dibujar objetos
    for item in items:
        screen.blit(item_img, (item[0], item[1]))

    # Dibujar jugador
    screen.blit(jugador_img, (player_x, player_y))

    # Mostrar puntuación
    score_text = font.render(f"Puntos: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
