import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Game settings
PLAYER_SIZE = 50
OBSTACLE_SIZE = 50
COIN_SIZE = 30
PLAYER_SPEED = 5
OBSTACLE_SPEED = 5
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collect Coins Game")

# Load player image
player_img = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_img.fill(WHITE)

# Load obstacle image
obstacle_img = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE))
obstacle_img.fill(RED)

# Load coin image
coin_img = pygame.Surface((COIN_SIZE, COIN_SIZE))
coin_img.fill(GOLD)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += OBSTACLE_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE)
            self.rect.y = random.randint(-100, -40)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - COIN_SIZE)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += OBSTACLE_SPEED
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - COIN_SIZE)
            self.rect.y = random.randint(-100, -40)

# Main game function
def main():
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    coins = pygame.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Create obstacles
    for _ in range(10):
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Create coins
    for _ in range(5):
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Score
    score = 0
    font = pygame.font.SysFont(None, 55)

    # Game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()

        # Check for collisions
        if pygame.sprite.spritecollideany(player, obstacles):
            running = False  # Game over if collision with obstacle

        coin_collisions = pygame.sprite.spritecollide(player, coins, True)
        score += len(coin_collisions)

        # Draw
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        # Flip the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
