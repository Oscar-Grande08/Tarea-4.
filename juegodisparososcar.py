import pygame
import random
import sys

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Juego de Disparos")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.SysFont("Arial", 36)

# Jugador 
jugador_img = pygame.image.load("imagenes/Truump.jpg")
jugador_img = pygame.transform.scale(jugador_img, (50, 50))  # tamaño
player_size = 50
player_x = 400
player_y = 500
player_speed = 5

# Enemigo 
enemigo_img = pygame.image.load("imagenes/Maduro.jpg") 
enemigo_img = pygame.transform.scale(enemigo_img, (40, 40))  # tamaño
enemy_size = 40
enemy_speed = 2
enemies = []

# Balas
bullets = []
bullet_speed = 7

# Puntuación
score = 0

# Funciones de dibujado 
def draw_player(x, y):
    screen.blit(jugador_img, (x, y))

def draw_enemy(x, y):
    screen.blit(enemigo_img, (x, y))

def draw_bullet(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, 5, 10))  # bala sigue simple

# Menú de dificultad
def menu_dificultad():
    global enemy_speed, enemy_frequency
    font_title = pygame.font.SysFont("Arial", 60, bold=True)
    font_option = pygame.font.SysFont("Arial", 40)
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
                if event.key == pygame.K_1:
                    enemy_speed = 2
                    enemy_frequency = 40
                    return
                elif event.key == pygame.K_2:
                    enemy_speed = 3
                    enemy_frequency = 25
                    return
                elif event.key == pygame.K_3:
                    enemy_speed = 5
                    enemy_frequency = 15
                    return

# Bucle principal
enemy_frequency = 30
menu_dificultad()
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_size//2 - 2, player_y])
                
    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 800 - player_size:
        player_x += player_speed
        
    # Generar enemigos
    if random.randint(1, enemy_frequency) == 1:
        enemies.append([random.randint(0, 800 - enemy_size), 0])
        
    # Mover enemigos
    for enemy in enemies[:]:
        enemy[1] += enemy_speed
        if enemy[1] > 600:
            enemies.remove(enemy)
        else:
            draw_enemy(enemy[0], enemy[1])
            
    # Mover balas
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
        else:
            draw_bullet(bullet[0], bullet[1])
            
    # Detectar colisiones bala-enemigo
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (bullet[0] < enemy[0] + enemy_size and
                bullet[0] + 5 > enemy[0] and
                bullet[1] < enemy[1] + enemy_size and
                bullet[1] + 10 > enemy[1]):
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemies:
                    enemies.remove(enemy)
                score += 1
                    
    draw_player(player_x, player_y)
    
    # Mostrar puntuación
    score_text = font.render(f"Puntos: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
