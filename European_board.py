import pygame
from Peg import Peg

class European_board:
  def __init__(self, screen_width, rows, cols):
    # Définir les dimensions des cases
    self._rows = rows
    self._cols = cols
    self._cell_size = screen_width // self._rows
    
    self._state_game = "beginning" #end_game
    self._pegs_position_str = self._create_pegs_position() # represention du plateau simplefie en string peg ont des identifiants
    self._pegs = self._create_new_game_pegs() #list de tous les Peg du plateau
    self._num_peg = len(self._pegs)
    
    self._color_background = (248, 228, 207)
    self._color_background_dark = (150, 75, 0)
    self._border_color = (48, 29, 12)
    self._border_size = ""
  
  def _create_pegs_position(self) : 
    
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

  def _create_new_game_pegs(self):
      pegs = []
      k = 0
      for i in range(self._rows) : 
        for j in range(self._cols) : 
          if self._pegs_position_str[i][j] == "o" : 
            self._pegs_position_str[i][j] = str(k)
            pegs.append(Peg((i,j), self._cell_size, str(k)))
            k+=1

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
    self.draw_peg(screen)
  
  def draw_peg(self, screen) : 
    for peg in self._pegs : 
      peg.draw(screen)

  def _check_if_peg_clic(self, pos) : 
    """ pos position xy"""
    for peg in self._pegs : 
      if peg._is_clic(pos) :
        return True, peg.get_name()
    return False, ""
    
  def _remove_peg(self, name) : 
    # pour le peg ij si clique, on supprime peg str
    for row in self._pegs_position_str:
      for i in range(len(row)):
          if row[i] == name:
              row[i] = ' '
              break
    # puis on supprime le Peg de la liste
    self._pegs = [peg for peg in self._pegs if peg.get_name() != name]

# ----------- beginning ------------------

  def _remove_first_peg(self, pos) : 
    peg_clic, name = self._check_if_peg_clic(pos)
    if peg_clic : 
     self._remove_peg_beginning(name)
     # mise a jour des can move des pegs
     return True
    else : 
      return False
  
  def _remove_peg_beginning(self, name) : 
    # pour le peg ij si clique, on supprime peg str
    found = False
    for i in range (self._cols):
      for j in range (self._rows):
          if self._pegs_position_str[i][j] == name:
              self._pegs_position_str[i][j] = ' '
              self.update_pegs_can_move_beginning(i, j)
              found = True
              break
      if found : 
        break
    # puis on supprime le Peg de la liste
    self._pegs = [peg for peg in self._pegs if peg.get_name() != name]
    
  def update_pegs_can_move_beginning(self, i, j) : 
    """ When we remove the first peg, some pegs may immediately move """
    # on a la case on ya le vide
    # on change en can move les peg (façon croix) if
    # si il y a un peg, ou plutot si il ny a pas de "*" et quon est pas hor range
    # donc dabord recupere les case peg quil faut changer
    # puis ensuite seulement faire les modif
    
    cross = [[i-2, j],  [i, j-2], [i, j+2], [i+2, j]]
    for pos in cross : 
      if 0<=pos[0]<self._rows and 0<=pos[1]<self._cols and self._pegs_position_str[pos[0]][pos[1]] != "*": 
        self._get_peg_from_name(self._pegs_position_str[pos[0]][pos[1]])._set_can_move(True)
        self._get_peg_from_name(self._pegs_position_str[pos[0]][pos[1]])._add_position_move(pos)
  
  def _get_peg_from_name(self, name) : 
    for peg in self._pegs : 
      if peg.get_name() == name : 
        return peg
    