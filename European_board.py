import pygame
from Peg import Peg

class European_board:
  def __init__(self, screen_width):
    # Définir les dimensions des cases
    self._rows = 7
    self._cols = 7
    self._cell_size = screen_width // self._rows
    
    self._state_game = "beginning" #end_game
    self._pegs_position_str = self._create_pegs_position()
    self._pegs = self._create_new_game_pegs()
    self._num_peg = len(self._pegs)
    
    self._color_background = (248, 228, 207)
    self._color_background_dark = (150, 75, 0)
    self._border_color = (48, 29, 12)
    self._border_size = ""
  
  def _create_pegs_position(self) : 
    # for k in [0, 1, -1, -2] : 
    #   pegs[0, k] = "*"
    #   pegs[-1, k] = "*"
      
    # for k in [0, -1] :
    #   pegs[1, k] = "*"
    #   pegs[-2, k] = "*"
    
    pegs_position = [["o" for i in range(7)] for j in range(7)]
    positions = [
        (0, k) for k in [0, 1, -1, -2]
    ] + [
        (1, k) for k in [0, -1]
    ] + [
        (-1, k) for k in [0, 1, -1, -2]
    ] + [
        (-2, k) for k in [0, -1]
    ]
    
    for (i, j) in positions:
        pegs_position[i][j] = "*"
    
    for row in pegs_position: # ok
        print(" ".join(row))
        
    return pegs_position

  def _create_new_game_pegs(self):  # Private
      pegs = []
      for i in range(self._rows) : 
        for j in range(self._cols) : 
          if self._pegs_position_str[i][j] == "o" : 
            pegs.append(Peg((i,j), self._cell_size))

      # pegs = [Peg(peg_pos, cell_size) for peg_pos in self._pegs_position]

      return pegs
      
  def get_state_game(self) :
    return self.state_game

  def get_num_pegs(self) :
    return self.num_pegs

  def remove_peg():
    return None

  def draw(self, screen) : 
    # Dessiner la grille
    for row in range(len(self._pegs_position_str)):
        for col in range(len(self._pegs_position_str)):
            if self._pegs_position_str[row][col] == "*" : 
                color = self._color_background_dark
            else:
                color = self._color_background  
            rect = pygame.Rect(col * self._cell_size, row * self._cell_size, self._cell_size, self._cell_size)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen,self._border_color, rect, 1)
  
  def draw_peg(self, screen) : 
    for peg in self._pegs : 
      peg.draw(screen, self._cell_size)
