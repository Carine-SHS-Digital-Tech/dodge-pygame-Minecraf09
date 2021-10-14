# Basic Pygame Structure

import pygame                               # Imports pygame and other libraries
import random
pygame.init()                               # Pygame is initialised (starts running)
# Define classes (sprites) here
class Fallingobject(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.timecreated = pygame.time.get.ticks()      # Note the time the object is created in.
        self.image = pygame.Surface({30,30})            # Create a surface on which to display graphics.
        self.image.set_colourkey(black)                 # Set a colour to be transparent.

        self.rect = self.image.get_rect()               # These lines create the regular sprite,
        self.rect.x = random.randint(0,670)             # the same size as the image surface and then
        self.rect.y = 0                                 # assigns it coordinates.

    def setImage(self,graphicSelected):
        fallingObjectsImage = pygame.image.load(graphicSelected)
        self.image.blit(fallingObjectsImage,(0,0))
screen = pygame.display.set_mode([700,500]) # Set the width and height of the screen [width,height]
pygame.display.set_caption("Dodge")
background_image = pygame.image.load("OrchardBackground.jpg").convert()# Load in the background image
done = False                                # Loop until the user clicks the close button.
clock = pygame.time.Clock()                 # Used to manage how fast the screen updates
black    = (   0,   0,   0)                 # Define some colors using rgb values.  These can be
white    = ( 255, 255, 255)                 # used throughout the game instead of using rgb values.

# Define additional Functions and Procedures here

# -------- Main Program Loop -----------
while done == False:

    for event in pygame.event.get():        # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:       # If user clicked close window
            done = True                     # Flag that we are done so we exit this loop

    # Update sprites here
screen.blit(background_image, [0,0])
pygame.display.flip()                   # Go ahead and update the screen with what we've drawn.
clock.tick(20)                          # Limit to 20 frames per second

pygame.quit()                               # Close the window and quit.


