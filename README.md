# peg-solitaire

Genetic algorithm for the game "peg solitaire"

## Reflexion strategie code POO

On a des cases :

- des carres (dimension)
- couleur (color) et contour (epaisseur float)
- position xy fixe
- peuvent être vide ou occupée (bool)
- interaction possible par clic
- on interaction (bool) si peut être selectionnée par le joueur pour deplacer une bille
  si true change de couleur

On a des billes

- rond (dimension)
- couleur (color) et contour (epaisseur float)
- position xy mobile
- interaction possible par clic
- on clic (bool) si true change de couleur

## Interactions

- 1 clic sur une bille, change de couleur pour dire qu'elle est selectionnée
- les cases possibles changent alors de couleurs

## Affichage bonus en haut du plateau

- Nombre de billes restantes
- Temps écoulé
- état de la partie (commencer, en cours, fin)

## Savoir si une bille peut être jouée et comment

- fonction pour definir les billes jouables, de position (x,y)

  - jouable si (x-1, y) = plein et (x-2, y) = vide ==> case (x-2, y) couleur et cliquable
  - (x+1, y) = plein et (x+2, y) = vide ==> case (x+2, y) couleur et cliquable
  - (x, y-1) = plein et (x, y-2) = vide ==> case (x, y-2) couleur et cliquable
  - (x, y+1) = plein et (x, y+2) = vide ==> case (x, y+2) couleur et cliquable
  - attention au hors range

  - pour optimisation, lorsque nb de bille >= nb bille//2 verifier avant la case vide
  - puis quand nb de bille < nb bille//2 verifier avant case occupée

  - Si il n'existe plus de billes respectant une de ces conditions --> fin de la partie

## Objectif pour l'IA

- Le moins de billes restant sur le plateau à la fin de la partie
- Plus qu'une bille sur le plateau :)
- Le dernière bille est sur la case vide du debut de la partie
