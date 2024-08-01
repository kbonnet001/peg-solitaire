import pygame
from European_board import European_board

class Game: 
    def __init__(self, screen_width, rows, cols):
        self.europ_board = European_board(screen_width, rows, cols)
        self.screen = pygame.display.set_mode((screen_width, screen_width))
        self.running = True
        self.game_start = False

    def beginning_game(self):
        """ At the beginning, player needs to choose the first peg to remove
        (Usually, in the middle of the board)
        """
        
        while self.running and self.game_start != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    self.game_start =  self.europ_board._remove_first_peg(pos)
                        
            self.europ_board.draw(self.screen)
            pygame.display.flip()
            
            
    def main_game(self):
        """  # Quand on clique sur un peg, il devient on clic et change de couleur
        # si et seuleement si le peg et jouable, sinon rien
        # une fleche apparait ou plusieurs vers la les cases jouables

        # si on clique sur une des case jouable, le peg se deplace sur la case
        # mise a jour du plateau
        # si on clique ailleurs que une de ces case jouable, le peg revient en off clic 
        
        """
        
        while self.running and self.game_start :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    
                    # if pos est sur un peg jouable
                    # on fqit le jeu
                    # else rien du tout
                    self.europ_board._play(pos)
                    
                    # mise à jour de game_start, False si plus de peg jouable
                    self.game_start = self.europ_board._find_peg_can_move()
                        
            self.europ_board.draw(self.screen)
            pygame.display.flip()

    def run(self):
        """Main game loop"""
        self.beginning_game()
        self.main_game()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Handle other mouse click events

            self.europ_board.draw(self.screen)
            pygame.display.flip()

        pygame.quit()




    
    
    
    
    