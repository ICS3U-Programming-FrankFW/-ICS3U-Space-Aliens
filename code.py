#!/usr/bin/env python3
# Created By: Frankie Fox Wagoosh
# Date: Dec , 19 , 2022
# This program is the game that can be played on the PyBadge "Xenon"

import ugame
import stage

def game_scene():
  # This function is basically the game main theme

  image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
  background = stage.Grid(image_bank_background, 10, 8)
    
  game = stage.Stage(ugame.display, 60)
  game.layers = [background]
  game.render_block()
  #This will repeat forever since it is a loop
  while True:
    pass # This is our placeholder for now 

if __name__ == "__main__":
  game_scene()

