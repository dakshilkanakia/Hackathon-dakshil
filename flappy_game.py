from pickle import FALSE
import pygame
import subprocess
from pygame import K_ESCAPE, KEYDOWN
from header import *
from barrier import *
from security import safe_command

start_time = time.time()

# Initialize game window
pygame.init()
clock = pygame.time.Clock()
bird_clock = pygame.time.Clock()
running = True

# Load background
background_image = pygame.image.load("sprites/sky.jpg")
background_image = pygame.transform.scale(background_image, (WIN_WIDTH, WIN_HEIGHT))

# Load animated bird sprite
bird_frames = []

frame_folder = "sprites/bird_frames"
for frame_number in range(1, 5):
    frame_path = os.path.join(frame_folder, f"frame-{frame_number}.png")
    frame_image = pygame.image.load(frame_path)
    frame_image = pygame.transform.scale(frame_image, (60, 60))
    bird_frames.append(frame_image)

bird_x = 50
bird_y = (SCREEN.get_height() - bird_frames[0].get_height()) // 2
bird_speed_y = 0
frame_index = 0

# Number of barriers per set
barriers = [Barrier(WIN_WIDTH + i * 300) for i in range(4)]

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)

# Run Game
while running:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("Escape key pressed")
                running = False
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # If space bar is pressed, make the bird jump
            bird_speed_y = -22
            bird_clock.tick(50)

    # Draw background sky img
    SCREEN.blit(background_image, (0, 0))

    ## ----- Bird animation ----- ##
    # Gravity
    bird_speed_y += 3

    # Update the vertical position of the bird
    bird_y += bird_speed_y

    # Keep the bird within the screen boundaries
    bird_y = max(0, min(bird_y, WIN_HEIGHT - 75))

    # Draw bird gif
    bird_rect = SCREEN.blit(bird_frames[frame_index], (bird_x, bird_y))
    frame_index = (frame_index + 1) % len(bird_frames)

    ## ----- Barriers ----- ##
    for barrier in barriers:
        barrier.update()
        barrier.draw()

        # Check for collision with the bird
        top_barrier_rect = pygame.Rect(barrier.x, 0, 50, barrier.top_height)
        bottom_barrier_rect = pygame.Rect(barrier.x, barrier.top_height + barrier.gap, 50, WIN_HEIGHT - barrier.top_height - barrier.gap)

        if is_collision(bird_rect, top_barrier_rect) or is_collision(bird_rect, bottom_barrier_rect):
            # Bird collided with a barrier
            bird_y = (SCREEN.get_height() - bird_frames[0].get_height()) // 2
            bird_speed_y = 0
            barriers = [Barrier(WIN_WIDTH + i * 300) for i in range(4)]  # Reset barriers

            # Display pop-up on loss
            game_over_text = font.render("Game Over! Press SPACE to restart.", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
            SCREEN.blit(game_over_text, game_over_rect)

            pygame.display.flip()

            # Wait for space key to restart
            waiting_for_restart = True
            while waiting_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_restart = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        waiting_for_restart = False
                        TOTAL_DISTANCE = 0
                        start_time = time.time()
            break

        # Check if the player has reached the distance for the next level
        elif TOTAL_DISTANCE >= REQ_DISTANCE:
            # Display "Next Level" option
            next_level_text = font.render("You've reached the destination! Press SPACE to advance.", True, (255, 0, 0))
            next_level_rect = next_level_text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50))
            SCREEN.blit(next_level_text, next_level_rect)
    

            pygame.display.flip()

            # Check for key press to advance to the next level
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        print("jjujjujjuju")
                        script_path1 = "lastpage.py"
                        safe_command.run(subprocess.run, ['python', script_path1])
                        waiting = False
                        running = False
                        pygame.quit()
                        sys.exit()
            break
    end_time = time.time()

    if end_time - start_time > 9:
        # Update total distance
        TOTAL_DISTANCE += barriers[0].speed

        # Display total distance in real-time
        distance_text = font.render(f"Distance: {int(TOTAL_DISTANCE)} mi", True, (255, 255, 255))
        SCREEN.blit(distance_text, (10, 10))

    pygame.display.flip()

    # Increase the speed over time
    for barrier in barriers:
        barrier.speed += 0.0075  # Adjust the rate of speed increase

    # Window fps
    clock.tick(25)
    
