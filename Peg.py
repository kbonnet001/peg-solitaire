import pygame
import math

class Peg:
  def __init__(self, position, cell_size, name):
    self.name = name # identifiant
    self._position_board = [] # x y 
    self._position = position #[][] #i j 
    self.update_position(cell_size)
    self._radius = cell_size // 3
    self._on_plateau = True
    
    # off clic
    # self._color_off_clic = (206, 148, 100)
    self._border_color = (83, 42, 6)
    self._border_size_off_clic = 2
    
    # on clic
    self._on_clic = False
    # self._color_on_clic = (255, 255, 255)
    self._border_size_on_clic = 5
    
    #initialisation
    self._color = (206, 148, 100)
    self._border_size = self._border_size_off_clic
    
    self._can_move = False
    self._position_move = [] # list of position where peg could move

  def set_position(self, new_position) : 
    self._position = new_position
  
  def set_moves(self, new_moves) : 
    self._can_move = new_moves
  
  def _set_on_clic(self) : 
    self._on_clic = True
    # self._color = self._color_on_clic
    self._border_size = self._border_size_on_clic
    self._border_size = self._border_size_on_clic 
    
  def _set_off_clic(self) : 
    self.on_clic = False
    # self._color = self._color_off_clic
    self._border_size = self._border_size_off_clic
    self._border_size = self._border_size_off_clic

  def _remove_peg():
    return None

  def draw(self, screen) :
    if self._can_move == False : 
      pygame.draw.circle(screen, self._color, self._position_board, self._radius)
    else : 
      pygame.draw.circle(screen, (255, 255, 255), self._position_board, self._radius)
    pygame.draw.circle(screen, self._border_color, self._position_board, self._radius, self._border_size)

  def update_position(self, cell_size) : 
    self._position_board = (self._position[0] * cell_size + cell_size // 2, self._position[1] * cell_size + cell_size // 2)
  
  def _is_clic(self, pos) : 
    distance = math.sqrt((pos[0] - self._position_board[0]) ** 2 + (pos[1] - self._position_board[1]) ** 2)
    
    print("distance <= self._radius ", distance <= self._radius)
        
    return distance <= self._radius # bool ok
    
  def get_name(self) : 
    return self.name

  def _set_can_move(self, move) : 
    self._can_move = move
    
  def get_can_move(self) : 
    return self._can_move
  
  def _clic_on_pos_move(self, pos, cell_size) :
    for pos_move in self._position_move : 
      if pos[0] // cell_size <= pos_move[0] <= pos[0] // cell_size + 1 \
      and pos[1] // cell_size <= pos_move[1] <= pos[1] // cell_size + 1 :
        return True
    return False
    
  def get_position(self) : 
    return self._position
  
  def _add_position_move(self, position) :
    # position [int][int]
    if position not in self._position_move : 
      self._position_move.append(position)
      self._set_can_move(True)
      print("")
  
  def _remove_position_move(self, position) :
    if position in self._position_move : 
      self._position_move.remove(position)
      if self._position_move == [] :
        self._set_can_move(False)
        self._set_off_clic()
      print("")
  
  def _clean_can_move(self) :
    self._position_move = []
    self._set_can_move(False)
      
  def __str__(self):
        return f"Peg name : {self.name},\n position : {self._position},\n can move : {self._can_move},\nposition move : {self._position_move}"