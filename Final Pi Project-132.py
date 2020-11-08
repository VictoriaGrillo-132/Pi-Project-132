import pygame, sys
import random

#color white RGB code
WHITE = (255, 255, 255)

#function that allows text to be displayed
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

    
#defines how the player appears and both the player and bullet are in the same position    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pcship.png").convert()
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def create_bullet(self):
        return Bullet(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    
#defines what the bullets look like and how fast they move
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
        #Will be how fast the enemy moves
        self.speed = 1
        
    #getting the sprite to move based on the speed
    #removing it when it goes past the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

#defines how the background will look
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


#initializes pygame
pygame.init()
#frames per second
clock = pygame.time.Clock()
#screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
#makes the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.mouse.set_visible(False) 

#calls the player class and makes a player group for sprites
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
#defines the sprites groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemy= pygame.sprite.Group()
bullet = pygame.sprite.Group()
#displays the title of the game & creates the background image
pygame.display.set_caption("Event Horizon")
Background = Background('space.png', [0,0])
#creates enemys within the game
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
#defines score and sets value to zero
score = 0
################################################
# Main Program
################################################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #when left side of the mouse is pressed, one bullet is fired per click    
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
        pygame.quit()
        print("Game Over. Your score was " + str(score) + '.')
        break

    #when the bullet hits the enemy, the enemy dies
    hits = pygame.sprite.groupcollide(enemy, bullet, True, True)
    for hit in hits:
        score += 1
        e = Enemy()
        all_sprites.add(e)
        enemy.add(e)


    #drawing things/ objects on the display
    screen.fill((0, 0, 0))
    screen.blit(Background.image, Background.rect)
    enemy.draw(screen)
    bullet.draw(screen)
    player_group.draw(screen)
    draw_text(screen, str(score), 18, SCREEN_WIDTH/2, 10)
    player_group.update()
    bullet.update()
    enemy.update()
    pygame.display.flip()
    #frames per second
    clock.tick(120)
