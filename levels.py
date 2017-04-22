import pygame
import enemies
import constants
import platforms
import obstacles
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    obstacle_list = None
    treasure_list = None
    key_list = None
    door_list = None
    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000
    
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.obstacle_list = pygame.sprite.Group()
        self.treasure_list = pygame.sprite.Group()
        self.key_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.player = player
        
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.obstacle_list.update()
        self.treasure_list.update()
        self.key_list.update()
        self.door_list.update()
       
    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.GOLD)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.door_list.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.obstacle_list.draw(screen)
        self.treasure_list.draw(screen)
        self.key_list.draw(screen)
        
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        for obstacle in self.obstacle_list:
            obstacle.rect.x += shift_x
        for treasure in self.treasure_list:
            treasure.rect.x += shift_x
        for key in self.key_list:
            key.rect.x += shift_x
        for door in self.door_list:
            door.original_x += shift_x
            door.rect.x = door.original_x//3
    def reset(self):
        self.shift_world(self.world_shift* -1)
        self.player.rect.x = 120


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.GRASS_LEFT, 500, 500],
                  [platforms.GRASS_MIDDLE, 570, 500],
                  [platforms.GRASS_RIGHT, 640, 500],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 100],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
                  
        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 1420
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)

        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 1490
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)

        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 1560
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)

        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 1630
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)
        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 1630+70
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)

        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 1630+140
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self  

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -3
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 1500+70
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)

      
        self.obstacle_list.add(spike)
        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 2000-70
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)

        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 2070+70
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self  
        
        self.obstacle_list.add(spike)

     
        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 2140+70
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self   

        self.obstacle_list.add(spike)

        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 2210+70
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self  
        
        self.obstacle_list.add(spike)

class Level_03(Level):
    def __init__(self, player):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -3000



        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 600],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 600],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 600],
                  [platforms.GRASS_LEFT, 800, 700],
                  [platforms.GRASS_MIDDLE, 870, 700],
                  [platforms.GRASS_RIGHT, 940, 700],
                  [platforms.GRASS_LEFT, 950, 500],
                  [platforms.GRASS_MIDDLE, 1020, 500],
                  [platforms.GRASS_RIGHT, 1090, 500],
                  [platforms.STONE_PLATFORM_LEFT, 450, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 520, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 590, 400],
                  [platforms.STONE_PLATFORM_LEFT, 350, 260],
                  [platforms.STONE_PLATFORM_MIDDLE, 420, 260],
                  [platforms.STONE_PLATFORM_RIGHT, 490, 260],
                  [platforms.STONE_PLATFORM_LEFT, 800, 180],
                  [platforms.STONE_PLATFORM_MIDDLE, 870, 180],
                  [platforms.STONE_PLATFORM_RIGHT, 940, 180],
                  [platforms.STONE_PLATFORM_LEFT, 1000, 250],
                  [platforms.STONE_PLATFORM_MIDDLE, 1070, 250],
                  [platforms.STONE_PLATFORM_RIGHT, 1140, 250],
                  [platforms.STONE_PLATFORM_MIDDLE, 1210, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1280, 310],
                  [platforms.STONE_PLATFORM_MIDDLE, 1350, 340],
                  [platforms.STONE_PLATFORM_MIDDLE, 1420, 370],
                  [platforms.STONE_PLATFORM_MIDDLE, 1490, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 430],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 540],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 430],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 470],
                  [platforms.STONE_PLATFORM_MIDDLE, 1630, 370],
                    
                  [platforms.STONE_PLATFORM_LEFT, 1690, 340],
                  [platforms.STONE_PLATFORM_MIDDLE, 1760, 310],
                  [platforms.STONE_PLATFORM_RIGHT, 1830, 310],
                  [platforms.STONE_PLATFORM_MIDDLE, 1900, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1970, 250],
                  [platforms.STONE_PLATFORM_MIDDLE, 2040, 340],
                  [platforms.STONE_PLATFORM_MIDDLE, 2110, 370],
                  ]
 # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

class Level_04(Level):
    def __init__(self, player):
        """ Create level 4. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -8000



        level_platforms = [[ platforms.GRASS_LEFT, 200, 300],
                [ platforms.GRASS_MIDDLE, 270, 300],
                [ platforms.GRASS_RIGHT, 340, 300],
                ]
 # Go through the array above and add platforms
        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            
                


        spike = obstacles.Spike(*obstacles.SPIKES)
        spike.rect.x = 300
        spike.rect.y = constants.SCREEN_HEIGHT - obstacles.SPIKES[3]
        spike.player = self.player
        spike.level = self
        
        self.obstacle_list.add(spike)
        
   
        gem = obstacles.Treasure(*obstacles.RED_GEM)
        gem.rect.x = 600
        gem.rect.y = constants.SCREEN_HEIGHT - obstacles.RED_GEM[3]
        gem.player = self.player
        gem.level = self
        self.treasure_list.add(gem)

        gem = obstacles.Treasure(*obstacles.GREEN_GEM)
        gem.rect.x = 900
        gem.rect.y = constants.SCREEN_HEIGHT - obstacles.GREEN_GEM[3]
        gem.player = self.player
        gem.level = self
        self.treasure_list.add(gem)
        
        self.treasure_list.add(gem)
        gem = obstacles.Treasure(*obstacles.BLUE_GEM)
        gem.rect.x = 1800
        gem.rect.y = constants.SCREEN_HEIGHT - obstacles.BLUE_GEM[3]
        gem.player = self.player
        gem.level = self
        self.treasure_list.add(gem)

        gem = obstacles.Treasure(*obstacles.RED_GEM)
        gem.rect.x = 2500
        gem.rect.y = constants.SCREEN_HEIGHT - obstacles.RED_GEM[3]
        gem.player = self.player
        gem.level = self
        
        
        self.treasure_list.add(gem)
        
        door = obstacles.Door(obstacles.TOP_DOOR, obstacles.BOTTOM_DOOR)
        self.door12 = door
        door2 = obstacles.Door(obstacles.TOP_DOOR, obstacles.BOTTOM_DOOR)
        self.door13 = door2

        door.rect.x = 3500
        door.original_x = 3500
        door.rect.y = constants.SCREEN_HEIGHT - door.height
        door.player = self.player
        door.level = self
        door.other_level = Level_05(self.player, self)
        door.ol_d = door.other_level.door12
        door.keys = [ 1, 2 ]
        
        
        self.door_list.add(door)
        


       
        door2.rect.x = 3700
        door2.original_x = 3700
        door2.rect.y = constants.SCREEN_HEIGHT - door2.height
        door2.player = self.player
        door2.level = self
        door2.other_level = door.other_level
        door2.ol_d = door.other_level.door13
        door2.keys = [ 1, 3 ]


        self.door_list.add(door2)

              
        key = obstacles.Key(*obstacles.RED_KEY)
        key.rect.x = 400
        key.rect.y = 400
        key.player = self.player
        key.level = self
        key.key_no = 1
        self.key_list.add(key)
        

        key = obstacles.Key(*obstacles.YELLOW_KEY)
        key.rect.x = 2000
        key.rect.y = 550
        key.player = self.player
        key.level = self
        key.key_no = 2
        self.key_list.add(key)

        key = obstacles.Key(*obstacles.BLUE_KEY)
        key.rect.x = 1500
        key.rect.y = 30
        key.player = self.player
        key.level = self
        key.key_no = 3
        self.key_list.add(key)

        block = platforms.ConveyerBelt(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 500
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
class Level_05(Level):
    def __init__(self, player, other_level):
        """ Create level 5. """

        # Call the parent constructor
        Level.__init__(self, player)                                                                
        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -8000

        door3 = obstacles.Door(obstacles.TOP_DOOR, obstacles.BOTTOM_DOOR)
        self.door13 = door3
        door = obstacles.Door(obstacles.TOP_DOOR, obstacles.BOTTOM_DOOR)
        self.door12 = door
        door.rect.x = 500
        door.original_x = 500
        door.rect.y = constants.SCREEN_HEIGHT - door.height
        door.player = self.player
        door.level = self
        door.other_level = other_level
        door.ol_d = door.other_level.door12
        door.keys = [ 1, 2 ]

        self.door_list.add(door)

        
        door3.rect.x = 700
        door3.original_x = 700
        door3.rect.y = constants.SCREEN_HEIGHT - door3.height
        door3.player = self.player
        door3.level = self
        door3.other_level = other_level
        door3.ol_d = door3.other_level.door13
        door3.keys = [ 1, 3 ]

        self.door_list.add(door3)

        gem = obstacles.Treasure(*obstacles.RED_GEM)
        gem.rect.x = 600
        gem.rect.y = constants.SCREEN_HEIGHT - obstacles.RED_GEM[3]
        gem.player = self.player
        gem.level = self

        self.treasure_list.add(gem)
class Intro_Level(Level):
    def __init__(self, player, *next_levels):
        Level.__init__(self, player)                                                                
        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constants.WHITE)
        #LEVEL LIMIT IS 2100
        self.level_limit = -2100

        
        level_platforms = [
                 # [platforms.STONE_PLATFORM_LEFT, 500, ],
                 # [platforms.STONE_PLATFORM_MIDDLE, 570, 600],
                  #[platforms.STONE_PLATFORM_RIGHT, 640, 600],
                 # [platforms.GRASS_LEFT, 800, 700],
                 # [platforms.GRASS_MIDDLE, 870, 700],
                 # [platforms.GRASS_RIGHT, 940, 700],
                  [platforms.GRASS_LEFT, 950, 500],
                  [platforms.GRASS_MIDDLE, 1020, 500],
                  [platforms.GRASS_RIGHT, 1090, 500],
                  [platforms.STONE_PLATFORM_LEFT, 450, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 520, 400],
                  [platforms.STONE_PLATFORM_RIGHT, 590, 400],
                  [platforms.STONE_PLATFORM_LEFT, 350, 260],
                  [platforms.STONE_PLATFORM_MIDDLE, 420, 260],
                  [platforms.STONE_PLATFORM_RIGHT, 490, 260],
                  [platforms.STONE_PLATFORM_LEFT, 800, 180],
                  [platforms.STONE_PLATFORM_MIDDLE, 870, 180],
                  [platforms.STONE_PLATFORM_RIGHT, 940, 180],
                  [platforms.STONE_PLATFORM_LEFT, 1000, 250],
                  [platforms.STONE_PLATFORM_MIDDLE, 1070, 250],
                  [platforms.STONE_PLATFORM_RIGHT, 1140, 250],
                  [platforms.STONE_PLATFORM_MIDDLE, 1210, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1280, 310],
                  [platforms.STONE_PLATFORM_MIDDLE, 1350, 340],
                  [platforms.STONE_PLATFORM_MIDDLE, 1420, 370],
                  [platforms.STONE_PLATFORM_MIDDLE, 1490, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 400],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 430],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 540],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 430],
                  [platforms.STONE_PLATFORM_MIDDLE, 1560, 470],
                  [platforms.STONE_PLATFORM_MIDDLE, 1630, 370],
                    
                  [platforms.STONE_PLATFORM_LEFT, 1690, 340],
                  [platforms.STONE_PLATFORM_MIDDLE, 1760, 310],
                  [platforms.STONE_PLATFORM_RIGHT, 1830, 310],
                  [platforms.STONE_PLATFORM_MIDDLE, 1900, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1970, 250],
                  [platforms.STONE_PLATFORM_MIDDLE, 2040, 340],
                  [platforms.STONE_PLATFORM_MIDDLE, 2110, 370],
                  ]
        for platform in level_platforms:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        level_gems = [
            [obstacles.BLUE_GEM,1020, 430],
            [obstacles.RED_GEM, 1070, 180]]

        for gem in level_gems:
            gem_sprite = obstacles.Treasure(*gem[0])
            gem_sprite.rect.x = gem[1]
            gem_sprite.rect.y = gem[2]
            gem_sprite.player = self.player
            self.treasure_list.add(gem_sprite)
        level_spikes = [
            [100,constants.SCREEN_HEIGHT - obstacles.SPIKES[3]]] 

        for spike_info in level_spikes:
            
            spike = obstacles.Spike(*obstacles.SPIKES)
            spike.rect.x = spike_info[0]
            spike.rect.y = spike_info[1]
            spike.player = self.player
            spike.level = self
        
            self.obstacle_list.add(spike)
        level_enemies = [
            [1250, constants.SCREEN_HEIGHT - 90]] 
        for enemy_info in level_enemies:
            enemy = enemies.Enemy()
            enemy.rect.x = enemy_info[0]
            enemy.rect.y = enemy_info[1]
            enemy.level = self
            enemy.player = self.player

            self.enemy_list.add(enemy)

           

      
