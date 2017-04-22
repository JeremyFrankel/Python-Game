"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

from platforms import MovingPlatform, ConveyerBelt
from obstacles import Spike, Treasure
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
    keep_score = None
    
    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0
    speed = 1
    health = 2
    invincible = False
    inv_counter = 0
    flashing = False
    blank_image = None
    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None
    key_no_list = None
    
    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.blank_image = pygame.Surface([66, 90])
        self.blank_image.fill(constants.WHITE)
        self.blank_image.set_colorkey(constants.WHITE)
        sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.keep_score = 0
        self.key_no_list = []
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        #updating invincibility
        if self.invincible:
            self.inv_counter -= 1
            if self.inv_counter < 0:
                self.invincible = False
        print "adsaeda"+str(self.flashing)
        self.flashing = self.invincible and not self.flashing
        # Move left/right
        self.rect.x += self.change_x *self.speed
        pos = self.rect.x + self.level.world_shift
        if self.flashing:
            self.image = self.blank_image
        elif self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
             #If we are moving right,
             #set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                 #Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # See if we hit anything
        obs_hit_list = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        for obs in obs_hit_list:
             #If we are moving right,
             #set our right side to the left side of the item we hit
            if isinstance(obs, Spike):
                if self.change_x > 0:
                    self.rect.right = obs.rect.left
                elif self.change_x < 0:
                     #Otherwise if we are moving left, do the opposite.
                    self.rect.left = obs.rect.right
        tre_hit_list = pygame.sprite.spritecollide(self, self.level.treasure_list, True)     
        for tre in tre_hit_list:
            self.keep_score += tre.score
            print self.keep_score
        key_hit_list = pygame.sprite.spritecollide(self, self.level.key_list, True)     
        for key in key_hit_list:
            self.key_no_list.append(key.key_no)
            print self.key_no_list
        self.rect.y += self.change_y
            
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

             #Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

             #Stop our vertical movement
            self.change_y = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
            if isinstance(block, ConveyerBelt):
                block.is_moving = True
            
        obs_hit_list = pygame.sprite.spritecollide(self, self.level.obstacle_list, False)
        for obs in obs_hit_list:
            if isinstance(obs, Spike):
                self.die()
        tre_hit_list = pygame.sprite.spritecollide(self, self.level.treasure_list, True)     
        for tre in tre_hit_list:
            self.keep_score += tre.score
            print self.keep_score
        
        key_hit_list = pygame.sprite.spritecollide(self, self.level.key_list, True)     
        for key in key_hit_list:
            self.key_no_list.append(key.key_no)
            print self.key_no_list
            
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "R"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "L"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
    def run(self):
        """When user holds shift down."""
        self.speed = 2.5
    def walk(self):
        self.speed = 1
    def die(self):
        self.level.reset()
        self.health = 2
    def do_damage(self, damage_dealt):
        print "health = "+str(self.health)
        
        if not self.invincible:
            self.health -= (damage_dealt)
        
            if self.health < 0:
                self.die()
                
            else:
                self.invincible = True
                self.inv_counter = 180
                
