
#!/usr/bin/env python3
 
# Created By: Frankie
# Date: Jan. 17th, 2023
import ugame
import stage
 
import constants
 
 
def game_scene():
    # this is the main scene for space alien
 
    #buttons you want to keep information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
 
    #Gets the sound being able to play
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
 
 
    #image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")
 
    #set the background to image 0 in the image bank
    #   and the size
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
 
    #The sprite that will update every frame
    ship = stage.Sprite(image_bank_sprite, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
 
    #create a stage for the background to show up on
    #   and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = [ship]+[background]
    #render all sprites
    game.render_block()
 
    #repeat forever game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()
 
        #A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        # B button
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        #input to make the sprite move
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
 
 
        #update game logic
        #play a sound in A was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        #redraw sprite
        game.render_sprites([ship])
        game.tick()        
 
if __name__ == "__main__":
    game_scene()
