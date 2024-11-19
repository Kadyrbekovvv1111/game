import pygame

pygame.init()

clock = pygame.time.Clock()

pygame.mixer.init()


pygame.mixer.music.load("music/game.mp3")
pygame.mixer.music.play(-1, 0.0)

screen = pygame.display.set_mode((800, 449))
pygame.display.set_caption("Game")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("images/backround.jpg")


walk_left = [
    pygame.image.load('images/player_left/person_left_1.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_2.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_3.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_4.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_5.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_6.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_7.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_8.png').convert_alpha(),
    pygame.image.load('images/player_left/person_left_9.png').convert_alpha(),
]

walk_right = [
    pygame.image.load('images/player_right/person_right_1.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_2.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_3.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_4.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_5.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_6.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_7.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_8.png').convert_alpha(),
    pygame.image.load('images/player_right/person_right_9.png').convert_alpha(),
]


player= pygame.image.load('images/person.png').convert_alpha()


jump = pygame.image.load('images/person.png').convert_alpha()


player_x = 80
player_y = 270
player_speed = 10
player_amin_count = 0
is_jumping = False
jump_velocity = -15
gravity = 1 
player_y_velocity = 0 

bg_x = 0

running = True
while running:


    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + 800, 0))

    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        player_y_velocity = jump_velocity


    if is_jumping:
        player_y += player_y_velocity
        player_y_velocity += gravity


        if player_y >= 270:
            player_y = 270
            is_jumping = False
            player_y_velocity = 0


    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_amin_count], (player_x, player_y))
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        screen.blit(walk_right[player_amin_count], (player_x, player_y))
        player_x += player_speed
    else:
        screen.blit(player, (player_x, player_y))



    if player_amin_count == 8:
        player_amin_count = 0    
    else:
        player_amin_count += 1


    bg_x -= 2
    if bg_x <= -800:
        bg_x = 0


    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(25)


pygame.mixer.music.stop()
