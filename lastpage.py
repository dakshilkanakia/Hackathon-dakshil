import pygame
import webbrowser
from pygame.locals import *
from header import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Congratulations Page")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load font
font_h1 = pygame.font.Font(None, 56)  # Larger font for h1
font_h2 = pygame.font.Font(None, 44)  # Font for h2

# Load background GIF
background_gif = pygame.image.load("winning_page.gif")  # Replace with your background GIF path
background_gif = pygame.transform.scale(background_gif, (1280, 720))  # Resize the GIF to match the screen size

# Load video image

image_dict = [['arctic_tern.png','https://www.youtube.com/watch?v=LyqmOpVncxI'],
               ['common_swift.png','https://www.youtube.com/watch?v=kxii_mxQ1dY'],
               ['loggerhead.png','https://www.youtube.com/watch?v=90U533C2pTI'],
               ['bluefin_tuna.png','https://www.youtube.com/watch?v=CGVDK7aTaZw'], 
               ['Siberian_Rubythroat.png','https://www.youtube.com/watch?v=LDN6GzLunLg'],
                ['snow_goose.png','https://www.youtube.com/watch?v=K4vj2nl-cCA'],
                ['european_eel.png','https://www.youtube.com/watch?v=cNqp4tcRRms'],
                ['leatherback.png','https://www.youtube.com/watch?v=UW-rcxcONYY'],
                ]
video_image = pygame.image.load(image_dict[temp][0])  # Replace with your video icon image

image_size = (200, 200)

# Resize the image
video_image = pygame.transform.scale(video_image, image_size)

# Set up clickable area for the video
video_rect = video_image.get_rect(center=(640, 420))  # Adjust the position to the bottom of the screen

# YouTube link
youtube_link = image_dict[temp][1]  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is within the video area
            if video_rect.collidepoint(pygame.mouse.get_pos()):
                webbrowser.open(youtube_link)  # Open the YouTube link in the default web browser
    if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print("Escape key pressed")
                running = False
                pygame.quit()

    # Blit the background GIF
    screen.blit(background_gif, (0, 0))

    # Draw h1 header (Congratulations) above the image
    congrats_text = font_h1.render("Thank you for assisting me on my migration journey!", True, (255, 0, 0))  # Vibrant red font color
    congrats_rect = congrats_text.get_rect(center=(640, 100))
    screen.blit(congrats_text, congrats_rect)

    # Draw h2 header (Blank Header)
    header2_text = font_h2.render("Click if you wanna learn more about me!", True, BLACK)
    header2_rect = header2_text.get_rect(center=(640, 270))
    screen.blit(header2_text, header2_rect)

    # Draw video image
    screen.blit(video_image, video_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()