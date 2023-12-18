import pygame
import random

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE - Developed by Abdulrahman Bucheeri")

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

block_size = 20
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)

pygame.mixer.music.load("one.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) # Play the music in a loop

def display_score(score):
    score_text = score_font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, [0, 0])

def draw_snake(block_size, snake_body):
    for block in snake_body:
        pygame.draw.rect(window, BLUE, [block[0], block[1], block_size, block_size])

def game_loop():
    game_over = False
    game_exit = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, height - block_size) / block_size) * block_size

    while not game_exit:

        while game_over:
            window.fill(BLACK)
            game_over_text = font_style.render("Game Over MAEAAH! Press Q- Quit or C- Play again.", True, RED)
            window.blit(game_over_text, [width/6, height/3])
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0
        

        x1 += x1_change
        y1 += y1_change

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True
        
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [food_x, food_y, block_size, block_size])
        snake_head = [x1, y1]
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]
        
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True
        
        draw_snake(block_size, snake_body)
        display_score(snake_length - 1)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, height - block_size) / block_size) * block_size
            snake_length += 1
        
        clock.tick(snake_speed)
    
    pygame.mixer.music.stop()
    pygame.quit()
    quit()

game_loop()