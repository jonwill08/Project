#death sound effect (when bird hits the pipe)
pygame.mixer.init()
def death_sound(sound):
    sound1= pygame.mixer.Sound("collision.wav")
    sound1.play()
#anytime the space bar is used
def jump_sound(sound):
    sound2 = pygame.mixer.Sound("jump.wav")
    sound2.play()
