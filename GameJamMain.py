# import the pygame module, so you can use it
import pygame
import os

# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    pygame.display.set_caption("Escape The Village")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1920, 1080))

    # define a variable to control the main loop
    running = True
    character_x = 1920/2
    character_y = 1080/2
    background = pygame.image.load(os.path.join('background-1.png'))
    background = pygame.transform.scale(background, (840*4, 650*4))
    background_x = 0
    background_y = 0

    clock = pygame.time.Clock()

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: background_y += 3
        if pressed[pygame.K_DOWN]: background_y -= 3
        if pressed[pygame.K_LEFT]: background_x += 3
        if pressed[pygame.K_RIGHT]: background_x -= 3

        color = (255, 100, 0)
        screen.fill((0, 0, 0))
        screen.blit(background, (background_x, background_y))
        pygame.draw.rect(screen, color, pygame.Rect(character_x, character_y, 60, 60))
        pygame.display.flip()
        clock.tick(60)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
