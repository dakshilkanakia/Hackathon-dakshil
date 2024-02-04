from header import *

# 
# check for collision between two rectangles
#
# @param rect1 barrier 1
# @param rect2 barrier 2
# @return True if both Rect intersect, F otherwise
#
def is_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Barrier class
class Barrier:

    #
    # @param x starting x coordinate
    #
    def __init__(self, x):
        self.x = x
        self.gap = random.randint(170, 300)  # Random gap length
        self.top_height = random.randint(50, WIN_HEIGHT - self.gap - 50)  # Random top barrier height

        self.image_top = pygame.image.load("sprites/tree_upper.png")
        self.image_top = pygame.transform.scale(self.image_top, (50, self.top_height))

        self.image_bottom = pygame.image.load("sprites/tree_lower.png")
        self.image_bottom = pygame.transform.scale(self.image_bottom, (50, WIN_HEIGHT - self.top_height - self.gap))

        self.speed = 5  # Initial speed

    # Updates each barrier set
    def update(self):
        self.x -= self.speed  # Adjust barrier speed
        if self.x < -50:
            self.x = WIN_WIDTH
            self.gap = random.randint(170, 300) # Random gap between barrier

            self.top_height = random.randint(50, WIN_HEIGHT - self.gap - 50)
            self.top_height = max(self.top_height, 50)
            self.top_height = min(self.top_height, WIN_HEIGHT - self.gap - 50)

            self.image_top = pygame.transform.scale(self.image_top, (50, self.top_height))
            self.image_bottom = pygame.transform.scale(self.image_bottom, (50, WIN_HEIGHT - self.top_height - self.gap))

    # Draw barriers
    def draw(self):
        SCREEN.blit(self.image_top, (self.x, 0))
        SCREEN.blit(self.image_bottom, (self.x, self.top_height + self.gap))