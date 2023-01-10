#!/usr/bin/env python3
# Created By: Frankie Fox Wagoosh
# Date: Dec , 19 , 2022
# This program is the game that can be played on the PyBadge "Xenon"

import ugame
import stage

def game_scene():
  # This function is basically the game main theme
  
  #The image banks for the circuit python 
  image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
  image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")    
  
  
  #Set the background to image 0 in image bank
  # and the size (10x8 tiles 16x16)
  background = stage.Grid(image_bank_background, 10, 8)

  # A sprite that will be updated every frame
  ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
 
 # This makes it so it runs at an amazing 60 frames per second
 #also letting it create a stage for the background to show up
  game = stage.Stage(ugame.display, 60)
  
  # Sets the layers , items show up in order 
 
  game.layers = [ship] + [background]
   
   # Render the background and initial location of sprite list
  #most likely you will only render background once per scene 
  game.render_block()
 
 #This will repeat forever since it is a loop
  while True:
   #get user input 
   keys = ugame.buttons.get_pressed()

   # This occurs when A is being pressed
   if keys & ugame.K_X:
    print("A")
    # This occurs when B is being pressed
   if keys & ugame.K_O:
    print("B")
   # This occurs when Start is being pressed
   if keys & ugame.K_START:
    print("Start")
   # This occurs when Select is being pressed
   if keys & ugame.K_SELECT:
    print("Select") 
   # This occurs when the right d pad is clicked moving the sprite to the right
   if keys & ugame.K_RIGHT:
    ship.move(ship.x + 1, ship.y)
  # This occurs when the left d pad is clicked moving the sprite to the left
   if keys & ugame.K_LEFT:
    ship.move(ship.x - 1, ship.y)
   # This occurs when the up d pad is clicked moving the sprite upwards
   if keys & ugame.K_UP:
    ship.move(ship.x, ship.y - 1)
   # This occurs when the down d pad is clicked moving the sprite downwards
   if keys & ugame.K_DOWN:
    ship.move(ship.x, ship.y + 1)
   
   #update game logic 

  # Redraw sprite
   game.render_sprites([ship])
   game.tick()



if __name__ == "__main__":
 game_scene()

