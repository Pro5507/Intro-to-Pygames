import pygame
pygame.init()
s= pygame.display.set_mode((400,500))
pygame.display.set_caption('Addig background image to pygame')
bg= pygame.transform.scale(pygame.image.load('bg.jpeg').convert(),(s))
text= pygame.font.Font(None,40).render('Hello World', True, pygame.Color('black'))
def game_loop():
    clock= pygame.time.Clock()
    running= True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
  game_loop()