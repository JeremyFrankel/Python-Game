import pygame
import constants
import player

from spritesheet_functions import SpriteSheet
FULL_HEART = (0, 94, 53, 45)
HALF_HEART = (0, 0, 53, 45)

class Health_bar(pygame.sprite.Sprite):
  
    player = None
    hud_sheet = None
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.hud_sheet = SpriteSheet("hud_spritesheet.png")
    
    
    def draw_hearts(self):
        hp = self.player.health
        whole_hp = int(hp//1)
        half_hp = hp%1*2
        full_height = FULL_HEART[3]
        full_width = FULL_HEART[2]*whole_hp + half_hp*HALF_HEART[2]
        image = pygame.Surface([full_width, full_height]).convert()
        current_x = 0
        for i in range(whole_hp):
            image.blit(self.hud_sheet.sprite_sheet, (current_x, 0), FULL_HEART)
            current_x += FULL_HEART[2]
        if half_hp > 0:
            image.blit(self.hud_sheet.sprite_sheet, (current_x, 0), HALF_HEART)
        self.image = image
        self.image.set_colorkey(constants.BLACK)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.draw_hearts()
        self.rect.x = 5
        self.rect.y = 5
