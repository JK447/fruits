import pygame
import sys
import random


pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("フルーツ落としゲーム")


WHITE = (255, 255, 255)
FRUIT_COLORS = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]


class Fruit(pygame.sprite.Sprite):
    def __init__(self, color, size, position):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self.size = size
        self.falling = True 


fruit_group = pygame.sprite.Group()

def create_fruit(x, y):
    size = random.randint(20, 50)
    color = random.choice(FRUIT_COLORS)
    fruit = Fruit(color, size, (x, y - size))
    fruit_group.add(fruit)


def update_fruits():
    for fruit in fruit_group:
        if fruit.falling:  
            fruit.rect.y += 5
            if fruit.rect.bottom >= SCREEN_HEIGHT:
                fruit.rect.bottom = SCREEN_HEIGHT
                fruit.falling = False 


running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            x, y = pygame.mouse.get_pos()
            create_fruit(x, y)

    update_fruits()  
    fruit_group.draw(screen)  
    pygame.display.flip() 
    pygame.time.Clock().tick(30) 
