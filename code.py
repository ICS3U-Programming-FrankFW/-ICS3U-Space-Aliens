#!/usr/bin/env python3
 
# Created By: Frankie
# Date: Jan. 17th, 2023

import stage
import ugame

 
 
# The pybadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
FP5 = 60
SPRITE_MOVEMENT_SPEED = 1


# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
 
def game_scene():
    # this is the main scene for space alien

    #image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
 
    #set the background to image 0 in the image bank
    #   and the size
    background = stage.Grid(image_bank_background, 10,8)
    
    #a sprite that will update every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, SCREEN_Y - (2 * SPRITE_SIZE))
 
    alien = stage.Sprite(image_bank_sprites, 9,
        int(SCREEN_X / 2 - SPRITE_SIZE / 2),16)

    #buttons you want to keep information on
    a_button = button_state["button_up"]
    b_button = button_state["button_up"]
    start_button = button_state["button_up"]
    select_button = button_state["button_up"]
 
    #get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    
    #create a stage for the background to show up on
    #   and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)
    #set the layers of all the sprites, items show up in order
    game.layers = [ship]+[alien]+[background]
    #render all sprites
    game.render_block()
 
    #repeat forever game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()

        #A button to fire
        if keys & ugame.K_O != 0:
            if a_button == button_state["button_up"]:
                a_button = button_state["button_just_pressed"]
            elif a_button == button_state["button_just_pressed"]:
                a_button = button_state["button_still_pressed"]
        else:
            if a_button == button_state["button_still_pressed"]:
                a_button = button_state["button_released"]
            else:
                a_button = button_state["button_up"]
        
        # B button
        if keys & ugame.K_X != 0:
            pass
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")
            
        #input to make the sprite move
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (SCREEN_X - SPRITE_SIZE):
                ship.move((ship.x + SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((SCREEN_X - SPRITE_SIZE), ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass
 
        # update game logic
        # play a sound in A was just pressed
        if a_button == button_state["button_just_pressed"]:
            sound.play(pew_sound)
            
        #redraw sprite
        game.render_sprites([ship] + [alien])
        game.tick()        
 
if __name__ == "__main__" :
     game_scene()
