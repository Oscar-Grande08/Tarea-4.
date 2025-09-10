import pygame
import random
import sys 

# Inicialización
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Evasión")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial",30)

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK =(0,0,0)

# Cargar imágenes
fondo = pygame.image.load("Imagenes/Becindad.jpg")
fondo = pygame.transform.scale(fondo,(SCREEN_WIDTH, SCREEN_HEIGHT))
jugador_img = pygame.image.load("Imagenes/DonRamon.jpg")
jugador_img= pygame.transform.scale(jugador_img,(70,70))
enemigo_img = pygame.image.load("Imagenes/SeñorBarriga.png")
enemigo_img = pygame.transform.scale(enemigo_img, (60, 60))

# Jugador
player_size = 70
player_x = 400
player_y = 500
player_speed = 5

# Enemigos
enemies = []
enemy_size = 60
enemy_speed = 3

# ---- Menú de dificultad ----
def menu_dificultad():
    global enemy_speed
    font_title=pygame.font.SysFont(None, 60)
    font_option= pygame.font.SysFont(None, 40)
    while True: 
        screen.fill(BLACK)
        titulo= font_title.render("Escoge un nivel de dificultad:", True, WHITE)
        opcion1= font_option.render("1. Fácil", True, WHITE)
        opcion2= font_option.render("2. Medio", True, WHITE)
        opcion3= font_option.render("3. Difícil", True, WHITE)

        screen.blit(titulo, (SCREEN_WIDTH//2 - titulo.get_width()//2, 150))
        screen.blit(opcion1, (SCREEN_WIDTH//2 - opcion1.get_width()//2, 250))
        screen.blit(opcion2, (SCREEN_WIDTH//2 - opcion2.get_width()//2, 300))
        screen.blit(opcion3, (SCREEN_WIDTH//2 - opcion3.get_width()//2, 350))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_1:
                    enemy_speed= 3
                    return
                elif event.key== pygame.K_2:
                    enemy_speed= 6
                    return 
                elif event.key== pygame.K_3:
                    enemy_speed= 10
                    return

# ---- Bucle del juego ----
def game_loop():
    global player_x, player_y, enemies
    player_x = 400
    player_y = 500
    enemies = []
    score = 0
    running = True

    while running:
        screen.blit(fondo, (0,0))   # Fondo de la vecindad

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed

        # Generar enemigos
        if random.randint(1, 20) == 1:
            enemies.append([random.randint(0, SCREEN_WIDTH - enemy_size), 0])

        # Mover y dibujar enemigos
        for enemy in enemies[:]:
            enemy[1] += enemy_speed
            if enemy[1] > SCREEN_HEIGHT:
                enemies.remove(enemy)
                score += 1   # sumar puntos por esquivar
            else:
                screen.blit(enemigo_img, (enemy[0], enemy[1]))

            # Detectar colisiones
            if (player_x < enemy[0] + enemy_size and
                player_x + player_size > enemy[0] and
                player_y < enemy[1] + enemy_size and
                player_y + player_size > enemy[1]):
                running = False

        # Dibujar jugador
        screen.blit(jugador_img,(player_x, player_y))

        # Dibujar puntaje
        score_text= font.render(f"Puntaje: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

# ---- PROGRAMA PRINCIPAL ----
menu_dificultad()
game_loop()
pygame.quit()
