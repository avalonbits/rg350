# Import the necessary libraries.
import sys, pygame

# Initialize pygame.
pygame.init()

# Define some constants.
# Define the screen size. This is the exact size of the RG350 screen.
width, height = 320, 240

# Define the speed of the ball in the X and Y axis.
speed = [2, 2]

# Define the background color. This is an RGB color, so we need 3 values.
black = 0, 0, 0

# Now we can create the screen with the appropriate size.
screen = pygame.display.set_mode((width, height))

# Load the ball image from a file.
ball = pygame.image.load("ball.png")

# Get its rectangle. This defines the top, bottom, left and right edges of
# the image and we will use to check if the ball hit the edges of the screen.
ballrect = ball.get_rect()

# Loop forever
while 1:
    # Read the next game event.
    for event in pygame.event.get():
        # If this event was a keypress, exit the app.
        if event.type == pygame.KEYDOWN:
            sys.exit()

    # No event to process, let's draw!

    # First, move the ball using the speed values. This will return the
    # updated rectangle.
    ballrect = ballrect.move(speed)

    # Now check if we hit an edge. If we did, reverse the speed for the
    # corresponding direction.
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0] # Reversing speed on X-axis
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1] # Reversing speed on Y-axis

    # Now that the ball has been updated, let's draw!

    # First, fille the screen with a black color.
    screen.fill(black)

    # Now, draw (blit) the ball image to the screen using the rectangle for
    # its position.
    screen.blit(ball, ballrect)

    # This is where we actually send the updated screen to be rendered.
    # Up to here all are drawing was invisible. By calling flip, we tall
    # the program to send our new screen to the video card for rendering.
    pygame.display.flip()
