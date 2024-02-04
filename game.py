from functools import cache
import pygame
from pygame.locals import *
import sys
import subprocess
from header import *
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))

bg_image = pygame.image.load("home_bg.jpg").convert()
scaled_image = pygame.transform.scale(bg_image, (1280, 720))
option_image1 = pygame.image.load("arctic_tern.png").convert()
option_image1 = pygame.transform.scale(option_image1, (150, 150))
option_image2 = pygame.image.load("common_swift.png").convert()
option_image2 = pygame.transform.scale(option_image2, (150, 150))
option_image3 = pygame.image.load("loggerhead.png").convert()
option_image3 = pygame.transform.scale(option_image3, (150, 150))
option_image4 = pygame.image.load("bluefin_tuna.png").convert()
option_image4 = pygame.transform.scale(option_image4, (150, 150))
option_image5 = pygame.image.load("Siberian_Rubythroat.png").convert()
option_image5 = pygame.transform.scale(option_image5, (150, 150))
option_image6 = pygame.image.load("snow_goose.png").convert()
option_image6 = pygame.transform.scale(option_image6, (150, 150))
option_image7 = pygame.image.load("european_eel.png").convert()
option_image7 = pygame.transform.scale(option_image7, (150, 150))
option_image8 = pygame.image.load("leatherback.png").convert()
option_image8 = pygame.transform.scale(option_image8, (150, 150))
exit_image = pygame.image.load("exit.jpg").convert()
exit_image = pygame.transform.scale(exit_image, (150, 90))
instruction = pygame.image.load("instruction.jpg").convert()
instruction = pygame.transform.scale(instruction, (150,90))

option1_x = 50+100
option1_y = 70+150
option2_x = 170+100+100
option2_y = 70+150
option5_x = 50+100
option5_y = 200+150+50
option6_x = 170+100+100
option6_y = 200+150+50

option3_x = 430+350
option3_y = 70+150
option4_x = 550+350+100
option4_y = 70+150
option7_x = 430+350
option7_y = 200+150+50
option8_x = 550+350+100
option8_y = 200+150+50

exit_button_x = 570+500
exit_button_y = 400+200
instruction_x = 50
instruction_y = 400+200

option_rect1 = option_image1.get_rect(topleft=(option1_x, option1_y))
option_rect2 = option_image2.get_rect(topleft=(option2_x, option2_y))
option_rect3 = option_image3.get_rect(topleft=(option3_x, option3_y))
option_rect4 = option_image4.get_rect(topleft=(option4_x, option4_y))
option_rect5 = option_image5.get_rect(topleft=(option5_x, option5_y))
option_rect6 = option_image6.get_rect(topleft=(option6_x, option6_y))
option_rect7 = option_image7.get_rect(topleft=(option7_x, option7_y))
option_rect8 = option_image8.get_rect(topleft=(option8_x, option8_y))
exit_button = exit_image.get_rect(topleft=(exit_button_x, exit_button_y))
instruction_button = instruction.get_rect(topleft=(instruction_x, instruction_y))

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the font
font = pygame.font.Font(None, 110)  # None uses the default system font, 36 is the font size

# Create a text surface
game_name = font.render('Game Name!', True, BLACK)  # Text, antialias, text color, background color
bird_name = font.render('Birds', True, BLACK)  # Text, antialias, text color, background color
animal_name = font.render('Animals', True, BLACK)  # Text, antialias, text color, background color
# Get the text surface rectangle
game_name_position = game_name.get_rect()
bird_name_position = bird_name.get_rect()
animal_name_position = animal_name.get_rect()

# Center the text on the screen
game_name_position.center = (1280 // 2, 80)
bird_name_position.center = (330, 170)
animal_name_position.center = (950,170)

SCREEN.blit(scaled_image, (0, 0))
SCREEN.blit(option_image1, (option1_x, option1_y))
SCREEN.blit(option_image2, (option2_x, option2_y))
SCREEN.blit(option_image3, (option3_x, option3_y))
SCREEN.blit(option_image4, (option4_x, option4_y))
SCREEN.blit(option_image5, (option5_x, option5_y))
SCREEN.blit(option_image6, (option6_x, option6_y))
SCREEN.blit(option_image7, (option7_x, option7_y))
SCREEN.blit(option_image8, (option8_x, option8_y))
SCREEN.blit(exit_image, (exit_button_x, exit_button_y))
SCREEN.blit(instruction, (instruction_x, instruction_y))
pygame.draw.line(SCREEN, BLACK, (640, 150), (640, 720), 5)
SCREEN.blit(game_name, game_name_position)
SCREEN.blit(bird_name, bird_name_position)
SCREEN.blit(animal_name, animal_name_position)
pygame.display.flip()


def romil(START_COORDS,DESTINATION_COORDS):
    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
    CONTINENTS_MAP = pygame.transform.scale(pygame.image.load("world_map.jpg"), (1280, 720))
    BIRD_IMAGE = pygame.transform.scale(pygame.image.load("snow_goose.png"), (50, 50))

    # Colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    # Initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bird's Journey")

    # Bird properties
    bird_rect = BIRD_IMAGE.get_rect()
    bird_rect.topleft = START_COORDS
    bird_speed = 10

    # Progress bar
    progress_width = 300
    progress_height = 20
    progress_bar = pygame.Rect((SCREEN_WIDTH - progress_width) // 2, 50, progress_width, progress_height)

    # Flag to check if the bird has reached the destination
    reached_destination = False

    # Main game loop
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle key events
        keys = pygame.key.get_pressed()
        if not reached_destination:
            if keys[pygame.K_LEFT] and bird_rect.left > 0:
                bird_rect.x -= bird_speed

            if keys[pygame.K_RIGHT] and bird_rect.right < SCREEN_WIDTH:
                bird_rect.x += bird_speed

            if keys[pygame.K_UP] and bird_rect.top > 0:
                bird_rect.y -= bird_speed

            if keys[pygame.K_DOWN] and bird_rect.bottom < SCREEN_HEIGHT:
                bird_rect.y += bird_speed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Escape key pressed")
                    pygame.quit()
            # Calculate progress based on distance to destination
            current_position = pygame.math.Vector2(bird_rect.topleft)
            distance_to_destination = current_position.distance_to(DESTINATION_COORDS)
            max_distance = START_COORDS.distance_to(DESTINATION_COORDS)
            progress = 1.0 - min(1.0, distance_to_destination / max_distance)

            # Check if the bird has reached the destination
            if progress >= 0.9:
                reached_destination = True

        # Draw everything
        screen.fill(WHITE)
        screen.blit(CONTINENTS_MAP, (0, 0))

        if not reached_destination:
            # Draw black border for the progress bar
            border_rect = pygame.Rect(progress_bar.left - 2, progress_bar.top - 2, progress_bar.width + 4, progress_bar.height + 4)
            pygame.draw.rect(screen, BLACK, border_rect)

            # Update progress bar based on the current coordinates
            progress_bar.width = progress_width * progress
            pygame.draw.rect(screen, GREEN, progress_bar)

            # Draw percentage inside the progress bar
            pygame.font.init()
            font = pygame.font.SysFont(None, 20)
            percentage = int(progress * 100)
            percentage_text = font.render(f'{percentage}%', True, BLACK)
            percentage_text_rect = percentage_text.get_rect(center=progress_bar.center)
            screen.blit(percentage_text, percentage_text_rect)

        screen.blit(BIRD_IMAGE, bird_rect.topleft)
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Escape key pressed")
                    pygame.quit()
        # Draw a line from source to destination when the bird reaches the destination
        if reached_destination:
            pygame.draw.line(screen, BLACK, START_COORDS, DESTINATION_COORDS, 2)
            pygame.font.init()
            font = pygame.font.SysFont(None, 55)
            text = font.render('You have reached the correct destination!', True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            #ADD picture then the game will start
            game_transition = pygame.image.load("Game_transition.png").convert()
            game_transition = pygame.transform.scale(game_transition, (1280, 720))
            screen.blit(game_transition, (0, 0))
            pygame.time.delay(5000)
            pygame.display.flip()
            script_path = "flappy_game.py"
            subprocess.run(['python', script_path])
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print("Escape key pressed")
                    pygame.quit()

        pygame.display.flip()
        clock.tick(30)

def popup(a):
    if a == 1:
        bg_image = pygame.image.load("popup1.jpg").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        START_COORDS = pygame.math.Vector2(660, 25)
        DESTINATION_COORDS = pygame.math.Vector2(950, 630)
        romil(START_COORDS,DESTINATION_COORDS)

    elif a == 2:
        bg_image = pygame.image.load("popup2.jpg").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        START_COORDS = pygame.math.Vector2(600,120)
        DESTINATION_COORDS = pygame.math.Vector2(660,250)
        romil(START_COORDS,DESTINATION_COORDS)

    elif a == 3:
        bg_image = pygame.image.load("popup3.jpg").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        START_COORDS = pygame.math.Vector2(1110,200)
        DESTINATION_COORDS = pygame.math.Vector2(280, 260)
        romil(START_COORDS,DESTINATION_COORDS)

    elif a == 4:
        bg_image = pygame.image.load("popup4.jpg").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        START_COORDS = pygame.math.Vector2(1100,200)
        DESTINATION_COORDS = pygame.math.Vector2(190,210)
        romil(START_COORDS,DESTINATION_COORDS)

    elif a == 5:
        bg_image = pygame.image.load("popup5.jpg").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        START_COORDS = pygame.math.Vector2(980,60)
        DESTINATION_COORDS = pygame.math.Vector2(980,320)
        romil(START_COORDS,DESTINATION_COORDS)

    elif a == 6:
        bg_image = pygame.image.load("snow_goose_popup.png").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))    
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000) 
        START_COORDS = pygame.math.Vector2(200,120)
        DESTINATION_COORDS = pygame.math.Vector2(240,260)
        romil(START_COORDS,DESTINATION_COORDS)

    elif a == 7:
        bg_image = pygame.image.load("popup7.jpg").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000) 
        START_COORDS = pygame.math.Vector2(330, 190)
        DESTINATION_COORDS = pygame.math.Vector2(570, 220)
        romil(START_COORDS,DESTINATION_COORDS)

    elif a == 8:
        bg_image = pygame.image.load("popup8.jpg").convert()
        scaled_image = pygame.transform.scale(bg_image, (1280, 720))        
        SCREEN.blit(scaled_image, (0, 0))
        pygame.display.update()
        pygame.time.delay(10000)
        START_COORDS = pygame.math.Vector2(165, 180)
        DESTINATION_COORDS = pygame.math.Vector2(1010, 320)
        romil(START_COORDS,DESTINATION_COORDS)

running = True
while running:
    for event in pygame.event.get():     
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # Check if the mouse click occurred within the clickable area of the card
            if option_rect1.collidepoint(event.pos):
                temp = 1
                popup(temp)
                print("Bird1 selected!")
            elif option_rect2.collidepoint(event.pos):
                print("Bird2 selected!")
            elif option_rect3.collidepoint(event.pos):
                print("Bird3 selected!")
            elif option_rect4.collidepoint(event.pos):
                print("Bird4 selected!")
            elif option_rect5.collidepoint(event.pos):
                print("Bird5 selected!")
            elif option_rect6.collidepoint(event.pos):
                temp = 6
                popup(temp)
                print("Bird6 selected!")
            elif option_rect7.collidepoint(event.pos):
                print("Bird7 selected!")
            elif option_rect8.collidepoint(event.pos):
                print("Bird8 selected!")
            elif instruction_button.collidepoint(event.pos):
                print("Instruction button clicked")
            elif exit_button.collidepoint(event.pos):
                print("Exit button clicked")
                pygame.quit()
