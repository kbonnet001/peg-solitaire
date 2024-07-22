import pygame
from European_board import European_board

class Game: 
    def __init__(self, screen_width, rows, cols):
        self.europ_board = European_board(screen_width, rows, cols)
        self.screen = pygame.display.set_mode((screen_width, screen_width))
        self.running = True

    def beginning_game(self):
        """At the beginning, player needs to choose the first peg to remove
        (Usually, in the middle of the board)"""
        
        game_start = False
        
        while self.running and game_start != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    game_start =  self.europ_board._remove_first_peg(pos)
                        
            self.europ_board.draw(self.screen)
            pygame.display.flip()

    def run(self):
        """Main game loop"""
        self.beginning_game()
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




    
    
    
    
    # le joeur doit cliquer + etre sur lq position d'un peg
    # si clic, recupere position clic et donner à board
    # board regarde si un peg est clique
    # si oui on l'enleve
    # on modifie les peg necessqire pour qu'il deviennet des cqn move
    # on retourne l'informqtion que l'on q bien commence la partie
    
    # sinon, = il ny q pqs de peg clique, on retourne false et cette boucle vq poursuivre
    