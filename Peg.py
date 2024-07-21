import pygame

class Peg:
  def __init__(self, position, cell_size):
    self._position_board = []
    self._position = position #[][]
    self.update_position(cell_size)
    self._size = ""
    self._on_plateau = True
    
    # off clic
    self._color_off_clic = (206, 148, 100)
    self._border_color_off_clic = (83, 42, 6)
    self._border_size_off_clic = ""
    
    # on clic
    self._on_clic = False
    self._color_on_clic = (255, 255, 255)
    self._border_size_on_clic = ""
    
    #initialisation
    self._color = self._color_off_clic
    self._border_color = self._border_color_off_clic
    self._border_size = self._border_size_off_clic
    
    self._can_move = [False for k in range (4)]

  def set_position(self, new_position) : 
    self._position = new_position
  
  def set_moves(self, new_moves) : 
    self._can_move = new_moves
  
  def set_on_clic(self) : 
    self._on_clic = True
    self._color = self._color_on_clic
    self._border_color = self._border_color_on_clic
    self._border_size = self._border_size_on_clic 
    
  def set_off_clic(self) : 
    self.on_clic = False
    self._color = self._color_off_clic
    self._border_color = self._border_color_off_clic
    self._border_size = self._border_size_off_clic

  def remove_peg():
    return None

  def draw(self, screen, cell_size) :
    pygame.draw.circle(screen, self._color, self._position_board, cell_size // 3)
    pygame.draw.circle(screen, self._border_color, self._position_board, cell_size // 3, 2)

  def update_position(self, cell_size) : 
    self._position_board = (self._position[0] * cell_size + cell_size // 2, self._position[1] * cell_size + cell_size // 2)