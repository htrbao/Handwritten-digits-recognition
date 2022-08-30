from lib2to3.pgen2.literals import test
from random import triangular
import small_load
import mnist_loader
import network
import pygame

fps = pygame.time.Clock()

def show_score(choice, color, font, size):
   
    # creating font object score_font
    my_font = pygame.font.Font('grapple.ttf', 135)
     
    # create the display surface object
    # score_surface
    score_surface = my_font.render('Number : ' + str(choice), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)

# training_data = small_load.load_training()
# validation_data = small_load.load_validation()
# test_data = small_load.load_validation()

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network.Network([784, 250, 10])
net.SGD(training_data, 30, 10, 2.0, test_data= test_data)

pygame.init()
 
# Initialise game window
pygame.display.set_caption('Paint Writing Recognize')
game_window = pygame.display.set_mode((800, 150))

while True:
    game_window.fill(0)

    test_image = small_load.load_image('one.png')

    print(net.recognize(test_image))

    show_score(net.recognize(test_image), pygame.Color(255, 255, 255), 'a', 10)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
    
    fps.tick(1)