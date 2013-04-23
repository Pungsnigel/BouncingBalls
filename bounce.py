# Author Jesper Persson
# A template for bouncing balls physics simulation.
import pygame

# Class for representing a ball. Probably no point in changing this for the bouncing balls lab.
class Ball:
    def __init__(self, color, center_x, center_y, radius, dx, dy):
        self.color = color
        self.x = center_x
        self.y = center_y
        self.radius = radius
        self.dx = dx
        self.dy = dy


# ----------------- Main program ----------------- #
# Define some colors. Use them freely throughtout application.
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width,height].
size = [800,600]
screen = pygame.display.set_mode(size)

# Set window title.
pygame.display.set_caption("Bouncing Balls")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define balls and add them to array.
ball_1 = Ball(white, 50, 50, 50, 5, 5)
ball_2 = Ball(green, 500, 300, 30, 6, 6)
myBalls = [ball_1, ball_2]

 
# -------- Main Program Loop ----------- #
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(black)
 
    # Update and draw the balls. Starts by drawing, then updates position for next frame.
    for ball in myBalls:

        #Setting the last argument (width of the line) will tell pygame to draw rather than filling the ball.
        pygame.draw.circle(screen,ball.color,[ball.x,ball.y],ball.radius, 0)

        # Bounce the ball if needed
        if ball.y > size[1] - ball.radius or ball.y < ball.radius:
            ball.dy = ball.dy * -1
        if ball.x > size[0] - ball.radius or ball.x < ball.radius:
            ball.dx = ball.dx * -1
        # Move the ball         
        ball.x += ball.dx
        ball.y += ball.dy
     
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(20)
     
# Close the window and quit.
pygame.quit()