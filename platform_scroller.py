"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller example.

From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame

import constants
import levels
import interface
from player import Player

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    #level_list.append(levels.Level_01(player))
    #level_list.append(levels.Level_02(player))
    #level_list.append(levels.Level_03(player))
    #level_list.append(levels.Level_04(player))
    level_list.append(levels.Intro_Level(player))
    # Set the current level1
    current_level_no = 0
    current_level = level_list[current_level_no]
    hud_group = pygame.sprite.Group()
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = constants.SCREEN_WIDTH / 2
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)


    hud_group.add(interface.Health_bar(player))
    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()

                if event.key == pygame.K_UP:
                    
                    door_hit_list = pygame.sprite.spritecollide(player, current_level.door_list, False)
                    closest_door = None
                    min_dist = None
                    for door in door_hit_list:
                        distance = ((door.rect.centerx - player.rect.centerx)**2 + (door.rect.centery - player.rect.centery)**2)**0.5
                        if min_dist == None or distance < min_dist:
                            closest_door = door
                            min_dist = distance
                    if closest_door == None:
                        player.jump()
                    else:
                        all_keys_found = False
                        for key_f_d in closest_door.keys:
                            found_key = False
                            for key_f_p in player.key_no_list:
                                if key_f_d ==key_f_p:
                                    found_key = True
                                    break
                            if found_key == False:
                                all_keys_found = False
                                break
                            else:
                                all_keys_found = True
                        if all_keys_found == True:
                            player.rect.x = closest_door.ol_d.rect.x
                            current_level = closest_door.other_level
                            player.level = current_level
                      



    #for each key in the doors checklist, 
	#for key1 in player checklist,
		#key is equal to key1
		#	stop searching
            #if the key wasn't found, stop searching
        #if key is there, open door

                if event.key == pygame.K_LSHIFT:
                    player.run()
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_LSHIFT:
                    player.walk()
                
        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()
        hud_group.update()
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        if player.rect.x <= 0:
             player.rect.x = 0
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        hud_group.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
       
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
