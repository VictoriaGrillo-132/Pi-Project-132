import pygame
import random


#current version of the game
TITLE = "Event Horizon"
#VERSION = 0.0
#LAST_UPDATE = datetime.fromtimestamp(os.path.getmtime(__file__))
AUTHOR = 'JA, ID, VG'


#setting GUI size
#width = 900
#height = 500
#window= Tk()
#window.geometry('{}x{}'.format(width, height))
#window.title(TITLE)
#screen size



#setting up the keys for the game
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

RED = (255, 0, 0)

#making the player object by using pygmae.sprite.Sprite
#This allows us to make the game how we want i.e. making the player start on one side of the
#screena and also have the attacks come from the other side of the screen
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_keys[K_SPACE]:
            Bullet.shoot(self)

        #keeping the player from going out of bounds
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

#defining enemys by the pygame sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 2 #Will be how fast the enemy moves
    #getting the sprite to move based on the speed
    #removing it when it goes past the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((15, 5))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.speed = 3 #how fast the bullet will be to attack the enemy

        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centrex = x
        self.speedy = -10
    def __init__(self, x, y):
        self.radius = 15
        self.speed = 3
        self.x = x
        self.y = y
    def shoot(self):
        x = 1
        y = 1
        self.shooting = True
        while self.shooting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #quit()
            pygame.time.Clock().tick(100)

            if y <= 0:
                self.shooting = False
    def update(self):
        self.y -= self.speedy
    def draw(self):
        pygame.draw.circle(d, (255, 0, 0), (self.x, self.y), self.radius)
    

#initialize pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#creating a custom event for adding an enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

#when the enemy is attacked with the player
player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#to keep the game running
running = True
#Main loop for game
while running:
    for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
            bullets.append(bullet(p.x+p.width//2, p.y))
            for b in bullets:
                b.update()
                if b.y < 0:
                    bullets.remove(b)
            for b in bullets:
                b.draw()
                
        #seeing if the player or user hits a key
        if event.type == KEYDOWN:
            #if escape key is pressed, it will stop the loop
            if event.key == K_ESCAPE:
                running = False
        #if the player chooses to close the game
        elif event.type == QUIT:
            running = False

        #adding a new enemy
        elif event.type == ADDENEMY:
            #creating the new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        
        

    #getting the key that is currently being pressed
    pressed_keys = pygame.key.get_pressed()
    #updating player sprite due to the user pressing the keys
    player.update(pressed_keys)
    #updating enemy poistion
    enemies.update()

    #screen filled with black
    screen.fill((0, 0, 0))
    #Having the player drawn on the screen
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        
    #seeing if enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        #if yes, player dies and the loop stops
        player.kill()
        running = False
    ##screen.blit(player.surf, player.rect)
    #updating the display for the game
    pygame.display.flip()








