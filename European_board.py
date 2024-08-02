import pygame
from Peg import Peg

class European_board:
  def __init__(self, screen_width, rows, cols):
    # Définir les dimensions des cases
    self._rows = rows
    self._cols = cols
    self._cell_size = screen_width // self._rows
    
    self._state_game = "beginning" #end_game
    self._pegs_position_str = self._create_pegs_position() # represention du plateau simplifie en string peg ont des identifiants
    self._pegs = self._create_new_game_pegs() #list de tous les Peg du plateau
    self._num_peg = len(self._pegs)
    
    self._color_background = (248, 228, 207)
    self._color_background_dark = (150, 75, 0)
    self._border_color = (48, 29, 12)
    self._border_size = ""
    
    self._one_peg_clic = "" # peg name
  
  def _create_pegs_position(self) : 
    
    """ Create a table with correct position for pegs easily represented by "o"
    Non playable case are in "*"
    Will be replace by peg's name after

    Returns:
        pegs_position : (table string) positions for peg
    """
    
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
              self._pegs_position_str[i][j] = " "
              self._pegs.remove(self._get_peg_from_name(name))
              self.update_pegs_can_move_beginning(i, j)
              found = True
              break
      if found : 
        break
    # puis on supprime le Peg de la liste
    # self._pegs = [peg for peg in self._pegs if peg.get_name() != name]
    
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
        # self._get_peg_from_name(self._pegs_position_str[pos[0]][pos[1]])._set_can_move(True)
        self._get_peg_from_name(self._pegs_position_str[pos[0]][pos[1]])._add_position_move([i,j])
  
  def _get_peg_from_name(self, name) : 
    for peg in self._pegs : 
      if peg.get_name() == name : 
        return peg
    
  def _find_peg_can_move(self) : 
    for peg in self._pegs : 
      if peg.get_can_move() : 
        return True
    return False
  
  
  def _play(self, pos) : 
    
    # Search if a playable peg is cliked 
    for peg in self._pegs : 
      if peg._is_clic(pos) and peg.get_can_move():  
        # new peg is found, don't need to search more ...
        new_peg_selected = peg 
        break
    
    # 1) A peg is already on clic
    if self._one_peg_clic != "" : 
      
      peg_selected = self._get_peg_from_name(self._one_peg_clic)
      # 1 cas, un peg est en on clic, 
      
      # soit on clique sur une case jouable donc on bouge le pion
      print("")
      
      if peg_selected._clic_on_pos_move(pos, self._cell_size) : 
        pos_initial = peg_selected.get_position()
        pos_final = [pos[0]//self._cell_size, pos[1]//self._cell_size]
        pos_middle = [int((pos_initial[i] + pos_final[i])/2) for i in range(2)]
        # Move new peg
        peg_selected.set_position(pos_final)
        # ICI mettre peg au bon endroit dans peg str
        peg_selected.update_position(self._cell_size)
        # Remove peg
        self._del_peg_with_pos(pos_initial, pos_final)
        # Update can move
        self._update_can_move(peg_selected.get_position(), pos_middle, pos_final)

        print("")
      
      elif 'new_peg_selected' in locals() and new_peg_selected._is_clic(pos) : 
        peg_selected._set_off_clic()
        new_peg_selected._set_on_clic()
        self._set_one_peg_on_clic(new_peg_selected.name)
      else : 
        # soit on clique sur une case non jouqble et donc on le met off clic
        # mais dqns tous les cas, faut passer en off apres
        peg_selected._set_off_clic()
        self._remove_one_peg_on_clic()
      
    else : 
      # 2 cas, pas de peg on clic
      # on cherche qui est clique
      for peg in self._pegs : 
        if peg._is_clic(pos) and peg.get_can_move():  
          # le bouton est clique
          # on le passe en mode on clic
          peg._set_on_clic()
          self._set_one_peg_on_clic(peg.get_name())
        
  def _set_one_peg_on_clic(self, peg_name) : 
    self._one_peg_clic = peg_name
  
  def _remove_one_peg_on_clic(self) : 
    self._one_peg_clic = ""
    
  def _del_peg_with_pos(self, pos_initial, pos_final) : 
    # Peg move pos initial to pos final,
    # The peg beetween this two position must be removed
    pos_to_remove = [int((pos_initial[i] + pos_final[i])/2) for i in range(2)]
    self._pegs.remove(self._get_peg_from_name(self._pegs_position_str[pos_to_remove[0]][pos_to_remove[1]]))
    self._pegs_position_str[pos_to_remove[0]][pos_to_remove[1]] = " "
    
  def _update_can_move(self, pos_i, pos_m, pos_f) : 
    # pos_f --> peg non jouable 
    self. _update_can_move_false(pos_f[0], pos_f[1])
  
  def _update_can_move_false(self, i, j) : 
    cross = [[i,j], [i-2, j],  [i, j-2], [i, j+2], [i+2, j]]
    for pos in cross : 
      if 0<=pos[0]<self._rows and 0<=pos[1]<self._cols and (self._pegs_position_str[pos[0]][pos[1]] != "*" or self._pegs_position_str[pos[0]][pos[1]] != " " ): 
        self._get_peg_from_name(self._pegs_position_str[pos[0]][pos[1]])._remove_position_move([i,j])