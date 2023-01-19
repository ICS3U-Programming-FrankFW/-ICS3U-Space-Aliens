

#!/usr/bin/env python3
 
# Created By: Frankie
# Date: Jan. 17th, 2023

#!/usr/bin/env python3
#The game's name is Xenon


# Modules used.
import ugame
import stage
import constants
import time
import random
#Splash Scene
def splash_scene():
    #Gets sound ready.
    coin_sound = open("coin.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)


    # Gets images from file (16x16) and sets it as the stage.


    # Background
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")


    # Sets the background to image 0 in the image bank.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )


    background.tile(2, 2, 0)  # blank white


    background.tile(3, 2, 1)


    background.tile(4, 2, 2)


    background.tile(5, 2, 3)


    background.tile(6, 2, 4)


    background.tile(7, 2, 0)  # blank white






    background.tile(2, 3, 0)  # blank white


    background.tile(3, 3, 5)


    background.tile(4, 3, 6)


    background.tile(5, 3, 7)


    background.tile(6, 3, 8)


    background.tile(7, 3, 0)  # blank white






    background.tile(2, 4, 0)  # blank white


    background.tile(3, 4, 9)


    background.tile(4, 4, 10)


    background.tile(5, 4, 11)


    background.tile(6, 4, 12)


    background.tile(7, 4, 0)  # blank white






    background.tile(2, 5, 0)  # blank white


    background.tile(3, 5, 0)


    background.tile(4, 5, 13)


    background.tile(5, 5, 14)


    background.tile(6, 5, 0)


    background.tile(7, 5, 0)  # blank white


    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)


    # Creates a list of layers for the game (In order left appear first)
    game.layers = [background]


    # Renders all sprites
    # Mostly renders the background once every game scene.
    game.render_block()


    # Repeat forever , game loop.
    while True:
        #Wait 2 seconds.
        time.sleep(2.0)
        menu_scene()


#Menu Scene
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
    # Displays the image stage background at a rate of 60 frames and
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


    def show_alien():
        #This function takes an alien from off screen and moves it on screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE),constants.OFF_TOP_SCREEN)
                break
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


    #For loop to randomise tiles in background.
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location, y_location, tile_picked)
    # Initializes the ship variable to a sprite from image bank sprites and gets the fifth image.
    ship = stage.Sprite(
        image_bank_sprites, 4, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )
    # Initializes the alien variable to a sprite from image bank sprites and gets the 9th image.
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)
    #Place An Alien on the Screen.
    show_alien()


    #Create a list of lasers for shooting.
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)


    # Displays the image stage background at a rate of 60 Hz and
    # 60 Frames Per Sec (FPS)
    game = stage.Stage(ugame.display, constants.FP5)


    # Creates a list of layers for the game (In order left appear first)
    game.layers = aliens + lasers + [ship] + [background]


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
            #Fire a laser if we have enough power (if we have available lasers)
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(pew_sound)
                    break
        # Each frame move the laser that has been fired up.
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
       
        # Each frame move aliens down.
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
        # Redraw sprites
        game.render_sprites(aliens + lasers + [ship])
        game.tick()




if __name__ == "__main__":
    splash_scene()













