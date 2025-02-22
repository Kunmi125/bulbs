import pygame

pygame.init()

WIDTH = 500
HEIGHT = 600

sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc.fill((128,128,128))

img = pygame.image.load("bulbs_off.jpg")
sc.blit(img, (90,90))
pygame.display.update()
running = True

while running:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
         img = pygame.image.load("bulbs_on.jpg")
         sc.blit(img, (90,90))
         pygame.display.update()
    
        elif event.type == pygame.MOUSEBUTTONUP:
            img = pygame.image.load("bulbs_off.jpg")
            sc.blit(img, (90,90))
            pygame.display.update()
      

pygame.quit()

   



