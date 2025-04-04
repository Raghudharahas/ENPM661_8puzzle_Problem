import pygame
import time
import numpy as np
import imageio.v2 as imageio  # Use v2 to avoid deprecation warning

# Load path from nodePath.txt
track = []
with open('nodePath.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]  # Skip blank lines

    for i in range(0, len(lines), 3):
        values = []
        for j in range(3):
            values.extend(map(int, lines[i + j].split()))
        state = np.array(values).reshape(3, 3)
        track.append(state)  # <- DO NOT transpose

# Initialize Pygame
pygame.init()
window_size = (300, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("8 Puzzle Animation")

# Colors and font
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
font = pygame.font.SysFont('Arial', 30)

# Grid setup
grid_size = 3
cell_size = 100

# Drawing function
def draw_board(state):
    for i in range(grid_size):
        for j in range(grid_size):
            number = state[i, j]
            x, y = j * cell_size, i * cell_size
            color = white if number != 0 else grey
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
            if number != 0:
                text = font.render(str(number), True, black)
                text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
                screen.blit(text, text_rect)

# Animate and capture frames
frames = []
for state in track:
    screen.fill(grey)
    draw_board(state)
    pygame.display.update()

    # Capture current frame
    frame = pygame.surfarray.array3d(screen)
    frame = np.transpose(frame, (1, 0, 2))  # Pygame to image format
    frames.append(frame)

    time.sleep(0.5)

# Save animation
imageio.mimsave('8puzzle_animation.gif', frames, duration=0.5)
pygame.quit()
print("✅ GIF saved as 8puzzle_animation.gif")
