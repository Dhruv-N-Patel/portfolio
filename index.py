import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions and setup
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rama's Leap")

# Load assets
BACKGROUND_IMG = pygame.image.load("ocean.png")  # Ocean background
HANUMAN_IMG = pygame.image.load("hanuman.png")  # Hanuman sprite
SCROLL_IMG = pygame.image.load("scroll.png")  # Scroll sprite
DEMON_IMG = pygame.image.load("demon.png")  # Demon sprite
FIREBALL_IMG = pygame.image.load("fireball.png")  # Fireball sprite

# Resize assets
HANUMAN_IMG = pygame.transform.scale(HANUMAN_IMG, (50, 50))
SCROLL_IMG = pygame.transform.scale(SCROLL_IMG, (30, 30))
DEMON_IMG = pygame.transform.scale(DEMON_IMG, (50, 50))
FIREBALL_IMG = pygame.transform.scale(FIREBALL_IMG, (50, 50))
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Fonts and Colors
FONT = pygame.font.Font(None, 48)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game variables
GRAVITY = 0.8
LEAP_STRENGTH = -12
SCROLL_RESTORE = 15
OBSTACLE_SPEED = 5
energy = 1000
score = 0
scrolls_collected = 0
TARGET_SCROLLS = 10

# States
game_active = False
game_won = False

# Game objects
hanuman = pygame.Rect(100, SCREEN_HEIGHT // 2, 50, 50)
hanuman_velocity = 0
obstacles = []
scrolls = []
obstacle_timer = 0
scroll_timer = 0

# Background variables for parallax
bg_x1 = 0
bg_x2 = SCREEN_WIDTH

# Functions
def display_text(text, x, y, color=WHITE):
    """Display text on the screen."""
    rendered_text = FONT.render(text, True, color)
    SCREEN.blit(rendered_text, (x, y))

def create_obstacle():
    """Create a flying demon or fireball."""
    obstacle_type = random.choice(["demon", "fireball"])
    height = random.randint(50, SCREEN_HEIGHT - 50)
    obstacle = pygame.Rect(SCREEN_WIDTH, height, 50, 50)
    return obstacle, obstacle_type

def create_scroll():
    """Create a scroll (collectible)."""
    height = random.randint(50, SCREEN_HEIGHT - 50)
    scroll = pygame.Rect(SCREEN_WIDTH, height, 30, 30)
    return scroll

def draw_background():
    """Draw scrolling background."""
    global bg_x1, bg_x2
    SCREEN.blit(BACKGROUND_IMG, (bg_x1, 0))
    SCREEN.blit(BACKGROUND_IMG, (bg_x2, 0))
    bg_x1 -= 2
    bg_x2 -= 2
    if bg_x1 <= -SCREEN_WIDTH:
        bg_x1 = SCREEN_WIDTH
    if bg_x2 <= -SCREEN_WIDTH:
        bg_x2 = SCREEN_WIDTH

def draw_elements():
    """Draw all game elements."""
    SCREEN.blit(HANUMAN_IMG, (hanuman.x, hanuman.y))
    for obstacle, obstacle_type in obstacles:
        img = FIREBALL_IMG if obstacle_type == "fireball" else DEMON_IMG
        SCREEN.blit(img, (obstacle.x, obstacle.y))
    for scroll in scrolls:
        SCREEN.blit(SCROLL_IMG, (scroll.x, scroll.y))

def move_elements():
    """Move obstacles and scrolls."""
    for obstacle, _ in obstacles:
        obstacle.x -= OBSTACLE_SPEED
    for scroll in scrolls:
        scroll.x -= OBSTACLE_SPEED

def check_collision():
    """Check for collisions and interactions."""
    global energy, scrolls_collected
    for obstacle, _ in obstacles:
        if hanuman.colliderect(obstacle):
            return True  # Collision with obstacle
    for scroll in scrolls[:]:
        if hanuman.colliderect(scroll):
            scrolls.remove(scroll)
            scrolls_collected += 1
            energy += SCROLL_RESTORE
    return False

def reset_game():
    """Reset all variables for a new game."""
    global obstacles, scrolls, hanuman, hanuman_velocity, energy, score, scrolls_collected
    obstacles.clear()
    scrolls.clear()
    hanuman = pygame.Rect(100, SCREEN_HEIGHT // 2, 50, 50)
    hanuman_velocity = 0
    energy = 1000
    score = 0
    scrolls_collected = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    SCREEN.fill(WHITE)
    draw_background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                reset_game()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            hanuman_velocity = LEAP_STRENGTH
            energy -= 10

    if game_active:
        # Move Hanuman
        hanuman_velocity += GRAVITY
        hanuman.y += hanuman_velocity

        # Spawn obstacles and scrolls
        obstacle_timer += 1
        if obstacle_timer > 80:
            obstacle_timer = 0
            obstacles.append(create_obstacle())

        scroll_timer += 1
        if scroll_timer > 150:
            scroll_timer = 0
            scrolls.append(create_scroll())

        # Move elements and check collisions
        move_elements()
        obstacles = [ob for ob in obstacles if ob[0].x > 0]
        scrolls = [sc for sc in scrolls if sc.x > 0]
        if check_collision() or energy <= 0:
            game_active = False
        elif scrolls_collected >= TARGET_SCROLLS:
            game_active = False
            game_won = True

        # Update score
        score += 1

        # Draw game elements
        draw_elements()
        display_text(f"Score: {score}", 10, 10)
        display_text(f"Energy: {energy}", 10, 50)
        display_text(f"Scrolls: {scrolls_collected}/{TARGET_SCROLLS}", 10, 90)
    else:
        if game_won:
            display_text("You Win!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, RED)
        else:
            display_text("Game Over", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, RED)
        display_text("Press SPACE to Retry", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, WHITE)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
