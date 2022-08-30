import pygame 

def show_score(choice, color, font, size):
   
    # creating font object score_font
    my_font = pygame.font.Font('grapple.ttf', 50)
     
    # create the display surface object
    # score_surface
    score_surface = my_font.render('Number : ' + str(choice), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)

fps = pygame.time.Clock()
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Paint Writing Recognize')
game_window = pygame.display.set_mode((800, 600))

num = 0

while True:
    num += 1

    game_window.fill(0)

    show_score(num, pygame.Color(255, 255, 255), 'a', 10)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
    
    fps.tick(1)