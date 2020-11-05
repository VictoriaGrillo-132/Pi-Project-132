import pygame, sys
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pcship.png").convert()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

    def update(self):
        self.rect.x += 8

        if self.rect.x >= SCREEN_WIDTH + 200:
            self.kill()

#defining enemies by the pygame sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sharknpc.png").convert()
        self.rect = self.image.get_rect(center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random.randint(0, SCREEN_HEIGHT),))
        self.speed = 1 #Will be how fast the enemy moves
    #getting the sprite to move based on the speed
    #removing it when it goes past the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init
clock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(False) 

player = Player()
player_group = pygame.sprite.Group()
player_group.add(Player())

all_sprites = pygame.sprite.Group()
all_sprites.add(Player())
enemy= pygame.sprite.Group()



bullet_group = pygame.sprite.Group()




ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet_group.add(player.create_bullet())
            
        #adding a new enemy
        elif event.type == ADDENEMY:
            #creating the new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemy.add(new_enemy)
            all_sprites.add(new_enemy)


    if pygame.sprite.spritecollideany(player, enemy):
        #if yes, player dies and the loop stops
        player.kill()
        running = False

##    if pygame.sprite.spritecollideany(bullet_group, enemy):
##        #if yes, enemy and bullet both die
##        Bullet().kill()
##        Enemy().kill()


    screen.fill((0, 0, 0))
    enemy.draw(screen)
    bullet_group.draw(screen)
    player_group.draw(screen)
    
    player_group.update()
    bullet_group.update()
    enemy.update()
    pygame.display.flip()
    clock.tick(120)
