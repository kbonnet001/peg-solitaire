import pygame
import sys
from European_board import European_board

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Plateau de Jeu")

# Couleurs (simples pour l'exemple)
background_color = (255, 255, 255)
grid_color = (150, 75, 0)
border_color = (0, 0, 0)
circle_color = (200, 100, 50)
highlight_color = (255, 255, 255)

# Définir les dimensions des cases
rows, cols = 7, 7
cell_size = screen_width // rows

board = European_board(screen_width)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplir l'écran de blanc
    screen.fill(background_color)

    board.draw(screen)
    # # Dessiner la grille
    # for row in range(rows):
    #     for col in range(cols):
    #         if (row < 2 or row > 4) and (col < 2 or col > 4):
    #             color = grid_color
    #         else:
    #             color = (255, 204, 153)  # couleur différente pour les cases valides
    #         rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
    #         pygame.draw.rect(screen, color, rect)
    #         pygame.draw.rect(screen, border_color, rect, 1)

    # Dessiner les cercles
    circle_positions = [
        (3 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2),
        (4 * cell_size + cell_size // 2, 3 * cell_size + cell_size // 2)
    ]
    for pos in circle_positions:
        pygame.draw.circle(screen, circle_color, pos, cell_size // 3)

    # Dessiner le cercle avec bordure
    bordered_circle_position = (4 * cell_size + cell_size // 2, 4 * cell_size + cell_size // 2)
    pygame.draw.circle(screen, highlight_color, bordered_circle_position, cell_size // 3)
    pygame.draw.circle(screen, border_color, bordered_circle_position, cell_size // 3, 2)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
sys.exit()
