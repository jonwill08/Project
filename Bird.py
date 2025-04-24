import pygame, random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("The Bird")
clock = pygame.time.Clock()

# Bird setup
bird_rect = pygame.Rect(150, 300, 60, 60)
bird = pygame.Surface((bird_rect.width, bird_rect.height))
bird.fill("Yellow")

# Pipes
pipe_rect1 = pygame.Rect(760, -450, 100, 600)
pipe1 = pygame.Surface((pipe_rect1.width, pipe_rect1.height))
pipe1.fill("Green")

pipe_rect2 = pygame.Rect(760, pipe_rect1.y + 850, 100, 600)
pipe2 = pygame.Surface((pipe_rect2.width, pipe_rect2.height))
pipe2.fill("Green")

# Fonts
font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 70)

# Floating bird effect
hover_offset = 0
hover_direction = 1

#Death sound (when bird hits the pipe)
pygame.mixer.init()
def death_sound(sound):
    sound1= pygame.mixer.Sound("collision.wav")
    sound1.play()
#Space bar sound
def jump_sound(sound):
    sound2 = pygame.mixer.Sound("jump.wav")
    sound2.play()

# Buttons (placed near bottom)
start_button = pygame.Rect(100, 630, 120, 50)
exit_button = pygame.Rect(280, 630, 120, 50)
play_again_button = pygame.Rect(100, 400, 150, 60)
exit_game_button = pygame.Rect(280, 400, 120, 60)
#Images
background = pygame.image.load("./img.png")
# Game states
menu = True
game = False
game_over = False
score = 0
scored_pipe = False

def draw_menu():
    screen.fill((135, 206, 250))  # Sky blue

    # Floating bird animation
    global hover_offset, hover_direction
    if hover_offset >= 10:
        hover_direction = -1
    elif hover_offset <= -10:
        hover_direction = 1
    hover_offset += hover_direction * 0.3
    screen.blit(bird, (220, 280 + hover_offset))

    # Title
    title = big_font.render("THE BIRD GAME", True, (255, 255, 0))
    screen.blit(title, ((500 - title.get_width()) // 2, 100))

    # Instructions for front screen
    instruction1 = font.render("Press SPACE to fly.", True, (255, 255, 255))
    instruction2 = font.render("Avoid the pipes to stay alive!", True, (255, 255, 255))
    instruction3 = font.render("Click 'Start' to begin or 'Exit' to leave.", True, (255, 255, 255))
    Question=font.render("Are you up for the challenge?", True, (255, 255, 255))



    screen.blit(instruction1, ((500 - instruction1.get_width()) // 2, 460))
    screen.blit(instruction2, ((500 - instruction2.get_width()) // 2, 500))
    screen.blit(instruction3, ((500 - instruction3.get_width()) // 2, 580))
    screen.blit(Question, ((500 - Question.get_width()) // 2, 540))


    # Buttons
    pygame.draw.rect(screen, "White", start_button)
    pygame.draw.rect(screen, "White", exit_button)

    start_txt = font.render("Start", True, "Black")
    exit_txt = font.render("Exit", True, "Black")

    screen.blit(start_txt, (start_button.x + (start_button.width - start_txt.get_width()) // 2, start_button.y + 10))
    screen.blit(exit_txt, (exit_button.x + (exit_button.width - exit_txt.get_width()) // 2, exit_button.y + 10))

def draw_gameover(score):
    screen.fill("Black")
    game_over_text = big_font.render("Game Over", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    prompt = font.render("Play Again or Exit?", True, (255, 255, 255))
    play_again_txt = font.render("Play Again", True, "Black")
    exit_txt = font.render("Exit", True, "Black")

    screen.blit(game_over_text, (130, 120))
    screen.blit(score_text, (200, 200))
    screen.blit(prompt, (120, 280))
    pygame.draw.rect(screen, "White", play_again_button)
    pygame.draw.rect(screen, "White", exit_game_button)
    screen.blit(play_again_txt, (play_again_button.x + 5, play_again_button.y + 17.5))
    screen.blit(exit_txt, (exit_game_button.x + 30, exit_game_button.y + 17.5))
    #original code
    #screen.blit(play_again_txt, (play_again_button.x + 10, play_again_button.y + 10))
    #screen.blit(exit_txt, (exit_game_button.x + 25, exit_game_button.y + 10))

def show_score(score):
    display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(display, (10, 10))

# Main loop
while True:
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if menu:
                    if start_button.collidepoint(mouse):
                        menu = False
                        game = True
                        score = 0
                        bird.fill("Yellow")
                        bird_rect.y = 300
                        pipe_rect1.x = 760
                        pipe_rect1.y = random.randint(-500, -200)
                        pipe_rect2.x = 760
                        pipe_rect2.y = pipe_rect1.y + 850
                        scored_pipe = False
                    elif exit_button.collidepoint(mouse):
                        pygame.quit()
                        exit()
                elif game_over:
                    if play_again_button.collidepoint(mouse):
                        game_over = False
                        menu = True
                    elif exit_game_button.collidepoint(mouse):
                        pygame.quit()
                        exit()

    if game:
        if keys[pygame.K_SPACE]:
            bird_rect = bird_rect.move(0, -8)
            def jump_sound(sound):
    sound2 = pygame.mixer.Sound("jump.wav")
    sound2.play()

        bird_rect = bird_rect.move(0, 5)

        if bird_rect.y > 690:
            bird_rect.y = 690
        elif bird_rect.y < 0:
            bird_rect.y = 0

        pipe_rect1.x -= 5
        pipe_rect2.x -= 5

        if pipe_rect1.x < -100:
            pipe_rect1.x = 760
            pipe_rect1.y = random.randint(-500, -200)
            pipe_rect2.x = 760
            pipe_rect2.y = pipe_rect1.y + 850
            scored_pipe = False

        if bird_rect.colliderect(pipe_rect1) or bird_rect.colliderect(pipe_rect2):
            bird.fill("Yellow")
            game = False
            game_over = True
            def death_sound(sound):
    sound1= pygame.mixer.Sound("collision.wav")
    sound1.play()

        if pipe_rect1.x + pipe_rect1.width < bird_rect.x and not scored_pipe:
            score += 1
            scored_pipe = True

        screen.blit(pygame.transform.scale(background, (500,750)), (0,0))
        screen.blit(bird, bird_rect.topleft)
        screen.blit(pipe1, pipe_rect1.topleft)
        screen.blit(pipe2, pipe_rect2.topleft)
        show_score(score)
        pygame.display.update()
        clock.tick(60)

    elif menu:
        draw_menu()
        pygame.display.flip()

    elif game_over:
        draw_gameover(score)
        pygame.display.flip()
