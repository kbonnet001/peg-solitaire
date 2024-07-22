class Player:
    def __init__(self, name):
        self.name = name

    def select_piece(self, board, x, y):
        """
        Sélectionne une pièce sur le plateau.
        """
        if board.grid[y][x] is not None:
            return board.grid[y][x]
        else:
            raise ValueError("Pas de pièce à cette position.")

    def move_piece(self, game, from_x, from_y, to_x, to_y):
        """
        Déplace une pièce sur le plateau de jeu.
        """
        game.move_piece(from_x, from_y, to_x, to_y)