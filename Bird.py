import pygame, random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((500,750))
pygame.display.set_caption("The Bird")
clock = pygame.time.Clock()
# bird code
bird_rect = pygame.Rect(150,300,60,60)
bird = pygame.Surface((bird_rect.width ,bird_rect.height))
bird.fill('Yellow')
# pipe code
pipe_rect1 = pygame.Rect(760, -450, 100, 600)
pipe1 = pygame.Surface((pipe_rect1.width, pipe_rect1.height))
pipe1.fill('Green')

pipe_rect2 = pygame.Rect(760, (pipe_rect1.y+850), 100, 600)
pipe2 = pygame.Surface((pipe_rect2.width, pipe_rect2.height))
pipe2.fill('Green')
# text
font = pygame.font.Font(None, 40)
#Buttons
start_button = pygame.Rect(100,250,120,50)
quit_button = pygame.Rect(300,250,120,50)
def title_screen():
    screen.fill('Black')
    title = font.render("Bird Game", True, (255,255,255))
    start = font.render("Start", True, ("Black"))
    Quit = font.render("Quit", True, ("Black"))
    screen.blit(title, (200, 100))
    pygame.draw.rect(screen, ("White"),(100,250,120,50))
    pygame.draw.rect(screen, ("White"),(300,250,120,50))
    screen.blit(start,(133,260))
    screen.blit(Quit,(330,260))


game = False
start_clicked = False
quit_clicked = False

while True:
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                    if start_button.collidepoint(mouse_pos):
                        start_clicked = True
                    if quit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        exit()

    if start_clicked and not game:
        game = True
        start_clicked = False
        bird.fill('Yellow')
        bird_rect.y = 300
        pipe_rect1.x = 760
        pipe_rect2.x = 760
    if game:
        if keys[pygame.K_SPACE]:
            bird_rect = bird_rect.move(0,-8)
            screen.fill(color=(0,0,0))
        if bird_rect.y > 690:
            bird_rect.y = 690
        elif bird_rect.y < 0:
            bird_rect.y = -1
        if pipe_rect1.x < -100:
            pipe_rect1.x = 760
            pipe_rect1.y = random.randint(-500, -200)
        if pipe_rect2.x < -100:
            pipe_rect2.x = 760
            pipe_rect2.y = pipe_rect1.y +850
        if bird_rect.colliderect(pipe_rect1):
            bird.fill("Red")
            game = False
        elif bird_rect.colliderect(pipe_rect2):
            bird.fill("Red")
            game = False
        pipe_rect1 = pipe_rect1.move(-5, 0)
        pipe_rect2 = pipe_rect2.move(-5, 0)
        bird_rect = bird_rect.move(0, 5)
        screen.fill(color=(0, 0, 0))
        screen.blit(bird, (bird_rect.x, bird_rect.y))
        screen.blit(pipe1, (pipe_rect1.x, pipe_rect1.y))
        screen.blit(pipe2, (pipe_rect2.x, pipe_rect2.y))
        pygame.display.update()
        clock.tick(60)
    if not game:
        title_screen()

        pygame.display.flip()
