

#!/usr/bin/env python3
 
# Created By: Frankie
# Date: Jan. 17th, 2023

#!/usr/bin/env python3
#The game's name is Xenon



# Modules used.
import ugame
import stage
import constants
def menu_scene():
    # Gets images from file (16x16) and sets it as the stage.


    # Background
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")


    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )


    # add text objects
    text = []
    text1 =stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("Frankie Studios")
    text.append(text1)


    text2 =stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40,110)
    text2.text("PRESS START")
    text.append(text2)
    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)


    # Creates a list of layers for the game (In order left appear first)
    game.layers = text + [background]


    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()


    # Place Holder
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # A button to fire
   
        if keys & ugame.K_START !=0:
            game_scene()
        # Update game logic.


        # Redraw sprites
        game.tick()




def game_scene():
    # Gets images from file (16x16) and sets it as the stage.


    # Background
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Sprite
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")


    # Buttons state information.
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]


    # get sound file ready.
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    # Displays image variable image_bank_background 10x8 for each tile.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # Initializes the ship variable to a sprite from image bank sprites and gets the fifth image.
    ship = stage.Sprite(
        image_bank_sprites, 4, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    # Initializes the alien variable to a sprite from image bank sprites and gets the 9th image.
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )
    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)


    # Creates a list of layers for the game (In order left appear first)
    game.layers = [ship] + [alien] + [background]


    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()


    # Place Holder
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()
        # A button to fire
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
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            else:
                ship.move(0, ship.y)
        # Update game logic.


        # Play sound if A button was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        # Redraw sprites
        game.render_sprites([ship] + [alien])
        game.tick()




if __name__ == "__main__":
    menu_scene()










