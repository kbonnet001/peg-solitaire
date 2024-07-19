from Peg import Peg

class European_board:
  def __init__(self):
    self._state_game = "beginning" #end_game
    self._pegs_position = _create_pegs_position()
    self._pegs = _create_new_game_pegs()
    self._num_peg = len(self.pegs)
    
    self._color_background = (248, 228, 207)
    self._color_background_dark = (150, 75, 0)
    self._border_color = (48, 29, 12)
    self._border_size = ""
  
def _create_pegs_position() : 
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
  
  for row in pegs_position:
      print(" ".join(row))
      
  return pegs_position

def _create_new_game_pegs(self):  # Private
  
    pegs = [Peg(peg_pos) for peg_pos in self.pegs_position]

    return pegs
    
def get_state_game(self) :
  return self.state_game

def get_num_pegs(self) :
  return self.num_pegs



def remove_peg():
  ""

