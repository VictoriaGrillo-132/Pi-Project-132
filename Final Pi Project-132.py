import pygame, sys
import random

WHITE = (255, 255, 255)
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
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

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(False) 

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemy= pygame.sprite.Group()



bullet = pygame.sprite.Group()

pygame.display.set_caption("Event Horizon")
Background = Background('space.png', [0,0])

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet.add(player.create_bullet())
            
        #adding a new enemy
        elif event.type == ADDENEMY:
            #creating the new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemy.add(new_enemy)
            all_sprites.add(new_enemy)

    all_sprites.update()
    #if yes, player dies and the loop stops and game is over
    hits = pygame.sprite.spritecollide(player, enemy, False)
    if hits:
        running = False

    #when the bullet hits the enemy, the enemy dies
    hits = pygame.sprite.groupcollide(enemy, bullet, True, True)
    for hit in hits:
        score += 1
        print(score)
        e = Enemy()
        all_sprites.add(e)
        enemy.add(e)


    
    screen.fill((0, 0, 0))
    screen.blit(Background.image, Background.rect)
    #draw_text(screen, str(score), 18, SCREEN_WIDTH/2, SCREEN_HEIGHT )
    enemy.draw(screen)
    bullet.draw(screen)
    player_group.draw(screen)
    draw_text(screen, str(score), 18, SCREEN_WIDTH/2, 10)
    player_group.update()
    bullet.update()
    enemy.update()
    pygame.display.flip()
    clock.tick(120)
