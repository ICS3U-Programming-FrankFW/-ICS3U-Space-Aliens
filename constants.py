#!/usr/bin/env python3


# Created by : Frankie Fox
# Created on  January , 11 , 2023
# These are the constants in the game xenon which are used for boundaries
# They also are used for the sprite size , how many aliens


# The pybadge screen size is 160x128 and sprites are 16x16
#!/usr/bin/env python3


SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
FP5 = 60
SPRITE_MOVEMENT_SPEED = 1


#Button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}


RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
