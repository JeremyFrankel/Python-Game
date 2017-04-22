"""
Module for managing platforms.
"""
import pygame
import constants
from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

SPIKES = (347, 35, 70, 35)

TOP_DOOR = (648, 360 , 70, 70 - 2)
BOTTOM_DOOR = (648, 430 + 2, 70, 70 - 2)


BLUE_GEM  = (144, 362, 70, 70, 5)
GREEN_GEM = (144, 290, 70, 70, 1)
RED_GEM = (144, 218, 70, 70, 10)


BLUE_KEY = (131, 0 ,70,70)
GREEN_KEY = (130,146,70,70)
RED_KEY = (72,435,70,70)
YELLOW_KEY = (72,363,70,70)



#347 0 70 70
class Obstacle(pygame.sprite.Sprite):
    """ Obstacle for user """

    def __init__(self, x, y, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("items_spritesheet.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(x,
                                            y,
                                            width,
                                            height)

        self.rect = self.image.get_rect()


class Spike(Obstacle):
    """ This is a set of spikes """
   

    level = None
    player = None

class Treasure(Obstacle):
    level = None
    player = None

    score = None
    def __init__(self, x, y, width, height, score):
        Obstacle.__init__(self, x, y, width, height)
        self.score = score

class Key(Obstacle):
    player = None
    level = None
    key_no = None
    
class Door(Obstacle):
    player = None
    level = None
    other_level = None
    keys = None
    original_x = None
    ol_d = None
    def __init__(self, *coordinates):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        
        pygame.sprite.Sprite.__init__(self)
    
        total_width = None
        total_height = 0
        for coord in coordinates:
            total_height += coord[3]
            if total_width == None or coord[2] > total_width:
                total_width = coord[2]
            
        self.height = total_height
        self.width = total_width
        self.image = pygame.Surface([total_width, total_height]).convert()
        

                
        sprite_sheet = SpriteSheet("tiles_spritesheet.png")
        # Grab the image for this platform
        current_y = 0
        for coord in coordinates:
            self.image.blit(sprite_sheet.sprite_sheet, (0, current_y), coord)
            current_y += coord[3]
        self.image.set_colorkey(constants.BLACK)
        self.rect = self.image.get_rect()
    
    
